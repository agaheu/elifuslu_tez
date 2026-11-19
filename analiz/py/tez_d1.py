"""Tez güncellemesi, 1. kısım: Bölüm 5.1–5.6. Her değişiklik bir bulguya (analiz/py/icerik.py) bağlıdır."""
import re
from tezarac import *
from tez_sayi import *

src = SRC.read_text(encoding="utf8")

# ============================================================ B1: semboller ve denklem numaraları (gruplu)
G_ALFA = None
segs = []
for sg in re.findall(r"\$\$.+?\$\$|\$[^$\n]+\$", src):
    if r"\alpha_{i}" in sg and sg not in segs: segs.append(sg)
for sg in segs:
    for k in range(1, H0.count(I(sg)) + 1):
        G_ALFA = deg("B1", sg, sg.replace(r"\alpha_{i}", "c_{i}"), "Ülke sabit etkisinin simgesi α yerine c yapıldı; α yalnızca aşırı yayılım parametresi için kullanılıyor (aynı simgenin üç ayrı anlamı vardı).", kacinci=k, grup=G_ALFA, tur="biçim")
bc_eq = [l.strip() for l in src.split("\n") if r"\alpha_{1}" in l][0]
deg("B1", bc_eq, bc_eq.replace(r"\alpha_{1}", "q_{1}").replace(r"\alpha_{2}", "q_{2}"), grup=G_ALFA)

G_NO = None
numarasiz = [l.strip() for l in src.split("\n") if l.strip().startswith("$$") and l.strip().endswith("$$") and l.count("$$") == 2]
assert len(numarasiz) == 8, len(numarasiz)
for sg, n in zip(numarasiz, [14, 15, 16, 19, 20, 21, 22, 23]):
    G_NO = ek("B1", sg, rf"\({n}\)", "Numarasız denklemler numaralandı: (13)'ten sonraki denklemler (14)–(23).", grup=G_NO, tur="biçim")
ek("B1", "K~i,t~ = (1 − δ)K~i,t−1~ + P~i,t~", r"\(18\)", grup=G_NO)

# ============================================================ B2: atıf yazımı (gruplu)
G_B2 = deg("B2", "Hausman ve diğ.(1984)", "Hausman ve diğ. (1984)", "Metin içi atıflarda “&” ve “and” yerine “ve”; eksik boşluk ve virgüller düzeltildi.", tur="biçim")
for a, b_ in [("(Allison&Waterman, 2002)", "(Allison ve Waterman, 2002)"), ("(Efron&Tibshirani, 1993)", "(Efron ve Tibshirani, 1993)"), ("(Allison andWaterman, 2002)", "(Allison ve Waterman, 2002)"),
              ("ulaşmıştır(OECD,2026).", "ulaşmıştır (OECD, 2026)."), ("sağlamaktadır(Bel ve Joseph,2018).", "sağlamaktadır (Bel ve Joseph, 2018)."),
              ("(Dechezleprêtre ve diğ.,2011; Veefkind ve diğ., 2012; Haščič ve Migotto 2015)", "(Dechezleprêtre ve diğ., 2011; Veefkind ve diğ., 2012; Haščič ve Migotto, 2015)"),
              ("etkilemektedir(Bel&Joseph,2018).", "etkilemektedir (Bel ve Joseph, 2018)."), ("Pakes&Griliches(1984)", "Pakes ve Griliches (1984)"), ("Bel&Joseph(2018) çalışmalarında", "Bel ve Joseph (2018) çalışmalarında")]:
    deg("B2", a, b_, grup=G_B2)

# ============================================================ 5.1
deg("Y6", "Bağımlı değişkenin yalnızca pozitif değerler alabildiği durumlarda", "Bağımlı değişkenin negatif olmayan değerler aldığı durumlarda", "Sayım değişkeni sıfır da alabilir; “yalnızca pozitif” yerine “negatif olmayan”.")
deg("Y6", "En yaygın biçimi olan negatif binom modelinde olasılık fonksiyonu", "En yaygın biçimi olan ve NB2 olarak adlandırılan negatif binom modelinde olasılık fonksiyonu", "Kullanılan biçim adlandırıldı (NB2).")
deg("Y6", "Aşırı yayılım bulunduğunda negatif binom modeli Poisson tahmincisine göre daha etkin tahminler üretmektedir.", "Aşırı yayılım bulunduğunda ve varyans fonksiyonu doğru tanımlandığında negatif binom modeli Poisson tahmincisine göre daha etkin tahminler üretmektedir.", "Etkinlik üstünlüğü koşula bağlandı.")
deg("M5", "Sabit etkili Poisson tahmincisi ayrıca dağılım varsayımına karşı sağlamdır (Cameron ve Trivedi, 2013).", "Sabit etkili Poisson tahmincisi ayrıca dağılım varsayımına karşı sağlamdır (Wooldridge, 1999; Cameron ve Trivedi, 2013).", "Asıl kaynak (Wooldridge, 1999) kaynakçada vardı ama metinde atıf yoktu.")

