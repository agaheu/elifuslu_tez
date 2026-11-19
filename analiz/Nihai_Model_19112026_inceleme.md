# "Nihai_Model_19112026.docx" — Beşinci Bölüm İnceleme Raporu

İncelenen belge: *Beşinci Bölüm — AB ETS'nin Yeşil İnovasyon Üzerindeki Etkisinin Ekonometrik Analizi* (metin, 5 şekil, 17 tablo, kaynakça).
İnceleme tarihi: 19.11.2026

Rapor dört kısımdan oluşuyor:

1. Genel değerlendirme (güçlü yönler)
2. Yöntemsel / içerik sorunları (önem sırasına göre)
3. Sayısal tutarlılık kontrolü (yeniden hesaplanan değerler)
4. Metin, biçim ve kaynakça hataları (satır satır)

---

## 1. Genel değerlendirme

Bölüm bütün olarak tutarlı, iyi kurgulanmış ve sayım veri ekonometrisi açısından doğru bir çerçeveye oturuyor. Öne çıkan güçlü yönler:

- **Model seçimi gerekçeli.** Poisson QML (Gourieroux ve diğ., 1984; Wooldridge, 1999) ve koşulsuz sabit etkili NB (Allison & Waterman, 2002) tercihi, Hausman-Hall-Griliches koşullu NB'nin neden kullanılmadığı doğru açıklanmış.
- **Maruziyet değişkeni (GSYİH) kullanımı** ve "yeşil patent yoğunluğu" yorumu doğru; esnekliğin serbest bırakıldığı (b) modeli ile kısıtın test edilmesi iyi bir sağlamlık kontrolü.
- **İki modelin tamamlayıcılığı** (ortalama faz etkisi + segmentli ITS ile düzey/eğim ayrıştırması) iyi düşünülmüş; yıl etkileri grafiği (Şekil 5.5) bulguları görsel olarak destekliyor.
- **Stoklu/stoksuz ayrımı** (doğrudan etki vs. toplam etki) tezin en özgün katkısı; üçüncü faz yorumu bu ayrıma dayanıyor ve mantığı sağlam.
- **Sağlamlık testleri** kapsamlı: Almanya hariç, tek tek ülke dışlama, plasebo kırılmalar, gecikme yapısı, VIF, birim kök/eşbütünleşme.
- Raporlanan sayıların **iç tutarlılığı yüksek** (bkz. Kısım 3: yüzde etkiler, p değerleri, gözlem sayıları, ağırlıklı ortalamalar tamamen doğrulanıyor).

Aşağıdaki sorunlar tezi geçersiz kılacak nitelikte değil; ancak jüri tarafından sorulması muhtemel noktalar ve düzeltilmesi gereken hatalar.

---

## 2. Yöntemsel / içerik sorunları

### 2.1 (Kritik) Kontrol grubu yok — faz etkileri ortak zaman şoklarından ayrıştırılamıyor

Tasarım, 14 ülkenin tamamının aynı tarihlerde "işlem gördüğü" bir **önce–sonra (before–after)** karşılaştırması. Yıl sabit etkileri konulamıyor (faz kuklalarıyla çakışır — metin bunu doğru söylüyor, satır 351). Bu durumda faz kuklaları, AB ETS dışındaki **tüm ortak zaman şoklarını** da içine alır. Özellikle:

| Faz | Aynı dönemde yürürlükte olan / gerçekleşen |
|---|---|
| Faz 2 (2008–2012) | **Kyoto Protokolü birinci taahhüt dönemi (2008–2012) — birebir çakışıyor**; 2007 İklim-Enerji Paketi (20-20-20); 2009/28/AT Yenilenebilir Enerji Direktifi; 2008 petrol fiyatı zirvesi; finansal kriz |
| Faz 1 (2005–2007) | Kyoto'nun yürürlüğe girmesi (Şubat 2005); 2006/32/AT enerji verimliliği direktifi |
| Faz 3 (2013–2020) | Paris Anlaşması (2015); küresel düşük karbon patent gerilemesi (Probst ve diğ., 2021 — metinde anılıyor) |

Metin "fazlar ile inovasyon arasında ters nedensellik yoktur" diyor (satır 125) — bu doğru, ama asıl sorun ters nedensellik değil, **atlanan ortak zaman değişkenleri**. Satır 127'deki "yıl etkileri modeli ve plasebo testleri AB ETS'den kaynaklandığı yorumunu desteklemektedir" ifadesi fazla güçlü: yıl etkileri modeli *ne zaman* değiştiğini gösterir, *neden* değiştiğini ayırt etmez; plasebo testleri ise yalnızca ETS öncesi dönemde kendiliğinden kırılma olmadığını gösterir.

