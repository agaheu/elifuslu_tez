"""Güncellenmiş tez metnini üretir (bulgulara göre, izlenebilir değişikliklerle).

Girdi : dokumanlar/Nihai_Model_19112026_metin.md, analiz/cikti/*.json (tez_guncel.json dâhil)
Çıktı : docs/tez/guncel.html (değişiklik işaretli), docs/tez/sekiller/, docs/data/tez_degisiklik.json,
        dokumanlar/Nihai_Model_guncel_metin.md (temiz metin), dokumanlar/Nihai_Model_guncel.docx,
        analiz/Tez_Guncelleme_Degisiklik_Listesi.md
Kullanım: python analiz/py/tez_guncel_hesap.py 1999 && python analiz/py/tez_guncelle.py
"""
import json, re, shutil, datetime, subprocess, collections
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import tez_d1, tez_d2  # noqa: F401  (değişiklik tanımları)
import tezarac as T
from tez_sayi import yb, R, TG, tr
import icerik as IC

ROOT = T.ROOT; DOCS = ROOT / "docs"; (DOCS / "tez" / "sekiller").mkdir(parents=True, exist_ok=True)
bugun = datetime.date.today().strftime("%d.%m.%Y")
H = T.uygula(); T.bolum_ata(H); T.kaydet_cache()

# ------------------------------------------------------------------ Şekil 5.5 (bootstrap aralıklarıyla)
yil = list(range(1997, 2021)); b = [0 if y == 2004 else yb[str(y)]["b"] for y in yil]
sb = [0 if y == 2004 else yb[str(y)]["se_boot"] for y in yil]; sc = [0 if y == 2004 else yb[str(y)]["se_cl"] for y in yil]
fig, ax = plt.subplots(figsize=(8.2, 4.3), dpi=200)
for x in (2004.5, 2007.5, 2012.5): ax.axvline(x, color="#c3c2b7", lw=0.8, ls=(0, (4, 3)), zorder=1)
ax.axhline(0, color="#52514e", lw=0.8, zorder=1)
for y, v, s1, s2 in zip(yil, b, sb, sc):
    if y == 2004: continue
    ax.plot([y, y], [v - 2.1604 * s1, v + 2.1604 * s1], color="#9cc3ef", lw=5, solid_capstyle="butt", zorder=2)
    ax.plot([y, y], [v - 1.96 * s2, v + 1.96 * s2], color="#0b0b0b", lw=1.1, zorder=3)
ax.plot(yil, b, color="#2a78d6", lw=1.6, marker="o", ms=4.5, mfc="#2a78d6", mec="white", mew=0.8, zorder=4)
for x, t_ in ((2000.5, "ETS öncesi"), (2006, "Faz 1"), (2010, "Faz 2"), (2016.5, "Faz 3")): ax.text(x, 1.015, t_, ha="center", va="bottom", fontsize=9, color="#52514e", transform=ax.get_xaxis_transform())
ax.plot([], [], color="#9cc3ef", lw=5, label="%95 güven aralığı: bootstrap standart hatası, t(13)"); ax.plot([], [], color="#0b0b0b", lw=1.1, label="%95 güven aralığı: kümelenmiş standart hata")
ax.legend(loc="lower left", frameon=False, fontsize=8.5)
ax.set_xticks(range(1997, 2021, 2)); ax.set_xlim(1996.3, 2020.7); ax.set_ylabel("Yıl katsayısı (referans: 2004)", fontsize=9.5); ax.tick_params(labelsize=9)
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:.1f}".replace(".", ",").replace("-", "−")))
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.grid(axis="y", color="#e1e0d9", lw=0.6); ax.set_axisbelow(True)
fig.tight_layout(); fig.savefig(ROOT / "dokumanlar" / "sekiller" / "sekil5_5_guncel.png", facecolor="white"); plt.close(fig)
for f in (ROOT / "dokumanlar" / "sekiller").glob("*.png"): shutil.copy(f, DOCS / "tez" / "sekiller" / f.name)