deg("C2", "MacKinnon ve Webb (2017), wild kümelenmiş bootstrap yöntemini inceledikleri çalışmada, küme büyüklüklerinin birbirinden çok farklı olduğu durumlarda asimptotik kümelenmiş standart hataların daha da güvenilmez hâle geldiğini göstermiştir. Bu durumlarda çıkarsama, kümelenmiş eşli bootstrap ile yapılmaktadır.",
    "MacKinnon ve Webb (2017), kümelerin birbirinden çok farklı olduğu durumlarda asimptotik kümelenmiş standart hataların daha da güvenilmez hâle geldiğini göstermiştir. Bu çalışmalar az sayıda küme için wild kümelenmiş bootstrap yöntemini önermektedir; ancak bu yöntem esas olarak doğrusal modeller için geliştirilmiştir. Bu çalışmada, doğrusal olmayan sayım modellerine doğrudan uygulanabildiği için kümelenmiş eşli bootstrap kullanılmıştır. Küme sayısı az ve kümelerin tahmindeki ağırlıkları dengesiz olduğunda eşli bootstrap standart hataları da iyimser olabilmektedir; bu nedenle bulgular küme jackknife yöntemiyle ayrıca sınanmıştır.",
    "Anlatılan yöntem (wild bootstrap) ile uygulanan yöntem (eşli bootstrap) arasındaki kopukluk giderildi; kaynak yalnızca gerçekten söylediği şey için kullanıldı; yöntemin sınırı yazıldı.")
blok("C4", "Ortak hipotezler, bootstrap kovaryans matrisiyle hesaplanan Wald istatistiğiyle sınanmaktadır.",
     r"Sapma düzeltmeli aralık, bootstrap dağılımının nokta tahmini etrafında yaklaşık simetrik olduğu durumlar için uygundur. Bootstrap dağılımı nokta tahminine göre belirgin biçimde kaymışsa ${\widehat{z}}_{0}$ büyümekte ve aralık kararsızlaşmaktadır; bu nedenle sapma düzeltmeli aralıkların yanında yüzdelik aralıklar da raporlanmıştır.",
     "Sapma düzeltmeli (BC) aralığın sınırı yazıldı.", once=True)
blok("C2 C5 C9", "Eşli bootstrap, modelin tamamını her yeniden örneklemde yeniden tahmin ettiğinden",
     r"""Küme jackknife yönteminde model, her seferinde bir küme dışarıda bırakılarak $G$ kez yeniden tahmin edilmekte ve varyans

$${\widehat{V}}_{JK}\left( \widehat{\beta} \right) = \frac{G - 1}{G}\sum_{g = 1}^{G}\left( {\widehat{\beta}}_{(g)} - \bar{\beta} \right)^{2}$$ (17)

biçiminde hesaplanmaktadır. Burada ${\widehat{\beta}}_{(g)}$, $g$ kümesi dışarıda bırakıldığında elde edilen tahmini, $\bar{\beta}$ ise bu tahminlerin ortalamasını göstermektedir. Test istatistiği $G - 1$ serbestlik dereceli $t$ dağılımıyla değerlendirilmektedir. Az sayıda ve dengesiz kümelerde bu yöntem, kümelenmiş ve bootstrap standart hatalarına göre daha temkinli sonuç vermektedir (MacKinnon, Nielsen ve Webb, 2023).""",
     "İkinci çıkarsama yöntemi olarak küme jackknife tanıtıldı.")

# ============================================================ 5.2 – 5.3
ek("T9", "her fazdaki yeşil patent yoğunluğu bu referans döneme göre ölçülmektedir.",
   "Referans dönem, sistemin fiilen başladığı 2005 yılından önceki bütün tahmin yıllarını kapsamaktadır. 2003/87/AT sayılı Direktif Ekim 2003'te kabul edildiğinden 2003–2004 yıllarında beklenti etkileri oluşmuş olabilir; bu nedenle referans dönemin 1997–2002 ile sınırlandırıldığı tahmin sağlamlık testi olarak sunulmuştur (Bölüm 5.8.1).",
   "Referans dönemin seçimi gerekçelendirildi; Direktif'in 2003'te kabul edildiği belirtildi.")
deg("T10", "Fazların başlangıç ve bitiş tarihleri ile kuralları, AB düzeyindeki yasama süreçlerinde, ülkelerin inovasyon faaliyetinden bağımsız olarak belirlenmiştir. Dolayısıyla, fazlar ile inovasyon arasında ters nedensellik ilişkisi bulunmamaktadır.",
    "Fazların başlangıç ve bitiş tarihleri, AB düzeyindeki yasama süreçlerinde, ülkelerin inovasyon faaliyetinden bağımsız olarak belirlenmiştir; ilk iki fazda tahsis miktarları ise üye devletlerin Komisyon onayına sunduğu Ulusal Tahsis Planlarıyla saptanmıştır. Dolayısıyla, faz takvimi ile inovasyon arasında ters nedensellik ilişkisi bulunmamaktadır.",
    "İlk iki fazda tahsislerin ulusal planlarla belirlendiği eklendi; dışsallık savı faz takvimiyle sınırlandı.")
m = re.search(r'<h2 id="birinci-model-ab-ets[^>]*>', H0)
G_BAS = ham("B1", m.group(0), '<p class="bicim" @AT@ title="Bu paragraf Word dosyasında yanlışlıkla “Başlık 2” stilindeydi; “Normal” stiline alındı.">', "biçim", "5.2'nin son paragrafı yanlışlıkla başlık stilindeydi; normal paragrafa çevrildi (içindekiler tablosunda görünmemesi için).", "(Başlık 2 stili)", "(Normal paragraf)")
k = H0.index("</h2>", m.end()); ED.append((k, k + 5, "</p>", len(ED), False))
deg("T1", "Tahmin edilen etkilerin AB ETS'den kaynaklandığı yorumu; yıl etkileri modeli ve ETS öncesi döneme yerleştirilen plasebo kırılma testleriyle desteklenmektedir.",
    "Tahmin edilen farkların zamanlaması, yıl etkileri modeli ve ETS öncesi döneme yerleştirilen plasebo kırılma testleriyle incelenmektedir. Örneklemdeki bütün ülkeler AB ETS'ye aynı tarihte dâhil olduğundan tasarım bir önce–sonra karşılaştırmasıdır; tahmin edilen faz farkları aynı dönemde gerçekleşen diğer ortak gelişmelerin etkisini de içerebilir. Bu nedenle bulgular nedensel etki olarak değil, AB ETS fazlarıyla ilişkili farklar olarak yorumlanmaktadır (Bölüm 5.11).",
    "Nedensellik iddiası tasarımın taşıyabileceği düzeye indirildi; karşılaştırma grubu bulunmadığı açıkça yazıldı.")
