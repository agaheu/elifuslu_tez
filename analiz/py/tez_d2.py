"""Tez güncellemesi, 2. kısım: Bölüm 5.7–5.10, yeni 5.11 ve kaynakça."""
import re
from tezarac import *
from tezarac import _no, _ekle, _at
from tez_sayi import *

YN = r"\*\*\* p \< 0,01; \*\* p \< 0,05; \* p \< 0,10."
T13 = "Anlamlılık düzeyleri 13 serbestlik dereceli t dağılımına göre belirlenmiştir."
anl = lambda p: (duzey(p) + " düzeyinde anlamlı") if duzey(p) else "anlamsız"
ga = lambda ad, fam, k: anl(g(ad, fam, k, "p_boot_t"))

# ============================================================ 5.7.1
t11 = TZ.T511
G_YIL = hucre("C6", "5.11", "Faz 1 (2005", 4, tezh(*t11[P]["F1"][:2]), "Yıldızlar 13 serbestlik dereceli t dağılımına göre yeniden belirlendi (Tablo 5.11, 5.13, 5.14 ve 5.17): beş katsayı bir kademe düştü.")
hucre("C6", "5.11", "Faz 2 (2008", 4, tezh(*t11[P]["F2"][:2]), "", grup=G_YIL)
hucre("C6 C8", "5.11", "Ticaret açıklığı", 1, tezh(*t11[N]["trade_l1"][:2]), "", grup=G_YIL)
assert tezh(*t11[P]["F1"][:2]).count("*") == 1 and tezh(*t11[P]["F2"][:2]).count("*") == 2 and tezh(*t11[N]["F1"][:2]).count("*") == 2 and tezh(*t11[N]["F2"][:2]).count("*") == 3
ek("C4 C6 T5", YN, T13 + " Bootstrap dağılımları çarpık olduğundan sapma düzeltmeli aralıklar asimetriktir; yüzdelik aralıklar Tablo 5.11a'da verilmiştir. Yeşil patent stoku bağımlı değişkenin geçmişinden türetildiğinden faz katsayıları yukarı yanlı olabilir ve üst sınır olarak okunmalıdır (Bölüm 5.6.4).",
   "Tablo 5.11 notuna üç uyarı eklendi: t(13), BC aralıklarının asimetrisi, stok kaynaklı yukarı yanlılık.", kacinci=1)

nbF1 = [bo("m1", N, "F1", "p"), pt(c("m1", N, "F1"), bo("m1", N, "F1")), c("m1", N, "F1", "p_cv3")]
nbF2 = [bo("m1", N, "F2", "p"), pt(c("m1", N, "F2"), bo("m1", N, "F2")), c("m1", N, "F2", "p_cv3")]
poF1 = [bo("m1", P, "F1", "p"), pt(c("m1", P, "F1"), bo("m1", P, "F1")), c("m1", P, "F1", "p_cv3")]
assert max(nbF2) < .05 and max(nbF1) < .05 and max(poF1) > .10 and pt(*t11[P]["F1"][:2]) < .10 and pt(*t11[P]["F2"][:2]) < .05
deg("C5", "Bulgular, AB ETS'nin ilk iki fazında yeşil patent yoğunluğunun ETS öncesi döneme göre anlamlı biçimde yükseldiğini göstermektedir.",
    "Bulgular, AB ETS'nin ilk iki fazında yeşil patent yoğunluğunun ETS öncesi döneme göre daha yüksek olduğunu göstermektedir. İkinci faz farkı negatif binom tahmincisinde kullanılan bütün çıkarsama yöntemlerinde anlamlıdır; birinci faz farkı ise negatif binom tahmincisinde anlamlı ya da sınırda, Poisson tahmincisinde çıkarsama yöntemine duyarlıdır (Tablo 5.11a).",
    "İki faz için tek cümlelik “anlamlı biçimde yükseldi” yargısı ayrıştırıldı: ikinci faz güçlü, birinci faz temkinli.")
cik("C4", "Her iki fazın sapma düzeltmeli güven aralığı sıfırı içermemektedir.", "Anlamlılık yargısı kararsız BC aralıklarına dayandırılmıyor.")
deg("C6 C3", "Poisson QML modeli de aynı sonucu vermektedir: Birinci fazın etkisi yüzde 8,0, ikinci fazın etkisi yüzde 21,6'dır ve her iki katsayı da istatistiksel olarak anlamlıdır.",
    "Poisson QML modelinde birinci fazın farkı yüzde 8,0 (yüzde 10 düzeyinde anlamlı), ikinci fazın farkı yüzde 21,6'dır (yüzde 5 düzeyinde anlamlı). İki tahminci arasındaki fark büyük ölçüde ağırlıklandırmadan kaynaklanmaktadır: Poisson katsayıları başvuru ağırlıklı, negatif binom katsayıları ülkelere daha eşit ağırlık veren ortalama farkları göstermektedir (Bölüm 5.6.1).",
    "Poisson sonuçlarının anlamlılık düzeyleri t(13)'e göre düzeltildi; iki tahminci arasındaki farkın nedeni yazıldı.")
ek("Y3", "Üçüncü fazın katsayısı ise her iki modelde de sıfırdan anlamlı biçimde farklı değildir.",
   "Başka bir deyişle üçüncü fazda, yeşil patent stoku sabitken ETS öncesine göre ek bir fark bulunduğuna ilişkin yeterli istatistiksel kanıt elde edilememiştir; tahminin belirsizliği yüksek olduğundan bu sonuç, üçüncü fazın etkisiz olduğu biçiminde yorumlanmamalıdır.",
   "“Etki yok” ile “kanıt bulunamadı” ayrımı yapıldı (birinci jürinin istediği ifade).")
G_512 = hucre("C4 Y3", "5.12", "Faz 3 (2013", 3, yaral(*t11[N]["F3"][2:]), "Tablo 5.12'de “Anlamsız” yerine güven aralığının kendisi yazıldı (Tablo 5.11'deki aralıkların yüzdeye çevrilmiş hâli).")
hucre("C4 Y3", "5.12", "Faz 3 (2013", 6, yaral(*t11[P]["F3"][2:]), "", grup=G_512)
deg("T4", "Bu sonuçlar, sistemin en güçlü doğrudan etkisinin ikinci fazda ortaya çıktığını, üçüncü fazda ise doğrudan etkinin belirgin biçimde zayıfladığını göstermektedir.",
    "Bu sonuçlar, stok sabitken gözlenen farkın en yüksek değerine ikinci fazda ulaştığını, üçüncü fazda ise belirgin biçimde küçüldüğünü göstermektedir.", "“Doğrudan etki” terimi değiştirildi.")
assert pt(*t11[N]["trade_l1"][:2]) < .10 and bo("m1", P, "trade_l1", "p") > .10
deg("C8", "Kontrol değişkenleri arasında dış ticaret açıklığı, negatif binom modelinde negatif ve yüzde 5 düzeyinde anlamlıdır. Ticaret açıklığındaki 10 puanlık bir artış, yeşil patent yoğunluğunu yaklaşık yüzde 4,8 azaltmaktadır.",
    "Kontrol değişkenleri arasında dış ticaret açıklığının katsayısı negatif binom modelinde negatif ve yüzde 10 düzeyinde anlamlıdır; Poisson modelinde anlamlı değildir. Bu nedenle dış ticaret açıklığına ilişkin güçlü bir yorum yapılmamıştır.",
    "Sınırdaki ve tek tahminciye özgü sonuca iktisadi yorum yüklenmedi.")
ek("M3", "iktisadi büyümenin yeşil patent yoğunluğu üzerinde anlamlı bir ek etkisinin saptanmadığını göstermektedir.",
   "Ancak bu değişkenler ülke içinde yeşil patent stokuyla birlikte hareket ettiğinden (Tablo 5.4, Panel B), etkileri stokun etkisinden ayrıştırılamamış olabilir.", "Kontrol değişkenlerinin anlamsızlığı “etki yok” diye değil, “ayrıştırılamadı” diye yorumlandı.")

sat = "| Katsayı | Tahminci | Katsayı | Bootstrap SH | p: bootstrap, normal | p: bootstrap, $t(13)$ | p: küme jackknife, $t(13)$ | p: parametrik bootstrap (tek yönlü) | %95 yüzdelik aralık |\n|---|---|---|---|---|---|---|---|---|\n"
for m_, k, ad, j in [("m1", "F1", "Birinci model: Faz 1", 0), ("m1", "F2", "Birinci model: Faz 2", 1), ("m1", "F3", "Birinci model: Faz 3", 2), ("m2", "S1", "İkinci model: Faz 1 eğim", 4), ("m2", "F2", "İkinci model: Faz 2 düzey", 5)]:
    for fam in (N, P):
        b_, se = c(m_, fam, k), bo(m_, fam, k); lo, hi = bo(m_, fam, k, "pct")
        sat += f"| {ad} | {FAM[fam]} | {tr(b_, 4)} | {tr(se, 4)} | {pv(bo(m_, fam, k, 'p'))} | {pv(pt(b_, se))} | {pv(c(m_, fam, k, 'p_cv3'))} | {mcr(fam, j)} | \\[{tr(lo, 4)}; {tr(hi, 4)}\\] |\n"
