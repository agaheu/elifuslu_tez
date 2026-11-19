"""Sonuç dosyalarından (analiz/cikti) kapsamlı raporu ve site verisini üretir.

    python analiz/py/rapor_uret.py
Çıktılar: analiz/Kapsamli_Yeniden_Inceleme.md, docs/data/*.json, docs/raporlar/*.md
"""
import json, shutil, datetime
import icerik as I
from icerik import R, E, U, S, tr, pv, pct, c, bo, ek, P, N, ROOT, pt13
import tez_degerleri as TEZ
import sade as SD
for _b in I.BULGULAR: _b["sade"] = SD.SADE[_b["id"]]

DOCS = ROOT / "docs"; (DOCS / "data").mkdir(parents=True, exist_ok=True); (DOCS / "raporlar").mkdir(parents=True, exist_ok=True)
AD = {"F1": "Faz 1 (2005–2007)", "F2": "Faz 2 (2008–2012)", "F3": "Faz 3 (2013–2020)", "lnK1": "ln(1+K₍t−1₎)", "gdp_growth_l1": "GSYİH büyümesi₍t−1₎",
      "renew_wdi_l1": "Yenilenebilir payı₍t−1₎", "impdep_l1": "Enerji ithalat bağ.₍t−1₎", "manuf_l1": "İmalat payı₍t−1₎", "trade_l1": "Ticaret açıklığı₍t−1₎",
      "tstar": "ETS öncesi eğilim (t*)", "S1": "Faz 1 eğim (φ₁)", "S2": "Faz 2 eğim (φ₂)", "S3": "Faz 3 eğim (φ₃)"}
AD2 = dict(AD, F1="Faz 1 düzey (λ₁)", F2="Faz 2 düzey (λ₂)", F3="Faz 3 düzey (λ₃)")
FAM = {P: "Poisson QML", N: "Negatif binom"}
L = []
w = L.append


def tablo(bas, satirlar):
    w("| " + " | ".join(bas) + " |"); w("|" + "|".join(["---"] * len(bas)) + "|")
    for s in satirlar: w("| " + " | ".join(str(x) for x in s) + " |")
    w("")


# ---------------------------------------------------------------- yeniden üretim özet sayıları
def uyum_sayisi():
    tot = ok = 0
    for fam in (P, N):
        for k, v in TEZ.T511[fam].items():
            tot += 1; ok += abs(c("m1", fam, k) - v[0]) < 6e-5
        for k, v in TEZ.T513[fam].items():
            tot += 1; ok += abs(c("m2", fam, k) - v[0]) < 6e-5
        for nm in "abc":
            for j, f in enumerate(I.PHN if hasattr(I, "PHN") else ["F1", "F2", "F3"]):
                tot += 1; ok += abs(R["saglamlik"][nm][fam][f]["b"] - TEZ.T514[nm][fam][j][0]) < 6e-5
    for cn, v in R["loo"].items():
        for j in range(3):
            tot += 1; ok += abs(v["hesap"][j][0] - v["tez"][2 * j]) < 6e-5
    for v in R["tanim"]["t52"].values():
        tot += 4; ok += 4 * v["uyum"]
    for v in R["tanim"]["vif"].values():
        tot += 1; ok += abs(v["tez"] - v["hesap"]) < 0.006
    for x in R["tanim"]["t54"]:
        tot += 1; ok += abs(x["tez"] - x["ham"]) < 0.006
    return int(ok), tot