deg("T2 Y2", "Fazların etkisi, ETS öncesi eğilimden bağımsız olarak ortaya çıkmaktadır.", "Birinci fazdaki hızlanma ve ikinci fazın başındaki düzey artışı, ETS öncesi eğilim hesaba katıldığında da ortaya çıkmaktadır.",
    "H5 yeniden yazıldı: “eğilimden bağımsız” iddiası stokun modelde olmasına bağlıydı; yeni ifade verinin desteklediği kadarını söylüyor.", kacinci=1)

# ============================================================ 5.4
deg("M6", "en yakın tam sayıya yuvarlanmıştır.", f"en yakın tam sayıya, yarım değerler yukarı yuvarlanmıştır. Yuvarlanmamış değerlerle yapılan Poisson tahmininde faz katsayıları üçüncü ondalıkta aynıdır ({tr(R['ek']['kesirli']['F1'], 4)} ve {tr(R['ek']['kesirli']['F2'], 4)}).",
    "Yuvarlama kuralı veri dosyasıyla tutarlı hâle getirildi; sonuçların değişmediği belirtildi.")
blok("Y5", "EPO başvurularının kullanılması iki avantaj sağlamaktadır.",
     "Bu çalışmada yeşil inovasyon, Avrupa Patent Ofisine yapılan iklim değişikliği azaltım teknolojisi patent başvurularıyla ölçülmektedir. Patent başvuruları buluş faaliyetinin göstergesidir; buluşların niteliğini, yayılmasını ve çevresel etkisini doğrudan ölçmez. Bu nedenle bulgular yeşil patentleme faaliyetine ilişkindir. Ayrıca en son yıllara ait başvuru sayıları, verinin derlendiği tarihe bağlı olarak eksik olabilmektedir; 2018–2020 yılları dışarıda bırakıldığında bulgular zayıflamamaktadır (Bölüm 5.8.1).",
     "“Yeşil inovasyon”un işlemsel tanımı ve patent göstergesinin sınırları eklendi.")
ek("M8", "hiçbir gözlemde sıfır değer bulunmamaktadır.",
   f"Sıfır değer gözlenebilir olduğundan (tahmin dönemi öncesinde {R['veri']['sifir_ccm'][0][0]} için {R['veri']['sifir_ccm'][0][1]} yılında sıfır başvuru vardır) sıfır-kesikli bir model gerekmemektedir; sıfır-kesikli negatif binom tahmininde katsayılar yalnızca dördüncü ondalıkta değişmektedir (birinci faz {tr(J['sifir']['zt_nb']['F1'], 4)}; ikinci faz {tr(J['sifir']['zt_nb']['F2'], 4)}).",
   "İkinci jürinin sıfır-kesikli model sorusuna hazır cevap.")
deg("Y6", "En yüksek yoğunluk Danimarka, Almanya, Finlandiya ve İsveç'te, en düşük yoğunluk ise Yunanistan, Portekiz ve İspanya'da gözlemlenmektedir.",
    f"ETS döneminde en yüksek yoğunluk Danimarka, Almanya, Finlandiya ve İsveç'te, en düşük yoğunluk ise Yunanistan, Portekiz ve İspanya'da gözlemlenmektedir; ETS öncesi dönemde en yüksek ortalama yoğunluk Lüksemburg'a aittir ({tr(R['veri']['yogunluk_ulke']['Lüksemburg'][0], 2)}).",
    "Sıralama yalnızca ETS dönemi için doğruydu.")
deg("Y6 B1", "Modelde altı kontrol değişkeni olarak; yeşil patent stoku, GSYİH büyüme oranı, yenilenebilir enerji payı, enerji ithalat bağımlılığı, imalat sanayi payı ve dış ticaret hacmi yer almaktadır.",
    "Modelde yeşil patent stoku ile beş kontrol değişkeni (GSYİH büyüme oranı, yenilenebilir enerji payı, enerji ithalat bağımlılığı, imalat sanayi payı ve dış ticaret açıklığı) yer almaktadır.",
    "Tablo 5.5 ile tutarlı sayım (stok + beş kontrol) ve tek değişken adı.")
deg("Y6", "δ = 0,15 yıllık eskime oranını göstermektedir.", "δ = 0,15 yıllık eskime oranını göstermektedir (Hall ve Mairesse, 1995; Popp, 2002; Noailly ve Smeets, 2015).", "Eskime oranı için metin içi atıf eklendi (üçü de kaynakçada var).")
deg("Y6", "ortalama yıllık büyüme oranıdır (0,0691)", "ortalama yıllık logaritmik büyümesidir (0,0691)", "0,0691 aritmetik değil logaritmik ortalama büyümedir.")
deg("T4", "Yeşil patent stoku, inovasyon girdilerinin yeşil teknolojiler alanındaki birikmiş çıktısını doğrudan ölçtüğünden, ülkelerin Ar-Ge kapasitesindeki farklılıklar da bu değişken tarafından kontrol edilmektedir.",
    "Yeşil patent stoku birikmiş patent çıktısını ölçmekte ve ülkelerin Ar-Ge kapasitesinin dolaylı bir göstergesi olarak kullanılmaktadır; Ar-Ge harcamaları modelde ayrıca yer almamaktadır.",
    "Stok bir girdi değil çıktı ölçüsüdür; Ar-Ge'nin “kontrol edildiği” iddiası yumuşatıldı.")