**Öneriler**
- 5.10'a (ya da ayrı bir **"5.11 Sınırlılıklar"** alt bölümüne) bu sınırlılığı açıkça yazın. Mevcut hâliyle bölümde hiç sınırlılık tartışması yok; jüri bunu mutlaka soracaktır.
- İddiayı yumuşatın: "AB ETS'nin etkisi" yerine, uygun yerlerde "AB ETS dönemiyle ilişkili etki / AB ETS'nin de içinde yer aldığı iklim politikası paketinin etkisi".
- Mümkünse ek bir sağlamlık testi: ülkeler arasında **ETS maruziyeti değişen** bir değişkenle etkileşim (örn. ETS kapsamındaki tesislerin ülke emisyonlarındaki payı, ya da ETS sektörlerinin katma değer payı). Bu, yıl sabit etkilerinin eklenmesine imkân verir ve ortak şokları temizler. Bel & Joseph (2018) benzer bir "stringency" ölçüsü kullanıyor.

### 2.2 (Kritik) Yatay kesit bağımlılığı bulunuyor ama çıkarsama bunu yok sayıyor

Tablo 5.9'da **CD testi yedi değişkenin tamamında yüzde 1'de reddediliyor** (CD istatistikleri 30–47). Buna rağmen standart hatalar yalnızca ülke düzeyinde kümeleniyor. Ülke kümelemesi ülke içi zaman korelasyonunu ele alır; **ülkeler arası (yatay) korelasyonu ele almaz**. Faz kuklaları zaman boyutunda değiştiği için asıl belirsizlik kaynağı yıl boyutundadır; etkin örneklem büyüklüğü 336 değil, 24 yıla yakındır.

**Öneriler**
- Ülke **ve** yıl düzeyinde iki yönlü kümeleme (Cameron, Gelbach & Miller, 2011) ya da Driscoll-Kraay tipi standart hatalarla ana tabloyu yeniden raporlayın (en azından Poisson QML için; Stata'da `ppmlhdfe ... , cluster(country year)`).
- Sonuçlar zayıflarsa bunu dürüstçe yazın; özellikle Faz 1 (NB p = 0,021; Poisson p = 0,044) bu durumda anlamlılığını yitirebilir.
- 5.6.7–5.6.8'de CD testi sonucu ile 5.6.5'teki çıkarsama tercihi arasındaki kopukluğu metinde açıklayın.

### 2.3 (Önemli) Bootstrap yönteminin seçimi ve gerekçesi uyumsuz

- 5.1.8'de **wild cluster bootstrap** (MacKinnon & Webb, 2017) anlatılıyor, fakat uygulanan **eşli (pairs) küme bootstrap-SE**. Cameron, Gelbach & Miller (2008) tam olarak şunu gösteriyor: az kümede **bootstrap-SE + normal kritik değer** aşırı red üretir; önerdikleri **wild cluster bootstrap-t** (ya da en azından percentile-t). Mevcut uygulama, kaynak gösterilen çalışmaların önerdiği yöntem değil.
- MacKinnon & Webb'in "farklı küme büyüklükleri" argümanı, **küme başına gözlem sayısındaki** farkla ilgilidir. Burada her ülkenin 24 gözlemi var; farklı olan patent sayısının büyüklüğü (Almanya %45). Bu bir kaldıraç (leverage) sorunudur; MacKinnon-Webb'e atıf bu hâliyle tam oturmuyor.
- 14 kümede eşli bootstrap'ta Almanya'nın örnekleme hiç girmediği (≈%35 olasılık) ya da 2–3 kez girdiği tekrarlar çoktur; bootstrap dağılımının bu yüzden iki modlu olup olmadığına bakılmalı.
- Yıl etkileri ve plasebo testlerinde asimptotik kümelenmiş SH kullanılmış (satır 407). 5.1.8'de "bu SH'ler az kümede güvenilmez" dendikten sonra aynı SH'lerin kullanılması çelişki. Gerekçe (örn. hesaplama yükü) yazılmalı ya da bootstrap burada da uygulanmalı.

**Öneri:** Ana tabloya wild cluster bootstrap-t p değerleri ekleyin (Stata: `boottest`, Roodman ve diğ., 2019 — Poisson için `boottest` çalışır; NB için en azından percentile-t raporlayın). Metinde yöntem adını uygulananla eşleştirin.

### 2.4 (Önemli) "ETS öncesi eğilim yok" bulgusu stok değişkenine koşullu

Şekil 5.1'de ham başvurular 1997–2004 arasında 1.707'den ~2.750'ye (%60) yükseliyor; Tablo 5.3'te ham yoğunluk da artıyor. Buna karşın Model 2'de ETS öncesi eğilim katsayısı sıfır (−0,007). Fark, **yeşil patent stokunun eğilimi mekanik olarak emmesinden** kaynaklanıyor (stok, geçmiş y'lerin birikimi). Dolayısıyla H5 ("fazların etkisi ETS öncesi eğilimden bağımsız") **stoklu modele koşullu** bir bulgu.