for m_, k in [("m2", "S1"), ("m2", "F2")]:
    assert max(bo(m_, N, k, "p"), pt(c(m_, N, k), bo(m_, N, k)), c(m_, N, k, "p_cv3")) < .05
blok("C5 C4 C9", "Diğer kontrol değişkenlerinin katsayıları bootstrap çıkarsamasıyla istatistiksel olarak anlamlı değildir.",
     f"""Tablo 5.11a, temel katsayılara ilişkin çıkarsamanın kullanılan yönteme duyarlılığını göstermektedir. İkinci faz farkı ile ikinci modeldeki birinci faz eğim artışı ve ikinci faz düzey farkı, negatif binom tahmincisinde kullanılan bütün çıkarsama yöntemlerinde yüzde 5 düzeyinde anlamlıdır. Birinci modeldeki birinci faz farkı negatif binom tahmincisinde bootstrap ve küme jackknife ile yüzde 5 düzeyinde anlamlı, parametrik bootstrap ile sınırdadır (p = {mcr(N, 0)}); Poisson tahmincisinde ise küme jackknife (p = {pv(c('m1', P, 'F1', 'p_cv3'))}) ve parametrik bootstrap (p = {mcr(P, 0)}) ile anlamlı değildir. Poisson tahmincisinde ikinci faz farkı küme jackknife ile yüzde 10 düzeyinde anlamlıdır (p = {pv(c('m1', P, 'F2', 'p_cv3'))}).

**Tablo 5.11a.** Temel Katsayılar İçin Çıkarsama Duyarlılığı

{sat}
Not: Bootstrap standart hataları ve yüzdelik aralıklar ülke düzeyinde kümelenmiş {R['meta']['B']} tekrarlı eşli bootstrap ile yeniden hesaplanmıştır; Tablo 5.11 ve 5.13'teki 1000 tekrarlı değerlerden en çok yüzde 9 farklıdır. Küme jackknife, her seferinde bir ülke dışarıda bırakılarak hesaplanmıştır. Parametrik bootstrap, faz etkilerinin sıfır olduğu varsayımı altında tahmin edilen modelden üretilen {tr(SP['ayar']['tekrar'], 0)} yapay örneklemde, gözlenen katsayı kadar ya da daha büyük bir katsayının elde edilme sıklığıdır; aralık, dört veri üretim senaryosundaki en küçük ve en büyük değeri göstermektedir.""",
     "Çıkarsama duyarlılığı tablosu eklendi: dört yöntemle p değerleri ve yüzdelik aralıklar.")

# ============================================================ 5.7.2
t13_ = TZ.T513
hucre("C6 C8", "5.13", "Ticaret açıklığı", 1, tezh(*t13_[N]["trade_l1"][:2]), "", grup=G_YIL)
hucre("Y6", "5.13", "Faz 1 ortak test", 4, "15,39 (0,000)", "χ²(2) = 15,39 için olasılık değeri 0,000'dır (0,001 değil).")
ek("C6", YN, T13 + " Kontrol değişkenlerinin güven aralıkları yazılım çıktısından eklenmelidir.", "Tablo 5.13 notu: t(13). YAZAR: kontrol değişkenlerinin boş bırakılan güven aralığı hücreleri Stata çıktısından doldurulmalı.", kacinci=2)
ms = TG["m2_stoksuz"]
deg("T2", "Bu sonuç, birinci modelde tahmin edilen faz etkilerinin ETS'den önce başlamış bir yükselişin devamı olmadığı yorumunu desteklemektedir.",
    f"Ancak stok, geçmiş başvuruların birikimi olduğundan zamanla yüksek düzeyde eşdoğrusaldır (ülke içi korelasyon {tr(ik['lnK1~zaman'], 2)}). Stok modelden çıkarıldığında ETS öncesi dönemde yılda yaklaşık yüzde {yuzde(ms[N]['tstar']['b'])} (negatif binom; {ga('m2_stoksuz', N, 'tstar')}) ve yüzde {yuzde(ms[P]['tstar']['b'])} (Poisson; {ga('m2_stoksuz', P, 'tstar')}) düzeyinde bir artış eğilimi görülmektedir (Tablo 5.13a). Dolayısıyla ETS öncesinde eğilim bulunmadığı sonucu, stokun modelde yer almasına bağlıdır. Birinci fazdaki eğim artışı ve ikinci fazın başındaki düzey farkı ise stoksuz modelde de ortaya çıkmaktadır: negatif binom modelinde eğim artışı {tr(ms[N]['S1']['b'], 3)} ({ga('m2_stoksuz', N, 'S1')}), düzey farkı {tr(ms[N]['F2']['b'], 3)} ({ga('m2_stoksuz', N, 'F2')}); Poisson modelinde sırasıyla {tr(ms[P]['S1']['b'], 3)} ({ga('m2_stoksuz', P, 'S1')}) ve {tr(ms[P]['F2']['b'], 3)} ({ga('m2_stoksuz', P, 'F2')}).",
    "“ETS öncesi eğilim yok” sonucunun stoka bağlı olduğu yazıldı; stoksuz ikinci model sonuçları eklendi.")
deg("Y6", "negatif binom modelinde yaklaşık yüzde 11,7, Poisson modelinde yüzde 9,1 yükselmiştir.", "negatif binom modelinde yaklaşık 11,7 yüzde puan, Poisson modelinde 9,1 yüzde puan daha yüksektir.", "Birim hatası: yüzde değil yüzde puan.")
IT = [("ETS öncesi eğilim ($t^{*}$)", "tstar"), (r"Faz 1 düzey ($\lambda_{1}$)", "F1"), (r"Faz 1 eğim ($\phi_{1}$)", "S1"), (r"Faz 2 düzey ($\lambda_{2}$)", "F2"), (r"Faz 2 eğim ($\phi_{2}$)", "S2"), (r"Faz 3 düzey ($\lambda_{3}$)", "F3"), (r"Faz 3 eğim ($\phi_{3}$)", "S3")]
blok("T2", "İkinci modelin ilk önemli bulgusu, ETS öncesi eğilim katsayısının her iki modelde de sıfırdan anlamlı biçimde farklı olmamasıdır.",
     "**Tablo 5.13a.** İkinci Model, Yeşil Patent Stoku Hariç\n\n| Değişken | NB katsayı (bootstrap SH) | Poisson QML katsayı (bootstrap SH) |\n|---|---|---|\n" + "".join(f"| {a} | {kh('m2_stoksuz', N, k)} | {kh('m2_stoksuz', P, k)} |\n" for a, k in IT) +
     f"\nNot: Ülke sabit etkileri ve beş kontrol değişkeni modelde yer almaktadır; yeşil patent stoku dışarıda bırakılmıştır. Parantez içindeki değerler ülke düzeyinde kümelenmiş {TG['meta']['B']} tekrarlı bootstrap standart hatalarıdır. {T13} " + YN,
     "Stoksuz ikinci model tablosu eklendi.")
deg("T7", "Bu durum, ikinci fazın başında ulaşılan yüksek düzeyin faz boyunca korunduğunu göstermektedir.",
    "Model faz içinde doğrusal bir eğim varsaydığından bu sonuç yıllık dalgalanmayı göstermemektedir; yıl etkileri, farkın ikinci fazın ilk yıllarında (2008–2010) yoğunlaştığını ve fazın sonuna doğru zayıfladığını ortaya koymaktadır (Bölüm 5.7.3).",
    "“Faz boyunca korunmaktadır” ifadesi yıl etkileriyle çelişiyordu.")
ek("Y3", "Bu sonuç, birinci modelde üçüncü faz katsayısının anlamlı olmamasıyla tutarlıdır.",
   "Üçüncü faz tahminlerinin belirsizliği yüksek olduğundan bu sonuç, üçüncü fazın etkisiz olduğu biçiminde değil, ek bir fark bulunduğuna ilişkin yeterli kanıt elde edilemediği biçiminde yorumlanmalıdır.", "Üçüncü faz yorumu temkinli hâle getirildi.")