# ============================================================ 5.5
deg("T8", "Birleşik Krallık 2020 tarihinde AB üyeliğinden çıktığı için analize dahil edilmemiştir.",
    "Örneklem, ETS öncesi referans dönemin tamamında AB üyesi olan on beş ülkeden on dördünü kapsamaktadır. Birleşik Krallık 2020 sonuna kadar AB ETS kapsamında kalmış olmakla birlikte ana örnekleme alınmamıştır; bu durum çalışmanın bir sınırlılığıdır (Bölüm 5.11).",
    "Yanlış gerekçe çıkarıldı (Birleşik Krallık 31.12.2020'ye kadar AB ETS içindeydi); örneklem ölçütü yazıldı. YAZAR: gerçek dışlama gerekçesi eklenmeli ya da 15 ülkeyle sağlamlık tahmini yapılmalı.")
deg("Y6", "İlgili ülkelere ait kontrol değişkenleri bir dönem gecikmeli olarak modele girdiğinden, veriler 1996 yılından itibaren veri tabanlarından eksiksiz temin edilebilmiştir.",
    "Reel GSYİH serisi 1995'ten, GSYİH büyüme oranı 1996'dan itibaren bütün ülkeler için mevcuttur; kontrol değişkenleri bir dönem gecikmeli olarak modele girdiğinden tahmin döneminin ilk yılı 1997'dir.",
    "Tahmin döneminin neden 1997'de başladığı açık yazıldı.")
blok("Y6", ("tablo", "5.3"), "Not: Kontrol değişkenleri ve yeşil patent stoku cari dönem ($t$) değerleriyle verilmiştir; modelde bir dönem gecikmeli olarak yer almaktadır.", "Tablo 5.3'ün cari dönem değerleri verdiği notla belirtildi (Tablo 5.2 gecikmeli değerleri veriyor).")

kor = lambda a, b_: tr(ici[(a, b_)] if (a, b_) in ici else ici[(b_, a)], 2)
CC = ["lnK1", "gdp_growth_l1", "renew_wdi_l1", "impdep_l1", "manuf_l1", "trade_l1"]; CN = [r"$\ln\left( 1 + K_{t - 1} \right)$", "Büyüme", "Yenilenebilir", "İthalat bağ.", "İmalat", "Ticaret"]
deg("M3", "Değişkenler arasındaki korelasyonların mutlak değeri 0,35'i aşmamaktadır. Bu sonuç, kontrol değişkenleri arasında ciddi bir çoklu doğrusallık sorunu bulunmadığını göstermektedir.",
    f"Havuzlanmış korelasyonların mutlak değeri en fazla 0,35 düzeyindedir (Panel A). Ancak sabit etkili modelde katsayılar ülke içi değişimden tahmin edildiğinden belirleyici olan, değişkenlerin ülke ortalamalarından arındırılmış değerleri arasındaki korelasyonlardır (Panel B). Ülke içi korelasyonlar daha yüksektir: yeşil patent stoku ile yenilenebilir enerji payı arasında {kor('lnK1', 'renew_wdi_l1')}, dış ticaret açıklığı ile {kor('lnK1', 'trade_l1')}. Bu nedenle söz konusu kontrol değişkenlerinin katsayıları stokun etkisinden tam olarak ayrıştırılamamaktadır.",
    "Havuzlanmış korelasyonlar sabit etkili model için yanıltıcıydı; ülke içi korelasyonlar eklendi.")
ek("M3", "**Tablo 5.4.** Kontrol Değişkenleri Arasındaki Pearson Korelasyon Katsayıları", "(Panel A: havuzlanmış)", "Tablo 5.4 iki panelli yapıldı.")
pb = "| | " + " | ".join(CN) + " |\n|---|" + "---|" * 6 + "\n"
for i, a in enumerate(CC): pb += f"| {CN[i]} | " + " | ".join(("1,00" if j == i else kor(a, CC[j]) if j < i else "") for j in range(6)) + " |\n"
blok("M3", "Not: Tüm değişkenler bir dönem gecikmelidir (t − 1).",
     "**Tablo 5.4 (devam).** Panel B: Ülke İçi (Ülke Ortalamalarından Arındırılmış) Korelasyon Katsayıları\n\n" + pb + "\nNot: Değişkenlerin ülke ortalamalarından farkları arasındaki Pearson korelasyon katsayılarıdır. Tüm değişkenler bir dönem gecikmelidir (t − 1).",
     "Tablo 5.4'e Panel B (ülke içi korelasyonlar) eklendi.")

# ============================================================ 5.6
G_BOS = ham("B1", '<h4 id="section"></h4>\n', '<span class="bicim" @AT@></span>', "biçim", "İki boş başlık paragrafı silindi (Tablo 5.5'ten sonra ve 5.10'dan önce).", "(boş başlık)", "(silindi)")
ham("B1", '<h2 id="section-1"></h2>\n', '<span class="bicim" @AT@></span>', "biçim", grup=G_BOS)

ek("M5", "Bu çalışmada her ülke için 24 yıllık gözlem bulunduğundan, söz konusu sapma daha da sınırlıdır.",
   "Aynı çalışma, bu tahmincinin standart hatalarının olduğundan küçük tahmin edilebildiğini de göstermektedir; bu nedenle çıkarsama asimptotik standart hatalarla değil bootstrap ile yapılmıştır.",
   "Kaynağın (Allison ve Waterman, 2002) standart hatalara ilişkin uyarısı eklendi.")