**Öneri:** Model 2'yi **stoksuz** da tahmin edip raporlayın (Tablo 5.14'teki (a) mantığıyla). Stoksuz ITS'de ETS öncesi eğilim anlamlı çıkarsa, H5'in yorumu "stok kontrol edildiğinde" diye sınırlanmalı. Bu test eksik olduğu sürece H5 jüride savunması zor bir hipotez.

### 2.5 (Önemli) Dinamik panel sorunu — tek paragrafla geçiştirilmiş

ln(1+K_{t−1}) bağımlı değişkenin gecikmelerinden türetilmiş; sabit etkilerle birlikte Nickell tipi sapma var. Metin "T = 24, sapma 1/T mertebesinde" diyor; bu savunulabilir ama literatürde standart çözüm mevcut: **Blundell, Griffith & Windmeijer (2002) "pre-sample mean" tahmincisi** ya da **Blundell, Griffith & Van Reenen (1999)** — patent sayımı + bilgi stoku literatürünün standart referansları. Bunlardan hiçbiri kaynakçada yok.

**Öneri:** En azından BGW (2002) atıfı ile tartışmayı güçlendirin; mümkünse 1990–1996 dönemini "pre-sample" olarak kullanan bir sağlamlık tahmini ekleyin (veri zaten 1990'dan itibaren var).

### 2.6 (Önemli) H1'in kanıtı ana model değil, sağlamlık modeli

Tablo 5.17'de H1 "toplam etki üç fazda pozitif ve anlamlı (NB: %43,8; %101,2; %88,8)" ile destekleniyor; bu değerler **stoksuz (a) modelinden**. Ana modelde Faz 3 anlamsız; stoksuz Poisson'da da Faz 3 anlamsız (0,2687). Yani H1 için kanıt **tek tahmincinin tek bir alternatif tanımına** dayanıyor; seçici görünüyor.

**Öneri:** H1 için doğrudan bir test raporlayın: tek bir "ETS" kuklasıyla (2005–2020 = 1) ana model; ya da H1'i "ilk iki fazda" diye yeniden ifade edin; ya da Tablo 5.17'de Poisson sonucunu da yazıp "kısmen desteklenmektedir" deyin.

### 2.7 (Orta) Referans dönemde beklenti (anticipation) etkisi

Direktif 2003/87/AT Ekim 2003'te kabul edildi; Yeşil Kitap 2000, Komisyon önerisi 2001. Referans dönemin son 2–4 yılı (2001–2004) ETS beklentisiyle kirlenmiş olabilir. Bu, faz etkilerini **aşağı yönlü** yanlı yapar (muhafazakâr); yani bulgular lehine bir argüman, ama yazılmalı. Plasebo kırılmaları (2000, 2001, 2002) bu noktayı kısmen kapsıyor; 2003 kırılması test edilmemiş (yalnızca 2 yıl kaldığı için anlaşılır).

### 2.8 (Orta) Örneklem tanımı eksik gerekçeli

Satır 193: yalnızca Birleşik Krallık'ın dışlanma nedeni yazılmış. 2004 ve sonrası üye olan 13 ülkenin neden dışarıda kaldığı (ETS öncesi dönemde AB üyesi olmamaları / referans dönemde ETS yasama sürecine taraf olmamaları / veri) açıkça yazılmalı. Örneklem fiilen **AB-15 eksi Birleşik Krallık**; bunu bir cümleyle söyleyin.

### 2.9 (Orta) Plasebo testlerinin gücü düşük

N = 112 gözlemle 13 ülke kuklası + eğilim + stok + 5 kontrol + 2 plasebo terimi ≈ 22 parametre. Reddetmeme, "kırılma yok" demek için zayıf kanıt. Metinde "ETS öncesi dönemde kırılma bulunmamaktadır" yerine "kırılma kanıtı bulunamamıştır" biçiminde ifade edin ve güç kısıtını belirtin.

### 2.10 (Orta) Sabit etkiler modeli ile Tablo 5.4 korelasyonları

Tablo 5.4 ham (pooled) Pearson korelasyonları; VIF ise doğru biçimde ülke-içi dönüştürülmüş veriyle hesaplanmış. Tutarlılık için korelasyonlar da ülke-içi (demeaned) verilerle raporlanmalı ya da notta ham olduğu belirtilmeli.

### 2.11 (Küçük) Diğer yöntemsel notlar

- **Kesirli sayımların yuvarlanması** (satır 149): Poisson QML tamsayı gerektirmez (Stata `poisson` kesirli y kabul eder); yalnızca `nbreg` için gereklidir. Bunu söyleyin; isterseniz yuvarlanmamış veriyle Poisson sağlamlık sonucu ekleyin.
- **Son yıllarda veri kesilmesi (truncation):** Öncelik tarihine göre 2018–2020 başvuruları, veri çekim tarihine göre eksik olabilir (yayın gecikmesi 18 ay + PATSTAT gecikmesi). OECD'nin bu konudaki uyarısına atıf yapıp 2020'nin tam sayılıp sayılmadığını belirtin.
- **Tablo 5.12** "Anlamsız" yerine Faz 3 için de aralığı yazın (örn. [−%18,0; %33,6]).
- **Tablo 5.13** kontrol değişkenlerinin güven aralıkları boş bırakılmış; tamamlayın ya da notta neden yazın.
- **Satır 373** ("Birinci ve ikinci faz katsayılarının stoksuz modelde de pozitif ve anlamlı olması…") bulgulara ileri atıf; 5.6'da değil 5.8.1'de olmalı (zaten orada tekrar ediyor).
- **Satır 407** "katsayılar adlandırılmış ifadeler olarak tanımlanarak" — Stata'ya özgü teknik ayrıntı; okuyucu için anlaşılmaz. Ya nedenini açıklayın (çoğaltılan kümeler için kukla sayısı tekrardan tekrara değiştiği için) ya da çıkarın.
- Kaynakçada **Wooldridge (1999)** var ama metinde kullanılmamış; 5.1.5'te FE Poisson'un dağılım varsayımına karşı sağlamlığı için en doğru atıf budur.
- Stata 19 için StataCorp (2025) kaynakça kaydı yok.

---

## 3. Sayısal tutarlılık kontrolü

Aşağıdaki değerler metindeki katsayılardan bağımsız olarak yeniden hesaplandı.

| Kontrol | Metin | Hesap | Sonuç |
|---|---|---|---|
| Yüzde etkiler, Tablo 5.12 (6 değer) | 14,3 / 31,1 / 3,9 / 8,0 / 21,6 / −8,8 | aynı | ✓ |
| BC aralıkların yüzdeye çevrimi (8 değer) | [6,0; 33,2] … [7,3; 33,9] | aynı | ✓ |
| Model 2 yüzde etkiler | 11,7 / 9,1 / 42,3 / 38,2 | aynı | ✓ |
| Yıllık sapmalar 2005–2008 | 4,4 / 16,7 / 30,3 / 42,3; faz boyunca %31–42 | 4,4 / 16,7 / 30,3 / 42,3; 2012'de 31,1 | ✓ |
| Sağlamlık (a) ve (c) yüzdeleri | 43,8 / 101,2 / 88,8; 17,9 / 36,7 | aynı | ✓ |
| Wald χ²(1) p değerleri | 0,037; 0,013; <0,001; <0,001 | aynı | ✓ |
| Ortak test χ²(2) p değerleri | 0,002; **0,001**; 0,000; 0,000; 0,694; 0,329 | 0,002; **0,000**; 0,000; 0,000; 0,694; 0,330 | Poisson Faz 1 ortak test p = 0,000 olmalı (15,39 için) |
| Plasebo χ²(2) p değerleri (6) | 0,333 … 0,767 | aynı | ✓ |
| Gözlem dağılımı | 112/42/70/112 = 336 | aynı | ✓ |
| Toplam başvuru 107.759 | 320,71 × 336 | 107.759 | ✓ |
| Tablo 5.3 ağırlıklı ortalama | — | 320,71 | ✓ |
| Varyans/ortalama ≈ 980 | — | 977 | ✓ |
| 1 + α·μ ≈ 6,7 | — | 6,71 | ✓ |
| Stok %10 → ≈%6 | — | %6,2 | ✓ |
| Ticaret 10 puan → −%4,8 | — | −4,8 | ✓ |
| 2009 yıl etkisi 0,308 → ≈%36 | — | %36,1 | ✓ |
| Tablo 5.15 sayımları (7 adet p<0,05; 13 adet p<0,10; Fransa hariç) | — | aynı | ✓ |
| Tablo 5.15 Almanya satırı = Tablo 5.14 (c) Poisson | 0,1323 / 0,2597 / 0,0359 | aynı | ✓ |

**Tablo 5.11'deki asimetrik güven aralıkları (veri setiyle doğrulandı — bkz. Kısım 6.3):**

- *Enerji ithalat bağımlılığı*, NB: katsayı 0,0022, SH 0,0026, BC aralığı [−0,0000; **0,0241**]. Üst sınır nokta tahminin 8 SH üstünde. İlk okumada yazım hatası sanmıştım; veriyle yaptığım bootstrap aynı biçimi veriyor ([0,0001; 0,0197]). Yani hata değil, **BC yönteminin bu veri setinde kararsız çalıştığının** işareti: bootstrap dağılımı çok çarpık (çarpıklık 1,5) ve medyan sapması büyük (z₀ ≈ 0,46). Aşağıda 6.3'te açıklanıyor.
- *Ticaret açıklığı*, NB: z = −1,96 (p = 0,050), BC aralığı üst sınırı tam −0,0000; yüzdelik aralık ise sıfırı içeriyor ([−0,0066; 0,0020]). "**" işareti savunulamaz; en fazla "*" ya da "sınırda". Aynı durum Model 2'de de var.
- *İmalat payı*, NB: [−0,0392; 0,0422] asimetrik aralık da aynı BC kararsızlığının ürünü (replikasyon: [−0,0389; 0,0444]).

---

## 4. Metin, biçim ve kaynakça hataları

### 4.1 Yapısal / biçim

| Yer | Sorun | Düzeltme |
|---|---|---|
| Satır 127 ("Birinci model, AB ETS'nin her bir fazda…" paragrafı) | Paragrafın tamamı **Başlık 2** stilinde; içindekiler tablosuna girer | Normal metin stiline alın |
| Satır 323 ve 783 | Boş Başlık 4 / Başlık 2 paragrafları | Silin |
| 5.8 "Sağlamlık Testleri" | Başlık stili yok (düz metin) | Başlık 2 yapın |
| Başlıklar genel | Bir kısmı kalın paragraf (5.1.1–5.1.5, 5.2, 5.4.2 …), bir kısmı gerçek başlık stili (5.1.6, 5.1.7, 5.3, 5.4 …) | Tümünü Word başlık stillerine çevirin (İçindekiler ve numaralandırma için şart) |
| Denklem numaraları | (1)–(13) numaralı, sonrakiler (bootstrap SH, z₀, BC aralığı, 5.6.2–5.6.6 denklemleri) numarasız | Tutarlı numaralandırın |
| Sarı vurgulu (highlight) metin | Satır 351, 363, 403'te kalmış | Son hâlde kaldırın |
| Satır 375 | "Tablo 5.5" → VIF tablosu **Tablo 5.6** | Düzelt |
| Şekil 5.1 başlığı | "(1990–2020)" doğru ama metin tahmin dönemi 1997–2020; Şekil 5.5 başlığında dönem yok | Tutarlı yazın |
| Tablo 5.1 "Kukla Değ." satırı | Kaynak sütunu boş, tanım kısa | "Yazar tanımı; Direktif 2003/87/AT" |
| Notasyon | **α** üç ayrı anlamda kullanılıyor: α_i ülke sabit etkisi (denk. 9–12), α aşırı yayılım parametresi (denk. 6–8, Tablo 5.11), α₁/α₂ BC yüzdelik düzeyleri | Sabit etki için η_i ya da c_i; BC için p₁/p₂ kullanın |
| Denklem (12) | Maruziyet terimi ln e_it yok; (9)'da var | Ekleyin ya da "maruziyet terimi ihmal edilmiştir" notu |
| Matematik yazımı | "lnE", "lnL", "lne_it", "exp" eğik/bitişik yazılmış (Word denklem editörü) | \ln, \exp dik; boşluklar |

### 4.2 Terim tutarlılığı

- "dış ticaret hacmi" (satır 173) ↔ "Dış ticaret açıklığı" (başlık, Tablo 5.1) ↔ "Ticaret açıklığı" (Tablo 5.2, 5.11). Tek terim seçin.
- "Enerji İthalat bağımlılığı" (büyük İ) ↔ "Enerji ithalat bağımlılığı". Tek yazım.
- "Olasılık değeri" ve "p" birlikte kullanılıyor; tabloların bazısında "p", bazısında "Olasılık". Tek biçim.
- Satır 193: "2020 tarihinde" → "2020 yılında" (31 Ocak 2020).
- Satır 153: "(OECD,2026)" — kaynakçadaki kayıt "OECD … 2024; accessed 1 March 2026". Yıl ve biçim uyuşmuyor.

### 4.3 Atıf yazım hataları (boşluk / & / and)

Satır 81 "Hausman ve diğ.(1984)", "(Allison&Waterman, 2002)"; satır 109 "(Efron&Tibshirani, 1993)"; satır 183 "sağlamaktadır(Bel ve Joseph,2018)"; satır 193 "(Dechezleprêtre ve diğ.,2011; … Haščič ve Migotto 2015)"; satır 331 "(Allison andWaterman, 2002)"; satır 335 "etkilemektedir(Bel&Joseph,2018)"; satır 525 "Pakes&Griliches(1984)", "Bel&Joseph(2018)". Tez yazım kılavuzuna göre tek biçim ("ve", boşluklar).

### 4.4 Kaynakça

- **Biçim dışı kayıtlar:** "OECD. Environment-Related Technologies Patents [Dataset]; OECD Data Explorer…" (MDPI biçimi, APA değil); "Dechezleprêtre, A., Glachant, M., … & Ménière, Y. (2011). \"Invention and Transfer…\"" (tırnak, &). APA/TÜ kılavuzuna çevirin.
- **Metinde atıf var, kaynakçada yok:** Cameron, Gelbach & Miller (2011) [iki yönlü kümeleme — eklerseniz]; StataCorp (2025); Blundell, Griffith & Windmeijer (2002) [önerilen].
- **Kaynakçada var, bu bölümde kullanılmamış ama kullanılmalı:** Wooldridge (1999).
- Satır 1005 OECD kaydı ile satır 1101 "OECD. (2026)" veri kaynağı kaydı aynı veri setini iki kez, farklı yıllarla listeliyor. Birleştirin.
- "Probst ve diğ. (2021)" ✓, "Calel (2020)" ✓, "Bernal ve diğ. (2017)" ✓, "Wagner ve diğ. (2002)" ✓ — metin-kaynakça eşleşmesi kontrol edildi, bunlar tamam.

---

## 6. Veri seti değerlendirmesi ve replikasyon (AB14_nihai_veri.xlsx)

Veri seti `veri/AB14_nihai_veri.xlsx` olarak repoya eklendi; tüm hesaplar `analiz/py/replikasyon.py` ile yeniden üretilebilir (çıktı: `analiz/py/replikasyon_cikti.txt`).

### 6.1 Veri setinin yapısı ve kalitesi

- 3 sayfa: `Veri` (14 ülke × 1990–2020 = 434 satır, 10 sütun), `Yesil_stok` (stok hesabı, formüller ve parametreler), `Kaynaklar` (değişken tanımları). Düzenli ve belgelenmiş; panel tam dengeli.
- **Eksik değerler yalnızca 1990–1995'te** (gdp_real, manuf, gdp_growth) — tahmin örneklemini (1997–2020) ve gecikmeleri etkilemiyor. Stok için gereken `ccm` 1990'dan itibaren eksiksiz.
- `ccm_frac` (kesirli) ve `ccm` (yuvarlanmış) birlikte tutulmuş — iyi uygulama. `Kaynaklar` sayfasında "0,5 yukarı yuvarlandı" yazıyor; metinde "en yakın tam sayıya" deniyor. 62 gözlemde tam .5 var; ikisi aynı şey değil, metinde "yarım değerler yukarı yuvarlanmıştır" diye netleştirin. Kesirli seriyle Poisson tahmini neredeyse aynı (F1 0,0774; F2 0,1955; F3 −0,0927) — bunu bir cümleyle belirtmek yuvarlama sorusunu kapatır.
- Tek sıfır gözlem: Portekiz 1990 (yalnızca stok başlangıcında kullanılıyor; K₁₉₉₀ = 0 oluyor, sorun değil).
- Stok hesabı: Excel'deki K değerleri ile Python'da sıfırdan hesaplanan değerler arasındaki en büyük fark 5×10⁻¹¹ — **stok doğru hesaplanmış**; g = 0,0691 ✓.
- Veri kaynağı tutarlılığı: Tablo 5.1 ile `Kaynaklar` sayfası birebir uyumlu (Eurostat nama_10_gdp, nrg_ind_id; WDI EG.FEC.RNEW.ZS, NV.IND.MANF.ZS, NE.TRD.GNFS.ZS).

### 6.2 Tezdeki tablo ve katsayıların yeniden üretimi

| Tez | Replikasyon | Sonuç |
|---|---|---|
| Tablo 5.2 (tüm ortalama/sapma/min/maks) | aynı (3 ondalık) | ✓ |
| Medyan 142,5; çarpıklık 3,1; toplam 107.759; Almanya %45, Fransa %18 | aynı | ✓ |
| Tablo 5.3 patent, yoğunluk, stok sütunları | aynı | ✓ |
| Tablo 5.3 kontrol sütunları | **eşzamanlı (t)** değerlerle eşleşiyor, gecikmeli değil | Tablo notu ekleyin: "kontrol değişkenleri eşzamanlı; modelde t−1" — Tablo 5.4 notu "tümü t−1" dediği için okuyucu karışır |
| Tablo 5.4 korelasyonlar | aynı | ✓ (ama bkz. 6.4) |
| Tablo 5.6 VIF (ülke-içi) | aynı (9 değer) | ✓ |
| Tablo 5.11 — Poisson ve NB **tüm katsayılar** | 4 ondalığa kadar aynı | ✓ |
| α = 0,0178; LR = 669,77 | aynı | ✓ |
| Tablo 5.13 — Model 2 tüm katsayılar, α = 0,0161, LR = 564,59 | aynı | ✓ |
| Tablo 5.14 (a), (b), (c) katsayıları; GSYİH esnekliği 0,393 / 0,371 | aynı | ✓ |
| Yıl etkileri (2006: 0,102; 2007: 0,156; 2008: 0,195; 2009: 0,308; stok 0,810) | aynı | ✓ |
| Bootstrap SH (Poisson): 0,0383 / 0,0651 / 0,1048 | 0,0375 / 0,0638 / 0,1043 | ✓ (farklı RNG) |
| Bootstrap SH (NB): 0,0580 / 0,0842 / 0,1264 | 0,0563 / 0,0853 / 0,1271 | ✓ |
| BC aralıkları Faz 1–2 (NB): [0,0578; 0,2864], [0,1188; 0,4441] | [0,0523; 0,2834], [0,1056; 0,4433] | ✓ |

**Sonuç: Stata'da üretilen tüm nokta tahminleri, testler ve bootstrap SH'ler bağımsız yazılımla doğrulandı. Hesaplama hatası yok.**

### 6.3 Bootstrap dağılımları hakkında bulgu (yeni)

Kümelenmiş eşli bootstrap'ta Almanya'nın hiç seçilmediği tekrar oranı (13/14)¹⁴ ≈ %35. Bu, bootstrap dağılımlarını çarpık ve yanlı yapıyor:

| Katsayı (Poisson) | Nokta tahmin | Bootstrap ortalaması | z₀ (medyan sapması) |
|---|---|---|---|
| Faz 1 | 0,0772 | 0,0971 | −0,49 |
| ln(1+K) | 0,6127 | 0,5618 | +0,55 |
| Enerji ithalat bağ. | 0,0029 | 0,0016 | +0,46 (çarpıklık 1,5) |

z₀ değerlerinin 0,5'e yaklaşması BC yüzdeliklerini aşırı kaydırıyor (ln(1+K) için üst yüzdelik %99,9'a çıkıyor). Efron & Tibshirani bu büyüklükte sapmada BCa ya da percentile-t önerir. Tezde BC aralıklarının kullanıldığı yerlerde bu kararsızlık belirtilmeli; ana çıkarsama aracı olarak BC yerine **percentile-t (bootstrap-t)** ya da aşağıdaki jackknife daha savunulabilir.