deg("T7 T1", "Buna göre ETS öncesi eğilimden sapma, birinci fazın sonunda ulaşılan yüzde 30,3 düzeyinden ikinci fazın başında yüzde 42,3'e yükselmekte ve faz boyunca korunmaktadır. Birinci fazda başlayan süreç, ikinci fazda kurumsal kesinlikle pekişmektedir.",
    "Buna göre modelin öngördüğü sapma, birinci fazın sonunda ulaşılan yüzde 30,3 düzeyinden ikinci fazın başında yüzde 42,3'e yükselmektedir. Yıl etkileri ise bu farkın 2009'da en yüksek değerine ulaştıktan sonra fazın sonuna doğru azaldığını göstermektedir (Bölüm 5.7.3).",
    "“Kurumsal kesinlikle pekişmektedir” yorumu çıkarıldı; zamanlama bunu desteklemiyor.")

# ============================================================ 5.7.3
deg("C7", "yıl katsayılarını ve yüzde 95 güven aralıklarını göstermektedir.", "yıl katsayılarını, bootstrap standart hatalarına ve kümelenmiş standart hatalara dayanan yüzde 95 güven aralıklarıyla birlikte göstermektedir.", "Şekil 5.5 bootstrap aralıklarıyla yeniden çizildi.")
im = re.search(r'<img src="media/image5\.png"[^>]*/>', H0).group(0)
ham("C7", im, f'<del class="resim" @AT@>{im}</del><ins class="resim" @AT@><img src="media/sekil5_5_guncel.png" alt="Yıl etkileri: bootstrap ve kümelenmiş standart hatalarla güven aralıkları" /></ins>', "şekil",
    "Şekil 5.5 yeniden çizildi: bootstrap standart hatalarına dayanan aralıklar (kalın) ve tezdeki kümelenmiş standart hata aralıkları (ince) birlikte.", "Şekil 5.5 (yalnız kümelenmiş standart hatalar)", "Şekil 5.5 (bootstrap ve kümelenmiş standart hatalar)")
deg("C7", "ülke düzeyinde kümelenmiş standart hatalarla %95 güven aralıkları.", f"kalın çizgiler ülke düzeyinde kümelenmiş {R['meta']['B']} tekrarlı bootstrap standart hatalarına (13 serbestlik dereceli t dağılımı), ince çizgiler ülke düzeyinde kümelenmiş standart hatalara dayanan %95 güven aralıklarıdır.", "Şekil notu güncellendi.")
pre = [yb[str(y)]["b"] for y in range(1997, 2004)]; assert min(pre) > 0
deg("T2", "Bu sonuç, ETS'nin başlangıcından önce yeşil patent yoğunluğunun istikrarlı bir seyir izlediğini göstermektedir.",
    "Bununla birlikte yedi katsayının tamamı pozitiftir ve 2004'e doğru azalmaktadır; yeşil patent stoku kontrol edildiğinde ETS öncesinde yoğunluk istikrarlı değil, hafif azalan bir seyir izlemektedir.", "ETS öncesi katsayıların hepsi pozitif ve azalan; “istikrarlı” değil.")
pb13 = lambda y: pt(yb[str(y)]["b"], yb[str(y)]["se_boot"])
assert pb13(2009) < .05 and all(.05 < pb13(y) < .10 for y in (2006, 2007, 2008)) and pb13(2010) > .10 and pb13(2005) > .10
deg("C7", "Katsayılar 2006'dan itibaren anlamlı hale gelmekte ve kademeli olarak yükselmektedir:",
    "Katsayılar 2006'dan itibaren pozitiftir ve 2009'a kadar kademeli olarak yükselmektedir; bootstrap standart hatalarıyla yüzde 5 düzeyinde yalnızca 2009, yüzde 10 düzeyinde 2006–2008 katsayıları anlamlıdır:", "Yıl katsayılarının anlamlılığı bootstrap standart hatalarına göre yeniden yazıldı.")
deg("C7 T7", "Katsayılar 2010'da da anlamlı kalmakta, ikinci fazın sonuna doğru gerilemekte ve üçüncü fazda nokta tahminleri 2004 düzeyinin altında seyretmektedir.",
    f"Katsayılar 2010'dan itibaren gerilemekte (2010'da {tr(yb['2010']['b'], 3)}; 2011'de {tr(yb['2011']['b'], 3)}; 2012'de {tr(yb['2012']['b'], 3)}), ikinci fazın son yıllarında sıfırdan ayırt edilememekte ve üçüncü fazda nokta tahminleri 2004 düzeyinin altında seyretmektedir.",
    "İkinci faz içindeki düşüş rakamlarla yazıldı.")
deg("T4 T7", "Bu profil, birinci fazda kademeli hızlanmanın, ikinci fazda en yüksek etkinin ve üçüncü fazda doğrudan etkinin zayıflamasının yıllık verilerle de geçerli olduğunu göstermektedir.",
    "Bu profil, birinci fazda kademeli hızlanmanın, ikinci fazın ilk yıllarında en yüksek farkın ve üçüncü fazda stok sabitken gözlenen farkın kaybolmasının yıllık verilerde de görüldüğünü göstermektedir.", "Terimler ve zamanlama düzeltildi.")
deg("T4", "üçüncü fazdaki yüksek yeşil patent yoğunluğu yeşil patent stokundaki artışla açıklanmaktadır.",
    "üçüncü fazdaki yüksek yeşil patent yoğunluğu istatistiksel olarak yeşil patent stokundaki artışla ilişkilidir; stok AB ETS'den bağımsız nedenlerle de büyüdüğünden bu ilişki nedensel bir açıklama olarak yorumlanmamalıdır.", "“Açıklanmaktadır” yerine “ilişkilidir”.")
ham("B1", "<p>5.8 Sağlamlık Testleri</p>", '<h2 class="bicim" @AT@ title="Bu satır Word dosyasında düz paragraftı; başlık stili uygulandı.">5.8 Sağlamlık Testleri</h2>', "biçim", "“5.8 Sağlamlık Testleri” satırına başlık stili uygulandı.", "(düz paragraf)", "(Başlık 2)")

# ============================================================ 5.8.1
deg("T3 T5 T9 Y5", "Ana bulguların model tanımına duyarlılığı üç alternatif tanımla sınanmıştır.", "Ana bulguların model tanımına duyarlılığı yedi alternatif tanımla sınanmıştır.", "Dört yeni sağlamlık tanımı eklendi (d–g).")
t14 = TZ.T514
hucre("C6", "5.14", "Birinci model", 2, f"{tezh(*t11[P]['F1'][:2])} (0,0383)", "", kacinci=2, grup=G_YIL)
hucre("C6", "5.14", "Birinci model", 3, f"{tezh(*t11[P]['F2'][:2])} (0,0651)", "", kacinci=2, grup=G_YIL)
hucre("C6", "5.14", "Yeşil patent stoku hariç", 4, f"{tezh(*t14['a']['nb'][2])} (0,2251)", "", kacinci=1, grup=G_YIL)
assert tezh(*t14["a"]["nb"][2]).count("*") == 2
G_A = hucre("T4", "5.14", "Yeşil patent stoku hariç", 0, r"\(a\) Yeşil patent stoku hariç", "Tablo 5.14'te “(toplam etki)” nitelemesi kaldırıldı.", kacinci=1)
hucre("T4", "5.14", "Yeşil patent stoku hariç", 0, r"\(a\) Yeşil patent stoku hariç", "", kacinci=2, grup=G_A)
G_R = None
for ad, key, bl in [(r"\(d\) Yeşil patent stoku hariç, doğrusal eğilim eklenmiş", "stoksuz_egilim", "T3"), (r"\(e\) Referans dönem 1997–2002 (2003–2004 için ayrı kukla)", "referans_1997_2002", "T9"),
                    (rf"\(f\) 2018–2020 hariç (N = {TG['2018_2020_haric'][N]['_N']})", "2018_2020_haric", "Y5"), (r"\(g\) Ön-örneklem ortalaması tahmincisi (ülke sabit etkileri yerine)", "psm_m1", "T5")]:
    for fam in (N, P):
        G_R = satir_ekle(bl, "5.14", "Almanya hariç", [ad, FAM[fam]] + [kh(key, fam, k) for k in PH], "Tablo 5.14'e dört yeni tanım eklendi: (d) stoksuz ve eğilimli, (e) referans dönem 1997–2002, (f) 2018–2020 hariç, (g) ön-örneklem ortalaması tahmincisi.", kacinci=2, grup=G_R)
ek("C6 T3 T5 T9 Y5", YN, T13 + f" (d)–(g) satırlarındaki tahminler bu güncellemede eklenmiştir; parantez içindeki değerler {TG['meta']['B']} tekrarlı bootstrap standart hatalarıdır.", "Tablo 5.14 notu güncellendi.", kacinci=3)