deg("M7 C3", "alternatif tahminci olarak ise sabit etkili Poisson sözde en çok olabilirlik tahmincisi kullanılmıştır. Negatif binom modeli aşırı yayılımı açıkça modelleyerek etkinlik sağlamakta, Poisson sözde en çok olabilirlik tahmincisi ise dağılım varsayımına karşı tutarlılık güvencesi vermektedir.",
    "eş düzeyde ikinci tahminci olarak ise sabit etkili Poisson sözde en çok olabilirlik tahmincisi kullanılmıştır. Negatif binom modeli aşırı yayılımı açıkça modellemekte ve ülkelere daha dengeli ağırlık vermekte, Poisson sözde en çok olabilirlik tahmincisi ise dağılım varsayımına karşı tutarlılık güvencesi vermektedir.",
    "Poisson “alternatif” değil eş düzeyde ikinci tahminci; negatif binomun tercih gerekçesi ağırlıklandırmaya dayandırıldı.")
ag = "| Ülke | Poisson ağırlığı (%) | Negatif binom ağırlığı (%) |\n|---|---|---|\n"
for u in sorted(R["agirlik"], key=lambda x: -R["agirlik"][x][0]): ag += f"| {u} | {tr(R['agirlik'][u][0], 1)} | {tr(R['agirlik'][u][1], 1)} |\n"
blok("C3", "Tahminci seçimi üç değerlendirmeye dayanmaktadır.",
     f"İki tahminci ülkeleri farklı biçimde ağırlıklandırmaktadır. Poisson tahmincisi gözlemleri beklenen başvuru sayısıyla ağırlıklandırdığından Almanya'nın tahmindeki payı yaklaşık yüzde {tr(R['agirlik']['Almanya'][0], 0)}'tir; negatif binom tahmincisinde bu pay yaklaşık yüzde {tr(R['agirlik']['Almanya'][1], 0)}'dir (Tablo 5.5a). Dolayısıyla Poisson katsayıları başvuru ağırlıklı, negatif binom katsayıları ülkelere daha eşit ağırlık veren ortalama farkları göstermektedir; iki tahminci arasındaki farklar büyük ölçüde bu ağırlıklandırmadan kaynaklanmaktadır.\n\n**Tablo 5.5a.** Ülkelerin Tahmindeki Ağırlık Payları (Birinci Model)\n\n" + ag +
     "\nNot: Ağırlıklar, birinci modelin tahmin denklemlerinde gözlemlere verilen örtük ağırlıkların ülke toplamlarıdır (Poisson: beklenen başvuru sayısı; negatif binom: beklenen başvuru sayısının aşırı yayılıma göre düzeltilmiş değeri). Ülke sabit etkili Poisson modelinde bir ülkenin ağırlığı, o ülkenin toplam başvurulardaki payına eşittir.",
     "İki tahmincinin neden farklı sonuç verdiği açıklandı; ülke ağırlıkları tablosu eklendi.")
blok("M1", "Buna göre model, patent başvurularının sayısını değil, reel GSYİH başına beklenen başvuru sayısını",
     f"Reel GSYİH'nin maruziyet değişkeni olarak kullanılması, bağımlı büyüklüğü yeşil patent yoğunluğu olarak tanımlayan bir tercihtir. GSYİH esnekliği serbest bırakıldığında birim esneklik kısıtı reddedilmektedir (esneklik negatif binom modelinde {tr(TZ.T514['elast']['nb'][0], 3)}, Poisson modelinde {tr(TZ.T514['elast']['poisson'][0], 3)}; Bölüm 5.8.1). Bu nedenle sonuçlar her iki tanımla birlikte sunulmuştur; faz farklarının işareti iki tanımda aynıdır; birinci ve ikinci faz farkları serbest esneklik tanımında da anlamlıdır.",
     "Maruziyet kısıtının bir tercih olduğu ve veriyle reddedildiği yöntem bölümünde de belirtildi.")
deg("T1 B1", "[Ortak zaman değişimi, yeşil patent stoku ve zamanla değişen kontrol değişkenleri aracılığıyla kontrol edilmektedir.]{.mark}",
    "Ortak zaman değişimi, yeşil patent stoku ve zamanla değişen kontrol değişkenleri aracılığıyla kısmen kontrol edilmektedir; yıl sabit etkileri kullanılamadığından bütün ülkeleri aynı anda etkileyen ortak şoklar faz katsayılarından tümüyle ayrıştırılamamaktadır.",
    "“Kontrol edilmektedir” iddiası “kısmen” olarak düzeltildi; sarı vurgu kaldırıldı.")
G_VUR = ham("B1", "<mark>öngörücüsüne</mark>", '<span class="bicim vurgu" @AT@ title="Sarı vurgu kaldırıldı">öngörücüsüne</span>', "biçim", "Kalan sarı vurgular kaldırıldı.", "(sarı vurgulu)", "(vurgusuz)")
deg("T4", "Bu nedenle stok, emisyon ticaret sisteminin zaman içindeki etkisinin aktarıldığı bir aracı değişken niteliği taşımaktadır. Stoklu modelde faz katsayıları, yeşil patent stoku sabitken ilgili fazın yeşil patent yoğunluğu üzerindeki doğrudan etkisini ölçmektedir. Stok katsayısı ise önceki dönemlerde oluşan patentlerin sonraki yıllara taşınan etkisini göstermektedir. Stoksuz model ise politikanın stok kanalı dahil toplam etkisini ölçmektedir.",
    "Bu nedenle stok, emisyon ticaret sisteminin zaman içindeki etkisinin aktarılabileceği bir kanal niteliği taşımaktadır; ancak stok AB ETS'den bağımsız nedenlerle de büyümektedir. Stoklu modelde faz katsayıları, yeşil patent stoku sabitken ilgili fazdaki yeşil patent yoğunluğunun ETS öncesine göre farkını ölçmektedir (stok sabitken gözlenen fark). Stok katsayısı ise önceki dönemlerde biriken patentler ile cari başvurular arasındaki ilişkiyi göstermektedir. Stoksuz model, stok hesaba katılmadan gözlenen farkı vermektedir; bu fark ETS öncesinde başlayan artış eğilimini de içerdiğinden AB ETS'nin toplam etkisi olarak yorumlanmamaktadır.",
    "“Doğrudan etki / toplam etki” yerine “stok sabitken / stok hesaba katılmadan gözlenen fark”; aracılık yorumu yumuşatıldı.")