### 6.4 Çıkarsama yöntemine duyarlılık (yeni — raporun 2.2–2.3 maddelerinin sayısal karşılığı)

Model 1 faz katsayıları için farklı standart hata yöntemleri:

| | Faz 1 Poisson p | Faz 2 Poisson p | Faz 1 NB p | Faz 2 NB p |
|---|---|---|---|---|
| Asimptotik küme (ülke) | 0,000 | 0,000 | 0,016 | 0,001 |
| Eşli bootstrap-SE (tezdeki) | 0,040 | 0,002 | 0,017 | 0,002 |
| **İki yönlü küme (ülke & yıl)** | **0,084** | 0,004 | — | — |
| **Küme jackknife CV3, t(13)** (MacKinnon, Nielsen & Webb, 2023) | **0,228** | **0,068** | **0,041** | **0,022** |

Yorum:
- **Faz 2 bulgusu dayanıklı**: her yöntemde en az %10'da, çoğunda %1'de anlamlı; NB'de her yöntemde %5'te anlamlı.
- **Faz 1 bulgusu kırılgan**: yatay kesit bağımlılığını hesaba katan iki yönlü kümelemede %10'a, az-küme için önerilen CV3 jackknife'ta Poisson'da anlamsıza düşüyor. NB'de %5'te kalıyor. H2'nin "desteklenmektedir" yargısı "NB'de desteklenmekte, Poisson'da çıkarsama yöntemine duyarlı" biçiminde yumuşatılmalı.
- Wald δ₁=δ₂ testi NB'de asimptotik küme SH ile p = 0,052 (tezde bootstrap ile 0,037) — H3 de sınırda.
- Model 2'de yıl kümelemesi SH'leri ülke kümelemesinden küçük çıkıyor (S1: 0,009 vs 0,016); yani ITS bulguları (φ₁, λ₂) iki yönlü kümelemede de güçlü kalır.