deg("T4", "Yeşil patent stokunun modelden çıkarılması, AB ETS'nin bilgi birikimi kanalı dahil toplam etkisini vermektedir.", "Yeşil patent stokunun modelden çıkarılması, stok hesaba katılmadan gözlenen faz farklarını vermektedir.", "“Toplam etki” terimi değiştirildi.")
deg("C6", "üçüncü fazda ise yüzde 88,8 daha yüksektir ve üç katsayı da yüzde 1 düzeyinde anlamlıdır.", "üçüncü fazda ise yüzde 88,8 daha yüksektir; ilk iki katsayı yüzde 1, üçüncüsü yüzde 5 düzeyinde anlamlıdır.", "Anlamlılık düzeyi t(13)'e göre düzeltildi.")
se_ = TG["stoksuz_egilim"]
assert g("stoksuz_egilim", N, "F3", "p_boot_t") > .10 and max(g("stoksuz_egilim", f, k, "p_boot_t") for f in (N, P) for k in ("F1", "F2")) < .05
deg("T3 T4", "Birinci model ile bu model arasındaki fark, AB ETS'nin etkisinin önemli bir bölümünün yeşil patent stoku aracılığıyla sonraki yıllara taşındığını göstermektedir. Özellikle üçüncü fazda doğrudan etki anlamsızken toplam etkinin negatif binom modelinde güçlü ve anlamlı olması, bu fazdaki yüksek yeşil patent düzeyinin önceki fazlarda AB ETS'nin uyardığı bilgi birikimi tarafından sürdürüldüğünü ortaya koymaktadır.",
    f"Ancak bu modelde zaman eğilimi bulunmadığından katsayılar ETS öncesinde başlayan artış eğilimini de içermektedir: yalnızca ETS öncesi eğilimin sürmesi, negatif binom modelinde fazlar için sırasıyla yaklaşık {tr(eg['nb']['F1']['egilimden'], 2)}, {tr(eg['nb']['F2']['egilimden'], 2)} ve {tr(eg['nb']['F3']['egilimden'], 2)} büyüklüğünde katsayılar üretmektedir. Bu nedenle söz konusu yüzdeler AB ETS'nin toplam etkisi olarak yorumlanmamalıdır. Birinci model ile stoksuz model arasındaki fark, AB ETS'nin bilgi birikimi yoluyla taşınan etkisiyle tutarlıdır; ancak yeşil patent stoku ETS'den bağımsız nedenlerle de büyüdüğünden, bu fark nedensel bir aracılık etkisi olarak yorumlanmamalıdır.",
    "Stoksuz modelin yüzde 44 / 101 / 89 rakamlarının ETS öncesi eğilimi de içerdiği yazıldı; “bilgi birikimi sürdürüyor” çıkarımı yumuşatıldı.")
deg("T3", "Birinci ve ikinci faz katsayılarının stoksuz modelde de pozitif ve anlamlı olması, ayrıca, bu fazlara ilişkin bulguların stok değişkeninin modelde yer almasına bağlı olmadığını göstermektedir.",
    "Birinci ve ikinci faz katsayılarının stoksuz modelde, doğrusal eğilim eklendiğinde de pozitif ve anlamlı olması (satır d), bu fazlara ilişkin bulguların stok değişkeninin modelde yer almasına bağlı olmadığını göstermektedir.", "Kanıt eğilimli tanıma dayandırıldı.")
oran = 100 * (t14["b"]["nb"][0][0] / t11[N]["F1"][0] - 1)
deg("M1", "Ancak bu modelde faz katsayıları birinci modeldekilere yakındır:", f"Bu modelde ikinci ve üçüncü faz katsayıları birinci modeldekilere yakındır, birinci faz katsayısı ise yaklaşık yüzde {tr(oran, 0)} daha büyüktür:", "Birinci fazdaki fark gizlenmedi.")
ih = TG["irlanda_haric"][N]
deg("M1", "Dolayısıyla maruziyet kısıtı faz etkilerine ilişkin bulguları etkilememektedir. Tezin hipotezleri yeşil patent yoğunluğu üzerinden kurulduğundan, katsayıların yoğunluktaki oransal değişim olarak yorumlanmasını sağlayan maruziyet tanımı ana model olarak korunmuştur.",
    f"Dolayısıyla birim esneklik kısıtı veriyle reddedilmekle birlikte, faz farklarının işareti iki tanımda aynıdır; birinci ve ikinci faz farkları serbest esneklik tanımında da anlamlıdır. Tezin hipotezleri yeşil patent yoğunluğu üzerinden kurulduğundan maruziyet tanımı ana model olarak korunmuş, sonuçlar her iki tanımla birlikte raporlanmıştır. İrlanda'nın 2015 yılındaki yüzde 24,6'lık GSYİH artışının maruziyet değişkenini etkileyebileceği dikkate alınarak model İrlanda dışarıda bırakılarak da tahmin edilmiş, katsayılar belirgin biçimde değişmemiştir (negatif binom: birinci faz {tr(ih['F1']['b'], 3)}; ikinci faz {tr(ih['F2']['b'], 3)}).",
    "Reddedilen kısıtın neden korunduğu dürüstçe yazıldı; iki tanım birlikte raporlanıyor; İrlanda 2015 dipnotu eklendi.")
ek("C3", "Bu sonuç, AB ETS'nin etkisinin Almanya'ya özgü olmadığını, aksine diğer ülkelerde daha da belirgin olduğunu göstermektedir.",
   f"Almanya dışarıda bırakıldığında Poisson birinci faz katsayısı ({tr(t14['c']['poisson'][0][0], 4)}) negatif binom tahmincisinin tam örneklem değerine ({tr(t11[N]['F1'][0], 4)}) yaklaşmaktadır; bu durum, iki tahminci arasındaki farkın büyük ölçüde Poisson tahmincisinin Almanya'ya verdiği ağırlıktan kaynaklandığını göstermektedir.",
   "Almanya hariç tahmin, ağırlıklandırma çerçevesiyle yorumlandı.")