o = SP["A"]["nb"]["ort"]
deg("T5", "Bu çalışmada her ülke için 24 yıllık gözlem bulunmaktadır. Ayrıca stok, yalnızca bir önceki yılın patentlerinden değil, 1990'dan itibaren biriken ve her yıl yüzde 15 aşınan bir toplamdan oluştuğundan, tek bir gecikmeli bağımlı değişkene göre hata terimiyle ilişkisi çok daha zayıftır.",
    f"Bu çalışmada her ülke için 24 yıllık gözlem bulunmaktadır. Bununla birlikte stok, bağımlı değişkenin geçmiş değerlerinden türetildiğinden kesin dışsallık varsayımı sağlanmamaktadır. Sapmanın büyüklüğü benzetimle sınanmıştır: faz etkilerinin sıfır olduğu ve verinin tahmin edilen modele göre üretildiği (stok her tekrarda üretilen başvurulardan yeniden hesaplanarak) {tr(SP['ayar']['tekrar'], 0)} yapay örneklemde, birinci modelin negatif binom faz katsayıları ortalama olarak {tr(o[0], 3)}, {tr(o[1], 3)} ve {tr(o[2], 3)} bulunmuştur; yani gerçek etki sıfırken dahi faz katsayıları yukarı yanlı, stok katsayısı ise aşağı yanlıdır (gerçek değer {tr(SP['ayar']['gamma_A'], 2)}; ortalama tahmin {tr(SP['A']['nb']['ort_gamma'], 2)}). İkinci modelde birinci faz eğimi ve ikinci faz düzeyi için ortalama sapma sıfıra çok yakındır ({tr(o[4], 3)} ve {tr(o[5], 3)}). Bu nedenle birinci modelin faz katsayıları üst sınır olarak yorumlanmış, temel çıkarımlar ikinci modele dayandırılmıştır. Ayrıca ülke sabit etkileri yerine ön-örneklem ortalamasının kullanıldığı tahminci (Blundell, Griffith ve Van Reenen, 1999; Blundell, Griffith ve Windmeijer, 2002) sağlamlık testi olarak sunulmuştur (Bölüm 5.8.1).",
    "“Sapma ihmal edilebilir” savı sınanmamıştı; benzetim sonucu yazıldı, birinci modelin katsayıları üst sınır olarak nitelendi.")
deg("T3 T5", "Birinci ve ikinci faz katsayılarının stoksuz modelde de pozitif ve anlamlı olması, bu fazlara ilişkin bulguların stok değişkeninin modelde yer almasına bağlı olmadığını göstermektedir.",
    "Birinci ve ikinci faz katsayılarının stoksuz modelde, doğrusal eğilim eklendiğinde de pozitif ve anlamlı olması (Tablo 5.14, satır d), bu fazlara ilişkin bulguların stok değişkeninin modelde yer almasına bağlı olmadığını göstermektedir.",
    "Stoksuz modelin kanıt değeri, eğilim eklenmiş tanıma dayandırıldı.")
deg("Y6", "hesaplanmıştır (Tablo 5.5).", "hesaplanmıştır (Tablo 5.6).", "Yanlış tablo numarası.")
cik("T4", "Varyans şişirme faktörlerinin ortalaması 4,08'dir ve yaygın olarak kullanılan 10 eşiğinin altındadır.", "10 eşiği tek tek değişkenler içindir; ortalama için anlamı yoktur.")
ham("B1", "<mark>Bu durum, üçüncü faz kuklasının, ülke içinde zamanla birikerek artan yeşil patent stokuyla birlikte hareket etmesinden kaynaklanabilmektedir.</mark>",
    '<span class="bicim vurgu" @AT@ title="Sarı vurgu kaldırıldı">Bu durum, üçüncü faz kuklasının, ülke içinde zamanla birikerek artan yeşil patent stokuyla birlikte hareket etmesinden kaynaklanabilmektedir.</span>', "biçim", grup=G_VUR)
V2 = [("ETS öncesi eğilim ($t^{*}$)", "tstar"), ("Faz 1 düzey", "F1"), ("Faz 1 eğim", "S1"), ("Faz 2 düzey", "F2"), ("Faz 2 eğim", "S2"), ("Faz 3 düzey", "F3"), ("Faz 3 eğim", "S3"), (r"$\ln\left( 1 + K_{t - 1} \right)$", "lnK1"),
      ("GSYİH büyümesi", "gdp_growth_l1"), ("Yenilenebilir enerji payı", "renew_wdi_l1"), ("Enerji ithalat bağımlılığı", "impdep_l1"), ("İmalat payı", "manuf_l1"), ("Dış ticaret açıklığı", "trade_l1")]
blok("T2", "Ana bulguları oluşturan birinci ve ikinci faz kuklalarının faktörleri sırasıyla 1,80 ve 4,79",
     f"İkinci modelde ülke içi varyans şişirme faktörleri daha yüksektir (Tablo 5.6a): ETS öncesi eğilim için {tr(vif2['tstar'], 1)}, üçüncü faz düzeyi için {tr(vif2['F3'], 1)}, yeşil patent stoku için {tr(vif2['lnK1'], 1)}. Bu değerler, ikinci modelin ETS öncesi eğilim ile yeşil patent stokunu birbirinden ayırmakta zorlandığını göstermektedir; stok ile zaman arasındaki ülke içi korelasyon {tr(ik['lnK1~zaman'], 2)} düzeyindedir.\n\n**Tablo 5.6a.** İkinci Model İçin Varyans Şişirme Faktörleri\n\n| Değişken | VIF |\n|---|---|\n" +
     "".join(f"| {a} | {tr(vif2[k], 2)} |\n" for a, k in V2) + "\nNot: Değişkenlerin ülke ortalamalarından arındırılmış değerleriyle hesaplanmıştır.",
     "İkinci modelin (tezde raporlanmayan) varyans şişirme faktörleri eklendi.")