# ------------------------------------------------------------------ site parçası
S = re.sub(r'(<img src=")media/([^"]+)"( style="[^"]*")?', r'\1tez/sekiller/\2"', H)
(DOCS / "tez" / "guncel.html").write_text(S, encoding="utf8")

UYGULANMAYAN = [
    ("T1", "Ülkeler arasında farklılaşan bir ETS ölçüsüyle (kapsam payı, ulusal tahsis planı sıkılığı) karşılaştırmalı analiz; yeşil olmayan patentlerle plasebo tahmini", "Yeni veri gerekir", "Sınırlılıklar bölümünde (5.11) ileriki çalışma olarak yazıldı."),
    ("T4", "Ar-Ge harcamalarının GSYİH'ye oranının kontrol değişkeni olarak eklenmesi", "Yeni veri gerekir", "Metinde Ar-Ge'nin modelde ayrıca yer almadığı belirtildi."),
    ("T8", "Birleşik Krallık'ın eklendiği 15 ülkeli sağlamlık tahmini; gerçek dışlama gerekçesi", "Yeni veri / yazar bilgisi gerekir", "Yanlış gerekçe çıkarıldı, durum sınırlılık olarak yazıldı."),
    ("T11", "Yıllık izin (EUA) fiyatıyla sağlamlık tahmini", "Yeni veri gerekir", "Tartışmaya karbon fiyatı paragrafı eklendi."),
    ("Y4", "Pakes ve Griliches (1984) “1,6 yıl” ve Bel ve Joseph (2018) kapsam / tahminci aktarımları", "Kaynaktan doğrulanmalı", "Metin değiştirilmedi; üç cümle “yazar kontrolü” olarak işaretlendi."),
    ("M4", "Pedroni istatistiğinin (+2,255) test yönü", "Yazılım çıktısından doğrulanmalı", "Metin değiştirilmedi; ifade “yazar kontrolü” olarak işaretlendi."),
    ("M4", "Birim kök ve eşbütünleşme bölümünün kısaltılıp tabloların eke taşınması; Westerlund (2007) testi", "Yazarın kararı", "Uygulanmadı; yalnızca etiket, dönem ve aşırı genelleme düzeltildi."),
    ("C4", "Tablo 5.13'te kontrol değişkenlerinin boş bırakılan güven aralığı hücreleri", "Stata çıktısından doldurulmalı", "Tablo notuna hatırlatma eklendi."),
    ("Y2", "H1–H4 hipotez cümlelerinin betimleyici fiillerle yeniden yazılması; H1'in “ilk iki faz” ile daraltılması", "Yazarın kararı", "Hipotez cümleleri değiştirilmedi (H5 hariç); değerlendirme tablosu (5.17) güncellendi."),
    ("C3", "Ülke bazında faz farklarını gösteren ek tablo", "İsteğe bağlı", "Uygulanmadı; ülke ağırlıkları tablosu (5.5a) eklendi."),
    ("B1", "Word biçim işlemleri: alt başlıkların başlık stillerine çevrilmesi, tablolardaki denklem nesnesi alt indislerin düz metne çevrilmesi", "Yalnızca Word dosyasında yapılabilir", "Metinde yapılabilenler uygulandı: denklem numaraları, simgeler, boş başlıklar, vurgular, değişken adları."),
    ("T3", "Tez özeti ve genel sonuç bölümündeki yüzde 44 / 101 / 89 rakamları", "Bu dosyada yok (5. bölüm dışı)", "Aynı düzeltme özet ve sonuç bölümlerinde de yapılmalı."),
]
GENEL_NOT = [
    "Eklenen bütün yeni sayılar bu incelemede Python ile hesaplandı (ham veriden, tezin Stata sonuçlarını 164/164 yeniden üreten kodla). Teze girmeden önce Stata ile yeniden üretilmeleri önerilir; bootstrap standart hataları tekrar sayısına ve rastgele sayı üretecine göre üçüncü ondalıkta değişebilir.",
    "Yeni tablolar mevcut numaralandırmayı bozmamak için harf ekiyle adlandırıldı (5.4 Panel B, 5.5a, 5.6a, 5.6b, 5.11a, 5.13a, 5.14a). Son nüshada tablolar baştan numaralandırılmalı ve metin içi göndermeler güncellenmelidir.",
    "Yeni alt bölüm 5.11 (Çalışmanın Sınırlılıkları) eklendi; içindekiler tablosu güncellenmelidir.",
    "Şekil 5.5 Python ile yeniden çizildi; tezin diğer şekilleriyle aynı görsel biçime getirilmesi gerekebilir.",
    "Özgün Word dosyasına dokunulmadı. Güncel metnin Word sürümü düz metinden üretildi; üniversitenin tez biçimini taşımaz, değişikliklerin özgün dosyaya aktarılması gerekir.",
]
say = collections.Counter(d["tur"] for d in T.DEG)
uyg = sorted({x for d in T.DEG for x in d["bulgu"]}, key=lambda x: [b_["id"] for b_ in IC.BULGULAR].index(x))
json.dump({"tarih": bugun, "degisiklikler": T.DEG, "uygulanmayan": UYGULANMAYAN, "genel_not": GENEL_NOT, "sayim": dict(say), "nokta": len(T.ED), "bulgu_sayisi": len(uyg), "B": TG["meta"]["B"]},
          open(DOCS / "data" / "tez_degisiklik.json", "w"), ensure_ascii=False)