### 6.5 Stoksuz Model 2 (tezde eksik; H5 için kritik)

| | Poisson | NB |
|---|---|---|
| ETS öncesi eğilim (t*) — **stoklu** | −0,0225 (p=0,10) | −0,0068 (p=0,61) |
| ETS öncesi eğilim (t*) — **stoksuz** | **+0,0354 (p<0,001)** | **+0,0486 (p<0,001)** |
| φ₁ (Faz 1 eğim) — stoksuz | 0,0694 (p=0,004) | 0,1175 (p=0,001) |
| λ₂ (Faz 2 düzey) — stoksuz | 0,2517 (p<0,001) | 0,3692 (p=0,001) |
| φ₃ (Faz 3 eğim) — stoksuz | **−0,0249 (p=0,002)** | −0,0192 (p=0,33) |

Yalnızca 1997–2004 alt örnekleminde de aynı: stoksuz eğilim 0,077 (p<0,001), stoklu 0,057 (p=0,03).

Sonuç: "ETS öncesinde anlamlı eğilim yok" (satır 645) ifadesi **yalnızca stok kontrol edildiğinde** doğru; ham/stoksuz tanımda yılda ≈%3,5–5 artış eğilimi var. İyi haber: Faz 1 eğim ve Faz 2 düzey etkileri stoksuz ITS'de de güçlü — yani bulgular eğilimin stok tarafından emilmesine bağlı değil. H5'i buna göre yeniden yazın ve bu tabloyu Tablo 5.14'e ekleyin. Stoksuz Poisson'da Faz 3 eğiminin **negatif ve anlamlı** olması tartışma bölümünde ele alınmalı (Probst ve diğ., 2021 ile uyumlu).