assert min(g('referans_1997_2002', P, k, 'p_boot_t') for k in ('F1', 'F2')) > .10 and max(pt(*t14['b'][f][i]) for f in ('nb', 'poisson') for i in (0, 1)) < .05
r2, f6, pm, p2, et, fb = TG["referans_1997_2002"], TG["2018_2020_haric"], TG["psm_m1"], TG["psm_m2"], TG["ets_tek"], TG["faz2_bolunmus"]
assert max(g("psm_m2", f, k, "p_boot_t") for f in (N, P) for k in ("S1", "F2")) < .05 and min(g("psm_m1", f, k, "p_boot_t") for f in (N, P) for k in ("F1", "F2")) > .10
assert max(g("faz2_bolunmus", f, "F2a", "p_boot_t") for f in (N, P)) < .01 and min(g("faz2_bolunmus", f, "F2b", "p_boot_t") for f in (N, P)) > .10
blok("T3 T5 T7 T9 Y5", "**(c) Almanya hariç model.**",
     f"""**(d) Yeşil patent stoku hariç, doğrusal eğilimli model.** Stoksuz modele ETS öncesi artış eğilimini temsil eden doğrusal bir eğilim eklenmiştir. Bu tanımda faz katsayıları küçülmektedir: negatif binom modelinde birinci faz {tr(se_[N]['F1']['b'], 3)}, ikinci faz {tr(se_[N]['F2']['b'], 3)}, üçüncü faz {tr(se_[N]['F3']['b'], 3)}; Poisson modelinde sırasıyla {tr(se_[P]['F1']['b'], 3)}, {tr(se_[P]['F2']['b'], 3)} ve {tr(se_[P]['F3']['b'], 3)}. Birinci ve ikinci faz katsayıları her iki tahmincide de anlamlı kalmakta, üçüncü faz katsayısı ise anlamlılığını yitirmektedir. Stok hesaba katılmadığında üçüncü fazda görülen büyük fark, dolayısıyla, ETS öncesinde başlayan eğilimden ayırt edilememektedir.

**(e) Referans dönemin 1997–2002 ile sınırlandırıldığı model.** 2003/87/AT sayılı Direktif'in kabul edildiği 2003 yılından itibaren beklenti etkilerinin oluşmuş olabileceği dikkate alınarak 2003–2004 yılları için ayrı bir kukla eklenmiştir; bu kuklanın katsayısı negatiftir ({tr(r2[N]['ANT']['b'], 3)} ve {tr(r2[P]['ANT']['b'], 3)}) ancak anlamlı değildir. Bu tanımda negatif binom modelinde birinci faz katsayısı {tr(r2[N]['F1']['b'], 3)} ({ga('referans_1997_2002', N, 'F1')}), ikinci faz katsayısı {tr(r2[N]['F2']['b'], 3)} ({ga('referans_1997_2002', N, 'F2')}) olarak tahmin edilmektedir. Poisson modelinde birinci faz katsayısı {tr(r2[P]['F1']['b'], 3)}, ikinci faz katsayısı {tr(r2[P]['F2']['b'], 3)} değerine inmekte ve bootstrap standart hatalarıyla ikisi de anlamlı bulunmamaktadır. Faz farkları, özellikle Poisson tahmincisinde, referans dönemin seçimine duyarlıdır.

**(f) 2018–2020 yıllarının dışarıda bırakıldığı model.** En son yıllara ait patent verisinin eksik olabileceği dikkate alınarak model 1997–2017 dönemiyle yeniden tahmin edilmiştir. Bulgular zayıflamamaktadır: negatif binom modelinde birinci faz katsayısı {tr(f6[N]['F1']['b'], 3)}, ikinci faz katsayısı {tr(f6[N]['F2']['b'], 3)}; Poisson modelinde {tr(f6[P]['F1']['b'], 3)} ve {tr(f6[P]['F2']['b'], 3)} olarak tahmin edilmektedir.

**(g) Ön-örneklem ortalaması tahmincisi.** Yeşil patent stoku bağımlı değişkenin geçmişinden türetildiğinden, ülke sabit etkileri yerine ülkelerin tahmin dönemi öncesindeki (1990–1996) ortalama başvuru sayısının ve 1995–1996 ortalama reel GSYİH'sinin logaritmasının kullanıldığı tahminci uygulanmıştır (Blundell, Griffith ve Van Reenen, 1999; Blundell, Griffith ve Windmeijer, 2002). Bu tahmincide birinci modelin birinci ve ikinci faz katsayıları sıfıra yaklaşmakta ve anlamlılığını yitirmektedir (negatif binom: {tr(pm[N]['F1']['b'], 3)} ve {tr(pm[N]['F2']['b'], 3)}). İkinci modelde ise birinci faz eğimi (negatif binom {tr(p2[N]['S1']['b'], 3)}; Poisson {tr(p2[P]['S1']['b'], 3)}) ve ikinci faz düzeyi ({tr(p2[N]['F2']['b'], 3)}; {tr(p2[P]['F2']['b'], 3)}) aynı tahminciyle de yüzde 5 düzeyinde anlamlıdır. Sonuçlar ön-örneklem bilgisinin tanımına duyarlıdır; bu nedenle birinci modelin faz katsayıları üst sınır olarak yorumlanmış, temel çıkarımlar ikinci modele dayandırılmıştır.

Tablo 5.14a iki ek tanımın sonuçlarını göstermektedir. Üç faz kuklası yerine tek bir ETS dönemi kuklası (2005–2020) kullanıldığında, yeşil patent stoku ve kontrol değişkenleri sabitken ETS döneminde yeşil patent yoğunluğu ETS öncesine göre negatif binom modelinde yaklaşık yüzde {yuzde(et[N]['ETS']['b'])}, Poisson modelinde yüzde {yuzde(et[P]['ETS']['b'])} daha yüksektir ve fark her iki tahmincide yüzde 1 düzeyinde anlamlıdır. İkinci faz ikiye bölündüğünde fark 2008–2009 yıllarında yoğunlaşmaktadır: negatif binom modelinde 2008–2009 için {tr(fb[N]['F2a']['b'], 3)} (yüzde 1 düzeyinde anlamlı), 2010–2012 için {tr(fb[N]['F2b']['b'], 3)} (anlamsız); Poisson modelinde sırasıyla {tr(fb[P]['F2a']['b'], 3)} ve {tr(fb[P]['F2b']['b'], 3)}.

**Tablo 5.14a.** Ek Tanımlar: Tek ETS Kuklası ve İkinci Fazın Bölünmesi

| Tanım | Katsayı | NB (bootstrap SH) | Poisson QML (bootstrap SH) |
|---|---|---|---|
| Tek ETS dönemi kuklası | ETS (2005–2020) | {kh('ets_tek', N, 'ETS')} | {kh('ets_tek', P, 'ETS')} |
| İkinci faz ikiye bölünmüş | Faz 1 (2005–2007) | {kh('faz2_bolunmus', N, 'F1')} | {kh('faz2_bolunmus', P, 'F1')} |
| | Faz 2a (2008–2009) | {kh('faz2_bolunmus', N, 'F2a')} | {kh('faz2_bolunmus', P, 'F2a')} |
| | Faz 2b (2010–2012) | {kh('faz2_bolunmus', N, 'F2b')} | {kh('faz2_bolunmus', P, 'F2b')} |
| | Faz 3 (2013–2020) | {kh('faz2_bolunmus', N, 'F3')} | {kh('faz2_bolunmus', P, 'F3')} |

Not: Tüm modellerde ülke sabit etkileri, yeşil patent stoku ve kontrol değişkenleri yer almaktadır. Parantez içindeki değerler ülke düzeyinde kümelenmiş {TG['meta']['B']} tekrarlı bootstrap standart hatalarıdır. {T13} {YN}""",
     "Yeni sağlamlık tanımlarının açıklamaları (d–g), tek ETS kuklası ve ikinci fazın bölünmesi eklendi.")
assert g("ets_tek", N, "ETS", "p_boot_t") < .01 and g("ets_tek", P, "ETS", "p_boot_t") < .01 and g("faz2_bolunmus", N, "F2a", "p_boot_t") < .01

# ============================================================ 5.8.2
deg("Y1", "yedisinde yüzde 5, on üçünde yüzde 10 düzeyinde anlamlıdır ve sapma düzeltmeli güven aralığı on üç tahminde sıfırı içermemektedir.", "yedisinde yüzde 5, on üçünde yüzde 10 düzeyinde anlamlıdır.", "Tabloda karşılığı olmayan güven aralığı cümlesi çıkarıldı.")
deg("Y1", "Bu sonuçlar, bulguların herhangi bir ülkenin örneklemde bulunmasına bağlı olmadığını göstermektedir.",
    "Bu sonuçlar, ikinci faz farkının herhangi bir ülkenin örneklemde bulunmasına bağlı olmadığını, birinci faz farkının ise ülke bileşimine duyarlı olduğunu göstermektedir. Danimarka ya da Almanya dışarıda bırakıldığında faz katsayıları büyümekte ve üçüncü faz katsayısının işareti pozitife dönmektedir.",
    "Sonuç cümlesi tablonun gösterdiği kadarına indirildi.")

# ============================================================ 5.8.3
deg("T6", "2000, 2001 ve 2002 yılları için sahte kırılma noktaları tanımlanmıştır.", "1999, 2000, 2001, 2002 ve 2003 yılları için sahte kırılma noktaları tanımlanmıştır.", "Eksik raporlanan 1999 ve 2003 plaseboları eklendi.")
for y, (a, b_, c_, d_) in TZ.T516.items() if isinstance(TZ.T516, dict) and all(isinstance(v, (list, tuple)) and len(v) == 4 for v in TZ.T516.values()) else []:
    assert abs(pl[str(y)][P]["chi2_kume"] - a) < .011 and abs(pl[str(y)][N]["chi2_kume"] - c_) < .011, y
tb = "| Sahte kırılma yılı | Poisson $\\chi^{2}$(2) | p (kümelenmiş) | p (bootstrap) | NB $\\chi^{2}$(2) | p (kümelenmiş) | p (bootstrap) |\n|---|---|---|---|---|---|---|\n"
for y in ("1999", "2000", "2001", "2002", "2003"):
    v = pl[y]; tb += f"| {y} | {tr(v[P]['chi2_kume'], 2)} | {tr(v[P]['p_kume'], 3)} | {tr(v[P]['p_boot'], 3)} | {tr(v[N]['chi2_kume'], 2)} | {tr(v[N]['p_kume'], 3)} | {tr(v[N]['p_boot'], 3)} |\n"
