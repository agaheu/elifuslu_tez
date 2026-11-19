"""İkinci jüri raporunun ayrı değerlendirme raporu: analiz/Juri2_Raporu_Degerlendirmesi.md (rapor_uret.py çağırır)."""
import icerik as I
from icerik import R, J, tr, pv, P, N, ROOT

FAM = {P: "Poisson QML", N: "Negatif binom"}


def uret(tarih):
    L = []; w = L.append

    def tablo(bas, satirlar):
        w("| " + " | ".join(bas) + " |"); w("|" + "|".join(["---"] * len(bas)) + "|")
        for s in satirlar: w("| " + " | ".join(str(x) for x in s) + " |")
        w("")

    say = {}
    for j in I.JURI2: say[j[3]] = say.get(j[3], 0) + 1
    w("# İkinci Jüri Raporunun Değerlendirmesi"); w("")
    w(f"**Değerlendirilen belge:** `dokumanlar/Juri2_Degerlendirme_Raporu.docx` (metni: `dokumanlar/Juri2_Degerlendirme_Raporu.md`) · **Tarih:** {tarih}")
    w("")
    w("> İkinci jüri ekibinin raporundaki her madde (4 güçlü yön, 5 yöntemsel eleştiri, 5 tutarlılık notu ve kapanış yargısı) tek tek ele alındı. Her madde için jürinin ifadesi, benim değerlendirmem ve bu değerlendirmenin dayandığı hesap verilmiştir. Jürinin önerdiği sınamalar (ön-örneklem ortalaması tahmincisi, sıfır-kesikli model, İrlanda'nın etkisi) uygulanmıştır: `analiz/py/juri2.py` → `analiz/cikti/juri2.json`. Bulgu numaraları (T1, C9 …) ana rapora, `analiz/Kapsamli_Yeniden_Inceleme.md` Kısım 5'e atıftır. Sayılar hesap çıktılarından otomatik çekilir.")
    w("")
    w("## 1. Özet"); w("")
    w("İkinci jüri raporu kısa, isabetli ve yapıcı; beş eleştirisinin dördü birinci jüri raporu ve benim incelememle örtüşüyor, üç yeni öneri getiriyor (ön-örneklem ortalaması tahmincisi, karbon fiyatı, yeşil olmayan patentlerle plasebo). Üç noktada veriyle çelişiyor ya da fazla iyimser:")
    w("")
    w(f"1. **Çıkarsama övgüsü veriyle çelişiyor (G3).** Rapor, eşli bootstrap ve BC aralıklarının birinci tip hatayı “başarıyla kontrol ettiğini” söylüyor. Gerçek etkinin sıfır olduğu benzetimlerde bu yöntem %5 yerine {I.simrg('rej_boot', 'A')} oranında reddediyor.")
    w(f"2. **Önerilen çare sorunu çözmüyor (E1).** Stok eleştirisini “karşılayacağı” söylenen ön-örneklem ortalaması tahmincisi uygulandığında Model 1'in faz katsayıları sıfıra iniyor (negatif binom Faz 2: {tr(I.jp('psm', I.PSA, N, 'F2'), 3)}). Tezi ayakta tutan Model 2: Faz 1 eğimi ve Faz 2 düzeyi bu tahmincide de anlamlı.")
    w("3. **Kapanış yargısı fazla iyimser (S).** Listelenen düzeltmeler gerekli ama yeterli değil; raporun değinmediği altı kritik/önemli nokta var (Kısım 6).")
    w("")
    tablo(["Değerlendirme", "Madde sayısı", "Maddeler"], [[k, v, ", ".join(j[0] for j in I.JURI2 if j[3] == k)] for k, v in say.items()])
    w("İkinci jürinin iki küçük önerisi (sıfır-kesikli model, İrlanda) sınandı ve sonuçları değiştirmediği görüldü; tezde birer dipnot yeterli.")
    w("")

    w("## 2. Madde madde değerlendirme"); w("")
    grp = {"Güçlü yön": "2.1 Güçlü yönler ve özgün katkılar", "Eleştiri": "2.2 Ekonometrik ve yöntemsel eleştiriler", "Tutarlılık": "2.3 Veri seti ve metin içi tutarlılık denetimi", "Kapanış": "2.4 Kapanış yargısı"}
    for g, bas in grp.items():
        w(f"### {bas}"); w("")
        for j in [x for x in I.JURI2 if x[1] == g]:
            w(f"#### {j[0]} · {j[2]}"); w("")
            w(f"**Jürinin ifadesi.** {j[5]}"); w("")
            w(f"**Değerlendirme: {j[3]}.** {j[6]}"); w("")
            if j[7]: w(f"**Ana rapordaki ilgili bulgular:** {', '.join(j[7])}"); w("")

    w("## 3. Önerilen sınamaların tam sonuçları"); w("")
    w("### 3.1 Ön-örneklem ortalaması tahmincisi (E1)"); w("")
    w("Ülke kuklaları çıkarılıp ülke heterojenliği ön-örneklem dönemi bilgisiyle kontrol edildi (Blundell, Griffith ve Windmeijer, 2002). Ön-örneklem: patent için 1990–1996, GSYİH için 1995–1996. Hücreler: katsayı (ülke-kümeli t(13) p değeri).")
    w("")
    f = lambda d, k: f"{tr(d[k]['b'], 3)} ({pv(d[k]['p_t'])})" if k in d else "–"
    rows = []
    for nm, v in J["psm"].items():
        for fam in (N, P):
            rows.append([nm, FAM[fam], f(v[fam], "F1"), f(v[fam], "F2"), f(v[fam], "F3"), f(v[fam], "lnK1")])
    tablo(["Tanım", "Tahminci", "Faz 1", "Faz 2", "Faz 3", "Stok katsayısı"], rows)
    w("Okuma: (A) ve (B) tanımlarında stok katsayısı bire yaklaşıyor ve faz farkları kayboluyor; (C) tanımında stok katsayısı düşüyor ve faz farkları geri geliyor; stoksuz tanımlar (D, E) sabit etkili stoksuz tahminlere benziyor. 14 ülkelik yatay kesitte ülke heterojenliğini tek ya da iki değişkenle kontrol etmek kararsız; bu tahminci Model 1 için net bir hüküm vermiyor, ama sabit etkili tahminin tek doğru olmadığını gösteriyor.")
    w("")
    w("**Model 2 (kesintili zaman serisi), ön-örneklem ortalamalı (A tanımı):**"); w("")
    AD2 = {"tstar": "ETS öncesi eğilim", "F1": "Faz 1 düzey", "S1": "Faz 1 eğim", "F2": "Faz 2 düzey", "S2": "Faz 2 eğim", "F3": "Faz 3 düzey", "S3": "Faz 3 eğim", "lnK1": "Stok"}
    tablo(["Katsayı", "Negatif binom", "Poisson QML", "Tezin sabit etkili tahmini (NB)"], [[AD2[k], f(J["psm_m2"][N], k), f(J["psm_m2"][P], k), tr(R["m2"][N]["coef"][k]["b"], 3)] for k in AD2])
    w("Faz 1 eğimi ve Faz 2 düzeyi iki tahmincide de sabit etkili tahminlere çok yakın ve anlamlı. Bu, tezin en dayanıklı bulgusunun Model 2'de olduğunu bir kez daha gösteriyor. Kayıt: bu tanımda stok katsayısı biri aşıyor, ETS öncesi eğilim negatif ve Faz 3 eğimi pozitif çıkıyor; stok ile eğilim arasındaki paylaşım burada da kararsız olduğundan bu üç katsayıya ağırlık verilmemeli.")
    w("")
    w("### 3.2 Sıfır-kesikli model (E5)"); w("")
    Z = J["sifir"]
    tablo(["", "Faz 1", "Faz 2", "Faz 3", "Stok"], [
        ["Poisson (tezdeki)"] + [tr(Z["normal_poisson"][k], 4) for k in ("F1", "F2", "F3", "lnK1")],
        ["Sıfır-kesikli Poisson"] + [tr(Z["zt_poisson"][k], 4) for k in ("F1", "F2", "F3", "lnK1")],
        ["Negatif binom (tezdeki)"] + [tr(Z["normal_nb"][k], 4) for k in ("F1", "F2", "F3", "lnK1")],
        ["Sıfır-kesikli negatif binom"] + [tr(Z["zt_nb"][k], 4) for k in ("F1", "F2", "F3", "lnK1")]])
    w(f"Modele göre beklenen sıfır sayısı {tr(Z['beklenen_sifir_poisson'], 2)} (Poisson) ve {tr(Z['beklenen_sifir_nb'], 2)} (NB); gözlenen 0. En küçük beklenen değer {tr(Z['min_mu_nb'], 1)} ({Z['en_kucukler'][0][0]} {int(Z['en_kucukler'][0][1])}). 3 ve altında {Z['y_le_3']}, 5 ve altında {Z['y_le_5']} gözlem var. Yunanistan ve Portekiz çıkarıldığında: NB {tr(I.jp('sifir', 'GR_PT_haric', N, 'F1'), 3)} / {tr(I.jp('sifir', 'GR_PT_haric', N, 'F2'), 3)} / {tr(I.jp('sifir', 'GR_PT_haric', N, 'F3'), 3)}; Poisson {tr(I.jp('sifir', 'GR_PT_haric', P, 'F1'), 3)} / {tr(I.jp('sifir', 'GR_PT_haric', P, 'F2'), 3)} / {tr(I.jp('sifir', 'GR_PT_haric', P, 'F3'), 3)}.")
    w("")
    w("### 3.3 İrlanda 2015 (E3)"); w("")
    IR = J["irlanda"]
    rows = []
    for nm, key in [("Tezin ana modeli", None), ("İrlanda hariç", "haric"), ("İrlanda × 2015 sonrası kuklası eklenmiş", "kukla_2015_sonrasi"), ("Serbest GSYİH esnekliği, tam örneklem", "serbest_tam"), ("Serbest GSYİH esnekliği, İrlanda hariç", "serbest_haric")]:
        for fam in (N, P):
            d = IR[key][fam] if key else {k: {"b": R["m1"][fam]["coef"][k]["b"], "p_t": R["m1"][fam]["coef"][k]["p_cl_t"]} for k in ("F1", "F2", "F3")}
            rows.append([nm, FAM[fam], f(d, "F1"), f(d, "F2"), f(d, "F3"), f(d, "lngdp") if "lngdp" in d else (f(d, "IE15") + " (kukla)" if "IE15" in d else "–")])
    tablo(["Tanım", "Tahminci", "Faz 1", "Faz 2", "Faz 3", "GSYİH esnekliği / kukla"], rows)
    w(f"İrlanda'nın reel GSYİH'si 2014'te {tr(IR['gsyih_2014_2015'][0] / 1000, 1)}, 2015'te {tr(IR['gsyih_2014_2015'][1] / 1000, 1)} milyar €. Aynı yıl başvuru sayısı {IR['ccm_2014_2016'][0]} → {IR['ccm_2014_2016'][1]} → {IR['ccm_2014_2016'][2]} seyrettiği için yoğunluk 2015'te düşmedi ({tr(IR['yogunluk_2014_2016'][0], 3)} → {tr(IR['yogunluk_2014_2016'][1], 3)} → {tr(IR['yogunluk_2014_2016'][2], 3)}); GSYİH düzeyindeki kalıcı sıçrama sonraki yıllarda yoğunluğu mekanik olarak düşürüyor. İrlanda'nın Poisson tahminindeki ağırlığı %{tr(IR['poisson_agirlik'], 1)}.")
    w("")
    w("### 3.4 Tahmin döneminin başlangıcı (K3)"); w("")
    E = J["eksik"]
    tablo(["Değişken", "14 ülke için tam olduğu ilk yıl", "Eksik ülke sayısı (yıl: adet)"], [
        ["Reel GSYİH", E["ilk_tam_yil"]["gdp_real"], ", ".join(f"{y}: {n}" for y, n in E["gdp_real"].items())],
        ["GSYİH büyüme oranı", E["ilk_tam_yil"]["gdp_growth"], ", ".join(f"{y}: {n}" for y, n in E["gdp_growth"].items())],
        ["İmalat payı", E["ilk_tam_yil"]["manuf"], ", ".join(f"{y}: {n}" for y, n in E["manuf"].items())],
        ["Patent, ithalat bağımlılığı, yenilenebilir payı, ticaret", "1990", "eksik yok"]])
    w("Büyüme oranı 1996'dan itibaren tam olduğundan, bir dönem gecikmeyle tahmin 1997'de başlayabiliyor. Jürinin açıklaması doğru; teze bir cümleyle eklenmeli.")
    w("")

    w("## 4. Karbon fiyatı üzerine (E2)"); w("")
    w(I.B_["T11"]["tespit"]); w(""); w(I.B_["T11"]["kanit"]); w("")
    w("Fiyat verileri için dayanak: 2008 ortasındaki ≈30 € zirvesi ve sonrasındaki gerileme, 2016'daki ≈5 € düzeyi ile 2018 (15,5 €) ve 2019 (24,7 €) yıllık ortalamaları Avrupa Çevre Ajansı ve Hollanda İstatistik Kurumu yayınlarından; Faz 1 fiyat çöküşü tezin kaynakçasındaki Ellerman çalışmalarından. Tam yıllık seri elimde olmadığı için sayısal bir tahmin yapmadım; bu, tezde yapılması gereken bir ek analizdir.")
    w("")

    w("## 5. İki jüri raporunun karşılaştırması"); w("")
    tablo(["Konu", "1. jüri raporu", "2. jüri raporu", "Ana rapordaki karşılığı"], I.JURI_KARSILASTIRMA)
    w("İki rapor dört temel eleştiride birleşiyor (ortak şoklar, stok, maruziyet, birim kök). Ayrıştıkları tek esaslı nokta bootstrap: birinci jüri yöntemi sorguluyor, ikinci jüri övüyor; benzetim sonuçları birinci jüriyi destekliyor. Genel hükümde birinci jüri daha temkinli (“nedensel tanımlama yetersiz”), ikinci jüri daha iyimser (“düzeltmelerle yayına hazır”); bu incelemenin vardığı sonuç birinci jürinin hükmüne daha yakın.")
    w("")

    w("## 6. İkinci jüri raporunun değinmediği noktalar"); w("")
    for _id in ["T2", "T3", "C9", "T6", "T7", "T8", "C3", "M3", "Y1"]:
        b = I.B_[_id]; w(f"- **{_id} ({b['onem']}).** {b['baslik']}.")
    w("")
    w("Bunların ilk altısı savunmada ya da hakem sürecinde belirleyici olabilecek nitelikte; ayrıntıları ana raporun 5. kısmında.")
    w("")

    w("## 7. Savunma için cevap taslakları"); w("")
    for q, a in I.JURI2_CEVAP:
        w(f"**Soru: {q}**"); w(""); w(a); w("")

    w("## 8. Bu değerlendirme sonucunda ana raporda yapılan güncellemeler"); w("")
    for s in [
        "**Yeni bulgu T11** (karbon fiyatı): ikinci jürinin fiyat eleştirisi ve yıl etkileriyle karşılaştırması.",
        "**Yeni bulgu M8** (sıfır-kesikli model): önerinin sınanması; sonuç değişmiyor.",
        "**T5 genişletildi:** kesin dışsallık çerçevesi; ön-örneklem ortalaması tahmincisinin altı varyantı; Model 2'nin bu tahmincide de ayakta kaldığı.",
        "**T1 güncellendi:** yeşil olmayan EPO başvurularıyla plasebo sonuç önerisi.",
        "**M1 güncellendi:** İrlanda 2015 sınaması.",
        "**C9 ve T7'ye not eklendi:** ikinci jürinin “birinci tip hata kontrol ediliyor” ve “kalıcı düzey sıçraması” nitelemelerinin veriyle karşılaştırması.",
        "**Y6 güncellendi:** tahmin döneminin 1997'de başlama gerekçesi.",
        "**Kaynak etiketleri:** T1, T4, T5, M1, M4, Y6, B1, B2 bulgularına “2. jüri raporu” kaynağı eklendi.",
        "**Yeni Kısım 9** (ikinci jüri raporunun analizi) ve **Kısım 13** (tez bölümlerine göre bulgu haritası, kaynakça denetimi) eklendi; yapılacaklar listesine üç madde eklendi; “önceki incelememdeki düzeltmeler” tablosuna ön-örneklem tahmincisi notu eklendi.",
    ]:
        w(f"- {s}")
    w("")
    w("## 9. Yeniden üretim"); w("")
    w("```bash"); w("python analiz/py/juri2.py"); w("```"); w("")
    w("```bash"); w("python analiz/py/rapor_uret.py"); w("```"); w("")
    (ROOT / "analiz" / "Juri2_Raporu_Degerlendirmesi.md").write_text("\n".join(L), encoding="utf8")
    return len(" ".join(L).split())