### 6.6 Tablo 5.4'ün yanıltıcılığı (yeni)

Tablo 5.4 ham korelasyonları veriyor (|r| ≤ 0,35). Model ülke-içi değişimden tahmin edildiğinden ilgili korelasyonlar **ülke-içi** olanlardır:

| | ln(1+K) | Yenilenebilir | Ticaret |
|---|---|---|---|
| ln(1+K) | 1 | **0,81** | **0,64** |
| İmalat | −0,53 | −0,42 | −0,12 |

"Ciddi çoklu doğrusallık sorunu yok" cümlesi ham korelasyonlara dayanıyor; ülke-içi veride stok–yenilenebilir korelasyonu 0,81. Bu, yenilenebilir enerji payının modelde neden anlamsız çıktığını da açıklıyor (stokla eş hareket). Tablo 5.4'ü ülke-içi değerlerle değiştirin ya da iki paneli birlikte verin; VIF tablosu zaten doğru yaklaşımı kullanıyor.

### 6.7 H1 için doğrudan test (yeni)

Tek ETS kuklasıyla (2005–2020 = 1) ana model: Poisson 0,248 (p<0,001), NB 0,255 (p<0,001); stoksuz Poisson 0,334. H1 bu şekilde ana modelle doğrudan desteklenebilir — Tablo 5.17'de (a) modeline başvurmaya gerek kalmaz.