tablo_degistir("T6 C7", "5.16", tb, "Tablo 5.16 genişletildi: 1999 ve 2003 satırları ile bootstrap olasılık değerleri eklendi (2000–2002 satırlarındaki mevcut değerler aynen korundu).")
deg("C7", "Testler ülke düzeyinde kümelenmiş standart hatalarla yapılmıştır.", f"Ki-kare istatistikleri ülke düzeyinde kümelenmiş kovaryans matrisine dayanmaktadır; bootstrap olasılık değerleri, ülke düzeyinde kümelenmiş {R['meta']['B']} tekrarlı bootstrap kovaryans matrisiyle hesaplanan Wald istatistiğine aittir.", "Tablo notu güncellendi.")
assert pl["2003"][P]["p_kume"] < .01 and pl["2003"][N]["p_kume"] < .10 and min(pl[y][f]["p_boot"] for y in pl for f in (P, N)) > .10 and min(pl[y][f]["p_kume"] for y in ("1999", "2000", "2001", "2002") for f in (P, N)) > .10
deg("T6", "Üç sahte kırılma yılının hiçbirinde, hiçbir tahminci ile düzey ve eğim katsayıları ortak olarak anlamlı değildir. ETS öncesi dönemde yeşil patent yoğunluğunda, ETS döneminde gözlemlenen türden bir kırılma bulunmamaktadır. Bu sonuç, birinci model ve ikinci modelde tahmin edilen faz etkilerinin örneklem döneminin herhangi bir yerinde kendiliğinden ortaya çıkan rastlantısal kırılmalar olmadığını, AB ETS'nin faaliyete geçtiği dönemle sınırlı olduğunu göstermektedir.",
    f"1999–2002 yılları için tanımlanan sahte kırılmalarda, hiçbir tahminci ile düzey ve eğim katsayıları ortak olarak anlamlı değildir. 2003 yılı için kümelenmiş standart hatalarla anlamlı (Poisson p = {tr(pl['2003'][P]['p_kume'], 3)}; negatif binom p = {tr(pl['2003'][N]['p_kume'], 3)}), bootstrap ile anlamsız (p = {tr(pl['2003'][P]['p_boot'], 3)} ve {tr(pl['2003'][N]['p_boot'], 3)}) bir sapma görülmektedir. 2003–2004 yıllarında yoğunluk önceki eğilimin altında kalmıştır; bu sapma, Direktif'in 2003'te kabul edilmesinin ardından oluşan bekleme davranışıyla ilişkili olabilir. Sekiz yıllık dönemde ve 14 ülkeyle testin gücü sınırlı olduğundan, bu sonuçlar faz farklarının yalnızca AB ETS dönemine özgü olduğunun kesin kanıtı olarak yorumlanmamalıdır.",
    "Plasebo sonuçları eksiksiz ve temkinli yorumlandı; 2003 sonucu açıklandı.")

# ============================================================ 5.9
G_17 = hucre("T3 Y2", "5.17", "H1", 2, f"Tek ETS dönemi kuklası pozitif ve anlamlı (NB {tr(et[N]['ETS']['b'], 3)}; Poisson {tr(et[P]['ETS']['b'], 3)}; stok sabitken yaklaşık %{yuzde(et[N]['ETS']['b'])})", "Hipotez tablosu kanıtın gösterdiği düzeye çekildi: H1 kanıtı değişti, H2 ve H5 “kısmen”, H3'e zamanlama notu.")
hucre("T1 Y2", "5.17", "H1", 3, "Desteklenmektedir (önce–sonra karşılaştırması olarak)", "", grup=G_17)
hucre("C5 Y2", "5.17", "H2", 2, r"NB 0,1338\*\*; Poisson 0,0772\*; Poisson'da çıkarsama yöntemine duyarlı", "", grup=G_17)
hucre("C5 Y2", "5.17", "H2", 3, "Kısmen desteklenmektedir", "", grup=G_17)
hucre("C6 T7 Y2", "5.17", "H3", 2, r"NB 0,2705\*\*\*, Poisson 0,1954\*\*; $\delta_{1} = \delta_{2}$ reddedildi (p = 0,037; 0,013); fark ikinci fazın ilk yıllarında yoğunlaşmaktadır", "", grup=G_17)
hucre("T2 Y2", "5.17", "H5", 1, "Birinci fazdaki hızlanma ve ikinci fazın başındaki düzey artışı, ETS öncesi eğilim hesaba katıldığında da ortaya çıkmaktadır.", "", grup=G_17)
hucre("T2 Y2", "5.17", "H5", 2, r"$\phi_{1}$ ve $\lambda_{2}$ stoklu modelde ve stoksuz negatif binom modelinde anlamlı; ETS öncesi eğilim yalnızca stok kontrol edildiğinde anlamsız; üçüncü fazda ek fark yok", "", grup=G_17)
hucre("T2 Y2", "5.17", "H5", 3, "Kısmen desteklenmektedir (üçüncü faz hariç)", "", grup=G_17)
blok("T1 Y2 M1", ("tablo", "5.17"), "Not: Sonuçlar nedensel etki olarak değil, AB ETS fazlarıyla ilişkili farklar olarak yorumlanmalıdır (Bölüm 5.11). Faz katsayılarının işareti GSYİH esnekliğinin serbest bırakıldığı tanımda da aynıdır; birinci ve ikinci faz farkları bu tanımda da anlamlıdır (Tablo 5.14, satır b).", "Hipotez tablosuna yorum notu eklendi.")

# ============================================================ 5.10
deg("T7", "5.10.2 İkinci Faz: Kurumsal Kesinlik ve En Güçlü Etki", "5.10.2 İkinci Faz: İlk Yıllardaki Artış", "Alt başlık nötr hâle getirildi.")
deg("T4 T7", "AB ETS'nin yeşil inovasyon üzerindeki doğrudan etkisi ikinci fazda en yüksek düzeye ulaşmıştır. İkinci fazın üç kurumsal özelliği bu sonucu açıklamaktadır.",
    "Stok sabitken gözlenen fark ikinci fazda, özellikle fazın ilk yıllarında (2008–2010) en yüksek düzeye ulaşmıştır. İkinci fazın üç kurumsal özelliği bu sonuçla tutarlıdır.", "“Açıklamaktadır” yerine “tutarlıdır”; zamanlama belirtildi.")
deg("T10", "2020 yılına kadar geçerli olacak tek üst sınır", "2013'ten itibaren geçerli olacak tek üst sınır", "Doğrusal indirim faktörünün 2020'de biten bir süresi yoktu.")
deg("T7", "İkinci fazın başında ETS öncesi eğilimden sapmanın yükselmesi ve faz boyunca korunması, ikinci faz etkisinin 2008 finans krizi ve ardından gelen fiyat düşüşüne karşın sürdüğünü göstermektedir.",
    "İkinci fazın başında ETS öncesi eğilime göre belirgin bir düzey farkı oluşmuş, bu fark 2009'da en yüksek değerine ulaştıktan sonra fazın sonuna doğru azalmıştır; dolayısıyla artış fazın tamamına değil, ilk yıllarına aittir. 2009/29/AT sayılı Direktif Nisan 2009'da kabul edilmiş, fark ise bu tarihten sonra küçülmüştür.",
    "Veri, farkın “sürdüğünü” değil 2009'dan sonra azaldığını gösteriyor.")
deg("T1 T7", "Firmaların inovasyon kararlarını belirleyen sistemin uzun dönemli yönüne ilişkin beklentilerdir.",
    "Firmaların inovasyon kararlarını sistemin uzun dönemli yönüne ilişkin beklentilerin belirlemesi olasıdır; ancak bu veriyle beklenti kanalı, aynı döneme denk gelen diğer gelişmelerden ayırt edilememektedir.", "Kesin nedensel ifade olasılık ifadesine çevrildi.")
blok("T1 T7", "Bu bulgu, Schmidt ve diğ.'nin (2012) uzun dönemli hedeflerin inovasyonun önemli bir belirleyicisi olduğu yönündeki bulgusuyla tutarlıdır.",
     "İkinci fazın ilk yıllarındaki artış için AB ETS dışında başka açıklamalar da bulunmaktadır. İkinci faz, Kyoto Protokolü'nün birinci taahhüt dönemiyle (2008–2012) aynı yılları kapsamaktadır; enerji fiyatları 2008'de en yüksek düzeyine ulaşmış, 2009/28/AT sayılı Yenilenebilir Enerji Direktifi aynı dönemde kabul edilmiştir. Ayrıca 2008–2009 yıllarında başvurusu yapılan buluşlar, büyük ölçüde kriz öncesinde alınan Ar-Ge kararlarını yansıtmaktadır. 2010 sonrasındaki zayıflama ise kriz sonrası Ar-Ge kısıntıları ve izin fiyatındaki düşüşle aynı döneme denk gelmektedir. Bu çalışmanın tasarımı söz konusu açıklamaları birbirinden ayırt edememektedir.",
     "İkinci faz artışı için alternatif açıklamalar yan yana sayıldı.")