deg("C2 C7", "Küme sayısının azlığı ve küme büyüklüklerindeki farklılık nedeniyle ülke düzeyinde kümelenmiş eşli bootstrap uygulanmıştır. Yıl etkileri modeli ile plasebo kırılma testlerinde ülke düzeyinde kümelenmiş standart hatalar kullanılmıştır.",
    "Küme sayısının azlığı ve ülkelerin tahmindeki ağırlıklarının çok farklı olması nedeniyle ülke düzeyinde kümelenmiş eşli bootstrap uygulanmıştır. Yıl etkileri modeli ile plasebo kırılma testlerinde de aynı bootstrap yöntemi kullanılmış, ülke düzeyinde kümelenmiş standart hatalara dayanan sonuçlar karşılaştırma amacıyla ayrıca verilmiştir.",
    "Gerekçe düzeltildi (küme büyüklükleri eşit: her ülkede 24 gözlem; farklı olan ağırlıklar). Bütün tablolarda aynı çıkarsama yöntemi kullanıldı.")
cik("C2", "Negatif binom modelinde bootstrap, katsayılar adlandırılmış ifadeler olarak tanımlanarak uygulanmıştır.", "Okuyucu için anlamsız yazılım ayrıntısı çıkarıldı.")
deg("B2", "Tüm tahminler Stata 19 ile yapılmış,", "Tüm tahminler Stata 19 (StataCorp, 2025) ile yapılmış,", "Yazılım için atıf eklendi.")
sa = S["A"]; yzd = lambda x: tr(100 * x, 0)
st = "| Çıkarsama yöntemi | NB: Faz 1 | NB: Faz 2 | NB: Faz 3 | Poisson: Faz 1 | Poisson: Faz 2 | Poisson: Faz 3 |\n|---|---|---|---|---|---|---|\n"
for ad, k in [("Kümelenmiş standart hata, $t(13)$", "rej_cl"), ("Eşli bootstrap standart hatası, normal dağılım", "rej_boot"), ("Eşli bootstrap standart hatası, $t(13)$", "rej_boot_t"), ("Küme jackknife, $t(13)$", "rej_cv3")]:
    st += f"| {ad} | " + " | ".join(yzd(v) for v in sa["nb"][k] + sa["poisson"][k]) + " |\n"
blok("C1 C6 C9", "Aynı ülkeye ait gözlemlerin hata terimleri zaman boyunca ilişkili olabileceğinden, standart hatalar ülke düzeyinde kümelenmiştir.",
     f"""Küme sayısı az olduğundan katsayıların anlamlılık düzeyleri normal dağılıma göre değil, bootstrap standart hatasıyla hesaplanan test istatistiğinin $G - 1 = 13$ serbestlik dereceli $t$ dağılımıyla karşılaştırılmasıyla belirlenmiştir.

Yatay kesit bağımlılığı testleri ülkeler arasında bağımlılık bulunduğunu göstermektedir (Tablo 5.9). Ülke düzeyinde yeniden örnekleme bu bağımlılığı hesaba katmadığından, raporlanan anlamlılık düzeyleri iyimser olabilir; bu nedenle sonuçlar küme jackknife ile de sınanmıştır.

Çıkarsama yöntemlerinin sınırlı örneklemdeki davranışı benzetimle incelenmiştir. Faz etkilerinin sıfır olduğu ve verinin tahmin edilen modele göre üretildiği {sa['n']} yapay örneklemde, yüzde 5 anlamlılık düzeyinde boş hipotezin reddedilme oranları Tablo 5.6b'de verilmektedir. Gerçek etkinin sıfır olduğu bu benzetimlerde, kümelenmiş eşli bootstrap standart hatalarına dayanan testler boş hipotezi {simrg('rej_boot', 'A')} oranında reddetmektedir; ülkeler arasında küçük bir ortak şok eklendiğinde bu oran {simrg('rej_boot', 'B')} olmaktadır. Küme jackknife {simrg('rej_cv3', 'A')} ile nominal düzeye en yakın sonucu vermektedir. Bu nedenle sınırdaki sonuçlar temkinle yorumlanmış, temel bulgular küme jackknife ve parametrik bootstrap ile doğrulanmıştır (Tablo 5.11a).

**Tablo 5.6b.** Gerçek Etki Sıfırken Yüzde 5 Düzeyinde Ret Oranları (%, Birinci Model)

{st}
Not: Nominal düzey yüzde 5'tir. {sa['n']} benzetim tekrarı; her tekrarda {S['ayar']['B']} bootstrap tekrarı. Veriler, faz kuklaları dışarıda bırakılarak tahmin edilen ülke sabit etkili negatif binom modelinden üretilmiş, yeşil patent stoku her tekrarda üretilen başvurulardan yeniden hesaplanmıştır.""",
     "Yatay kesit bağımlılığının çıkarsamaya etkisi, t(13) kullanımı ve yöntemin benzetimle sınanması eklendi.")