---

## 7. Öncelikli yapılacaklar (özet)

1. **"Sınırlılıklar" alt bölümü** yazın: kontrol grubu yokluğu, ortak şoklar (özellikle Kyoto 2008–2012), yatay kesit bağımlılığı, 14 küme, beklenti etkisi, plasebo gücü.
2. **Çıkarsama duyarlılık tablosu** ekleyin (6.4'teki tablo hazır): iki yönlü kümeleme ve CV3 jackknife; Faz 1 / H2 yargısını yumuşatın. 5.1.8'deki wild-bootstrap anlatımını uygulananla eşleştirin; BC yerine percentile-t'yi değerlendirin (6.3).
3. **Stoksuz Model 2**'yi Tablo 5.14'e ekleyin (6.5'te hazır); H5'i "stok kontrol edildiğinde" diye sınırlayın.
4. **Tablo 5.4**'ü ülke-içi korelasyonlarla değiştirin (6.6); "çoklu doğrusallık yok" cümlesini düzeltin.
5. **H1** için tek ETS kuklalı modeli raporlayın (6.7); Tablo 5.17'yi buna göre güncelleyin.
6. Ticaret açıklığı anlamlılık işaretini (**→* / sınırda) düzeltin; Tablo 5.3'e "kontroller eşzamanlı" notu; "yarım değerler yukarı yuvarlandı" ifadesi; kesirli seriyle sonuçların değişmediği notu.
7. Poisson Faz 1 ortak test p değerini 0,000 yapın; Tablo 5.5→5.6; başlık stilleri, boş başlıklar, vurgulu metinler, atıf boşlukları, α notasyonu.
8. Örneklemin "AB-15 − Birleşik Krallık" olduğunu ve 2004 sonrası üyelerin neden dışlandığını yazın.