deg("Y3 T4", "5.10.3 Üçüncü Faz: Bilgi Birikiminin Taşıdığı Etki", "5.10.3 Üçüncü Faz: Ek Fark Gözlenmemesi ve Olası Açıklamalar", "Alt başlık kanıtın gösterdiği düzeye çekildi.")
deg("Y3 T3 T4", "Üçüncü fazda yeşil patent stoku kontrol edildiğinde ETS öncesine göre ek bir doğrudan etki bulunmamakta ancak stoksuz negatif binom modelinde ise üçüncü fazın toplam etkisi güçlü ve anlamlı çıkmaktadır. Bu iki bulgu birlikte değerlendirildiğinde, üçüncü fazdaki yüksek yeşil patent düzeyinin birinci ve ikinci fazlarda oluşan bilgi birikimi tarafından sürdürüldüğü, üçüncü fazın kendi kurallarının ise bu düzeyi daha ileriye taşıyacak ek bir teşvik yaratmadığı sonucuna ulaşılabilmektedir.",
    "Üçüncü fazda, yeşil patent stoku sabitken ETS öncesine göre ek bir fark bulunduğuna ilişkin yeterli istatistiksel kanıt elde edilememiştir; tahminin belirsizliği yüksek olduğundan bu sonuç üçüncü fazın etkisiz olduğu biçiminde yorumlanmamalıdır. Stok hesaba katılmadığında negatif binom modelinde üçüncü faz farkı büyük ve anlamlıdır; ancak bu fark ETS öncesinde başlayan artış eğilimini de içermekte, doğrusal eğilim eklendiğinde anlamlılığını yitirmektedir (Tablo 5.14, satır d). Bu bulgular iki açıklamayla bağdaşmaktadır: üçüncü fazda yeşil patentleme üzerindeki teşvikin zayıflamış olması ya da önceki fazlarda oluşan bilgi birikiminin ulaşılan düzeyi sürdürmesi. Bu veriyle iki açıklama birbirinden ayırt edilememektedir.",
    "Üçüncü faz yorumu yeniden yazıldı: iki olası açıklama yan yana; hangisinin geçerli olduğu bu veriyle belirlenemiyor.")
deg("T4", "Bu sonuç, politika etkisinin bilgi stoku aracılığıyla zaman içinde birikerek sürdüğünü göstermektedir. İlk iki fazda uyarılan buluşlar yeşil patent stokunu artırmış, bu stok da üçüncü fazda yeni yeşil patent faaliyetinin temel belirleyicisi olmuştur.",
    "Bulgular, politika etkisinin bilgi stoku aracılığıyla zaman içinde taşınmasıyla tutarlıdır; ancak stok AB ETS'den bağımsız nedenlerle de büyüdüğünden bu kanal ayrıştırılamamaktadır. İlk iki fazda artan başvurular yeşil patent stokunu büyütmüş, bu stok da üçüncü fazda yeni yeşil patent faaliyetiyle güçlü biçimde ilişkili olmuştur.", "Aracılık iddiası yumuşatıldı.")
deg("T1 T3", "bu küresel eğilimin 14 AB üyesi ülkede de gözlemlendiğini, ancak bilgi stoku kontrol edilmeden ölçülen toplam etkinin üçüncü fazda da güçlü kaldığını göstermektedir.",
    "bu küresel eğilimin 14 AB üyesi ülkede de gözlemlendiğini göstermektedir. Aynı ölçüt birinci ve ikinci faz için de geçerlidir: bu fazlardaki yükseliş de aynı dönemdeki küresel temiz teknoloji patentleme artışından etkilenmiş olabilir.",
    "Küresel eğilim ölçütü iki yöne de uygulandı (düşüş küresel eğilime, yükseliş ETS'ye bağlanıyordu).")
blok("T11", "Bu sonuç, politika etkisinin bilgi stoku aracılığıyla zaman içinde birikerek sürdüğünü göstermektedir.",
     "Karbon fiyatı bu çalışmada açıklayıcı değişken olarak yer almamaktadır. Üçüncü fazın büyük bölümünde izin fiyatının düşük seyretmesi, bu fazda ek bir fark gözlenmemesinin olası açıklamalarından biridir; ancak birinci fazın sonunda izin fiyatı çökerken farkın artması, fiyat ile patentleme arasında basit bir eşzamanlı ilişki bulunmadığına işaret etmektedir. İzin fiyatının modele dâhil edilmesi ileriki çalışmalara bırakılmıştır.",
     "Karbon fiyatının rolü tartışmaya eklendi. YAZAR: yıllık izin fiyatı serisiyle bir sağlamlık tahmini yapılması önerilir (yeni veri gerekir).")
ek("T5", "Yeşil patent stokunun esnekliği birinci modelde 0,61--0,63, ikinci modelde 0,66--0,79 aralığındadır ve tüm model tanımlarında yüzde 1 düzeyinde anlamlıdır.",
   "Benzetim sonuçları stok katsayısının aşağı yanlı tahmin edildiğini gösterdiğinden (Bölüm 5.6.4) bu değerler alt sınır olarak okunmalıdır.", "Stok katsayısının yanlılık yönü belirtildi.")
deg("T4", "Birinci model ile stoksuz model arasındaki fark, AB ETS'nin erken fazlardaki etkisinin bilgi stoku aracılığıyla kalıcılaştığını göstermektedir. AB ETS, yalnızca uygulandığı dönemde değil, yarattığı bilgi birikimi aracılığıyla sonraki dönemlerde de yeşil inovasyonu artırmıştır.",
    "Birinci model ile stoksuz model arasındaki fark, AB ETS'nin erken fazlardaki etkisinin bilgi stoku aracılığıyla taşınmasıyla tutarlıdır; ancak yeşil patent stoku AB ETS'den bağımsız nedenlerle de büyüdüğünden, bu fark nedensel bir aracılık etkisi olarak yorumlanmamalıdır.", "Kesin nedensel cümle çıkarıldı.")
deg("T4", "Bu nedenle ülkelerin Ar-Ge kapasitesi ve beşeri sermayesi, stok değişkeni aracılığıyla modelde yer almaktadır.", "Bu nedenle ülkelerin Ar-Ge kapasitesi ve beşeri sermayesi modelde yalnızca dolaylı olarak, stok değişkeni aracılığıyla temsil edilmektedir.", "Stokun Ar-Ge'yi “kontrol ettiği” iddiası yumuşatıldı.")
deg("T1", "sonucunu doğrulamakta ve dört yönde genişletmektedir.", "sonucuyla tutarlıdır ve bu sonucu dört yönde genişletmektedir.", "“Doğrulamakta” yerine “tutarlıdır”.")
deg("T4", "üçüncü fazda ek doğrudan etkinin bulunmaması ayrıştırılmıştır.", "üçüncü fazda stok sabitken ek bir farkın gözlenmemesi ayrıştırılmıştır.", "Terim değiştirildi.")
deg("T4", "Üçüncüsü, yeşil patent stoku modele dahil edilerek AB ETS'nin doğrudan etkisi ile bilgi birikimi yoluyla taşınan etkisi birbirinden ayrılmıştır.", "Üçüncüsü, yeşil patent stoku modele dahil edilerek stok sabitken gözlenen fark ile stok hesaba katılmadan gözlenen fark ayrı ayrı raporlanmıştır.", "Katkı cümlesi, yapılan şeyin gerçekte ne olduğuna göre yazıldı.")
kontrol("Y4", "Dördüncüsü, rassal etkili model yerine koşulsuz sabit etkili negatif binom ve sabit etkili Poisson modeli kullanılmıştır.", "Bel ve Joseph'in (2018) rassal etkili model kullandığı, makalenin yöntem bölümünden doğrulanmalıdır.", "YAZAR KONTROLÜ: Bel ve Joseph (2018) tahmincisi.")
kontrol("Y4", "Ayrıca Bel ve Joseph'in (2018) ana modeli enerji teknolojilerine ilişkin patentlere dayanırken, bu çalışma iklim değişikliği azaltım teknolojilerinin tamamını kapsamaktadır.", "Makalenin özeti genel iklim değişikliği azaltım teknolojisi patentlerinin de kullanıldığını belirtmektedir. Kapsam farkı makalenin veri bölümünden doğrulanmalı; doğrulanamazsa bu cümle çıkarılmalıdır.", "YAZAR KONTROLÜ: Bel ve Joseph (2018) kapsamı.")
deg("T1", "Bu çalışmada tahmin edilen ülke düzeyindeki etki daha büyüktür. Bu farkın iki nedeni bulunmaktadır.", "Bu çalışmada tahmin edilen ülke düzeyindeki fark daha büyüktür. Bu farkın üç olası nedeni bulunmaktadır.", "Üçüncü olası neden eklendi.")
ek("T1", "sistemin kalıcı olduğu beklentisinin ekonomi genelindeki etkisini de içermektedir.", "Üçüncüsü, karşılaştırma grubu bulunmadığından ülke düzeyindeki önce–sonra farkı, aynı döneme denk gelen diğer gelişmelerin etkisini de içerebilmektedir.", "Firma düzeyi çalışmayla farkın üçüncü olası nedeni: karşılaştırma grubu yok.")
deg("T1", "fazlar arasındaki farklılaşmanın temel açıklamasını oluşturmaktadır.", "fazlar arasındaki farklılaşmanın olası açıklamalarından birini oluşturmaktadır.", "“Temel açıklama” yerine “olası açıklamalardan biri”.")
deg("T1 T7 Y5", "Bu çalışmanın bulguları, AB ETS'nin etkisinin dönemden döneme değiştiğini ve emisyon izin arzının sıkı yönetildiği, kuralların uzun vadeli olarak kesinleştiği dönemlerde güçlü bir inovasyon etkisi ortaya çıktığını göstermektedir.",
    "Bu çalışmanın bulguları, AB ETS fazlarıyla ilişkili farkların dönemden döneme değiştiğini, yeşil patent yoğunluğunun birinci faz boyunca hızlandığını ve ikinci fazın ilk yıllarında en yüksek düzeyine ulaştığını göstermektedir; bu farkların ne kadarının izin arzının sıkılaştırılmasından ve kuralların kesinleşmesinden kaynaklandığı bu tasarımla ayırt edilememektedir.",
    "Bölümün kapanış cümlesi nedensel iddiadan betimleyici bulguya çevrildi.")