deg("M7", "Bu nedenle çalışmada, verinin yayılım yapısıyla uyumlu olan negatif binom modeli ana tahminci olarak kullanılmış, dağılım varsayımına karşı sağlam olan Poisson sözde en çok olabilirlik tahmincisi ise alternatif tahminci olarak raporlanmıştır.",
    f"Bununla birlikte aşırı yayılım ülkeler arasında belirgin biçimde farklılaşmaktadır (ülke bazında moment tahminleri Almanya için {tr(ALFA_I['Almanya'], 3)}, Lüksemburg için {tr(ALFA_I['Lüksemburg'], 2)}); bu nedenle negatif binom modelinin etkinlik üstünlüğü kesin değildir. Negatif binom tahmincisi, ülkelere daha dengeli ağırlık verdiği için ana tahminci olarak kullanılmış, dağılım varsayımına karşı sağlam olan Poisson sözde en çok olabilirlik tahmincisi eş düzeyde raporlanmıştır.",
    "Negatif binomun tercih gerekçesi değiştirildi: ortak aşırı yayılım varsayımı sağlanmıyor; asıl üstünlüğü dengeli ağırlıklandırma.")

# ---- 5.6.7 – 5.6.9
G_LN = hucre("M4", "5.7", "Yeşil Patent Yoğunluğu", 0, "ln(Yeşil patent yoğunluğu)", "Birim kök tablolarında satır adı düzeltildi: testler yoğunluğun logaritmasıyla yapılmış.")
hucre("M4", "5.8", "Yeşil patent yoğunluğu", 0, "ln(Yeşil patent yoğunluğu)", "", grup=G_LN)
hucre("M4", "5.9", "Yeşil Patent Yoğunluğu", 0, "ln(Yeşil patent yoğunluğu)", "", grup=G_LN)
ek("M4", "CIPS için olasılık değerleri standartlaştırılmış Z istatistiğine aittir.", "Testler 1996–2020 dönemi için uygulanmıştır.", "Test dönemi tablo notuna yazıldı.")
ci = U["inten"]["cips_c"]
ek("M4", "birinci nesil testlerden farklı olarak yeşil patent yoğunluğu ve yeşil patent stoku için birim kök boş hipotezi reddedilmektedir.",
   f"Testler yeşil patent yoğunluğunun logaritmasıyla yapılmıştır; yoğunluğun düzey değeriyle CIPS istatistiği {tr(ci['stat'], 2)} olup birim kök boş hipotezi yüzde 10 düzeyinde dahi reddedilememektedir. Dış ticaret açıklığı ise birinci nesil testlerde trend durağan görünürken CIPS testinde düzeyde birim kök içermektedir.",
   "Sonucun logaritmik dönüşüme bağlı olduğu ve iki tablo arasındaki farkın nedeni belirtildi.")
assert ci["stat"] > ci["kd"][2]
kontrol("M4", "Pedroni testinin üç istatistiğinin tamamı", "Değiştirilmiş Phillips-Perron istatistiği pozitiftir (+2,255). Yazılımın bu istatistiği hangi kuyrukta test ettiği çıktıdan kontrol edilmelidir; emin olunamazsa “üç istatistikten ikisi” yazılmalıdır.", "YAZAR KONTROLÜ: Pedroni istatistiğinin işareti.")
cik("M4", "Dolayısıyla düzey değerleriyle tahmin, her iki test grubunun sonuçları altında da geçerlidir.", "Testler bu genellemeyi göstermiyor.")
blok("M4", ("tablo", "5.10"), "Not: Kao testi 1997–2020 dönemi için uygulanmıştır.", "Test dönemi tablo notuna yazıldı.")
aic = lambda x: f"{x:.2f}".replace(".", ",")
deg("M2", "Kontrol değişkenlerinin gecikme yapısı, bir ve iki dönem gecikmeli", "Kontrol değişkenlerinin ve yeşil patent stokunun gecikme yapısı, bir ve iki dönem gecikmeli", "Raporlanan iki dönem gecikmeli model stoku da geciktiriyor.")
ek("M2", "iki dönem gecikmeli model için 2999,78 olarak hesaplanmıştır.", f"Yalnızca kontrol değişkenlerinin iki dönem geciktirildiği modelde Akaike bilgi kriteri {aic(R['gecikme'][N]['lag2_yalniz_kontrol'])} olup bir dönem gecikmeli yapı bu karşılaştırmada da tercih edilmektedir.", "Yalnız kontrollerin geciktirildiği karşılaştırma eklendi.")
kontrol("Y4", "firmaların Ar-Ge harcamaları ile patent başvuruları arasındaki ortalama gecikmenin yaklaşık 1,6 yıl olduğunu tespit etmiştir.", "Bu rakam kaynakta doğrulanamadı. Pakes ve Griliches (1984) bölümünden sayfa numarasıyla doğrulanmalı; bulunamazsa “patent başvurularının Ar-Ge harcamalarına büyük ölçüde aynı yıl ve izleyen yıl içinde tepki verdiğini göstermiştir” yazılmalıdır.", "YAZAR KONTROLÜ: Pakes ve Griliches (1984) “1,6 yıl” aktarımı.")

# ============================================================ B1: değişken adlarının tekleştirilmesi (yumuşak: başka değişiklikle çakışan yerler atlanır)
hepsi("B1", r"Enerji İthalat bağımlılığı", "Enerji ithalat bağımlılığı", "Değişken adının yazımı tekleştirildi")
hepsi("B1", r"Dış Ticaret [Aa]çıklığı", "Dış ticaret açıklığı", "Değişken adının yazımı tekleştirildi")
hepsi("B1", r"(?<!Dış )(?<!dış )Ticaret açıklığ", "Dış ticaret açıklığ", "Aynı değişken için tek ad: “dış ticaret açıklığı”")
hepsi("B1", r"(?<![Dd]ış )ticaret açıklığ", "dış ticaret açıklığ", "Aynı değişken için tek ad: “dış ticaret açıklığı”")