OK, TOT = uyum_sayisi()
_sf = sorted(abs(bo(m, fam, k) / v[1] - 1) for m, T in (("m1", TEZ.T511), ("m2", TEZ.T513)) for fam in (P, N) for k, v in T[fam].items())
se_fark, se_med = _sf[-1], _sf[len(_sf) // 2]

# ---------------------------------------------------------------- metin içi atıflar
import re as _re
_md = (ROOT / "dokumanlar" / "Nihai_Model_19112026_metin.md").read_text(encoding="utf8")
_govde, _kay = _md.split("# KAYNAKÇA")
_refs = []
for _ln in _kay.split("\n"):
    _m = _re.match(r"^([A-ZÇĞİÖŞÜa-zçğıöşüéèêôñáíóúâäëüßčšžæøå'’\-\. ]+?),.*?\((\d{4}[a-z]?)\)", _ln.strip())
    if _m: _refs.append((_m.group(1).strip().split()[0].replace("’", "'"), _m.group(2)[:4]))
N_KAYIT = len(_refs)
_STOP = {"Tablo", "Şekil", "Faz", "Direktif", "Model", "Etki", "F1", "F2", "F3", "Katsayılar", "Krallık", "Sayısı", "Testler", "Testleri", "Yoğunluğunun", "Üçüncüsü", "AT", "Aralık", "Ocak", "Ekim"}
_say = {}
for _m in _re.finditer(r"([A-ZÇĞİÖŞÜ][\wçğıöşüéèôáíČčšž'’\-]+)((?:\s+ve\s+van der Linde|\s+ve\s+diğ\.|\s*(?:ve|and|&)\s*[A-ZÇĞİÖŞÜ][\wçğıöşüéèôáíČčšž'’\-]+)?)(?:'[\wıüö]+)?\s*[,\(]?\s*\(?((?:19|20)\d{2}[a-z]?)", _govde):
    _a = _m.group(1).split("'")[0]; _r = _re.sub(r"\s*(and|&)\s*", " ve ", _m.group(2)).strip(); _r = _re.sub(r"'.*$", "", _r)
    if _a in _STOP: continue
    if _a == "Silva": _a, _r = "Santos Silva", "ve Tenreyro"
    _key = (_a + (" " + _r if _r else ""), _m.group(3))
    _say[_key] = _say.get(_key, 0) + 1
ATIFLAR = [{"atif": k[0], "yil": k[1], "adet": v, "kaynakcada": any(r[0] == k[0].split()[0] and r[1] == k[1][:4] for r in _refs) or k[0].startswith("OECD")} for k, v in sorted(_say.items())]

# ---------------------------------------------------------------- Monte Carlo metni
SIM_AD = {"A": "A — tezin kendi modeli (sabit etkili NB), etki = 0", "B": "B — A + ortak yıl şoku", "C": "C — sabit etkisiz stok modeli, etki = 0"}


def sim_tablolar():
    if not S: return
    w(f"Her senaryoda {S['A']['n']} yapay veri seti üretildi; hepsinde gerçek faz etkisi sıfır. Stok, üretilen patentlerden yeniden kuruldu (δ = 0,15). Her veri setinde tezin Model 1'i tahmin edildi; eşli bootstrap için B = {S['ayar']['B']}. Ortak yıl şokunun standart sapması ({tr(S['ayar']['sigma_ortak_sok'], 3)} log puan; AR(1) ρ = {tr(S['ayar']['rho'], 1)}), ETS öncesi yıl etkilerinin doğrusal eğilim etrafındaki sapmasından kalibre edildi.")
    w("")
    w("**Yanlılık — gerçek etki 0 iken tahmin edilen faz katsayılarının ortalaması**"); w("")
    tablo(["Senaryo", "Tahminci", "Faz 1", "Faz 2", "Faz 3", "Stok katsayısı (ort.)"],
          [[SIM_AD[g], FAM[f], *[tr(x, 3) for x in S[g][f]["ort_b"]], tr(S[g][f]["ort_gamma"], 2)] for g in "ABC" for f in (P, N)])
    w("**Boyut — gerçek etki 0 iken %5 düzeyinde “anlamlı” bulma oranı (ideal: %5)**"); w("")
    rows = []
    for g in "ABC":
        for f in (P, N):
            for key, lab in [("rej_cl", "Ülke-küme t(13)"), ("rej_2w", "İki yönlü küme"), ("rej_cv3", "Küme jackknife (CV3)"), ("rej_boot", "Eşli bootstrap SH, z (tezin yöntemi)"), ("rej_boot_t", "Eşli bootstrap SH, t(13)")]:
                rows.append([SIM_AD[g][:1], FAM[f], lab, *["%" + tr(100 * x, 0) for x in S[g][f][key]]])
    tablo(["Senaryo", "Tahminci", "Çıkarsama yöntemi", "Faz 1", "Faz 2", "Faz 3"], rows)


# ================================================================ RAPOR
bugun = "19.11.2026"
w("# AB ETS ve Yeşil İnovasyon — 5. Bölümün Kapsamlı Yeniden İncelemesi")
w("")
w(f"**İncelenen belge:** `dokumanlar/Nihai_Model_19112026.docx` (Beşinci Bölüm ve kaynakça) · **Veri:** `veri/AB14_nihai_veri.xlsx` · **Tarih:** {bugun}")
w("")
w("> Bu rapor, önceki iki aşamanın (ilk inceleme ve jüri raporu analizi) sonuçları dâhil **hiçbir şeyi doğru varsaymadan**, bölümün ve veri setinin baştan sona yeniden incelenmesidir. Bütün sayılar ham veriden yeniden hesaplanmış, rapordaki tablolar ve cümle içi sayılar doğrudan hesap çıktılarından üretilmiştir (`analiz/py/rapor_uret.py`). Önceki incelemede yanlış çıkan değerlendirmelerim Kısım 11'de açıkça listelenmiştir. **Güncelleme:** İkinci jüri ekibinin raporu ayrıca değerlendirilmiş (`analiz/Juri2_Raporu_Degerlendirmesi.md`), sonuçları bu rapora işlenmiştir (Kısım 9; T5, T11, M1, M8 bulguları).")
w("")
w("## İçindekiler"); w("")
for i, t in enumerate(["Kapsam ve yöntem", "Yönetici özeti", "Yeniden üretim: tezdeki sayılar doğru mu?", "Hipotezlerin yeniden değerlendirilmesi", "Bulgular", "Tasarımın Monte Carlo sınaması", "Çıkarsama duyarlılığı tabloları", "Birinci jüri raporunun analizi", "İkinci jüri raporunun analizi", "Bağımsız hakem okumasıyla karşılaştırma", "Önceki incelememdeki düzeltmeler", "Yapılacaklar", "Tez bölümlerine göre bulgu haritası ve kaynakça denetimi", "Dosyalar ve yeniden üretilebilirlik"], 1):
    w(f"{i}. {t}")
w("")

# ---- 1
w("## 1. Kapsam ve yöntem"); w("")
w("**Neler yapıldı**"); w("")
for s in [
    "Bölüm metni (1.109 satır), 17 tablo, 5 şekil ve kaynakça satır satır okundu; denklemler ve yöntem anlatımı kaynaklarıyla karşılaştırıldı.",
    "Veri seti baştan denetlendi (denge, mükerrer, eksik, iç tutarlılık, uç değerler, stok hesabı).",
    f"Tezdeki bütün tahminler bağımsız yazılımla (Python; kendi yazdığım Poisson IRLS ve NB2 en çok olabilirlik tahmincileri) yeniden üretildi: Model 1, Model 2, üç sağlamlık tanımı, 14 ülke dışlama tahmini, yıl etkileri, plasebo testleri, gecikme seçimi, birim kök ve yatay kesit bağımlılığı testleri. Eşli küme bootstrap B = {R['meta']['B']} tekrarla (tezde 1.000) uygulandı; tekrarların tamamı yakınsadı.",
    "Tezde olmayan ek analizler yapıldı: dört çıkarsama yöntemiyle karşılaştırma, etkin küme sayısı, stoksuz ITS, eğilimli tanımlar, beklenti kuklası, faz bölmeleri, ön-örneklem ortalamalı tahmin, ülke heterojenliği, 896 tanımlı spesifikasyon eğrisi ve tasarımın Monte Carlo sınaması.",
    "Önceki incelemelere demirlenmemek için, hiçbir sonuç verilmeden ayrı bir bağımsız hakem okuması yaptırıldı (`dokumanlar/Bagimsiz_Hakem_Raporu.md`); oradaki her iddia ayrıca yeniden hesaplanarak sınandı.",
    "Kullanıcının ilettiği iki jüri değerlendirme raporu madde madde, veriyle karşılaştırıldı; ikinci jürinin önerdiği sınamalar (ön-örneklem ortalaması tahmincisi, sıfır-kesikli model, İrlanda etkisi) uygulandı.",
    "Literatüre ve kurumsal olgulara ilişkin dört ifade web kaynaklarından kontrol edildi."]:
    w(f"- {s}")
w(""); w("**Neler yapılamadı (sınırlar)**"); w("")
for s in [
    "**Ham verinin kaynağından doğrulanması yapılamadı.** Çalışma ortamından OECD, Eurostat ve Dünya Bankası sunucularına erişim kapalıydı. Veri setinin iç tutarlılığı tam; ancak değerlerin kaynaklardaki güncel değerlerle aynı olduğu bu incelemede teyit edilmedi.",
    "Birleşik Krallık'ın eklenmesi, Ar-Ge harcaması kontrolü, NAP sıkılığına dayalı maruziyet tasarımı ve yeşil patent payı gibi öneriler yeni veri gerektirdiği için sınanamadı.",
    "Stata do-dosyası ve log çıktısı elimde yok; karşılaştırma tezde basılı değerlerle yapıldı. Pedroni testi ve Kao'nun düzeltilmiş istatistikleri yeniden üretilmedi.",
    "Tezin diğer bölümleri görülmedi; değerlendirme yalnızca 5. Bölüm içindir.",
    "Bu bir ekonometrik inceleme; nihai akademik hüküm danışman ve jüriye aittir."]:
    w(f"- {s}")
w("")

# ---- 2
krit = [b for b in I.BULGULAR if b["onem"] == "kritik"]
w("## 2. Yönetici özeti"); w("")
w(f"**Hesaplar doğru, yorumlar fazla iddialı.** Tezde raporlanan ve karşılaştırılan {TOT} sayısal değerin {'tamamı' if OK == TOT else str(OK) + ' tanesi'} (katsayılar, tanımlayıcı istatistikler, VIF ve korelasyonlar) bağımsız yazılımla birebir yeniden üretildi; bootstrap standart hataları tezdekilerden medyan %{tr(100 * se_med, 0)}, en çok %{tr(100 * se_fark, 0)} farklı (farklı rassal sayı üreteci ve tekrar sayısıyla beklenen düzey). Hesaplama ya da aktarım hatası bulunmadı. Sorunlar hesapta değil; tasarımın neyi tanımlayabildiğinde, çıkarsamanın dayanıklılığında ve hipotez tablosunun kanıttan ileri gitmesinde.")
w("")
w(f"**Sağlam olan.** Ülke sabit etkili tanımların hepsinde (stok, kontroller, doğrusal eğilim nasıl tanımlanırsa tanımlansın) 2006–2010 arasında yeşil patent yoğunluğunda belirgin bir yükseliş var: Faz 1 boyunca eğim artışı, Faz 2 başında düzey farkı. Bu örüntü ülkelerin tek tek dışlanmasında, 896 alternatif tanımın neredeyse tamamında ve “gerçek etki sıfır” varsayımıyla üretilen benzetimlere karşı sınandığında da ayakta kalıyor (negatif binom Faz 2 için Monte Carlo p = {I.mcr(N, 1)}; Model 2 Faz 2 düzeyi p = {I.mcr(N, 5)}; Faz 1 eğimi p = {I.mcr(N, 4)}). Faz 3'te stok kontrol edildiğinde ek bir fark yok.")
w("")
w("**Sağlam olmayan.**"); w("")
for b in krit:
    w(f"- **{b['id']} — {b['baslik']}.** {b['tespit'].split('. ')[0]}.")
w(f"- **Faz 1 bulgusu kırılgan.** Poisson'da küme jackknife p = {pv(c('m1', P, 'F1', 'p_cv3'))}, boş hipotez benzetimlerinde p = {I.mcr(P, 0)}; negatif binomda analitik yöntemlerle %5 düzeyinde anlamlı, benzetimlerde sınırda (p = {I.mcr(N, 0)}).")
w(f"- **Model 1'in faz katsayıları yukarı yanlı ve tezin çıkarsama yöntemi fazla sık reddediyor.** Gerçek etki sıfırken bile ortalama Faz 1 ≈ +{tr(I.SP['A'][N]['ort'][0], 2)}, Faz 2 ≈ +{tr(I.SP['A'][N]['ort'][1], 2)} tahmin ediliyor ve tezin yöntemi %5 yerine {I.simrg('rej_boot', 'A')} oranında “anlamlı” buluyor (T5, C9).")
w(f"- **Tanıma duyarlılık.** Ülke heterojenliği sabit etkiler yerine ön-örneklem ortalamasıyla kontrol edildiğinde Model 1'in Faz 1 ve Faz 2 katsayıları sıfıra iniyor; Model 2'nin Faz 1 eğimi ({tr(I.J['psm_m2'][N]['S1']['b'], 3)}) ve Faz 2 düzeyi ({tr(I.J['psm_m2'][N]['F2']['b'], 3)}) ise bu tahmincide de anlamlı (T5).")
w("")
w("**Genel değerlendirme.** Birinci jüri raporundaki “önemli düzeltme gerekli” yargısı bu incelemeyle örtüşüyor; ikinci jüri raporunun “düzeltmelerle uluslararası yayına hazır” yargısı ise fazla iyimser (Kısım 9). Bölüm, “AB ETS yeşil inovasyonu artırmıştır” biçimindeki nedensel iddiayı bu tasarımla taşıyamıyor; ama “AB ETS'nin ilk iki fazına denk gelen dönemde, öncesindeki eğilimin ve bilgi stokunun açıklayamadığı bir yükseliş vardır ve bu yükseliş üçüncü fazda sürmemiştir” biçimindeki betimleyici bulgu güçlü ve yeniden üretilebilir. Aşağıdaki düzeltmeler yapılırsa bölüm savunulabilir hâle gelir; düzeltmelerin çoğu yeni veri değil, yeniden yazım ve birkaç ek tablo gerektiriyor.")
w("")
say = {o: sum(1 for b in I.BULGULAR if b["onem"] == o) for o in ("kritik", "önemli", "orta", "küçük")}
tablo(["", "Kritik", "Önemli", "Orta", "Küçük", "Toplam"], [["Bulgu sayısı", say["kritik"], say["önemli"], say["orta"], say["küçük"], len(I.BULGULAR)]])

# ---- 3
w("## 3. Yeniden üretim: tezdeki sayılar doğru mu?"); w("")
w("### 3.1 Veri seti"); w("")
V = R["veri"]
tablo(["Kontrol", "Sonuç"], [
    ["Yapı", f"{V['satir']} satır = {V['ulke']} ülke × 31 yıl (1990–2020); tam dengeli; mükerrer ülke-yıl yok"],
    ["Tahmin örneklemi (1997–2020)", f"{R['meta']['N']} gözlem; hiçbir değişkende eksik değer yok"],
    ["Eksik değerler", "Yalnızca 1990–1995: reel GSYİH ve imalat payı 1990–1994, büyüme 1990–1995 (tahmini ve gecikmeleri etkilemiyor)"],
    ["İç tutarlılık", f"Büyüme oranı, GSYİH düzeylerinden hesaplananla en çok {tr(V['buyume_tutarlilik_max_fark'], 2)} puan farklı (yuvarlama)"],
    ["Stok", "Sıfırdan yeniden hesaplanan stok Excel sayfasındakiyle aynı (fark < 10⁻⁹); g = " + tr(R["meta"]["g"], 4)],
    ["Yuvarlama", f"Kesirli sayımlar yarım değerde yukarı yuvarlanmış; tahmin örnekleminde {V['yuvarlama_yarim']} gözlem tam ,5"],
    ["Sıfır gözlem", "Yalnız Portekiz 1990 (stok başlangıcı)"],
    ["Uç değerler", f"En yüksek başvuru {V['uc']['ccm_max'][0]} {V['uc']['ccm_max'][1]} ({int(V['uc']['ccm_max'][2])}); en yüksek yoğunluk {V['uc']['inten_max'][0]} {V['uc']['inten_max'][1]} ({tr(V['uc']['inten_max'][2], 3)}); en yüksek büyüme {V['uc']['buyume_max'][0]} {V['uc']['buyume_max'][1]} (%{tr(V['uc']['buyume_max'][2], 1)}); en düşük ithalat bağımlılığı {V['uc']['impdep_min'][0]} {V['uc']['impdep_min'][1]}"],
    ["Kaynak doğrulaması", "**Yapılamadı** (dış veri sunucularına erişim yok)"]])
w("### 3.2 Model 1 (Tablo 5.11)"); w("")
rows = []
for k in ["F1", "F2", "F3", "lnK1", "gdp_growth_l1", "renew_wdi_l1", "impdep_l1", "manuf_l1", "trade_l1"]:
    r = [AD[k]]
    for fam in (N, P):
        t = TEZ.T511[fam][k]
        r += [tr(t[0], 4), tr(c("m1", fam, k), 4), tr(t[1], 4), tr(bo("m1", fam, k), 4)]
    rows.append(r)
tablo(["Değişken", "NB tez", "NB hesap", "NB SH tez", "NB SH hesap", "Poisson tez", "Poisson hesap", "P. SH tez", "P. SH hesap"], rows)
w(f"α = {tr(R['m1'][N]['alpha'], 4)} [{tr(R['m1'][N]['alpha_ci'][0], 4)}; {tr(R['m1'][N]['alpha_ci'][1], 4)}] (tez 0,0178 [0,0137; 0,0230]); LR = {tr(R['m1']['LR'], 2)} (tez 669,77).")
w("")
w("### 3.3 Model 2 (Tablo 5.13)"); w("")
rows = []
for k in ["tstar", "F1", "S1", "F2", "S2", "F3", "S3", "lnK1"]:
    r = [AD2[k]]
    for fam in (N, P):
        t = TEZ.T513[fam][k]
        r += [tr(t[0], 4), tr(c("m2", fam, k), 4), tr(t[1], 4), tr(bo("m2", fam, k), 4)]
    rows.append(r)
tablo(["Değişken", "NB tez", "NB hesap", "NB SH tez", "NB SH hesap", "Poisson tez", "Poisson hesap", "P. SH tez", "P. SH hesap"], rows)
w(f"α = {tr(R['m2'][N]['alpha'], 4)}; LR = {tr(R['m2']['LR'], 2)} (tez 0,0161; 564,59). Ortak testler (bootstrap kovaryansı, χ²(2)): NB {' / '.join(tr(x['chi2'], 2) for x in R['m2'][N]['boot']['joint'])} (tez 12,27 / 21,02 / 0,73); Poisson {' / '.join(tr(x['chi2'], 2) for x in R['m2'][P]['boot']['joint'])} (tez 15,39 / 28,23 / 2,22).")
w("")
w("### 3.4 Diğer tablolar"); w("")
tablo(["Tablo / değer", "Durum", "Not"], [
    ["Tablo 5.2 (36 değer)", "✓ birebir", ""],
    ["Tablo 5.3", "✓ birebir", "Kontrol sütunları eşzamanlı (t) değerler; tabloda belirtilmemiş"],
    ["Tablo 5.4 (15 korelasyon)", "✓ birebir", "Ham korelasyonlar; ülke-içi değerler çok farklı (M3)"],
    ["Tablo 5.6 (9 VIF)", "✓ birebir", ""],
    ["Tablo 5.7 Fisher-ADF", "✓ birebir", "Yoğunluk satırı logaritmayla (M4)"],
    ["Tablo 5.7 IPS", "✓ ±0,2", "Momentler benzetimle üretildi"],
    ["Tablo 5.9 CD ve CIPS", "✓ birebir (3 ondalık)", "Stok CIPS: −2,775 (tez −2,771)"],
    ["Tablo 5.10 Kao", "◐ iki düzeltilmemiş istatistik birebir", "Düzeltilmiş istatistikler ve Pedroni yeniden üretilmedi"],
    ["Tablo 5.14 (18 katsayı, 18 SH)", "✓ katsayılar birebir, SH ±%4", f"Esneklik testi χ²: {tr(R['saglamlik']['b'][N]['elast_test_boot']['chi2'], 2)} / {tr(R['saglamlik']['b'][P]['elast_test_boot']['chi2'], 2)} (tez 10,78 / 15,92)"],
    ["Tablo 5.15 (42 katsayı, 42 p)", "✓ katsayılar birebir, p ±0,02", f"%5'te anlamlı Faz 1 sayısı: {I.loo_p5} (tez 7)"],
    ["Tablo 5.16 (plasebo)", "✓ birebir", "2003 raporlanmamış (T6)"],
    ["Yıl etkileri (Şekil 5.5)", "✓ birebir", "0,102 / 0,156 / 0,195 / 0,308; stok 0,810"],
    ["Gecikme seçimi AIC", "✓ birebir", "İki gecikmeli model stoku da geciktiriyor (M2)"]])

# ---- 4
w("## 4. Hipotezlerin yeniden değerlendirilmesi"); w("")
tablo(["", "Hipotez", "Tezin sonucu", "Yeniden değerlendirme", "Gerekçe"], [[h[0], h[1], h[2], f"**{h[3]}**", h[5]] for h in I.HIPOTEZ])

# ---- 5
w("## 5. Bulgular"); w("")
w("Her bulgu için: önem derecesi, tezdeki yeri (satır numaraları `dokumanlar/Nihai_Model_19112026_metin.md` dosyasına göre), hangi incelemede ortaya çıktığı, tespit, sayısal kanıt, öneri ve **adım adım düzeltme** (tezde hangi cümlenin, tablonun nasıl değişeceği; varsa teze yazılabilecek örnek metin). Aynı bulguların teknik olmayan okur için yazılmış sürümü ayrı bir belgededir: `analiz/Sade_Anlatim_ve_Duzeltme_Rehberi.md`. Etkileşimli, süzülebilir sürümü sitededir (sade / teknik anlatım seçeneğiyle).")
w("")
for kat in ["Tanımlama", "Çıkarsama", "Model", "Yorum", "Biçim", "Kaynakça"]:
    bs = [b for b in I.BULGULAR if b["kat"] == kat]
    if not bs: continue
    w(f"### 5.{['Tanımlama', 'Çıkarsama', 'Model', 'Yorum', 'Biçim', 'Kaynakça'].index(kat) + 1} {kat}"); w("")
    for b in bs:
        w(f"#### {b['id']} · {b['baslik']}"); w("")
        w(f"**Önem:** {b['onem']} · **Yer:** {b['yer']} · **Kaynak:** {', '.join(b['kaynak'])} · **Durum:** {b['durum']}"); w("")
        w(f"**Tespit.** {b['tespit']}"); w("")
        w(f"**Kanıt.** {b['kanit']}"); w("")
        w(f"**Öneri.** {b['oneri']}"); w("")
        w("**Adım adım düzeltme.**"); w("")
        for i_, a_ in enumerate(b["sade"]["adimlar"], 1): w(f"{i_}. {a_}")
        w("")
        if b["sade"]["ornek"]:
            w("**Teze yazılabilecek örnek metin.**"); w(""); w(f"> {b['sade']['ornek']}"); w("")
w("### 5.7 Doğrulanan (sorun bulunmayan) noktalar"); w("")
for a, b_ in I.DOGRULANAN: w(f"- **{a}.** {b_}")
w("")

# ---- 6
w("## 6. Tasarımın Monte Carlo sınaması"); w("")
w("Soru: **AB ETS'nin gerçek etkisi sıfır olsaydı, tezin tahmincisi ve çıkarsama yöntemi ne bulurdu?** Bunu görmek için üç senaryoda yapay veri üretildi (`analiz/py/simulasyon.py`).")
w("")
sim_tablolar()
SP = I.SP
w("**Parametrik bootstrap — tezin gözlenen katsayıları “sıfır etki” dağılımının neresinde?**"); w("")
w(f"Her senaryoda {SP['A']['n']} benzetim. Senaryo A2, A'nın ülkeye özgü aşırı yayılımlı hâlidir (M7). “Sıfır etki ort.” sütunu yanlılığı, p sütunu gözlenen değerin aşılma olasılığını (tek yönlü) verir.")
w("")
_rows = []
for j, nm in enumerate(SP["katsayilar"]):
    for fam in (N, P):
        _rows.append([nm, FAM[fam], tr(SP["gozlenen"][fam][j], 3)] + [f"{tr(SP[g][fam]['ort'][j], 3)} ({pv(SP[g][fam]['p_tek'][j])})" for g in ("A", "A2", "B", "C")])
tablo(["Katsayı", "Tahminci", "Tezdeki değer", "A: ort. (p)", "A2: ort. (p)", "B: ort. (p)", "C: ort. (p)"], _rows)
SIM_YORUM = "{{SIM_YORUM}}"
w(SIM_YORUM); w("")

# ---- 7
w("## 7. Çıkarsama duyarlılığı tabloları"); w("")
for m, nm, keys, ad in (("m1", "Model 1", ["F1", "F2", "F3", "lnK1"], AD), ("m2", "Model 2", ["tstar", "F1", "S1", "F2", "S2", "F3", "S3", "lnK1"], AD2)):
    w(f"### {nm}: p değerleri"); w("")
    rows = []
    for fam in (N, P):
        for k in keys:
            x = R[m][fam]["coef"][k]; b = R[m][fam]["boot"]["coef"][k]
            rows.append([FAM[fam], ad[k], tr(x["b"], 4), pv(x["p_cl_t"]), pv(x["p_2w"]) if x["p_2w"] is not None else "–", pv(x["p_cv3"]), pv(b["p"]), pv(pt13(x["b"], b["se"])),
                         f"[{tr(b['pct'][0], 3)}; {tr(b['pct'][1], 3)}]", f"[{tr(b['bc'][0], 3)}; {tr(b['bc'][1], 3)}]"])
    tablo(["Tahminci", "Katsayı", "b", "Ülke-küme t(13)", "İki yönlü", "Jackknife CV3", "Bootstrap z (tez)", "Bootstrap t(13)", "%95 yüzdelik", "%95 BC"], rows)
w(f"Notlar: ülke-küme ve iki yönlü kovaryanslar Stata'nın en çok olabilirlik kuralıyla (yalnız G/(G−1) düzeltmesi) hesaplandı. **İki yönlü sütunu ihtiyatla okuyun:** Kısım 6'daki benzetimde bu tahminci boş hipotez altında {I.simrg('rej_2w', 'A')} ret oranıyla en kötü performansı gösterdi; burada yalnız şeffaflık için raporlanıyor. Nominal düzeye en yakın yöntem küme jackknife (CV3; MacKinnon, Nielsen ve Webb, 2023). Parametrik bootstrap p değerleri Kısım 6'dadır.")
w("")
w("### Spesifikasyon eğrisi özeti (896 tanım)"); w("")
so = R["ek"]["spec_ozet"]
tablo(["", "Medyan katsayı", "En küçük", "En büyük", "Pozitif pay", "Pozitif ve %5'te anlamlı", "Negatif ve %5'te anlamlı"],
      [[AD[f], tr(so[f]["medyan"], 3), tr(so[f]["min"], 3), tr(so[f]["max"], 3), "%" + tr(100 * so[f]["pozitif_pay"], 1), "%" + tr(100 * so[f]["poz_anlamli5"], 1), "%" + tr(100 * so[f]["neg_anlamli5"], 1)] for f in ("F1", "F2", "F3")])
w(f"Tanımlar: tahminci (2) × stok var/yok × eskime oranı (0,10/0,15/0,20) × maruziyet sabit/serbest × kontroller tam/yok × örneklem (7) × gecikme 1/2 × doğrusal eğilim var/yok. Faz 3'ün pozitif ve anlamlı çıktığı tanımların neredeyse tamamı stoksuz olanlar (stoklu tanımlarda %{tr(100 * so['F3']['stok_1']['poz_anlamli5'], 1)}, stoksuzlarda %{tr(100 * so['F3']['stok_0']['poz_anlamli5'], 1)}). Bu eğri, bulguların *tanım seçimine* dayanıklılığını gösterir; ortak şoklara (T1) ve sabit etki/stok yapısına (T5) dayanıklılığını göstermez.")
w("")
w("### Seçilmiş ek tahminler (faz katsayıları; ülke-kümeli SH, t(13) p değeri)"); w("")
rows = []
for nm, lab in [("m1_trend", "Ana model + doğrusal eğilim"), ("m1_trend2", "Ana model + karesel eğilim"), ("kontrolsuz", "Yalnız stok (kontrolsüz)"), ("beklenti", "2003–2004 beklenti kuklası eklenmiş"),
                ("2020_haric", "2020 hariç"), ("2018_2020_haric", "2018–2020 hariç"), ("irlanda_haric", "İrlanda hariç"), ("luksemburg_haric", "Lüksemburg hariç"), ("DE_FR_haric", "Almanya ve Fransa hariç"),
                ("delta_0.05", "Eskime oranı 0,05"), ("delta_0.25", "Eskime oranı 0,25"), ("presample", "Sabit etki yerine ön-örneklem ortalaması")]:
    for fam in (N, P):
        o = R["ek"][nm][fam]
        rows.append([lab, FAM[fam], *[f"{tr(o[f]['b'], 3)} ({pv(o[f]['p_t'])})" for f in ("F1", "F2", "F3")]])
tablo(["Tanım", "Tahminci", "Faz 1", "Faz 2", "Faz 3"], rows)

# ---- 8
w("## 8. Birinci jüri raporunun analizi"); w("")
w("Jüri raporunun tam metni: `dokumanlar/Juri1_Degerlendirme_Raporu.md`. Jüri, kendi ifadesiyle, regresyonları yeniden tahmin edememişti; aşağıdaki değerlendirme her maddeyi veriyle sınıyor.")
w("")
tablo(["Jüri maddesi", "Değerlendirmem", "Veriyle desteklenen cevap"], [[j[0], j[1], j[3]] for j in I.JURI])
w("**Jüri raporunda bulunmayan, bu incelemede ortaya çıkan başlıca noktalar:** H5'in stok yan ürünü olması (T2), H1 kanıtının eğilimle kirlenmesi (T3), sabit etki/stok tanımına duyarlılık (T5), 2003 plasebosu ve plasebo gücü (T6), Faz 2'nin zamanlaması (T7), etkin küme sayısı ve Poisson–NB ağırlık farkı (C3), BC aralıklarının kararsızlığı (C4), birim kök tablosunda log/düzey etiketi (M4), gecikme seçimi tanımı (M2).")
w("")

# ---- 9 (ikinci jüri)
w("## 9. İkinci jüri raporunun analizi"); w("")
w("İkinci jüri ekibinin raporu (`dokumanlar/Juri2_Degerlendirme_Raporu.md`) ayrı bir belgede madde madde değerlendirildi: **`analiz/Juri2_Raporu_Degerlendirmesi.md`**. Burada özeti ve bu rapora etkisi verilmiştir.")
w("")
J2_OZET = {"G1": "Yeniden üretimimle aynı sonuç: 164 değer birebir.",
           "G2": "Tercih savunulabilir; negatif binomun ortak yayılım varsayımı ve iki tahmincinin farklı ağırlıklandırması not edilmeli.",
           "G3": f"Benzetimde yöntem %5 yerine {I.simrg('rej_boot', 'A')} oranında reddediyor; BC aralıkları kararsız.",
           "G4": "Model 2 gerçekten en sağlam kısım; ancak “kalıcı” nitelemesi yıl etkileriyle, plasebo övgüsü 2003 sonucuyla çelişiyor.",
           "E1": "Kesin dışsallık ihlali doğru ve ölçüldü; önerilen tahminci Model 1'i kurtarmıyor, Model 2'yi doğruluyor.",
           "E2": "Tanımlama eleştirisi birinci kritik bulguyla aynı; fiyatın “temel mekanizma” olduğu sınanmış değil.",
           "E3": "Kısıtsız model ana tabloda yer almalı; İrlanda sınandı, sonuç değişmiyor.",
           "E4": "Aynı eleştiri diğer incelemelerde de var; ek olarak log/düzey etiketi ve dönem farkı bulundu.",
           "E5": "Sıfır gözlenebilir, yalnız gerçekleşmemiş; sıfır-kesikli tahminler dördüncü ondalıkta aynı.",
           "K1": "Doğrulandı.", "K2": "Doğrulandı.", "K3": "Veriyle doğrulandı; metin bunu dolaylı söylüyor, bir cümle eklenmeli.", "K4": "Doğrulandı.", "K5": "Doğrulandı.",
           "S": "Liste gerekli ama yeterli değil; değinilmeyen altı kritik ya da önemli nokta var."}
tablo(["", "İkinci jürinin maddesi", "Değerlendirmem", "Gerekçe (özet)", "İlgili bulgular"], [[j[0], j[2], f"**{j[3]}**", J2_OZET[j[0]], ", ".join(j[7]) or "–"] for j in I.JURI2])
w(f"**Üç ana sonuç.** (1) Raporun çıkarsama övgüsü veriyle çelişiyor: eşli bootstrap + BC, gerçek etki sıfırken %5 yerine {I.simrg('rej_boot', 'A')} oranında reddediyor (C9). (2) Stok eleştirisi için önerilen ön-örneklem ortalaması tahmincisi uygulandı: Model 1'in faz katsayıları sıfıra iniyor (NB Faz 2: {tr(I.jp('psm', I.PSA, N, 'F2'), 3)}), Model 2'nin Faz 1 eğimi ({tr(I.J['psm_m2'][N]['S1']['b'], 3)}) ve Faz 2 düzeyi ({tr(I.J['psm_m2'][N]['F2']['b'], 3)}) ise anlamlı kalıyor (T5). (3) Karbon fiyatı ve yeşil olmayan patentlerle plasebo önerileri yerinde ve yeni; ilki için kanıt sınırlı (T11), ikincisi yeni veri gerektiriyor (T1).")
w("")
w("**İki jüri raporunun karşılaştırması**"); w("")
tablo(["Konu", "1. jüri raporu", "2. jüri raporu", "Bu rapordaki karşılığı"], I.JURI_KARSILASTIRMA)

# ---- 10
w("## 10. Bağımsız hakem okumasıyla karşılaştırma"); w("")
w("Hiçbir ön bilgi verilmeden yaptırılan ikinci okuma (`dokumanlar/Bagimsiz_Hakem_Raporu.md`) 27 madde üretti. Hepsi ayrıca yeniden hesaplandı (`analiz/py/ek_dogrulama.py`):")
w("")
tablo(["Hakemin iddiası", "Benim hesabım", "Sonuç"], [
    ["Model 2 ülke-içi VIF: eğilim 42,8; Faz 3 25,4; stok 12,0", f"{tr(E['vif_m2']['tstar'], 1)}; {tr(E['vif_m2']['F3'], 1)}; {tr(E['vif_m2']['lnK1'], 1)}", "✓ doğrulandı"],
    ["Stok–zaman ülke-içi korelasyonu 0,95", tr(E["ici_kor"]["lnK1~zaman"], 3), "✓"],
    ["Eğilim tek başına 0,27 / 0,46 / 0,78 log puan üretir (NB)", " / ".join(tr(E["egilim_katkisi"]["nb"][f]["egilimden"], 2) for f in ("F1", "F2", "F3")), "✓"],
    ["2003 plasebo kırılması reddediyor: Poisson χ² = 9,51 (p = 0,009); NB 5,45 (p = 0,066)", f"{tr(I.pl['2003'][P]['chi2_kume'], 2)} ({pv(I.pl['2003'][P]['p_kume'])}); {tr(I.pl['2003'][N]['chi2_kume'], 2)} ({pv(I.pl['2003'][N]['p_kume'])})", "✓ (bootstrap kovaryansıyla reddedilmiyor: ek bilgi)"],
    ["Bootstrap SH ile yıl etkilerinden yalnız 2009 %5'i geçiyor", "p: " + " / ".join(pv(I.yb[y]["p_boot"]) for y in ("2006", "2007", "2008", "2009", "2010")), "✓"],
    ["Yalnız kontroller 2 gecikmeli: AIC 2966,65", tr(R["gecikme"][N]["lag2_yalniz_kontrol"], 2), "✓"],
    ["Yoğunluk birim kök testleri logaritmayla yapılmış", "Fisher 22,94 ↔ 15,65; CD 36,913 ↔ 34,675", "✓ (ek: CIPS ve Kao da; düzeyle CIPS reddetmiyor)"],
    ["En büyük ham korelasyon 0,3510", tr(E["kucuk"]["max_ham_korelasyon"], 4), "✓"],
    ["g ortalama log büyüme (aritmetik 0,0769; bileşik 0,0716)", f"{tr(E['kucuk']['g_aritmetik'], 4)}; {tr(E['kucuk']['g_bilesik'], 4)}", "✓"],
    ["Faz 2 / Faz 1 oranı NB 2,02; Poisson 2,53", f"{tr(E['kucuk']['faz2_faz1_orani']['nb'], 2)}; {tr(E['kucuk']['faz2_faz1_orani']['poisson'], 2)}", "✓"],
    ["Pedroni değiştirilmiş PP +2,255'in “ret” sayılması şüpheli", "Yeniden üretilmedi", "Orta güvenle aktarıldı (M4)"],
    ["Birleşik Krallık 31.12.2020'ye kadar AB ETS'de", "Web kaynaklarından teyit", "✓"]])
w("İki bağımsız okumanın (benim ilk incelemem ve hakem okuması) birbirinden habersiz aynı kritik noktalara ulaşması (kontrol grubu, H5'in stoka bağlılığı, bootstrap gerekçesi, Tablo 5.4, BC aralıkları) bu bulguların güvenilirliğini artırıyor. Hakemin bulup benim ilk incelememde kaçırdıklarım: H1 kanıtının eğilimle kirlenmesi, 2003 plasebosu, Faz 2 zamanlaması, log/düzey etiketi, gecikme seçimi tanımı, NAP ayrıntısı.")
w("")

# ---- 11
w("## 11. Önceki incelememdeki düzeltmeler"); w("")
w("İlk incelemede (`analiz/arsiv/01_Ilk_Inceleme_ve_Juri_Analizi.md`) yazdığım ve bu aşamada yanlış ya da eksik çıkan değerlendirmeler:")
w("")
tablo(["Önceki ifadem", "Şimdiki durum"], [[a, b_] for a, b_ in I.DUZELTMELER])

# ---- 12
w("## 12. Yapılacaklar"); w("")
for oc in "ABCD":
    w(f"### {oc} — {I.ONCELIK[oc]}"); w("")
    for i, (o, t, ref) in enumerate([y for y in I.YAPILACAK if y[0] == oc], 1):
        w(f"{i}. {t} *(bkz. {ref})*")
    w("")

# ---- 13
w("## 13. Tez bölümlerine göre bulgu haritası ve kaynakça denetimi"); w("")
w("### 13.1 Bölümlere göre bulgular"); w("")
tablo(["Tez bölümü", "Kapsam", "Genel durum", "İlgili bulgular"], [[b[1], b[2], b[3], ", ".join(x["id"] for x in I.BULGULAR if b[0] in x["bolum"])] for b in I.BOLUMLER])
w("### 13.2 Kaynakça ve atıf denetimi"); w("")
w(I.KAYNAKCA["ozet"] + f" Bölümde {len(ATIFLAR)} farklı yazar–yıl atfı var; kaynakçada {N_KAYIT} kayıt bulunuyor (liste tezin tamamı için).")
w("")
w("**Atıf yazım hataları**"); w("")
tablo(["Satır", "Metindeki yazım", "Sorun"], I.KAYNAKCA["bicim"])
w("**Kaynakça kayıtları**"); w("")
tablo(["Kayıt", "Sorun"], I.KAYNAKCA["kayit"])
w("**Eksik metin içi atıflar**"); w("")
tablo(["Yer", "Konu", "Not"], I.KAYNAKCA["eksik_atif"])
w("**Birincil kaynaktan doğrulanması gereken aktarımlar**"); w("")
tablo(["Yer", "İfade", "Durum"], I.KAYNAKCA["dogrulanamayan"])
w("**Eklenmesi önerilen kaynaklar**"); w("")
tablo(["Kaynak", "Neden"], I.KAYNAKCA["onerilen"])

# ---- 14
w("## 14. Dosyalar ve yeniden üretilebilirlik"); w("")
tablo(["Dosya", "İçerik"], [
    ["`veri/AB14_nihai_veri.xlsx`", "Ham panel, stok sayfası, kaynaklar"],
    ["`dokumanlar/`", "Tez bölümü (docx + metin), şekiller, iki jüri raporu, bağımsız hakem raporu"],
    ["`analiz/Juri2_Raporu_Degerlendirmesi.md`", "İkinci jüri raporunun madde madde değerlendirmesi"],
    ["`analiz/Sade_Anlatim_ve_Duzeltme_Rehberi.md`", "Bulguların teknik olmayan okur için sade anlatımı ve adım adım düzeltme rehberi (`analiz/py/sade.py`)"],
    ["`dokumanlar/Nihai_Model_guncel_metin.md`, `Nihai_Model_guncel.docx`", "Bulgulara göre güncellenmiş tez metni (5. bölüm); yalnızca bulgularda işaretlenen yerler değiştirildi"],
    ["`analiz/Tez_Guncelleme_Degisiklik_Listesi.md`", "Güncellenmiş tezdeki bütün değişiklikler: gerekçe, önceki ve yeni metin, bulgu numarası; uygulanmayan öneriler"],
    ["`analiz/py/tez_guncel_hesap.py`, `tezarac.py`, `tez_d1.py`, `tez_d2.py`, `tez_guncelle.py`", "Güncellenmiş tezi üreten kod: yeni tablo satırları için bootstrap ve jackknife; izlenebilir değişiklik altyapısı; değişiklik tanımları"],
    ["`analiz/py/juri2.py`", "İkinci jürinin önerdiği sınamalar → `analiz/cikti/juri2.json`"],
    ["`analiz/py/tezlib.py`", "Veri hazırlama, Poisson IRLS, NB2 en çok olabilirlik, kümelenmiş kovaryanslar, bootstrap yardımcıları"],
    ["`analiz/py/yeniden_inceleme.py`", "Tüm tabloların yeniden üretimi ve ek analizler → `analiz/cikti/sonuclar.json`"],
    ["`analiz/py/birim_kok.py`", "Fisher-ADF, IPS, CD, CIPS"],
    ["`analiz/py/ek_dogrulama.py`", "Hakem iddialarının sınanması, yıl etkisi bootstrap'ı, plasebo, Kao"],
    ["`analiz/py/simulasyon.py`, `simulasyon_p.py`", "Monte Carlo sınaması (çıkarsama boyutu; parametrik bootstrap)"],
    ["`analiz/py/icerik.py`, `rapor_uret.py`", "Bulgular ve bu raporun üretimi (sayılar çıktılardan çekilir)"],
    ["`analiz/arsiv/`", "İlk inceleme raporu ve ilk replikasyon betiği"],
    ["`docs/`", "Etkileşimli site (GitHub Pages)"]])
w("```bash"); w("pip install pandas numpy scipy statsmodels openpyxl"); w("python analiz/py/yeniden_inceleme.py 1999"); w("python analiz/py/birim_kok.py"); w("python analiz/py/ek_dogrulama.py"); w("python analiz/py/simulasyon.py 300 199"); w("python analiz/py/simulasyon_p.py 1000"); w("python analiz/py/juri2.py"); w("python analiz/py/rapor_uret.py"); w("```")
w("")

rapor = "\n".join(L)
try:
    import sim_yorum
    rapor = rapor.replace(SIM_YORUM, sim_yorum.metin(S, tr))
    SIMY = sim_yorum.metin(S, tr)
except Exception as ex:
    raise
(ROOT / "analiz" / "Kapsamli_Yeniden_Inceleme.md").write_text(rapor, encoding="utf8")

# ---------------------------------------------------------------- sade anlatım ve düzeltme rehberi
G = []
g = G.append
ONEM_SIRA = ["kritik", "önemli", "orta", "küçük"]
g("# Sade Anlatım ve Düzeltme Rehberi"); g("")
g(f"**Konu:** Doktora tezi, Beşinci Bölüm (AB ETS ve yeşil inovasyon) · **Tarih:** {bugun}"); g("")
g("> Bu belge, kapsamlı yeniden inceleme raporundaki 36 bulgunun teknik olmayan okur için yazılmış sürümüdür. Her bulgu üç soruya cevap verir: **Sorun ne? Neden önemli? Ne yapılmalı?** Düzeltme adımları tezde hangi cümlenin ya da tablonun nasıl değişeceğini sırayla söyler; uygun yerlerde teze doğrudan yazılabilecek örnek metin vardır. Sayılar hesap çıktılarından otomatik çekilir. Teknik gerekçe ve kanıt için ana rapora bakın: `analiz/Kapsamli_Yeniden_Inceleme.md`, Kısım 5 (bulgu numaraları aynıdır).")
g("")
g("## Bu belge nasıl okunur?"); g("")
g("- **Önem dereceleri.** *Kritik:* tezin ana iddiasını etkiler, savunmadan önce mutlaka ele alınmalı. *Önemli:* bir hipotezin ya da ana tablonun yorumunu değiştirir. *Orta:* tutarlılık ve gerekçe sorunu; düzeltmesi kolaydır. *Küçük:* ifade ve biçim.")
g("- **Satır numaraları (L…)** tezin düz metin dosyasına göredir: `dokumanlar/Nihai_Model_19112026_metin.md`.")
g("- **“Hazır” denilen sayılar ve tablolar** ana raporda ve sitede bulunur; yeniden hesap gerekmez.")
g("- **“Yeni veri gerekir” denilen adımlar** bu inceleme sırasında yapılamadı; veri sağlanırsa yapılabilir.")
g("- Örnek metinler öneridir; tezin üslubuna göre uyarlanmalıdır.")
g("")
g("## Genel tablo"); g("")
g(f"Tezdeki hesaplar doğru: karşılaştırılan {OK} sayının {OK}'ü yeniden üretilebildi. Sorunlar hesapta değil, sonuçların nasıl yorumlandığında ve yöntemin nasıl gerekçelendirildiğinde. Bulguların dağılımı: " + ", ".join(f"{sum(1 for b in I.BULGULAR if b['onem'] == o)} {o}" for o in ONEM_SIRA) + ".")
g("")
g("### Önce bunlar (kritik bulgular)"); g("")
for b in I.BULGULAR:
    if b["onem"] == "kritik": g(f"- **{b['id']}** · {b['sade']['baslik']}")
g("")
g("### Bütün bulgular"); g("")
G.append("| No | Önem | Konu | Tezdeki yer |"); G.append("|---|---|---|---|")
for b in sorted(I.BULGULAR, key=lambda x: ONEM_SIRA.index(x["onem"])): G.append(f"| {b['id']} | {b['onem']} | {b['sade']['baslik']} | {b['yer']} |")
g("")
g("## Terimler sözlüğü"); g("")
for a_, t_ in SD.SOZLUK: g(f"- **{a_}.** {t_}")
g("")
KAT_AD = {"Tanımlama": "ETS'nin etkisi gerçekten ayırt edilebiliyor mu? (tanımlama)", "Çıkarsama": "Sonuçlar tesadüf olabilir mi? (çıkarsama)", "Model": "Modelin kuruluşu", "Yorum": "Sonuçların yorumu", "Biçim": "Biçim", "Kaynakça": "Kaynakça"}
for kat in ["Tanımlama", "Çıkarsama", "Model", "Yorum", "Biçim", "Kaynakça"]:
    bs = [b for b in I.BULGULAR if b["kat"] == kat]
    if not bs: continue
    g(f"## {KAT_AD[kat]}"); g("")
    for b in bs:
        sd = b["sade"]
        g(f"### {b['id']} · {sd['baslik']}"); g("")
        g(f"**Önem:** {b['onem']} · **Tezdeki yer:** {b['yer']}"); g("")
        g(f"**Sorun ne?** {sd['sorun']}"); g("")
        g(f"**Neden önemli?** {sd['neden']}"); g("")
        g("**Ne yapılmalı?**"); g("")
        for i_, a_ in enumerate(sd["adimlar"], 1): g(f"{i_}. {a_}")
        g("")
        if sd["ornek"]:
            g("**Teze yazılabilecek örnek metin:**"); g(""); g(f"> {sd['ornek']}"); g("")
rehber = "\n".join(G)
(ROOT / "analiz" / "Sade_Anlatim_ve_Duzeltme_Rehberi.md").write_text(rehber, encoding="utf8")

# ---------------------------------------------------------------- site verisi
import juri2_rapor
J2W = juri2_rapor.uret(bugun)
for f in ["sonuclar.json", "panel.json", "spec_egrisi.json", "bootstrap_m1.json", "birim_kok.json", "ek_dogrulama.json", "simulasyon.json", "simulasyon_p.json", "juri2.json"]:
    if (I.CK / f).exists(): shutil.copy(I.CK / f, DOCS / "data" / f)
json.dump({"bulgular": I.BULGULAR, "dogrulanan": I.DOGRULANAN, "duzeltmeler": I.DUZELTMELER, "hipotez": I.HIPOTEZ, "juri": I.JURI, "juri2": I.JURI2, "juri_karsilastirma": I.JURI_KARSILASTIRMA, "juri2_cevap": I.JURI2_CEVAP, "bolumler": I.BOLUMLER, "kaynakca": I.KAYNAKCA, "atiflar": ATIFLAR, "n_kayit": N_KAYIT,
           "yapilacak": I.YAPILACAK, "oncelik": I.ONCELIK, "sozluk": SD.SOZLUK,
           "ozet": {"uyum": [OK, TOT], "se_fark": se_fark, "se_med": se_med, "tarih": bugun, "sim_yorum": SIMY}},
          open(DOCS / "data" / "icerik.json", "w"), ensure_ascii=False, default=float)
for src, dst in [(ROOT / "analiz" / "Kapsamli_Yeniden_Inceleme.md", "Kapsamli_Yeniden_Inceleme.md"), (ROOT / "analiz" / "arsiv" / "01_Ilk_Inceleme_ve_Juri_Analizi.md", "01_Ilk_Inceleme_ve_Juri_Analizi.md"),
                 (ROOT / "dokumanlar" / "Juri1_Degerlendirme_Raporu.md", "Juri1_Degerlendirme_Raporu.md"), (ROOT / "dokumanlar" / "Juri2_Degerlendirme_Raporu.md", "Juri2_Degerlendirme_Raporu.md"),
                 (ROOT / "analiz" / "Juri2_Raporu_Degerlendirmesi.md", "Juri2_Raporu_Degerlendirmesi.md"), (ROOT / "analiz" / "Sade_Anlatim_ve_Duzeltme_Rehberi.md", "Sade_Anlatim_ve_Duzeltme_Rehberi.md"), (ROOT / "dokumanlar" / "Bagimsiz_Hakem_Raporu.md", "Bagimsiz_Hakem_Raporu.md"),
                 (ROOT / "dokumanlar" / "Nihai_Model_19112026_metin.md", "Tez_Bolum5_metin.md")]:
    shutil.copy(src, DOCS / "raporlar" / dst)
print("atıf:", len(ATIFLAR), "kaynakça kaydı:", N_KAYIT, "eşleşmeyen:", [a["atif"] + " " + a["yil"] for a in ATIFLAR if not a["kaynakcada"]], "| jüri2 raporu:", J2W, "kelime")
print("uyum:", OK, "/", TOT, " | SH en büyük göreli fark:", round(se_fark, 3), " | rapor:", len(rapor.split()), "kelime | rehber:", len(rehber.split()), "kelime")