# ============================================================ 5.11 (yeni)
blok("T1 C1 C9 T5 T8 T11 Y5 T4 T10", '<h1 id="kaynakça">KAYNAKÇA</h1>',
     f"""### 5.11 Çalışmanın Sınırlılıkları

Bu bölümün bulguları aşağıdaki sınırlılıklarla birlikte değerlendirilmelidir.

Birincisi, çalışmanın tasarımı bir önce–sonra karşılaştırmasıdır. Örneklemdeki bütün ülkeler AB ETS'ye aynı tarihte dâhil olduğundan sisteme tabi olmayan bir karşılaştırma grubu bulunmamaktadır. Tahmin edilen faz farkları, aynı dönemde gerçekleşen diğer ortak gelişmelerin (Kyoto Protokolü'nün 2008–2012 birinci taahhüt dönemi, 2004–2008 enerji fiyatı artışı, 2009 tarihli Yenilenebilir Enerji Direktifi, küresel temiz teknoloji patentleme dalgası) etkisini de içerebilir. Bu nedenle bulgular nedensel etki olarak değil, AB ETS fazlarıyla ilişkili farklar olarak yorumlanmalıdır.

İkincisi, yıl sabit etkileri faz kuklalarıyla birlikte tanımlanamadığından ortak şoklar tümüyle ayrıştırılamamaktadır. Yatay kesit bağımlılığı testleri ülkeler arasında bağımlılık bulunduğunu göstermektedir; ülke düzeyinde yeniden örnekleme bu bağımlılığı hesaba katmadığından anlamlılık düzeyleri iyimser olabilir.

Üçüncüsü, küme sayısı azdır (14) ve ülkelerin tahmindeki ağırlıkları dengesizdir. Benzetimler, bu koşullarda kullanılan bütün çıkarsama yöntemlerinin boş hipotezi nominal düzeyden daha sık reddettiğini göstermektedir (Tablo 5.6b). Sınırdaki sonuçlar, özellikle birinci modeldeki birinci faz farkı, bu nedenle temkinle yorumlanmalıdır.

Dördüncüsü, yeşil patent stoku bağımlı değişkenin geçmişinden türetilmektedir. Bu yapı birinci modelin faz katsayılarını yukarı, stok katsayısını aşağı yanlı kılmaktadır (Bölüm 5.6.4). Stok aynı zamanda zamanla yüksek düzeyde eşdoğrusal olduğundan ETS öncesi eğilim ile stokun etkisi birbirinden ayrıştırılamamakta; stoklu ve stoksuz modeller arasındaki fark nedensel bir aracılık etkisi olarak yorumlanamamaktadır.

Beşincisi, örneklem 14 ülkeyle sınırlıdır. 2020 sonuna kadar AB ETS kapsamında kalan Birleşik Krallık ile 2004 ve sonrasında AB'ye katılan ülkeler analizde yer almamaktadır.

Altıncısı, karbon fiyatı ve Ar-Ge harcamaları modelde açıklayıcı değişken olarak yer almamaktadır. Ar-Ge kapasitesi yalnızca dolaylı olarak, yeşil patent stoku aracılığıyla temsil edilmektedir.

Yedincisi, yeşil inovasyon patent başvurularıyla ölçülmektedir. Patent başvuruları buluş faaliyetinin göstergesidir; buluşların niteliğini, ticari olarak uygulanmasını ve çevresel etkisini doğrudan ölçmez.

İleriki çalışmalarda iki genişletme bu sınırlılıkların bir bölümünü giderebilir. İlk iki fazda tahsis miktarları Ulusal Tahsis Planlarıyla belirlendiğinden, sistemin sıkılığı ülkeden ülkeye farklılaşmıştır; ülkeler arasında farklılaşan bir maruziyet ölçüsü (örneğin emisyonların AB ETS kapsamındaki payı ya da ulusal planların sıkılığı) faz kuklalarıyla etkileştirilerek yıl sabit etkilerinin eklenmesine ve ortak şokların ayrıştırılmasına imkân verebilir. Ayrıca aynı modelin yeşil olmayan patent başvurularıyla tahmin edilmesi, gözlenen artışın yeşil teknolojilere özgü olup olmadığını gösterecektir.""",
     "Yeni alt bölüm: Çalışmanın Sınırlılıkları (karşılaştırma grubu, ortak şoklar, az küme, stok yapısı, örneklem, eksik değişkenler, ölçüm; ileriki çalışma önerileri).", once=True, ham_anchor=True)

# ============================================================ Kaynakça
deg("B2", r"""Dechezleprêtre, A., Glachant, M., Haščič, I., Johnstone, N., & Ménière, Y. (2011). \"Invention and Transfer of Climate Change--Mitigation Technologies: A Global Analysis.\" *Review of Environmental Economics and Policy, 5*(1), 109--130.""",
    "Dechezleprêtre, A., Glachant, M., Haščič, I., Johnstone, N. ve Ménière, Y. (2011). Invention and transfer of climate change–mitigation technologies: A global analysis. *Review of Environmental Economics and Policy, 5*(1), 109–130.",
    "Kaynakça kaydı diğerleriyle aynı biçime getirildi (“&” yerine “ve”, tırnaklar kaldırıldı, başlık cümle düzeninde).", tur="biçim")
cik("B2", r"OECD. Environment-Related Technologies Patents \[Dataset\]; OECD Data Explorer, OECD.STI.PIE; OECD: Paris, France, 2024; Available online: https://data-explorer.oecd.org (accessed on 1 March 2026).", "Aynı veri seti iki yerde, iki farklı yılla (2024 ve 2026) kayıtlıydı; metindeki atıfla (OECD, 2026) uyumlu olan kayıt bırakıldı.")

ks = H0.index('<h1 id="kaynakça">'); ke = H0.index('<h2 id="veri-kaynakları">')
kay = [(ks + m.start(), duz(m.group(0))) for m in re.finditer(r"<p>.*?</p>", H0[ks:ke], re.S)]
fold = lambda s_: s_.lower().translate(str.maketrans("çşıöüğéčİ", "csiougeci"))
YENI = [("Blundell, R., Griffith, R. ve Van Reenen, J. (1999). Market share, market value and innovation in a panel of British manufacturing firms. *Review of Economic Studies, 66*(3), 529–554.", None, "T5"),
        ("Blundell, R., Griffith, R. ve Windmeijer, F. (2002). Individual effects and dynamics in count data models. *Journal of Econometrics, 108*(1), 113–131.", None, "T5"),
        ("MacKinnon, J. G., Nielsen, M. Ø. ve Webb, M. D. (2023). Cluster-robust inference: A guide to empirical practice. *Journal of Econometrics, 232*(2), 272–299.", "MacKinnon, J. G. ve Webb", "C2 C9"),
        ("StataCorp. (2025). *Stata statistical software: Release 19*. StataCorp LLC.", None, "B2")]
G_K = None
for md, once, bl in YENI:
    pos = next(p_ for p_, t_ in kay if t_.startswith(once)) if once else next(p_ for p_, t_ in kay if fold(t_) > fold(md))
    G_K = G_K or _no("B2 T5 C2 C9", "ekleme", "Kaynakçaya dört kayıt eklendi: metne eklenen yeni atıfların karşılıkları ve Stata.", "", " / ".join(duz(I(x[0])) for x in YENI))
    _ekle(pos, pos, f'<div class="ekle" {_at(G_K, bl)}>\n<p>{I(md)}</p>\n</div>\n')