# ------------------------------------------------------------------ temiz metin (markdown + docx)
C = T.temiz(H)
assert "data-d=" not in C and "<del" not in C and "<ins" not in C, re.findall(r".{60}data-d=.{60}", C)[:3]
tex = lambda m: (f'<span class="math display">\\[{m.group(2)}\\]</span>' if m.group(1) == "block" else f'<span class="math inline">\\({m.group(2)}\\)</span>')
CT = re.sub(r'<math display="(inline|block)"[^>]*>.*?<annotation encoding="application/x-tex">(.*?)</annotation></semantics></math>', tex, C, flags=re.S)
CT = re.sub(r'(<img src=")media/([^"]+)"( style="[^"]*")?', r'\1sekiller/\2"', CT)
md = T.pandoc(CT, frm="html", to="markdown", extra=())
bas = f"<!-- Bu dosya analiz/py/tez_guncelle.py tarafından üretilmiştir ({bugun}). Özgün metin: Nihai_Model_19112026_metin.md. Değişiklik listesi: analiz/Tez_Guncelleme_Degisiklik_Listesi.md -->\n\n"
(ROOT / "dokumanlar" / "Nihai_Model_guncel_metin.md").write_text(bas + md, encoding="utf8")
try:
    subprocess.run(["pandoc", "-f", "html", "-t", "docx", "--resource-path", str(ROOT / "dokumanlar"), "-o", str(ROOT / "dokumanlar" / "Nihai_Model_guncel.docx")], input=CT, text=True, check=True, capture_output=True)
    docx_ok = True
except Exception as ex:
    docx_ok = False; print("docx üretilemedi:", str(ex)[:300])

# ------------------------------------------------------------------ değişiklik listesi (markdown)
L = []; w = L.append
BAS = {b_["id"]: b_["sade"]["baslik"] if "sade" in b_ else b_["baslik"] for b_ in IC.BULGULAR}
try:
    import sade as SD
    BAS = {k: v["baslik"] for k, v in SD.SADE.items()}
