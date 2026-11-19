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

**Şüpheli güven aralıkları (Tablo 5.11):**

- *Enerji ithalat bağımlılığı*, NB: katsayı 0,0022, SH 0,0026, BC aralığı [−0,0000; **0,0241**]. Üst sınır nokta tahminin **8,4 SH** üstünde; Poisson'da da [−0,0012; **0,0195**] üst sınır 5,2 SH üstünde. Bu aralıklar bootstrap SH ile bağdaşmıyor; büyük olasılıkla yazım hatası (0,0071 / 0,0095 gibi) ya da yanlış satırdan kopyalama. Stata çıktısıyla karşılaştırın.
- *Ticaret açıklığı*, NB: z = −1,96 (p = 0,050), BC aralığı üst sınırı tam −0,0000. Bu "**" (p<0,05) işareti sınırda; "*" olarak işaretlemek ya da metinde "sınırda anlamlı" demek daha dürüst olur. Aynı durum Model 2'de de var (−0,0051 / 0,0026).
- *İmalat payı*, NB: aralık [−0,0392; 0,0422], nokta tahminine göre çok asimetrik (−1,3 SH / +2,9 SH). BC aralıkları asimetrik olabilir ama kontrol edilmeli.

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

## 5. Öncelikli yapılacaklar (özet)

1. **"Sınırlılıklar" alt bölümü** yazın: kontrol grubu yokluğu, ortak şoklar (özellikle Kyoto 2008–2012), yatay kesit bağımlılığı, 14 küme, beklenti etkisi, plasebo gücü.
2. **İki yönlü kümeleme / Driscoll-Kraay** ile ana tabloyu yeniden raporlayın.
3. **Wild cluster bootstrap-t** (en azından Poisson için) ekleyin; 5.1.8'deki anlatımı uygulananla eşleştirin.
4. **Stoksuz Model 2** tahmin edip H5'i buna göre yeniden değerlendirin.
5. Tablo 5.11'deki **enerji ithalat bağımlılığı güven aralıklarını** Stata çıktısıyla karşılaştırıp düzeltin; ticaret açıklığı anlamlılık işaretini gözden geçirin.
6. Poisson Faz 1 ortak test p değerini 0,000 yapın; Tablo 5.5→5.6 düzeltin; başlık stilleri, boş başlıklar, vurgulu metinler, atıf boşlukları.
7. Örneklemin "AB-15 − Birleşik Krallık" olduğunu ve 2004 sonrası üyelerin neden dışlandığını yazın.