except Exception: pass
w("# Tez Güncellemesi: Değişiklik Listesi"); w("")
w(f"**Güncellenen belge:** `dokumanlar/Nihai_Model_19112026_metin.md` (Beşinci Bölüm ve kaynakça) · **Güncel metin:** `dokumanlar/Nihai_Model_guncel_metin.md` · **Tarih:** {bugun}"); w("")
w("> Tez metni, kapsamlı yeniden incelemedeki bulgulara ve önerilere göre güncellenmiştir. **Yalnızca bulgularda sorun olarak işaretlenen yerlere dokunulmuştur;** sorunsuz bulunan kısımlar aynen korunmuştur. Her değişiklik bir bulgu numarasına bağlıdır (`analiz/Kapsamli_Yeniden_Inceleme.md`, Kısım 5). Değişikliklerin metin içinde işaretli hâli sitededir (Güncellenmiş tez sayfası)."); w("")
w("## Özet"); w("")
w(f"- {len(T.DEG)} değişiklik kaydı, metinde {len(T.ED)} nokta; 36 bulgunun {len(uyg)}'i için en az bir değişiklik uygulandı.")
w("- Türlere göre: " + ", ".join(f"{v} {k}" for k, v in say.most_common()) + ".")
w("- “Kontrol” türündeki kayıtlarda metin **değiştirilmemiş**, yazarın kaynaktan ya da yazılım çıktısından doğrulaması gereken ifade işaretlenmiştir.")
w("")
w("## Genel notlar"); w("")
for g_ in GENEL_NOT: w(f"- {g_}")
w("")
w("## Uygulanmayan ya da yazara bırakılan öneriler"); w("")
w("| Bulgu | Öneri | Neden uygulanmadı | Ne yapıldı |"); w("|---|---|---|---|")
for a, b_, c_, d_ in UYGULANMAYAN: w(f"| {a} | {b_} | {c_} | {d_} |")
w("")
w("## Değişiklikler (metindeki sırayla)"); w("")
kisalt = lambda s, n: (s[:n] + "…") if len(s) > n else s
sira = {m.group(1): i for i, m in reversed(list(enumerate(re.finditer(r'data-d="(D\d+)"', H))))}
for d in sorted(T.DEG, key=lambda d: sira.get(d["no"], 10 ** 9)):
    w(f"### {d['no']} · Bölüm {d['bolum']} · {', '.join(d['bulgu'])} · {d['tur']}"); w("")
    if d["ozet"]: w(f"**Gerekçe.** {d['ozet']}"); w("")
    if d["eski"]: w(f"**Önceki metin.** {kisalt(d['eski'], 500)}"); w("")
    if d["yeni"]: w(f"**{'Yazar için not' if d['tur'] == 'kontrol' else 'Yeni metin'}.** {kisalt(d['yeni'], 800)}"); w("")
w("## Bulgulara göre dizin"); w("")
w("| Bulgu | Konu | Değişiklikler |"); w("|---|---|---|")
for b_ in IC.BULGULAR:
    ds = [d["no"] for d in sorted(T.DEG, key=lambda d: sira.get(d["no"], 10 ** 9)) if b_["id"] in d["bulgu"]]
    w(f"| {b_['id']} | {BAS[b_['id']]} | {', '.join(ds) if ds else '– (yalnızca “uygulanmayan öneriler” tablosunda)'} |")
w("")
liste = "\n".join(L)
(ROOT / "analiz" / "Tez_Guncelleme_Degisiklik_Listesi.md").write_text(liste, encoding="utf8")
(DOCS / "raporlar").mkdir(exist_ok=True)
shutil.copy(ROOT / "analiz" / "Tez_Guncelleme_Degisiklik_Listesi.md", DOCS / "raporlar" / "Tez_Guncelleme_Degisiklik_Listesi.md")
print(len(T.DEG), "değişiklik,", len(T.ED), "nokta,", len(uyg), "bulgu | bölümü bulunamayan:", [d["no"] for d in T.DEG if d["bolum"] == "?"], "| docx:", docx_ok, "| temiz metin:", len(md.split()), "kelime (özgün:", len(T.SRC.read_text(encoding='utf8').split()), ")")
