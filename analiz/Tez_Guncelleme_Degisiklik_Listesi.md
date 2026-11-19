# Tez Güncellemesi: Değişiklik Listesi

**Güncellenen belge:** `dokumanlar/Nihai_Model_19112026_metin.md` (Beşinci Bölüm ve kaynakça) · **Güncel metin:** `dokumanlar/Nihai_Model_guncel_metin.md` · **Tarih:** 19.11.2026

> Tez metni, kapsamlı yeniden incelemedeki bulgulara ve önerilere göre güncellenmiştir. **Yalnızca bulgularda sorun olarak işaretlenen yerlere dokunulmuştur;** sorunsuz bulunan kısımlar aynen korunmuştur. Her değişiklik bir bulgu numarasına bağlıdır (`analiz/Kapsamli_Yeniden_Inceleme.md`, Kısım 5). Değişikliklerin metin içinde işaretli hâli sitededir (Güncellenmiş tez sayfası).

## Özet

- 135 değişiklik kaydı, metinde 208 nokta; 36 bulgunun 36'i için en az bir değişiklik uygulandı.
- Türlere göre: 71 değişiklik, 34 ekleme, 12 biçim, 8 tablo, 5 çıkarma, 4 kontrol, 1 şekil.
- “Kontrol” türündeki kayıtlarda metin **değiştirilmemiş**, yazarın kaynaktan ya da yazılım çıktısından doğrulaması gereken ifade işaretlenmiştir.

## Genel notlar

- Eklenen bütün yeni sayılar bu incelemede Python ile hesaplandı (ham veriden, tezin Stata sonuçlarını 164/164 yeniden üreten kodla). Teze girmeden önce Stata ile yeniden üretilmeleri önerilir; bootstrap standart hataları tekrar sayısına ve rastgele sayı üretecine göre üçüncü ondalıkta değişebilir.
- Yeni tablolar mevcut numaralandırmayı bozmamak için harf ekiyle adlandırıldı (5.4 Panel B, 5.5a, 5.6a, 5.6b, 5.11a, 5.13a, 5.14a). Son nüshada tablolar baştan numaralandırılmalı ve metin içi göndermeler güncellenmelidir.
- Yeni alt bölüm 5.11 (Çalışmanın Sınırlılıkları) eklendi; içindekiler tablosu güncellenmelidir.
- Şekil 5.5 Python ile yeniden çizildi; tezin diğer şekilleriyle aynı görsel biçime getirilmesi gerekebilir.
- Özgün Word dosyasına dokunulmadı. Güncel metnin Word sürümü düz metinden üretildi; üniversitenin tez biçimini taşımaz, değişikliklerin özgün dosyaya aktarılması gerekir.

## Uygulanmayan ya da yazara bırakılan öneriler

| Bulgu | Öneri | Neden uygulanmadı | Ne yapıldı |
|---|---|---|---|
| T1 | Ülkeler arasında farklılaşan bir ETS ölçüsüyle (kapsam payı, ulusal tahsis planı sıkılığı) karşılaştırmalı analiz; yeşil olmayan patentlerle plasebo tahmini | Yeni veri gerekir | Sınırlılıklar bölümünde (5.11) ileriki çalışma olarak yazıldı. |
| T4 | Ar-Ge harcamalarının GSYİH'ye oranının kontrol değişkeni olarak eklenmesi | Yeni veri gerekir | Metinde Ar-Ge'nin modelde ayrıca yer almadığı belirtildi. |
| T8 | Birleşik Krallık'ın eklendiği 15 ülkeli sağlamlık tahmini; gerçek dışlama gerekçesi | Yeni veri / yazar bilgisi gerekir | Yanlış gerekçe çıkarıldı, durum sınırlılık olarak yazıldı. |
| T11 | Yıllık izin (EUA) fiyatıyla sağlamlık tahmini | Yeni veri gerekir | Tartışmaya karbon fiyatı paragrafı eklendi. |
| Y4 | Pakes ve Griliches (1984) “1,6 yıl” ve Bel ve Joseph (2018) kapsam / tahminci aktarımları | Kaynaktan doğrulanmalı | Metin değiştirilmedi; üç cümle “yazar kontrolü” olarak işaretlendi. |
| M4 | Pedroni istatistiğinin (+2,255) test yönü | Yazılım çıktısından doğrulanmalı | Metin değiştirilmedi; ifade “yazar kontrolü” olarak işaretlendi. |
| M4 | Birim kök ve eşbütünleşme bölümünün kısaltılıp tabloların eke taşınması; Westerlund (2007) testi | Yazarın kararı | Uygulanmadı; yalnızca etiket, dönem ve aşırı genelleme düzeltildi. |
| C4 | Tablo 5.13'te kontrol değişkenlerinin boş bırakılan güven aralığı hücreleri | Stata çıktısından doldurulmalı | Tablo notuna hatırlatma eklendi. |
| Y2 | H1–H4 hipotez cümlelerinin betimleyici fiillerle yeniden yazılması; H1'in “ilk iki faz” ile daraltılması | Yazarın kararı | Hipotez cümleleri değiştirilmedi (H5 hariç); değerlendirme tablosu (5.17) güncellendi. |
| C3 | Ülke bazında faz farklarını gösteren ek tablo | İsteğe bağlı | Uygulanmadı; ülke ağırlıkları tablosu (5.5a) eklendi. |
| B1 | Word biçim işlemleri: alt başlıkların başlık stillerine çevrilmesi, tablolardaki denklem nesnesi alt indislerin düz metne çevrilmesi | Yalnızca Word dosyasında yapılabilir | Metinde yapılabilenler uygulandı: denklem numaraları, simgeler, boş başlıklar, vurgular, değişken adları. |
| T3 | Tez özeti ve genel sonuç bölümündeki yüzde 44 / 101 / 89 rakamları | Bu dosyada yok (5. bölüm dışı) | Aynı düzeltme özet ve sonuç bölümlerinde de yapılmalı. |

## Değişiklikler (metindeki sırayla)

### D004 · Bölüm 5.1.1 · Y6 · değişiklik

**Gerekçe.** Sayım değişkeni sıfır da alabilir; “yalnızca pozitif” yerine “negatif olmayan”.

**Önceki metin.** Bağımlı değişkenin yalnızca pozitif değerler alabildiği durumlarda

**Yeni metin.** Bağımlı değişkenin negatif olmayan değerler aldığı durumlarda

### D005 · Bölüm 5.1.4 · Y6 · değişiklik

**Gerekçe.** Kullanılan biçim adlandırıldı (NB2).

**Önceki metin.** En yaygın biçimi olan negatif binom modelinde olasılık fonksiyonu

**Yeni metin.** En yaygın biçimi olan ve NB2 olarak adlandırılan negatif binom modelinde olasılık fonksiyonu

### D006 · Bölüm 5.1.4 · Y6 · değişiklik

**Gerekçe.** Etkinlik üstünlüğü koşula bağlandı.

**Önceki metin.** Aşırı yayılım bulunduğunda negatif binom modeli Poisson tahmincisine göre daha etkin tahminler üretmektedir.

**Yeni metin.** Aşırı yayılım bulunduğunda ve varyans fonksiyonu doğru tanımlandığında negatif binom modeli Poisson tahmincisine göre daha etkin tahminler üretmektedir.

### D001 · Bölüm 5.1.5 · B1 · biçim

**Gerekçe.** Ülke sabit etkisinin simgesi α yerine c yapıldı; α yalnızca aşırı yayılım parametresi için kullanılıyor (aynı simgenin üç ayrı anlamı vardı).

**Önceki metin.** [denklem]

**Yeni metin.** [denklem]

### D007 · Bölüm 5.1.5 · M5 · değişiklik

**Gerekçe.** Asıl kaynak (Wooldridge, 1999) kaynakçada vardı ama metinde atıf yoktu.

**Önceki metin.** Sabit etkili Poisson tahmincisi ayrıca dağılım varsayımına karşı sağlamdır (Cameron ve Trivedi, 2013).

**Yeni metin.** Sabit etkili Poisson tahmincisi ayrıca dağılım varsayımına karşı sağlamdır (Wooldridge, 1999; Cameron ve Trivedi, 2013).

### D003 · Bölüm 5.1.5 · B2 · biçim

**Gerekçe.** Metin içi atıflarda “&” ve “and” yerine “ve”; eksik boşluk ve virgüller düzeltildi.

**Önceki metin.** Hausman ve diğ.(1984)

**Yeni metin.** Hausman ve diğ. (1984)

### D008 · Bölüm 5.1.8 · C2 · değişiklik

**Gerekçe.** Anlatılan yöntem (wild bootstrap) ile uygulanan yöntem (eşli bootstrap) arasındaki kopukluk giderildi; kaynak yalnızca gerçekten söylediği şey için kullanıldı; yöntemin sınırı yazıldı.

**Önceki metin.** MacKinnon ve Webb (2017), wild kümelenmiş bootstrap yöntemini inceledikleri çalışmada, küme büyüklüklerinin birbirinden çok farklı olduğu durumlarda asimptotik kümelenmiş standart hataların daha da güvenilmez hâle geldiğini göstermiştir. Bu durumlarda çıkarsama, kümelenmiş eşli bootstrap ile yapılmaktadır.

**Yeni metin.** MacKinnon ve Webb (2017), kümelerin birbirinden çok farklı olduğu durumlarda asimptotik kümelenmiş standart hataların daha da güvenilmez hâle geldiğini göstermiştir. Bu çalışmalar az sayıda küme için wild kümelenmiş bootstrap yöntemini önermektedir; ancak bu yöntem esas olarak doğrusal modeller için geliştirilmiştir. Bu çalışmada, doğrusal olmayan sayım modellerine doğrudan uygulanabildiği için kümelenmiş eşli bootstrap kullanılmıştır. Küme sayısı az ve kümelerin tahmindeki ağırlıkları dengesiz olduğunda eşli bootstrap standart hataları da iyimser olabilmektedir; bu nedenle bulgular küme jackknife yöntemiyle ayrıca sınanmıştır.

### D002 · Bölüm 5.1.8 · B1 · biçim

**Gerekçe.** Numarasız denklemler numaralandı: (13)'ten sonraki denklemler (14)–(23).

**Yeni metin.** (14)

### D009 · Bölüm 5.1.8 · C4 · ekleme

**Gerekçe.** Sapma düzeltmeli (BC) aralığın sınırı yazıldı.

**Yeni metin.** Sapma düzeltmeli aralık, bootstrap dağılımının nokta tahmini etrafında yaklaşık simetrik olduğu durumlar için uygundur. Bootstrap dağılımı nokta tahminine göre belirgin biçimde kaymışsa [denklem] büyümekte ve aralık kararsızlaşmaktadır; bu nedenle sapma düzeltmeli aralıkların yanında yüzdelik aralıklar da raporlanmıştır.

### D010 · Bölüm 5.1.8 · C2, C5, C9 · ekleme

**Gerekçe.** İkinci çıkarsama yöntemi olarak küme jackknife tanıtıldı.

**Yeni metin.** Küme jackknife yönteminde model, her seferinde bir küme dışarıda bırakılarak [denklem] kez yeniden tahmin edilmekte ve varyans [denklem] (17) biçiminde hesaplanmaktadır. Burada [denklem], [denklem] kümesi dışarıda bırakıldığında elde edilen tahmini, [denklem] ise bu tahminlerin ortalamasını göstermektedir. Test istatistiği [denklem] serbestlik dereceli [denklem] dağılımıyla değerlendirilmektedir. Az sayıda ve dengesiz kümelerde bu yöntem, kümelenmiş ve bootstrap standart hatalarına göre daha temkinli sonuç vermektedir (MacKinnon, Nielsen ve Webb, 2023).

### D011 · Bölüm 5.2 · T9 · ekleme

**Gerekçe.** Referans dönemin seçimi gerekçelendirildi; Direktif'in 2003'te kabul edildiği belirtildi.

**Yeni metin.** Referans dönem, sistemin fiilen başladığı 2005 yılından önceki bütün tahmin yıllarını kapsamaktadır. 2003/87/AT sayılı Direktif Ekim 2003’te kabul edildiğinden 2003–2004 yıllarında beklenti etkileri oluşmuş olabilir; bu nedenle referans dönemin 1997–2002 ile sınırlandırıldığı tahmin sağlamlık testi olarak sunulmuştur (Bölüm 5.8.1).

### D012 · Bölüm 5.2 · T10 · değişiklik

**Gerekçe.** İlk iki fazda tahsislerin ulusal planlarla belirlendiği eklendi; dışsallık savı faz takvimiyle sınırlandı.

**Önceki metin.** Fazların başlangıç ve bitiş tarihleri ile kuralları, AB düzeyindeki yasama süreçlerinde, ülkelerin inovasyon faaliyetinden bağımsız olarak belirlenmiştir. Dolayısıyla, fazlar ile inovasyon arasında ters nedensellik ilişkisi bulunmamaktadır.

**Yeni metin.** Fazların başlangıç ve bitiş tarihleri, AB düzeyindeki yasama süreçlerinde, ülkelerin inovasyon faaliyetinden bağımsız olarak belirlenmiştir; ilk iki fazda tahsis miktarları ise üye devletlerin Komisyon onayına sunduğu Ulusal Tahsis Planlarıyla saptanmıştır. Dolayısıyla, faz takvimi ile inovasyon arasında ters nedensellik ilişkisi bulunmamaktadır.

### D013 · Bölüm 5.2 · B1 · biçim

**Gerekçe.** 5.2'nin son paragrafı yanlışlıkla başlık stilindeydi; normal paragrafa çevrildi (içindekiler tablosunda görünmemesi için).

**Önceki metin.** (Başlık 2 stili)

**Yeni metin.** (Normal paragraf)

### D014 · Bölüm 5.2 · T1 · değişiklik

**Gerekçe.** Nedensellik iddiası tasarımın taşıyabileceği düzeye indirildi; karşılaştırma grubu bulunmadığı açıkça yazıldı.

**Önceki metin.** Tahmin edilen etkilerin AB ETS’den kaynaklandığı yorumu; yıl etkileri modeli ve ETS öncesi döneme yerleştirilen plasebo kırılma testleriyle desteklenmektedir.

**Yeni metin.** Tahmin edilen farkların zamanlaması, yıl etkileri modeli ve ETS öncesi döneme yerleştirilen plasebo kırılma testleriyle incelenmektedir. Örneklemdeki bütün ülkeler AB ETS’ye aynı tarihte dâhil olduğundan tasarım bir önce–sonra karşılaştırmasıdır; tahmin edilen faz farkları aynı dönemde gerçekleşen diğer ortak gelişmelerin etkisini de içerebilir. Bu nedenle bulgular nedensel etki olarak değil, AB ETS fazlarıyla ilişkili farklar olarak yorumlanmaktadır (Bölüm 5.11).

### D015 · Bölüm 5.3 · T2, Y2 · değişiklik

**Gerekçe.** H5 yeniden yazıldı: “eğilimden bağımsız” iddiası stokun modelde olmasına bağlıydı; yeni ifade verinin desteklediği kadarını söylüyor.

**Önceki metin.** Fazların etkisi, ETS öncesi eğilimden bağımsız olarak ortaya çıkmaktadır.

**Yeni metin.** Birinci fazdaki hızlanma ve ikinci fazın başındaki düzey artışı, ETS öncesi eğilim hesaba katıldığında da ortaya çıkmaktadır.

### D016 · Bölüm 5.4.1 · M6 · değişiklik

**Gerekçe.** Yuvarlama kuralı veri dosyasıyla tutarlı hâle getirildi; sonuçların değişmediği belirtildi.

**Önceki metin.** en yakın tam sayıya yuvarlanmıştır.

**Yeni metin.** en yakın tam sayıya, yarım değerler yukarı yuvarlanmıştır. Yuvarlanmamış değerlerle yapılan Poisson tahmininde faz katsayıları üçüncü ondalıkta aynıdır (0,0774 ve 0,1955).

### D017 · Bölüm 5.4.1 · Y5 · ekleme

**Gerekçe.** “Yeşil inovasyon”un işlemsel tanımı ve patent göstergesinin sınırları eklendi.

**Yeni metin.** Bu çalışmada yeşil inovasyon, Avrupa Patent Ofisine yapılan iklim değişikliği azaltım teknolojisi patent başvurularıyla ölçülmektedir. Patent başvuruları buluş faaliyetinin göstergesidir; buluşların niteliğini, yayılmasını ve çevresel etkisini doğrudan ölçmez. Bu nedenle bulgular yeşil patentleme faaliyetine ilişkindir. Ayrıca en son yıllara ait başvuru sayıları, verinin derlendiği tarihe bağlı olarak eksik olabilmektedir; 2018–2020 yılları dışarıda bırakıldığında bulgular zayıflamamaktadır (Bölüm 5.8.1).

### D018 · Bölüm 5.4.1 · M8 · ekleme

**Gerekçe.** İkinci jürinin sıfır-kesikli model sorusuna hazır cevap.

**Yeni metin.** Sıfır değer gözlenebilir olduğundan (tahmin dönemi öncesinde Portekiz için 1990 yılında sıfır başvuru vardır) sıfır-kesikli bir model gerekmemektedir; sıfır-kesikli negatif binom tahmininde katsayılar yalnızca dördüncü ondalıkta değişmektedir (birinci faz 0,1342; ikinci faz 0,2709).

### D019 · Bölüm 5.4.2 · Y6 · değişiklik

**Gerekçe.** Sıralama yalnızca ETS dönemi için doğruydu.

**Önceki metin.** En yüksek yoğunluk Danimarka, Almanya, Finlandiya ve İsveç’te, en düşük yoğunluk ise Yunanistan, Portekiz ve İspanya’da gözlemlenmektedir.

**Yeni metin.** ETS döneminde en yüksek yoğunluk Danimarka, Almanya, Finlandiya ve İsveç’te, en düşük yoğunluk ise Yunanistan, Portekiz ve İspanya’da gözlemlenmektedir; ETS öncesi dönemde en yüksek ortalama yoğunluk Lüksemburg’a aittir (0,52).

### D020 · Bölüm 5.4.4 · Y6, B1 · değişiklik

**Gerekçe.** Tablo 5.5 ile tutarlı sayım (stok + beş kontrol) ve tek değişken adı.

**Önceki metin.** Modelde altı kontrol değişkeni olarak; yeşil patent stoku, GSYİH büyüme oranı, yenilenebilir enerji payı, enerji ithalat bağımlılığı, imalat sanayi payı ve dış ticaret hacmi yer almaktadır.

**Yeni metin.** Modelde yeşil patent stoku ile beş kontrol değişkeni (GSYİH büyüme oranı, yenilenebilir enerji payı, enerji ithalat bağımlılığı, imalat sanayi payı ve dış ticaret açıklığı) yer almaktadır.

### D021 · Bölüm 5.4.4 · Y6 · değişiklik

**Gerekçe.** Eskime oranı için metin içi atıf eklendi (üçü de kaynakçada var).

**Önceki metin.** δ = 0,15 yıllık eskime oranını göstermektedir.

**Yeni metin.** δ = 0,15 yıllık eskime oranını göstermektedir (Hall ve Mairesse, 1995; Popp, 2002; Noailly ve Smeets, 2015).

### D022 · Bölüm 5.4.4 · Y6 · değişiklik

**Gerekçe.** 0,0691 aritmetik değil logaritmik ortalama büyümedir.

**Önceki metin.** ortalama yıllık büyüme oranıdır (0,0691)

**Yeni metin.** ortalama yıllık logaritmik büyümesidir (0,0691)

### D023 · Bölüm 5.4.4 · T4 · değişiklik

**Gerekçe.** Stok bir girdi değil çıktı ölçüsüdür; Ar-Ge'nin “kontrol edildiği” iddiası yumuşatıldı.

**Önceki metin.** Yeşil patent stoku, inovasyon girdilerinin yeşil teknolojiler alanındaki birikmiş çıktısını doğrudan ölçtüğünden, ülkelerin Ar-Ge kapasitesindeki farklılıklar da bu değişken tarafından kontrol edilmektedir.

**Yeni metin.** Yeşil patent stoku birikmiş patent çıktısını ölçmekte ve ülkelerin Ar-Ge kapasitesinin dolaylı bir göstergesi olarak kullanılmaktadır; Ar-Ge harcamaları modelde ayrıca yer almamaktadır.

### D024 · Bölüm 5.5 · T8 · değişiklik

**Gerekçe.** Yanlış gerekçe çıkarıldı (Birleşik Krallık 31.12.2020'ye kadar AB ETS içindeydi); örneklem ölçütü yazıldı. YAZAR: gerçek dışlama gerekçesi eklenmeli ya da 15 ülkeyle sağlamlık tahmini yapılmalı.

**Önceki metin.** Birleşik Krallık 2020 tarihinde AB üyeliğinden çıktığı için analize dahil edilmemiştir.

**Yeni metin.** Örneklem, ETS öncesi referans dönemin tamamında AB üyesi olan on beş ülkeden on dördünü kapsamaktadır. Birleşik Krallık 2020 sonuna kadar AB ETS kapsamında kalmış olmakla birlikte ana örnekleme alınmamıştır; bu durum çalışmanın bir sınırlılığıdır (Bölüm 5.11).

### D025 · Bölüm 5.5 · Y6 · değişiklik

**Gerekçe.** Tahmin döneminin neden 1997'de başladığı açık yazıldı.

**Önceki metin.** İlgili ülkelere ait kontrol değişkenleri bir dönem gecikmeli olarak modele girdiğinden, veriler 1996 yılından itibaren veri tabanlarından eksiksiz temin edilebilmiştir.

**Yeni metin.** Reel GSYİH serisi 1995’ten, GSYİH büyüme oranı 1996’dan itibaren bütün ülkeler için mevcuttur; kontrol değişkenleri bir dönem gecikmeli olarak modele girdiğinden tahmin döneminin ilk yılı 1997’dir.

### D057 · Bölüm 5.5 · B1 · biçim

**Gerekçe.** Değişken adının yazımı tekleştirildi (6 yer)

**Önceki metin.** Enerji İthalat bağımlılığı

**Yeni metin.** Enerji ithalat bağımlılığı

### D058 · Bölüm 5.5 · B1 · biçim

**Gerekçe.** Değişken adının yazımı tekleştirildi (2 yer)

**Önceki metin.** Dış Ticaret Açıklığı

**Yeni metin.** Dış ticaret açıklığı

### D059 · Bölüm 5.5.1 · B1 · biçim

**Gerekçe.** Aynı değişken için tek ad: “dış ticaret açıklığı” (9 yer)

**Önceki metin.** Ticaret açıklığ

**Yeni metin.** Dış ticaret açıklığ

### D060 · Bölüm 5.5.1 · B1 · biçim

**Gerekçe.** Aynı değişken için tek ad: “dış ticaret açıklığı” (4 yer)

**Önceki metin.** ticaret açıklığ

**Yeni metin.** dış ticaret açıklığ

### D026 · Bölüm 5.5.1 · Y6 · ekleme

**Gerekçe.** Tablo 5.3'ün cari dönem değerleri verdiği notla belirtildi (Tablo 5.2 gecikmeli değerleri veriyor).

**Yeni metin.** Not: Kontrol değişkenleri ve yeşil patent stoku cari dönem ([denklem]) değerleriyle verilmiştir; modelde bir dönem gecikmeli olarak yer almaktadır.

### D027 · Bölüm 5.5.1 · M3 · değişiklik

**Gerekçe.** Havuzlanmış korelasyonlar sabit etkili model için yanıltıcıydı; ülke içi korelasyonlar eklendi.

**Önceki metin.** Değişkenler arasındaki korelasyonların mutlak değeri 0,35’i aşmamaktadır. Bu sonuç, kontrol değişkenleri arasında ciddi bir çoklu doğrusallık sorunu bulunmadığını göstermektedir.

**Yeni metin.** Havuzlanmış korelasyonların mutlak değeri en fazla 0,35 düzeyindedir (Panel A). Ancak sabit etkili modelde katsayılar ülke içi değişimden tahmin edildiğinden belirleyici olan, değişkenlerin ülke ortalamalarından arındırılmış değerleri arasındaki korelasyonlardır (Panel B). Ülke içi korelasyonlar daha yüksektir: yeşil patent stoku ile yenilenebilir enerji payı arasında 0,81, dış ticaret açıklığı ile 0,64. Bu nedenle söz konusu kontrol değişkenlerinin katsayıları stokun etkisinden tam olarak ayrıştırılamamaktadır.

### D028 · Bölüm 5.5.1 · M3 · ekleme

**Gerekçe.** Tablo 5.4 iki panelli yapıldı.

**Yeni metin.** (Panel A: havuzlanmış)

### D029 · Bölüm 5.5.1 · M3 · ekleme

**Gerekçe.** Tablo 5.4'e Panel B (ülke içi korelasyonlar) eklendi.

**Yeni metin.** Tablo 5.4 (devam). Panel B: Ülke İçi (Ülke Ortalamalarından Arındırılmış) Korelasyon Katsayıları [denklem] Büyüme Yenilenebilir İthalat bağ. İmalat Ticaret [denklem] 1,00 Büyüme −0,29 1,00 Yenilenebilir 0,81 −0,16 1,00 İthalat bağ. 0,03 0,05 0,08 1,00 İmalat −0,53 0,48 −0,42 0,01 1,00 Ticaret 0,64 −0,02 0,55 −0,02 −0,12 1,00 Not: Değişkenlerin ülke ortalamalarından farkları arasındaki Pearson korelasyon katsayılarıdır. Tüm değişkenler bir dönem gecikmelidir (t − 1).

### D030 · Bölüm 5.6 · B1 · biçim

**Gerekçe.** İki boş başlık paragrafı silindi (Tablo 5.5'ten sonra ve 5.10'dan önce).

**Önceki metin.** (boş başlık)

**Yeni metin.** (silindi)

### D031 · Bölüm 5.6.1 · M5 · ekleme

**Gerekçe.** Kaynağın (Allison ve Waterman, 2002) standart hatalara ilişkin uyarısı eklendi.

**Yeni metin.** Aynı çalışma, bu tahmincinin standart hatalarının olduğundan küçük tahmin edilebildiğini de göstermektedir; bu nedenle çıkarsama asimptotik standart hatalarla değil bootstrap ile yapılmıştır.

### D032 · Bölüm 5.6.1 · M7, C3 · değişiklik

**Gerekçe.** Poisson “alternatif” değil eş düzeyde ikinci tahminci; negatif binomun tercih gerekçesi ağırlıklandırmaya dayandırıldı.

**Önceki metin.** alternatif tahminci olarak ise sabit etkili Poisson sözde en çok olabilirlik tahmincisi kullanılmıştır. Negatif binom modeli aşırı yayılımı açıkça modelleyerek etkinlik sağlamakta, Poisson sözde en çok olabilirlik tahmincisi ise dağılım varsayımına karşı tutarlılık güvencesi vermektedir.

**Yeni metin.** eş düzeyde ikinci tahminci olarak ise sabit etkili Poisson sözde en çok olabilirlik tahmincisi kullanılmıştır. Negatif binom modeli aşırı yayılımı açıkça modellemekte ve ülkelere daha dengeli ağırlık vermekte, Poisson sözde en çok olabilirlik tahmincisi ise dağılım varsayımına karşı tutarlılık güvencesi vermektedir.

### D033 · Bölüm 5.6.1 · C3 · ekleme

**Gerekçe.** İki tahmincinin neden farklı sonuç verdiği açıklandı; ülke ağırlıkları tablosu eklendi.

**Yeni metin.** İki tahminci ülkeleri farklı biçimde ağırlıklandırmaktadır. Poisson tahmincisi gözlemleri beklenen başvuru sayısıyla ağırlıklandırdığından Almanya’nın tahmindeki payı yaklaşık yüzde 45’tir; negatif binom tahmincisinde bu pay yaklaşık yüzde 11’dir (Tablo 5.5a). Dolayısıyla Poisson katsayıları başvuru ağırlıklı, negatif binom katsayıları ülkelere daha eşit ağırlık veren ortalama farkları göstermektedir; iki tahminci arasındaki farklar büyük ölçüde bu ağırlıklandırmadan kaynaklanmaktadır. Tablo 5.5a. Ülkelerin Tahmindeki Ağırlık Payları (Birinci Model) Ülke Poisson ağırlığı (%) Negatif binom ağırlığı (%) Almanya 45,3 11,3 Fransa 17,8 10,7 Hollanda 6,6 9,5 İtalya 5,9 9,4 İsveç 5,4 9,0 Danimarka 5,4 8,7 Avusturya 3,3 8,1 Finlandiya 3,0 7,7 İspanya 2,9 7,4 Belçika 2,6 7,4 İrlanda 0,8 4,2 Lüksemb…

### D034 · Bölüm 5.6.2 · M1 · ekleme

**Gerekçe.** Maruziyet kısıtının bir tercih olduğu ve veriyle reddedildiği yöntem bölümünde de belirtildi.

**Yeni metin.** Reel GSYİH’nin maruziyet değişkeni olarak kullanılması, bağımlı büyüklüğü yeşil patent yoğunluğu olarak tanımlayan bir tercihtir. GSYİH esnekliği serbest bırakıldığında birim esneklik kısıtı reddedilmektedir (esneklik negatif binom modelinde 0,393, Poisson modelinde 0,371; Bölüm 5.8.1). Bu nedenle sonuçlar her iki tanımla birlikte sunulmuştur; faz farklarının işareti iki tanımda aynıdır; birinci ve ikinci faz farkları serbest esneklik tanımında da anlamlıdır.

### D035 · Bölüm 5.6.3 · T1, B1 · değişiklik

**Gerekçe.** “Kontrol edilmektedir” iddiası “kısmen” olarak düzeltildi; sarı vurgu kaldırıldı.

**Önceki metin.** Ortak zaman değişimi, yeşil patent stoku ve zamanla değişen kontrol değişkenleri aracılığıyla kontrol edilmektedir.

**Yeni metin.** Ortak zaman değişimi, yeşil patent stoku ve zamanla değişen kontrol değişkenleri aracılığıyla kısmen kontrol edilmektedir; yıl sabit etkileri kullanılamadığından bütün ülkeleri aynı anda etkileyen ortak şoklar faz katsayılarından tümüyle ayrıştırılamamaktadır.

### D036 · Bölüm 5.6.4 · B1 · biçim

**Gerekçe.** Kalan sarı vurgular kaldırıldı.

**Önceki metin.** (sarı vurgulu)

**Yeni metin.** (vurgusuz)

### D037 · Bölüm 5.6.4 · T4 · değişiklik

**Gerekçe.** “Doğrudan etki / toplam etki” yerine “stok sabitken / stok hesaba katılmadan gözlenen fark”; aracılık yorumu yumuşatıldı.

**Önceki metin.** Bu nedenle stok, emisyon ticaret sisteminin zaman içindeki etkisinin aktarıldığı bir aracı değişken niteliği taşımaktadır. Stoklu modelde faz katsayıları, yeşil patent stoku sabitken ilgili fazın yeşil patent yoğunluğu üzerindeki doğrudan etkisini ölçmektedir. Stok katsayısı ise önceki dönemlerde oluşan patentlerin sonraki yıllara taşınan etkisini göstermektedir. Stoksuz model ise politikanın stok kanalı dahil toplam etkisini ölçmektedir.

**Yeni metin.** Bu nedenle stok, emisyon ticaret sisteminin zaman içindeki etkisinin aktarılabileceği bir kanal niteliği taşımaktadır; ancak stok AB ETS’den bağımsız nedenlerle de büyümektedir. Stoklu modelde faz katsayıları, yeşil patent stoku sabitken ilgili fazdaki yeşil patent yoğunluğunun ETS öncesine göre farkını ölçmektedir (stok sabitken gözlenen fark). Stok katsayısı ise önceki dönemlerde biriken patentler ile cari başvurular arasındaki ilişkiyi göstermektedir. Stoksuz model, stok hesaba katılmadan gözlenen farkı vermektedir; bu fark ETS öncesinde başlayan artış eğilimini de içerdiğinden AB ETS’nin toplam etkisi olarak yorumlanmamaktadır.

### D038 · Bölüm 5.6.4 · T5 · değişiklik

**Gerekçe.** “Sapma ihmal edilebilir” savı sınanmamıştı; benzetim sonucu yazıldı, birinci modelin katsayıları üst sınır olarak nitelendi.

**Önceki metin.** Bu çalışmada her ülke için 24 yıllık gözlem bulunmaktadır. Ayrıca stok, yalnızca bir önceki yılın patentlerinden değil, 1990’dan itibaren biriken ve her yıl yüzde 15 aşınan bir toplamdan oluştuğundan, tek bir gecikmeli bağımlı değişkene göre hata terimiyle ilişkisi çok daha zayıftır.

**Yeni metin.** Bu çalışmada her ülke için 24 yıllık gözlem bulunmaktadır. Bununla birlikte stok, bağımlı değişkenin geçmiş değerlerinden türetildiğinden kesin dışsallık varsayımı sağlanmamaktadır. Sapmanın büyüklüğü benzetimle sınanmıştır: faz etkilerinin sıfır olduğu ve verinin tahmin edilen modele göre üretildiği (stok her tekrarda üretilen başvurulardan yeniden hesaplanarak) 1.000 yapay örneklemde, birinci modelin negatif binom faz katsayıları ortalama olarak 0,032, 0,046 ve 0,065 bulunmuştur; yani gerçek etki sıfırken dahi faz katsayıları yukarı yanlı, stok katsayısı ise aşağı yanlıdır (gerçek değer 0,72; ortalama tahmin 0,63). İkinci modelde birinci faz eğimi ve ikinci faz düzeyi için ortalama sapma sıfıra çok yakındır (−0,003 ve −0,006). Bu nedenle birinci modelin faz katsayıları üst sınır olarak y…

### D039 · Bölüm 5.6.4 · T3, T5 · değişiklik

**Gerekçe.** Stoksuz modelin kanıt değeri, eğilim eklenmiş tanıma dayandırıldı.

**Önceki metin.** Birinci ve ikinci faz katsayılarının stoksuz modelde de pozitif ve anlamlı olması, bu fazlara ilişkin bulguların stok değişkeninin modelde yer almasına bağlı olmadığını göstermektedir.

**Yeni metin.** Birinci ve ikinci faz katsayılarının stoksuz modelde, doğrusal eğilim eklendiğinde de pozitif ve anlamlı olması (Tablo 5.14, satır d), bu fazlara ilişkin bulguların stok değişkeninin modelde yer almasına bağlı olmadığını göstermektedir.

### D040 · Bölüm 5.6.4 · Y6 · değişiklik

**Gerekçe.** Yanlış tablo numarası.

**Önceki metin.** hesaplanmıştır (Tablo 5.5).

**Yeni metin.** hesaplanmıştır (Tablo 5.6).

### D041 · Bölüm 5.6.4 · T4 · çıkarma

**Gerekçe.** 10 eşiği tek tek değişkenler içindir; ortalama için anlamı yoktur.

**Önceki metin.** Varyans şişirme faktörlerinin ortalaması 4,08’dir ve yaygın olarak kullanılan 10 eşiğinin altındadır.

### D042 · Bölüm 5.6.4 · T2 · ekleme

**Gerekçe.** İkinci modelin (tezde raporlanmayan) varyans şişirme faktörleri eklendi.

**Yeni metin.** İkinci modelde ülke içi varyans şişirme faktörleri daha yüksektir (Tablo 5.6a): ETS öncesi eğilim için 42,8, üçüncü faz düzeyi için 25,4, yeşil patent stoku için 12,0. Bu değerler, ikinci modelin ETS öncesi eğilim ile yeşil patent stokunu birbirinden ayırmakta zorlandığını göstermektedir; stok ile zaman arasındaki ülke içi korelasyon 0,95 düzeyindedir. Tablo 5.6a. İkinci Model İçin Varyans Şişirme Faktörleri Değişken VIF ETS öncesi eğilim ([denklem]) 42,78 Faz 1 düzey 3,86 Faz 1 eğim 2,47 Faz 2 düzey 8,48 Faz 2 eğim 3,35 Faz 3 düzey 25,43 Faz 3 eğim 6,35 [denklem] 12,04 GSYİH büyümesi 1,51 Yenilenebilir enerji payı 4,57 Enerji ithalat bağımlılığı 1,05 İmalat payı 2,10 Dış ticaret açıklığı 2,29 Not: Değişkenlerin ülke ortalamalarından arındırılmış değerleriyle hesaplanmıştır.

### D043 · Bölüm 5.6.5 · C2, C7 · değişiklik

**Gerekçe.** Gerekçe düzeltildi (küme büyüklükleri eşit: her ülkede 24 gözlem; farklı olan ağırlıklar). Bütün tablolarda aynı çıkarsama yöntemi kullanıldı.

**Önceki metin.** Küme sayısının azlığı ve küme büyüklüklerindeki farklılık nedeniyle ülke düzeyinde kümelenmiş eşli bootstrap uygulanmıştır. Yıl etkileri modeli ile plasebo kırılma testlerinde ülke düzeyinde kümelenmiş standart hatalar kullanılmıştır.

**Yeni metin.** Küme sayısının azlığı ve ülkelerin tahmindeki ağırlıklarının çok farklı olması nedeniyle ülke düzeyinde kümelenmiş eşli bootstrap uygulanmıştır. Yıl etkileri modeli ile plasebo kırılma testlerinde de aynı bootstrap yöntemi kullanılmış, ülke düzeyinde kümelenmiş standart hatalara dayanan sonuçlar karşılaştırma amacıyla ayrıca verilmiştir.

### D044 · Bölüm 5.6.5 · C2 · çıkarma

**Gerekçe.** Okuyucu için anlamsız yazılım ayrıntısı çıkarıldı.

**Önceki metin.** Negatif binom modelinde bootstrap, katsayılar adlandırılmış ifadeler olarak tanımlanarak uygulanmıştır.

### D045 · Bölüm 5.6.5 · B2 · değişiklik

**Gerekçe.** Yazılım için atıf eklendi.

**Önceki metin.** Tüm tahminler Stata 19 ile yapılmış,

**Yeni metin.** Tüm tahminler Stata 19 (StataCorp, 2025) ile yapılmış,

### D046 · Bölüm 5.6.5 · C1, C6, C9 · ekleme

**Gerekçe.** Yatay kesit bağımlılığının çıkarsamaya etkisi, t(13) kullanımı ve yöntemin benzetimle sınanması eklendi.

**Yeni metin.** Küme sayısı az olduğundan katsayıların anlamlılık düzeyleri normal dağılıma göre değil, bootstrap standart hatasıyla hesaplanan test istatistiğinin [denklem] serbestlik dereceli [denklem] dağılımıyla karşılaştırılmasıyla belirlenmiştir. Yatay kesit bağımlılığı testleri ülkeler arasında bağımlılık bulunduğunu göstermektedir (Tablo 5.9). Ülke düzeyinde yeniden örnekleme bu bağımlılığı hesaba katmadığından, raporlanan anlamlılık düzeyleri iyimser olabilir; bu nedenle sonuçlar küme jackknife ile de sınanmıştır. Çıkarsama yöntemlerinin sınırlı örneklemdeki davranışı benzetimle incelenmiştir. Faz etkilerinin sıfır olduğu ve verinin tahmin edilen modele göre üretildiği 300 yapay örneklemde, yüzde 5 anlamlılık düzeyinde boş hipotezin reddedilme oranları Tablo 5.6b’de verilmektedir. Gerçek etkinin …

### D047 · Bölüm 5.6.6 · M7 · değişiklik

**Gerekçe.** Negatif binomun tercih gerekçesi değiştirildi: ortak aşırı yayılım varsayımı sağlanmıyor; asıl üstünlüğü dengeli ağırlıklandırma.

**Önceki metin.** Bu nedenle çalışmada, verinin yayılım yapısıyla uyumlu olan negatif binom modeli ana tahminci olarak kullanılmış, dağılım varsayımına karşı sağlam olan Poisson sözde en çok olabilirlik tahmincisi ise alternatif tahminci olarak raporlanmıştır.

**Yeni metin.** Bununla birlikte aşırı yayılım ülkeler arasında belirgin biçimde farklılaşmaktadır (ülke bazında moment tahminleri Almanya için 0,009, Lüksemburg için 0,26); bu nedenle negatif binom modelinin etkinlik üstünlüğü kesin değildir. Negatif binom tahmincisi, ülkelere daha dengeli ağırlık verdiği için ana tahminci olarak kullanılmış, dağılım varsayımına karşı sağlam olan Poisson sözde en çok olabilirlik tahmincisi eş düzeyde raporlanmıştır.

### D048 · Bölüm 5.6.7 · M4 · tablo

**Gerekçe.** Birim kök tablolarında satır adı düzeltildi: testler yoğunluğun logaritmasıyla yapılmış.

**Önceki metin.** Tablo 5.7, Yeşil Patent Yoğunluğu: Yeşil Patent Yoğunluğu

**Yeni metin.** ln(Yeşil patent yoğunluğu)

### D049 · Bölüm 5.6.7 · M4 · ekleme

**Gerekçe.** Test dönemi tablo notuna yazıldı.

**Yeni metin.** Testler 1996–2020 dönemi için uygulanmıştır.

### D050 · Bölüm 5.6.7 · M4 · ekleme

**Gerekçe.** Sonucun logaritmik dönüşüme bağlı olduğu ve iki tablo arasındaki farkın nedeni belirtildi.

**Yeni metin.** Testler yeşil patent yoğunluğunun logaritmasıyla yapılmıştır; yoğunluğun düzey değeriyle CIPS istatistiği −2,09 olup birim kök boş hipotezi yüzde 10 düzeyinde dahi reddedilememektedir. Dış ticaret açıklığı ise birinci nesil testlerde trend durağan görünürken CIPS testinde düzeyde birim kök içermektedir.

### D053 · Bölüm 5.6.8 · M4 · ekleme

**Gerekçe.** Test dönemi tablo notuna yazıldı.

**Yeni metin.** Not: Kao testi 1997–2020 dönemi için uygulanmıştır.

### D051 · Bölüm 5.6.8 · M4 · kontrol

**Gerekçe.** YAZAR KONTROLÜ: Pedroni istatistiğinin işareti.

**Önceki metin.** Pedroni testinin üç istatistiğinin tamamı

**Yazar için not.** Değiştirilmiş Phillips-Perron istatistiği pozitiftir (+2,255). Yazılımın bu istatistiği hangi kuyrukta test ettiği çıktıdan kontrol edilmelidir; emin olunamazsa “üç istatistikten ikisi” yazılmalıdır.

### D052 · Bölüm 5.6.8 · M4 · çıkarma

**Gerekçe.** Testler bu genellemeyi göstermiyor.

**Önceki metin.** Dolayısıyla düzey değerleriyle tahmin, her iki test grubunun sonuçları altında da geçerlidir.

### D054 · Bölüm 5.6.9 · M2 · değişiklik

**Gerekçe.** Raporlanan iki dönem gecikmeli model stoku da geciktiriyor.

**Önceki metin.** Kontrol değişkenlerinin gecikme yapısı, bir ve iki dönem gecikmeli

**Yeni metin.** Kontrol değişkenlerinin ve yeşil patent stokunun gecikme yapısı, bir ve iki dönem gecikmeli

### D055 · Bölüm 5.6.9 · M2 · ekleme

**Gerekçe.** Yalnız kontrollerin geciktirildiği karşılaştırma eklendi.

**Yeni metin.** Yalnızca kontrol değişkenlerinin iki dönem geciktirildiği modelde Akaike bilgi kriteri 2966,65 olup bir dönem gecikmeli yapı bu karşılaştırmada da tercih edilmektedir.

### D056 · Bölüm 5.6.9 · Y4 · kontrol

**Gerekçe.** YAZAR KONTROLÜ: Pakes ve Griliches (1984) “1,6 yıl” aktarımı.

**Önceki metin.** firmaların Ar-Ge harcamaları ile patent başvuruları arasındaki ortalama gecikmenin yaklaşık 1,6 yıl olduğunu tespit etmiştir.

**Yazar için not.** Bu rakam kaynakta doğrulanamadı. Pakes ve Griliches (1984) bölümünden sayfa numarasıyla doğrulanmalı; bulunamazsa “patent başvurularının Ar-Ge harcamalarına büyük ölçüde aynı yıl ve izleyen yıl içinde tepki verdiğini göstermiştir” yazılmalıdır.

### D061 · Bölüm 5.7.1 · C6 · tablo

**Gerekçe.** Yıldızlar 13 serbestlik dereceli t dağılımına göre yeniden belirlendi (Tablo 5.11, 5.13, 5.14 ve 5.17): beş katsayı bir kademe düştü.

**Önceki metin.** Tablo 5.11, Faz 1 (2005: 0,0772**

**Yeni metin.** 0,0772*

### D062 · Bölüm 5.7.1 · C4, C6, T5 · ekleme

**Gerekçe.** Tablo 5.11 notuna üç uyarı eklendi: t(13), BC aralıklarının asimetrisi, stok kaynaklı yukarı yanlılık.

**Yeni metin.** Anlamlılık düzeyleri 13 serbestlik dereceli t dağılımına göre belirlenmiştir. Bootstrap dağılımları çarpık olduğundan sapma düzeltmeli aralıklar asimetriktir; yüzdelik aralıklar Tablo 5.11a’da verilmiştir. Yeşil patent stoku bağımlı değişkenin geçmişinden türetildiğinden faz katsayıları yukarı yanlı olabilir ve üst sınır olarak okunmalıdır (Bölüm 5.6.4).

### D063 · Bölüm 5.7.1 · C5 · değişiklik

**Gerekçe.** İki faz için tek cümlelik “anlamlı biçimde yükseldi” yargısı ayrıştırıldı: ikinci faz güçlü, birinci faz temkinli.

**Önceki metin.** Bulgular, AB ETS’nin ilk iki fazında yeşil patent yoğunluğunun ETS öncesi döneme göre anlamlı biçimde yükseldiğini göstermektedir.

**Yeni metin.** Bulgular, AB ETS’nin ilk iki fazında yeşil patent yoğunluğunun ETS öncesi döneme göre daha yüksek olduğunu göstermektedir. İkinci faz farkı negatif binom tahmincisinde kullanılan bütün çıkarsama yöntemlerinde anlamlıdır; birinci faz farkı ise negatif binom tahmincisinde anlamlı ya da sınırda, Poisson tahmincisinde çıkarsama yöntemine duyarlıdır (Tablo 5.11a).

### D064 · Bölüm 5.7.1 · C4 · çıkarma

**Gerekçe.** Anlamlılık yargısı kararsız BC aralıklarına dayandırılmıyor.

**Önceki metin.** Her iki fazın sapma düzeltmeli güven aralığı sıfırı içermemektedir.

### D065 · Bölüm 5.7.1 · C6, C3 · değişiklik

**Gerekçe.** Poisson sonuçlarının anlamlılık düzeyleri t(13)'e göre düzeltildi; iki tahminci arasındaki farkın nedeni yazıldı.

**Önceki metin.** Poisson QML modeli de aynı sonucu vermektedir: Birinci fazın etkisi yüzde 8,0, ikinci fazın etkisi yüzde 21,6’dır ve her iki katsayı da istatistiksel olarak anlamlıdır.

**Yeni metin.** Poisson QML modelinde birinci fazın farkı yüzde 8,0 (yüzde 10 düzeyinde anlamlı), ikinci fazın farkı yüzde 21,6’dır (yüzde 5 düzeyinde anlamlı). İki tahminci arasındaki fark büyük ölçüde ağırlıklandırmadan kaynaklanmaktadır: Poisson katsayıları başvuru ağırlıklı, negatif binom katsayıları ülkelere daha eşit ağırlık veren ortalama farkları göstermektedir (Bölüm 5.6.1).

### D066 · Bölüm 5.7.1 · Y3 · ekleme

**Gerekçe.** “Etki yok” ile “kanıt bulunamadı” ayrımı yapıldı (birinci jürinin istediği ifade).

**Yeni metin.** Başka bir deyişle üçüncü fazda, yeşil patent stoku sabitken ETS öncesine göre ek bir fark bulunduğuna ilişkin yeterli istatistiksel kanıt elde edilememiştir; tahminin belirsizliği yüksek olduğundan bu sonuç, üçüncü fazın etkisiz olduğu biçiminde yorumlanmamalıdır.

### D067 · Bölüm 5.7.1 · C4, Y3 · tablo

**Gerekçe.** Tablo 5.12'de “Anlamsız” yerine güven aralığının kendisi yazıldı (Tablo 5.11'deki aralıkların yüzdeye çevrilmiş hâli).

**Önceki metin.** Tablo 5.12, Faz 3 (2013: Anlamsız

**Yeni metin.** [−%18,0; %33,6]

### D068 · Bölüm 5.7.1 · T4 · değişiklik

**Gerekçe.** “Doğrudan etki” terimi değiştirildi.

**Önceki metin.** Bu sonuçlar, sistemin en güçlü doğrudan etkisinin ikinci fazda ortaya çıktığını, üçüncü fazda ise doğrudan etkinin belirgin biçimde zayıfladığını göstermektedir.

**Yeni metin.** Bu sonuçlar, stok sabitken gözlenen farkın en yüksek değerine ikinci fazda ulaştığını, üçüncü fazda ise belirgin biçimde küçüldüğünü göstermektedir.

### D069 · Bölüm 5.7.1 · C8 · değişiklik

**Gerekçe.** Sınırdaki ve tek tahminciye özgü sonuca iktisadi yorum yüklenmedi.

**Önceki metin.** Kontrol değişkenleri arasında dış ticaret açıklığı, negatif binom modelinde negatif ve yüzde 5 düzeyinde anlamlıdır. Ticaret açıklığındaki 10 puanlık bir artış, yeşil patent yoğunluğunu yaklaşık yüzde 4,8 azaltmaktadır.

**Yeni metin.** Kontrol değişkenleri arasında dış ticaret açıklığının katsayısı negatif binom modelinde negatif ve yüzde 10 düzeyinde anlamlıdır; Poisson modelinde anlamlı değildir. Bu nedenle dış ticaret açıklığına ilişkin güçlü bir yorum yapılmamıştır.

### D070 · Bölüm 5.7.1 · M3 · ekleme

**Gerekçe.** Kontrol değişkenlerinin anlamsızlığı “etki yok” diye değil, “ayrıştırılamadı” diye yorumlandı.

**Yeni metin.** Ancak bu değişkenler ülke içinde yeşil patent stokuyla birlikte hareket ettiğinden (Tablo 5.4, Panel B), etkileri stokun etkisinden ayrıştırılamamış olabilir.

### D071 · Bölüm 5.7.1 · C5, C4, C9 · ekleme

**Gerekçe.** Çıkarsama duyarlılığı tablosu eklendi: dört yöntemle p değerleri ve yüzdelik aralıklar.

**Yeni metin.** Tablo 5.11a, temel katsayılara ilişkin çıkarsamanın kullanılan yönteme duyarlılığını göstermektedir. İkinci faz farkı ile ikinci modeldeki birinci faz eğim artışı ve ikinci faz düzey farkı, negatif binom tahmincisinde kullanılan bütün çıkarsama yöntemlerinde yüzde 5 düzeyinde anlamlıdır. Birinci modeldeki birinci faz farkı negatif binom tahmincisinde bootstrap ve küme jackknife ile yüzde 5 düzeyinde anlamlı, parametrik bootstrap ile sınırdadır (p = 0,021–0,066); Poisson tahmincisinde ise küme jackknife (p = 0,228) ve parametrik bootstrap (p = 0,215–0,326) ile anlamlı değildir. Poisson tahmincisinde ikinci faz farkı küme jackknife ile yüzde 10 düzeyinde anlamlıdır (p = 0,068). Tablo 5.11a. Temel Katsayılar İçin Çıkarsama Duyarlılığı Katsayı Tahminci Katsayı Bootstrap SH p: bootstrap, normal…

### D072 · Bölüm 5.7.2 · Y6 · tablo

**Gerekçe.** χ²(2) = 15,39 için olasılık değeri 0,000'dır (0,001 değil).

**Önceki metin.** Tablo 5.13, Faz 1 ortak test: 15,39 (0,001)

**Yeni metin.** 15,39 (0,000)

### D073 · Bölüm 5.7.2 · C6 · ekleme

**Gerekçe.** Tablo 5.13 notu: t(13). YAZAR: kontrol değişkenlerinin boş bırakılan güven aralığı hücreleri Stata çıktısından doldurulmalı.

**Yeni metin.** Anlamlılık düzeyleri 13 serbestlik dereceli t dağılımına göre belirlenmiştir. Kontrol değişkenlerinin güven aralıkları yazılım çıktısından eklenmelidir.

### D074 · Bölüm 5.7.2 · T2 · değişiklik

**Gerekçe.** “ETS öncesi eğilim yok” sonucunun stoka bağlı olduğu yazıldı; stoksuz ikinci model sonuçları eklendi.

**Önceki metin.** Bu sonuç, birinci modelde tahmin edilen faz etkilerinin ETS’den önce başlamış bir yükselişin devamı olmadığı yorumunu desteklemektedir.

**Yeni metin.** Ancak stok, geçmiş başvuruların birikimi olduğundan zamanla yüksek düzeyde eşdoğrusaldır (ülke içi korelasyon 0,95). Stok modelden çıkarıldığında ETS öncesi dönemde yılda yaklaşık yüzde 5,0 (negatif binom; yüzde 1 düzeyinde anlamlı) ve yüzde 3,6 (Poisson; yüzde 5 düzeyinde anlamlı) düzeyinde bir artış eğilimi görülmektedir (Tablo 5.13a). Dolayısıyla ETS öncesinde eğilim bulunmadığı sonucu, stokun modelde yer almasına bağlıdır. Birinci fazdaki eğim artışı ve ikinci fazın başındaki düzey farkı ise stoksuz modelde de ortaya çıkmaktadır: negatif binom modelinde eğim artışı 0,117 (yüzde 1 düzeyinde anlamlı), düzey farkı 0,369 (yüzde 1 düzeyinde anlamlı); Poisson modelinde sırasıyla 0,069 (yüzde 10 düzeyinde anlamlı) ve 0,252 (yüzde 1 düzeyinde anlamlı).

### D075 · Bölüm 5.7.2 · Y6 · değişiklik

**Gerekçe.** Birim hatası: yüzde değil yüzde puan.

**Önceki metin.** negatif binom modelinde yaklaşık yüzde 11,7, Poisson modelinde yüzde 9,1 yükselmiştir.

**Yeni metin.** negatif binom modelinde yaklaşık 11,7 yüzde puan, Poisson modelinde 9,1 yüzde puan daha yüksektir.

### D076 · Bölüm 5.7.2 · T2 · ekleme

**Gerekçe.** Stoksuz ikinci model tablosu eklendi.

**Yeni metin.** Tablo 5.13a. İkinci Model, Yeşil Patent Stoku Hariç Değişken NB katsayı (bootstrap SH) Poisson QML katsayı (bootstrap SH) ETS öncesi eğilim ([denklem]) 0,0486*** (0,0119) 0,0354** (0,0131) Faz 1 düzey ([denklem]) 0,0273 (0,0655) −0,0108 (0,0375) Faz 1 eğim ([denklem]) 0,1175*** (0,0378) 0,0694* (0,0331) Faz 2 düzey ([denklem]) 0,3692*** (0,1045) 0,2517*** (0,0748) Faz 2 eğim ([denklem]) −0,0047 (0,0266) −0,0132 (0,0213) Faz 3 düzey ([denklem]) 0,1343 (0,2165) −0,0439 (0,1679) Faz 3 eğim ([denklem]) −0,0192 (0,0189) −0,0249* (0,0118) Not: Ülke sabit etkileri ve beş kontrol değişkeni modelde yer almaktadır; yeşil patent stoku dışarıda bırakılmıştır. Parantez içindeki değerler ülke düzeyinde kümelenmiş 1999 tekrarlı bootstrap standart hatalarıdır. Anlamlılık düzeyleri 13 serbestlik dereceli t…

### D077 · Bölüm 5.7.2 · T7 · değişiklik

**Gerekçe.** “Faz boyunca korunmaktadır” ifadesi yıl etkileriyle çelişiyordu.

**Önceki metin.** Bu durum, ikinci fazın başında ulaşılan yüksek düzeyin faz boyunca korunduğunu göstermektedir.

**Yeni metin.** Model faz içinde doğrusal bir eğim varsaydığından bu sonuç yıllık dalgalanmayı göstermemektedir; yıl etkileri, farkın ikinci fazın ilk yıllarında (2008–2010) yoğunlaştığını ve fazın sonuna doğru zayıfladığını ortaya koymaktadır (Bölüm 5.7.3).

### D078 · Bölüm 5.7.2 · Y3 · ekleme

**Gerekçe.** Üçüncü faz yorumu temkinli hâle getirildi.

**Yeni metin.** Üçüncü faz tahminlerinin belirsizliği yüksek olduğundan bu sonuç, üçüncü fazın etkisiz olduğu biçiminde değil, ek bir fark bulunduğuna ilişkin yeterli kanıt elde edilemediği biçiminde yorumlanmalıdır.

### D079 · Bölüm 5.7.2 · T7, T1 · değişiklik

**Gerekçe.** “Kurumsal kesinlikle pekişmektedir” yorumu çıkarıldı; zamanlama bunu desteklemiyor.

**Önceki metin.** Buna göre ETS öncesi eğilimden sapma, birinci fazın sonunda ulaşılan yüzde 30,3 düzeyinden ikinci fazın başında yüzde 42,3’e yükselmekte ve faz boyunca korunmaktadır. Birinci fazda başlayan süreç, ikinci fazda kurumsal kesinlikle pekişmektedir.

**Yeni metin.** Buna göre modelin öngördüğü sapma, birinci fazın sonunda ulaşılan yüzde 30,3 düzeyinden ikinci fazın başında yüzde 42,3’e yükselmektedir. Yıl etkileri ise bu farkın 2009’da en yüksek değerine ulaştıktan sonra fazın sonuna doğru azaldığını göstermektedir (Bölüm 5.7.3).

### D080 · Bölüm 5.7.3 · C7 · değişiklik

**Gerekçe.** Şekil 5.5 bootstrap aralıklarıyla yeniden çizildi.

**Önceki metin.** yıl katsayılarını ve yüzde 95 güven aralıklarını göstermektedir.

**Yeni metin.** yıl katsayılarını, bootstrap standart hatalarına ve kümelenmiş standart hatalara dayanan yüzde 95 güven aralıklarıyla birlikte göstermektedir.

### D081 · Bölüm 5.7.3 · C7 · şekil

**Gerekçe.** Şekil 5.5 yeniden çizildi: bootstrap standart hatalarına dayanan aralıklar (kalın) ve tezdeki kümelenmiş standart hata aralıkları (ince) birlikte.

**Önceki metin.** Şekil 5.5 (yalnız kümelenmiş standart hatalar)

**Yeni metin.** Şekil 5.5 (bootstrap ve kümelenmiş standart hatalar)

### D082 · Bölüm 5.7.3 · C7 · değişiklik

**Gerekçe.** Şekil notu güncellendi.

**Önceki metin.** ülke düzeyinde kümelenmiş standart hatalarla %95 güven aralıkları.

**Yeni metin.** kalın çizgiler ülke düzeyinde kümelenmiş 1999 tekrarlı bootstrap standart hatalarına (13 serbestlik dereceli t dağılımı), ince çizgiler ülke düzeyinde kümelenmiş standart hatalara dayanan %95 güven aralıklarıdır.

### D083 · Bölüm 5.7.3 · T2 · değişiklik

**Gerekçe.** ETS öncesi katsayıların hepsi pozitif ve azalan; “istikrarlı” değil.

**Önceki metin.** Bu sonuç, ETS’nin başlangıcından önce yeşil patent yoğunluğunun istikrarlı bir seyir izlediğini göstermektedir.

**Yeni metin.** Bununla birlikte yedi katsayının tamamı pozitiftir ve 2004’e doğru azalmaktadır; yeşil patent stoku kontrol edildiğinde ETS öncesinde yoğunluk istikrarlı değil, hafif azalan bir seyir izlemektedir.

### D084 · Bölüm 5.7.3 · C7 · değişiklik

**Gerekçe.** Yıl katsayılarının anlamlılığı bootstrap standart hatalarına göre yeniden yazıldı.

**Önceki metin.** Katsayılar 2006’dan itibaren anlamlı hale gelmekte ve kademeli olarak yükselmektedir:

**Yeni metin.** Katsayılar 2006’dan itibaren pozitiftir ve 2009’a kadar kademeli olarak yükselmektedir; bootstrap standart hatalarıyla yüzde 5 düzeyinde yalnızca 2009, yüzde 10 düzeyinde 2006–2008 katsayıları anlamlıdır:

### D085 · Bölüm 5.7.3 · C7, T7 · değişiklik

**Gerekçe.** İkinci faz içindeki düşüş rakamlarla yazıldı.

**Önceki metin.** Katsayılar 2010’da da anlamlı kalmakta, ikinci fazın sonuna doğru gerilemekte ve üçüncü fazda nokta tahminleri 2004 düzeyinin altında seyretmektedir.

**Yeni metin.** Katsayılar 2010’dan itibaren gerilemekte (2010’da 0,226; 2011’de 0,135; 2012’de 0,050), ikinci fazın son yıllarında sıfırdan ayırt edilememekte ve üçüncü fazda nokta tahminleri 2004 düzeyinin altında seyretmektedir.

### D086 · Bölüm 5.7.3 · T4, T7 · değişiklik

**Gerekçe.** Terimler ve zamanlama düzeltildi.

**Önceki metin.** Bu profil, birinci fazda kademeli hızlanmanın, ikinci fazda en yüksek etkinin ve üçüncü fazda doğrudan etkinin zayıflamasının yıllık verilerle de geçerli olduğunu göstermektedir.

**Yeni metin.** Bu profil, birinci fazda kademeli hızlanmanın, ikinci fazın ilk yıllarında en yüksek farkın ve üçüncü fazda stok sabitken gözlenen farkın kaybolmasının yıllık verilerde de görüldüğünü göstermektedir.

### D087 · Bölüm 5.7.3 · T4 · değişiklik

**Gerekçe.** “Açıklanmaktadır” yerine “ilişkilidir”.

**Önceki metin.** üçüncü fazdaki yüksek yeşil patent yoğunluğu yeşil patent stokundaki artışla açıklanmaktadır.

**Yeni metin.** üçüncü fazdaki yüksek yeşil patent yoğunluğu istatistiksel olarak yeşil patent stokundaki artışla ilişkilidir; stok AB ETS’den bağımsız nedenlerle de büyüdüğünden bu ilişki nedensel bir açıklama olarak yorumlanmamalıdır.

### D088 · Bölüm 5.8 · B1 · biçim

**Gerekçe.** “5.8 Sağlamlık Testleri” satırına başlık stili uygulandı.

**Önceki metin.** (düz paragraf)

**Yeni metin.** (Başlık 2)

### D089 · Bölüm 5.8.1 · T3, T5, T9, Y5 · değişiklik

**Gerekçe.** Dört yeni sağlamlık tanımı eklendi (d–g).

**Önceki metin.** Ana bulguların model tanımına duyarlılığı üç alternatif tanımla sınanmıştır.

**Yeni metin.** Ana bulguların model tanımına duyarlılığı yedi alternatif tanımla sınanmıştır.

### D090 · Bölüm 5.8.1 · T4 · tablo

**Gerekçe.** Tablo 5.14'te “(toplam etki)” nitelemesi kaldırıldı.

**Önceki metin.** Tablo 5.14, Yeşil patent stoku hariç: (a) Yeşil patent stoku hariç (toplam etki)

**Yeni metin.** (a) Yeşil patent stoku hariç

### D091 · Bölüm 5.8.1 · T3 · tablo

**Gerekçe.** Tablo 5.14'e dört yeni tanım eklendi: (d) stoksuz ve eğilimli, (e) referans dönem 1997–2002, (f) 2018–2020 hariç, (g) ön-örneklem ortalaması tahmincisi.

**Yeni metin.** Tablo 5.14, yeni satır: \(d\) Yeşil patent stoku hariç, doğrusal eğilim eklenmiş | NB | 0,1876\*\*\* (0,0605) | 0,4204\*\*\* (0,0900) | 0,1783 (0,1291)

### D092 · Bölüm 5.8.1 · C6, T3, T5, T9, Y5 · ekleme

**Gerekçe.** Tablo 5.14 notu güncellendi.

**Yeni metin.** Anlamlılık düzeyleri 13 serbestlik dereceli t dağılımına göre belirlenmiştir. (d)–(g) satırlarındaki tahminler bu güncellemede eklenmiştir; parantez içindeki değerler 1999 tekrarlı bootstrap standart hatalarıdır.

### D093 · Bölüm 5.8.1 · T4 · değişiklik

**Gerekçe.** “Toplam etki” terimi değiştirildi.

**Önceki metin.** Yeşil patent stokunun modelden çıkarılması, AB ETS’nin bilgi birikimi kanalı dahil toplam etkisini vermektedir.

**Yeni metin.** Yeşil patent stokunun modelden çıkarılması, stok hesaba katılmadan gözlenen faz farklarını vermektedir.

### D094 · Bölüm 5.8.1 · C6 · değişiklik

**Gerekçe.** Anlamlılık düzeyi t(13)'e göre düzeltildi.

**Önceki metin.** üçüncü fazda ise yüzde 88,8 daha yüksektir ve üç katsayı da yüzde 1 düzeyinde anlamlıdır.

**Yeni metin.** üçüncü fazda ise yüzde 88,8 daha yüksektir; ilk iki katsayı yüzde 1, üçüncüsü yüzde 5 düzeyinde anlamlıdır.

### D095 · Bölüm 5.8.1 · T3, T4 · değişiklik

**Gerekçe.** Stoksuz modelin yüzde 44 / 101 / 89 rakamlarının ETS öncesi eğilimi de içerdiği yazıldı; “bilgi birikimi sürdürüyor” çıkarımı yumuşatıldı.

**Önceki metin.** Birinci model ile bu model arasındaki fark, AB ETS’nin etkisinin önemli bir bölümünün yeşil patent stoku aracılığıyla sonraki yıllara taşındığını göstermektedir. Özellikle üçüncü fazda doğrudan etki anlamsızken toplam etkinin negatif binom modelinde güçlü ve anlamlı olması, bu fazdaki yüksek yeşil patent düzeyinin önceki fazlarda AB ETS’nin uyardığı bilgi birikimi tarafından sürdürüldüğünü ortaya koymaktadır.

**Yeni metin.** Ancak bu modelde zaman eğilimi bulunmadığından katsayılar ETS öncesinde başlayan artış eğilimini de içermektedir: yalnızca ETS öncesi eğilimin sürmesi, negatif binom modelinde fazlar için sırasıyla yaklaşık 0,27, 0,46 ve 0,78 büyüklüğünde katsayılar üretmektedir. Bu nedenle söz konusu yüzdeler AB ETS’nin toplam etkisi olarak yorumlanmamalıdır. Birinci model ile stoksuz model arasındaki fark, AB ETS’nin bilgi birikimi yoluyla taşınan etkisiyle tutarlıdır; ancak yeşil patent stoku ETS’den bağımsız nedenlerle de büyüdüğünden, bu fark nedensel bir aracılık etkisi olarak yorumlanmamalıdır.

### D096 · Bölüm 5.8.1 · T3 · değişiklik

**Gerekçe.** Kanıt eğilimli tanıma dayandırıldı.

**Önceki metin.** Birinci ve ikinci faz katsayılarının stoksuz modelde de pozitif ve anlamlı olması, ayrıca, bu fazlara ilişkin bulguların stok değişkeninin modelde yer almasına bağlı olmadığını göstermektedir.

**Yeni metin.** Birinci ve ikinci faz katsayılarının stoksuz modelde, doğrusal eğilim eklendiğinde de pozitif ve anlamlı olması (satır d), bu fazlara ilişkin bulguların stok değişkeninin modelde yer almasına bağlı olmadığını göstermektedir.

### D097 · Bölüm 5.8.1 · M1 · değişiklik

**Gerekçe.** Birinci fazdaki fark gizlenmedi.

**Önceki metin.** Ancak bu modelde faz katsayıları birinci modeldekilere yakındır:

**Yeni metin.** Bu modelde ikinci ve üçüncü faz katsayıları birinci modeldekilere yakındır, birinci faz katsayısı ise yaklaşık yüzde 24 daha büyüktür:

### D098 · Bölüm 5.8.1 · M1 · değişiklik

**Gerekçe.** Reddedilen kısıtın neden korunduğu dürüstçe yazıldı; iki tanım birlikte raporlanıyor; İrlanda 2015 dipnotu eklendi.

**Önceki metin.** Dolayısıyla maruziyet kısıtı faz etkilerine ilişkin bulguları etkilememektedir. Tezin hipotezleri yeşil patent yoğunluğu üzerinden kurulduğundan, katsayıların yoğunluktaki oransal değişim olarak yorumlanmasını sağlayan maruziyet tanımı ana model olarak korunmuştur.

**Yeni metin.** Dolayısıyla birim esneklik kısıtı veriyle reddedilmekle birlikte, faz farklarının işareti iki tanımda aynıdır; birinci ve ikinci faz farkları serbest esneklik tanımında da anlamlıdır. Tezin hipotezleri yeşil patent yoğunluğu üzerinden kurulduğundan maruziyet tanımı ana model olarak korunmuş, sonuçlar her iki tanımla birlikte raporlanmıştır. İrlanda’nın 2015 yılındaki yüzde 24,6’lık GSYİH artışının maruziyet değişkenini etkileyebileceği dikkate alınarak model İrlanda dışarıda bırakılarak da tahmin edilmiş, katsayılar belirgin biçimde değişmemiştir (negatif binom: birinci faz 0,140; ikinci faz 0,264).

### D099 · Bölüm 5.8.1 · C3 · ekleme

**Gerekçe.** Almanya hariç tahmin, ağırlıklandırma çerçevesiyle yorumlandı.

**Yeni metin.** Almanya dışarıda bırakıldığında Poisson birinci faz katsayısı (0,1323) negatif binom tahmincisinin tam örneklem değerine (0,1338) yaklaşmaktadır; bu durum, iki tahminci arasındaki farkın büyük ölçüde Poisson tahmincisinin Almanya’ya verdiği ağırlıktan kaynaklandığını göstermektedir.

### D100 · Bölüm 5.8.1 · T3, T5, T7, T9, Y5 · ekleme

**Gerekçe.** Yeni sağlamlık tanımlarının açıklamaları (d–g), tek ETS kuklası ve ikinci fazın bölünmesi eklendi.

**Yeni metin.** (d) Yeşil patent stoku hariç, doğrusal eğilimli model. Stoksuz modele ETS öncesi artış eğilimini temsil eden doğrusal bir eğilim eklenmiştir. Bu tanımda faz katsayıları küçülmektedir: negatif binom modelinde birinci faz 0,188, ikinci faz 0,420, üçüncü faz 0,178; Poisson modelinde sırasıyla 0,139, 0,356 ve 0,101. Birinci ve ikinci faz katsayıları her iki tahmincide de anlamlı kalmakta, üçüncü faz katsayısı ise anlamlılığını yitirmektedir. Stok hesaba katılmadığında üçüncü fazda görülen büyük fark, dolayısıyla, ETS öncesinde başlayan eğilimden ayırt edilememektedir. (e) Referans dönemin 1997–2002 ile sınırlandırıldığı model. 2003/87/AT sayılı Direktif’in kabul edildiği 2003 yılından itibaren beklenti etkilerinin oluşmuş olabileceği dikkate alınarak 2003–2004 yılları için ayrı bir kukla eklen…

### D101 · Bölüm 5.8.2 · Y1 · değişiklik

**Gerekçe.** Tabloda karşılığı olmayan güven aralığı cümlesi çıkarıldı.

**Önceki metin.** yedisinde yüzde 5, on üçünde yüzde 10 düzeyinde anlamlıdır ve sapma düzeltmeli güven aralığı on üç tahminde sıfırı içermemektedir.

**Yeni metin.** yedisinde yüzde 5, on üçünde yüzde 10 düzeyinde anlamlıdır.

### D102 · Bölüm 5.8.2 · Y1 · değişiklik

**Gerekçe.** Sonuç cümlesi tablonun gösterdiği kadarına indirildi.

**Önceki metin.** Bu sonuçlar, bulguların herhangi bir ülkenin örneklemde bulunmasına bağlı olmadığını göstermektedir.

**Yeni metin.** Bu sonuçlar, ikinci faz farkının herhangi bir ülkenin örneklemde bulunmasına bağlı olmadığını, birinci faz farkının ise ülke bileşimine duyarlı olduğunu göstermektedir. Danimarka ya da Almanya dışarıda bırakıldığında faz katsayıları büyümekte ve üçüncü faz katsayısının işareti pozitife dönmektedir.

### D103 · Bölüm 5.8.3 · T6 · değişiklik

**Gerekçe.** Eksik raporlanan 1999 ve 2003 plaseboları eklendi.

**Önceki metin.** 2000, 2001 ve 2002 yılları için sahte kırılma noktaları tanımlanmıştır.

**Yeni metin.** 1999, 2000, 2001, 2002 ve 2003 yılları için sahte kırılma noktaları tanımlanmıştır.

### D104 · Bölüm 5.8.3 · T6, C7 · tablo

**Gerekçe.** Tablo 5.16 genişletildi: 1999 ve 2003 satırları ile bootstrap olasılık değerleri eklendi (2000–2002 satırlarındaki mevcut değerler aynen korundu).

**Önceki metin.** Tablo 5.16 (tamamı)

**Yeni metin.** Sahte kırılma yılı Poisson [denklem](2) p (kümelenmiş) p (bootstrap) NB [denklem](2) p (kümelenmiş) p (bootstrap) 1999 2,35 0,308 0,490 0,07 0,964 0,972 2000 2,20 0,333 0,540 0,23 0,891 0,897 2001 4,15 0,126 0,580 0,96 0,619 0,698 2002 4,35 0,114 0,507 0,53 0,767 0,804 2003 9,51 0,009 0,129 5,45 0,066 0,128

### D105 · Bölüm 5.8.3 · C7 · değişiklik

**Gerekçe.** Tablo notu güncellendi.

**Önceki metin.** Testler ülke düzeyinde kümelenmiş standart hatalarla yapılmıştır.

**Yeni metin.** Ki-kare istatistikleri ülke düzeyinde kümelenmiş kovaryans matrisine dayanmaktadır; bootstrap olasılık değerleri, ülke düzeyinde kümelenmiş 1999 tekrarlı bootstrap kovaryans matrisiyle hesaplanan Wald istatistiğine aittir.

### D106 · Bölüm 5.8.3 · T6 · değişiklik

**Gerekçe.** Plasebo sonuçları eksiksiz ve temkinli yorumlandı; 2003 sonucu açıklandı.

**Önceki metin.** Üç sahte kırılma yılının hiçbirinde, hiçbir tahminci ile düzey ve eğim katsayıları ortak olarak anlamlı değildir. ETS öncesi dönemde yeşil patent yoğunluğunda, ETS döneminde gözlemlenen türden bir kırılma bulunmamaktadır. Bu sonuç, birinci model ve ikinci modelde tahmin edilen faz etkilerinin örneklem döneminin herhangi bir yerinde kendiliğinden ortaya çıkan rastlantısal kırılmalar olmadığını, AB ETS’nin faaliyete geçtiği dönemle sınırlı olduğunu göstermektedir.

**Yeni metin.** 1999–2002 yılları için tanımlanan sahte kırılmalarda, hiçbir tahminci ile düzey ve eğim katsayıları ortak olarak anlamlı değildir. 2003 yılı için kümelenmiş standart hatalarla anlamlı (Poisson p = 0,009; negatif binom p = 0,066), bootstrap ile anlamsız (p = 0,129 ve 0,128) bir sapma görülmektedir. 2003–2004 yıllarında yoğunluk önceki eğilimin altında kalmıştır; bu sapma, Direktif’in 2003’te kabul edilmesinin ardından oluşan bekleme davranışıyla ilişkili olabilir. Sekiz yıllık dönemde ve 14 ülkeyle testin gücü sınırlı olduğundan, bu sonuçlar faz farklarının yalnızca AB ETS dönemine özgü olduğunun kesin kanıtı olarak yorumlanmamalıdır.

### D107 · Bölüm 5.9 · T3, Y2 · tablo

**Gerekçe.** Hipotez tablosu kanıtın gösterdiği düzeye çekildi: H1 kanıtı değişti, H2 ve H5 “kısmen”, H3'e zamanlama notu.

**Önceki metin.** Tablo 5.17, H1: Toplam etki üç fazda pozitif ve anlamlı (NB: %43,8; %101,2; %88,8)

**Yeni metin.** Tek ETS dönemi kuklası pozitif ve anlamlı (NB 0,255; Poisson 0,248; stok sabitken yaklaşık %29,1)

### D108 · Bölüm 5.9 · T1, Y2, M1 · ekleme

**Gerekçe.** Hipotez tablosuna yorum notu eklendi.

**Yeni metin.** Not: Sonuçlar nedensel etki olarak değil, AB ETS fazlarıyla ilişkili farklar olarak yorumlanmalıdır (Bölüm 5.11). Faz katsayılarının işareti GSYİH esnekliğinin serbest bırakıldığı tanımda da aynıdır; birinci ve ikinci faz farkları bu tanımda da anlamlıdır (Tablo 5.14, satır b).

### D109 · Bölüm 5.10.2 · T7 · değişiklik

**Gerekçe.** Alt başlık nötr hâle getirildi.

**Önceki metin.** 5.10.2 İkinci Faz: Kurumsal Kesinlik ve En Güçlü Etki

**Yeni metin.** 5.10.2 İkinci Faz: İlk Yıllardaki Artış

### D110 · Bölüm 5.10.2 · T4, T7 · değişiklik

**Gerekçe.** “Açıklamaktadır” yerine “tutarlıdır”; zamanlama belirtildi.

**Önceki metin.** AB ETS’nin yeşil inovasyon üzerindeki doğrudan etkisi ikinci fazda en yüksek düzeye ulaşmıştır. İkinci fazın üç kurumsal özelliği bu sonucu açıklamaktadır.

**Yeni metin.** Stok sabitken gözlenen fark ikinci fazda, özellikle fazın ilk yıllarında (2008–2010) en yüksek düzeye ulaşmıştır. İkinci fazın üç kurumsal özelliği bu sonuçla tutarlıdır.

### D111 · Bölüm 5.10.2 · T10 · değişiklik

**Gerekçe.** Doğrusal indirim faktörünün 2020'de biten bir süresi yoktu.

**Önceki metin.** 2020 yılına kadar geçerli olacak tek üst sınır

**Yeni metin.** 2013’ten itibaren geçerli olacak tek üst sınır

### D112 · Bölüm 5.10.2 · T7 · değişiklik

**Gerekçe.** Veri, farkın “sürdüğünü” değil 2009'dan sonra azaldığını gösteriyor.

**Önceki metin.** İkinci fazın başında ETS öncesi eğilimden sapmanın yükselmesi ve faz boyunca korunması, ikinci faz etkisinin 2008 finans krizi ve ardından gelen fiyat düşüşüne karşın sürdüğünü göstermektedir.

**Yeni metin.** İkinci fazın başında ETS öncesi eğilime göre belirgin bir düzey farkı oluşmuş, bu fark 2009’da en yüksek değerine ulaştıktan sonra fazın sonuna doğru azalmıştır; dolayısıyla artış fazın tamamına değil, ilk yıllarına aittir. 2009/29/AT sayılı Direktif Nisan 2009’da kabul edilmiş, fark ise bu tarihten sonra küçülmüştür.

### D113 · Bölüm 5.10.2 · T1, T7 · değişiklik

**Gerekçe.** Kesin nedensel ifade olasılık ifadesine çevrildi.

**Önceki metin.** Firmaların inovasyon kararlarını belirleyen sistemin uzun dönemli yönüne ilişkin beklentilerdir.

**Yeni metin.** Firmaların inovasyon kararlarını sistemin uzun dönemli yönüne ilişkin beklentilerin belirlemesi olasıdır; ancak bu veriyle beklenti kanalı, aynı döneme denk gelen diğer gelişmelerden ayırt edilememektedir.

### D114 · Bölüm 5.10.2 · T1, T7 · ekleme

**Gerekçe.** İkinci faz artışı için alternatif açıklamalar yan yana sayıldı.

**Yeni metin.** İkinci fazın ilk yıllarındaki artış için AB ETS dışında başka açıklamalar da bulunmaktadır. İkinci faz, Kyoto Protokolü’nün birinci taahhüt dönemiyle (2008–2012) aynı yılları kapsamaktadır; enerji fiyatları 2008’de en yüksek düzeyine ulaşmış, 2009/28/AT sayılı Yenilenebilir Enerji Direktifi aynı dönemde kabul edilmiştir. Ayrıca 2008–2009 yıllarında başvurusu yapılan buluşlar, büyük ölçüde kriz öncesinde alınan Ar-Ge kararlarını yansıtmaktadır. 2010 sonrasındaki zayıflama ise kriz sonrası Ar-Ge kısıntıları ve izin fiyatındaki düşüşle aynı döneme denk gelmektedir. Bu çalışmanın tasarımı söz konusu açıklamaları birbirinden ayırt edememektedir.

### D115 · Bölüm 5.10.3 · Y3, T4 · değişiklik

**Gerekçe.** Alt başlık kanıtın gösterdiği düzeye çekildi.

**Önceki metin.** 5.10.3 Üçüncü Faz: Bilgi Birikiminin Taşıdığı Etki

**Yeni metin.** 5.10.3 Üçüncü Faz: Ek Fark Gözlenmemesi ve Olası Açıklamalar

### D116 · Bölüm 5.10.3 · Y3, T3, T4 · değişiklik

**Gerekçe.** Üçüncü faz yorumu yeniden yazıldı: iki olası açıklama yan yana; hangisinin geçerli olduğu bu veriyle belirlenemiyor.

**Önceki metin.** Üçüncü fazda yeşil patent stoku kontrol edildiğinde ETS öncesine göre ek bir doğrudan etki bulunmamakta ancak stoksuz negatif binom modelinde ise üçüncü fazın toplam etkisi güçlü ve anlamlı çıkmaktadır. Bu iki bulgu birlikte değerlendirildiğinde, üçüncü fazdaki yüksek yeşil patent düzeyinin birinci ve ikinci fazlarda oluşan bilgi birikimi tarafından sürdürüldüğü, üçüncü fazın kendi kurallarının ise bu düzeyi daha ileriye taşıyacak ek bir teşvik yaratmadığı sonucuna ulaşılabilmektedir.

**Yeni metin.** Üçüncü fazda, yeşil patent stoku sabitken ETS öncesine göre ek bir fark bulunduğuna ilişkin yeterli istatistiksel kanıt elde edilememiştir; tahminin belirsizliği yüksek olduğundan bu sonuç üçüncü fazın etkisiz olduğu biçiminde yorumlanmamalıdır. Stok hesaba katılmadığında negatif binom modelinde üçüncü faz farkı büyük ve anlamlıdır; ancak bu fark ETS öncesinde başlayan artış eğilimini de içermekte, doğrusal eğilim eklendiğinde anlamlılığını yitirmektedir (Tablo 5.14, satır d). Bu bulgular iki açıklamayla bağdaşmaktadır: üçüncü fazda yeşil patentleme üzerindeki teşvikin zayıflamış olması ya da önceki fazlarda oluşan bilgi birikiminin ulaşılan düzeyi sürdürmesi. Bu veriyle iki açıklama birbirinden ayırt edilememektedir.

### D117 · Bölüm 5.10.3 · T4 · değişiklik

**Gerekçe.** Aracılık iddiası yumuşatıldı.

**Önceki metin.** Bu sonuç, politika etkisinin bilgi stoku aracılığıyla zaman içinde birikerek sürdüğünü göstermektedir. İlk iki fazda uyarılan buluşlar yeşil patent stokunu artırmış, bu stok da üçüncü fazda yeni yeşil patent faaliyetinin temel belirleyicisi olmuştur.

**Yeni metin.** Bulgular, politika etkisinin bilgi stoku aracılığıyla zaman içinde taşınmasıyla tutarlıdır; ancak stok AB ETS’den bağımsız nedenlerle de büyüdüğünden bu kanal ayrıştırılamamaktadır. İlk iki fazda artan başvurular yeşil patent stokunu büyütmüş, bu stok da üçüncü fazda yeni yeşil patent faaliyetiyle güçlü biçimde ilişkili olmuştur.

### D118 · Bölüm 5.10.3 · T1, T3 · değişiklik

**Gerekçe.** Küresel eğilim ölçütü iki yöne de uygulandı (düşüş küresel eğilime, yükseliş ETS'ye bağlanıyordu).

**Önceki metin.** bu küresel eğilimin 14 AB üyesi ülkede de gözlemlendiğini, ancak bilgi stoku kontrol edilmeden ölçülen toplam etkinin üçüncü fazda da güçlü kaldığını göstermektedir.

**Yeni metin.** bu küresel eğilimin 14 AB üyesi ülkede de gözlemlendiğini göstermektedir. Aynı ölçüt birinci ve ikinci faz için de geçerlidir: bu fazlardaki yükseliş de aynı dönemdeki küresel temiz teknoloji patentleme artışından etkilenmiş olabilir.

### D119 · Bölüm 5.10.3 · T11 · ekleme

**Gerekçe.** Karbon fiyatının rolü tartışmaya eklendi. YAZAR: yıllık izin fiyatı serisiyle bir sağlamlık tahmini yapılması önerilir (yeni veri gerekir).

**Yeni metin.** Karbon fiyatı bu çalışmada açıklayıcı değişken olarak yer almamaktadır. Üçüncü fazın büyük bölümünde izin fiyatının düşük seyretmesi, bu fazda ek bir fark gözlenmemesinin olası açıklamalarından biridir; ancak birinci fazın sonunda izin fiyatı çökerken farkın artması, fiyat ile patentleme arasında basit bir eşzamanlı ilişki bulunmadığına işaret etmektedir. İzin fiyatının modele dâhil edilmesi ileriki çalışmalara bırakılmıştır.

### D120 · Bölüm 5.10.4 · T5 · ekleme

**Gerekçe.** Stok katsayısının yanlılık yönü belirtildi.

**Yeni metin.** Benzetim sonuçları stok katsayısının aşağı yanlı tahmin edildiğini gösterdiğinden (Bölüm 5.6.4) bu değerler alt sınır olarak okunmalıdır.

### D121 · Bölüm 5.10.4 · T4 · değişiklik

**Gerekçe.** Kesin nedensel cümle çıkarıldı.

**Önceki metin.** Birinci model ile stoksuz model arasındaki fark, AB ETS’nin erken fazlardaki etkisinin bilgi stoku aracılığıyla kalıcılaştığını göstermektedir. AB ETS, yalnızca uygulandığı dönemde değil, yarattığı bilgi birikimi aracılığıyla sonraki dönemlerde de yeşil inovasyonu artırmıştır.

**Yeni metin.** Birinci model ile stoksuz model arasındaki fark, AB ETS’nin erken fazlardaki etkisinin bilgi stoku aracılığıyla taşınmasıyla tutarlıdır; ancak yeşil patent stoku AB ETS’den bağımsız nedenlerle de büyüdüğünden, bu fark nedensel bir aracılık etkisi olarak yorumlanmamalıdır.

### D122 · Bölüm 5.10.4 · T4 · değişiklik

**Gerekçe.** Stokun Ar-Ge'yi “kontrol ettiği” iddiası yumuşatıldı.

**Önceki metin.** Bu nedenle ülkelerin Ar-Ge kapasitesi ve beşeri sermayesi, stok değişkeni aracılığıyla modelde yer almaktadır.

**Yeni metin.** Bu nedenle ülkelerin Ar-Ge kapasitesi ve beşeri sermayesi modelde yalnızca dolaylı olarak, stok değişkeni aracılığıyla temsil edilmektedir.

### D123 · Bölüm 5.10.5 · T1 · değişiklik

**Gerekçe.** “Doğrulamakta” yerine “tutarlıdır”.

**Önceki metin.** sonucunu doğrulamakta ve dört yönde genişletmektedir.

**Yeni metin.** sonucuyla tutarlıdır ve bu sonucu dört yönde genişletmektedir.

### D124 · Bölüm 5.10.5 · T4 · değişiklik

**Gerekçe.** Terim değiştirildi.

**Önceki metin.** üçüncü fazda ek doğrudan etkinin bulunmaması ayrıştırılmıştır.

**Yeni metin.** üçüncü fazda stok sabitken ek bir farkın gözlenmemesi ayrıştırılmıştır.

### D125 · Bölüm 5.10.5 · T4 · değişiklik

**Gerekçe.** Katkı cümlesi, yapılan şeyin gerçekte ne olduğuna göre yazıldı.

**Önceki metin.** Üçüncüsü, yeşil patent stoku modele dahil edilerek AB ETS’nin doğrudan etkisi ile bilgi birikimi yoluyla taşınan etkisi birbirinden ayrılmıştır.

**Yeni metin.** Üçüncüsü, yeşil patent stoku modele dahil edilerek stok sabitken gözlenen fark ile stok hesaba katılmadan gözlenen fark ayrı ayrı raporlanmıştır.

### D126 · Bölüm 5.10.5 · Y4 · kontrol

**Gerekçe.** YAZAR KONTROLÜ: Bel ve Joseph (2018) tahmincisi.

**Önceki metin.** Dördüncüsü, rassal etkili model yerine koşulsuz sabit etkili negatif binom ve sabit etkili Poisson modeli kullanılmıştır.

**Yazar için not.** Bel ve Joseph'in (2018) rassal etkili model kullandığı, makalenin yöntem bölümünden doğrulanmalıdır.

### D127 · Bölüm 5.10.5 · Y4 · kontrol

**Gerekçe.** YAZAR KONTROLÜ: Bel ve Joseph (2018) kapsamı.

**Önceki metin.** Ayrıca Bel ve Joseph’in (2018) ana modeli enerji teknolojilerine ilişkin patentlere dayanırken, bu çalışma iklim değişikliği azaltım teknolojilerinin tamamını kapsamaktadır.

**Yazar için not.** Makalenin özeti genel iklim değişikliği azaltım teknolojisi patentlerinin de kullanıldığını belirtmektedir. Kapsam farkı makalenin veri bölümünden doğrulanmalı; doğrulanamazsa bu cümle çıkarılmalıdır.

### D128 · Bölüm 5.10.5 · T1 · değişiklik

**Gerekçe.** Üçüncü olası neden eklendi.

**Önceki metin.** Bu çalışmada tahmin edilen ülke düzeyindeki etki daha büyüktür. Bu farkın iki nedeni bulunmaktadır.

**Yeni metin.** Bu çalışmada tahmin edilen ülke düzeyindeki fark daha büyüktür. Bu farkın üç olası nedeni bulunmaktadır.

### D129 · Bölüm 5.10.5 · T1 · ekleme

**Gerekçe.** Firma düzeyi çalışmayla farkın üçüncü olası nedeni: karşılaştırma grubu yok.

**Yeni metin.** Üçüncüsü, karşılaştırma grubu bulunmadığından ülke düzeyindeki önce–sonra farkı, aynı döneme denk gelen diğer gelişmelerin etkisini de içerebilmektedir.

### D130 · Bölüm 5.10.5 · T1 · değişiklik

**Gerekçe.** “Temel açıklama” yerine “olası açıklamalardan biri”.

**Önceki metin.** fazlar arasındaki farklılaşmanın temel açıklamasını oluşturmaktadır.

**Yeni metin.** fazlar arasındaki farklılaşmanın olası açıklamalarından birini oluşturmaktadır.

### D131 · Bölüm 5.10.5 · T1, T7, Y5 · değişiklik

**Gerekçe.** Bölümün kapanış cümlesi nedensel iddiadan betimleyici bulguya çevrildi.

**Önceki metin.** Bu çalışmanın bulguları, AB ETS’nin etkisinin dönemden döneme değiştiğini ve emisyon izin arzının sıkı yönetildiği, kuralların uzun vadeli olarak kesinleştiği dönemlerde güçlü bir inovasyon etkisi ortaya çıktığını göstermektedir.

**Yeni metin.** Bu çalışmanın bulguları, AB ETS fazlarıyla ilişkili farkların dönemden döneme değiştiğini, yeşil patent yoğunluğunun birinci faz boyunca hızlandığını ve ikinci fazın ilk yıllarında en yüksek düzeyine ulaştığını göstermektedir; bu farkların ne kadarının izin arzının sıkılaştırılmasından ve kuralların kesinleşmesinden kaynaklandığı bu tasarımla ayırt edilememektedir.

### D132 · Bölüm 5.10.5 · T1, C1, C9, T5, T8, T11, Y5, T4, T10 · ekleme

**Gerekçe.** Yeni alt bölüm: Çalışmanın Sınırlılıkları (karşılaştırma grubu, ortak şoklar, az küme, stok yapısı, örneklem, eksik değişkenler, ölçüm; ileriki çalışma önerileri).

**Yeni metin.** 5.11 Çalışmanın Sınırlılıkları Bu bölümün bulguları aşağıdaki sınırlılıklarla birlikte değerlendirilmelidir. Birincisi, çalışmanın tasarımı bir önce–sonra karşılaştırmasıdır. Örneklemdeki bütün ülkeler AB ETS’ye aynı tarihte dâhil olduğundan sisteme tabi olmayan bir karşılaştırma grubu bulunmamaktadır. Tahmin edilen faz farkları, aynı dönemde gerçekleşen diğer ortak gelişmelerin (Kyoto Protokolü’nün 2008–2012 birinci taahhüt dönemi, 2004–2008 enerji fiyatı artışı, 2009 tarihli Yenilenebilir Enerji Direktifi, küresel temiz teknoloji patentleme dalgası) etkisini de içerebilir. Bu nedenle bulgular nedensel etki olarak değil, AB ETS fazlarıyla ilişkili farklar olarak yorumlanmalıdır. İkincisi, yıl sabit etkileri faz kuklalarıyla birlikte tanımlanamadığından ortak şoklar tümüyle ayrıştırılamama…

### D135 · Bölüm Kaynakça · B2, T5, C2, C9 · ekleme

**Gerekçe.** Kaynakçaya dört kayıt eklendi: metne eklenen yeni atıfların karşılıkları ve Stata.

**Yeni metin.** Blundell, R., Griffith, R. ve Van Reenen, J. (1999). Market share, market value and innovation in a panel of British manufacturing firms. Review of Economic Studies, 66(3), 529–554. / Blundell, R., Griffith, R. ve Windmeijer, F. (2002). Individual effects and dynamics in count data models. Journal of Econometrics, 108(1), 113–131. / MacKinnon, J. G., Nielsen, M. Ø. ve Webb, M. D. (2023). Cluster-robust inference: A guide to empirical practice. Journal of Econometrics, 232(2), 272–299. / StataCorp. (2025). Stata statistical software: Release 19. StataCorp LLC.

### D133 · Bölüm Kaynakça · B2 · biçim

**Gerekçe.** Kaynakça kaydı diğerleriyle aynı biçime getirildi (“&” yerine “ve”, tırnaklar kaldırıldı, başlık cümle düzeninde).

**Önceki metin.** Dechezleprêtre, A., Glachant, M., Haščič, I., Johnstone, N., & Ménière, Y. (2011). "Invention and Transfer of Climate Change–Mitigation Technologies: A Global Analysis." Review of Environmental Economics and Policy, 5(1), 109–130.

**Yeni metin.** Dechezleprêtre, A., Glachant, M., Haščič, I., Johnstone, N. ve Ménière, Y. (2011). Invention and transfer of climate change–mitigation technologies: A global analysis. Review of Environmental Economics and Policy, 5(1), 109–130.

### D134 · Bölüm Kaynakça · B2 · çıkarma

**Gerekçe.** Aynı veri seti iki yerde, iki farklı yılla (2024 ve 2026) kayıtlıydı; metindeki atıfla (OECD, 2026) uyumlu olan kayıt bırakıldı.

**Önceki metin.** OECD. Environment-Related Technologies Patents [Dataset]; OECD Data Explorer, OECD.STI.PIE; OECD: Paris, France, 2024; Available online: https://data-explorer.oecd.org (accessed on 1 March 2026).

## Bulgulara göre dizin

| Bulgu | Konu | Değişiklikler |
|---|---|---|
| T1 | Karşılaştırma grubu yok: ETS'nin etkisi aynı yıllardaki başka olaylardan ayrılamıyor | D014, D035, D079, D108, D113, D114, D118, D123, D128, D129, D130, D131, D132 |
| T2 | “ETS'den önce artış eğilimi yoktu” sonucu yanıltıcı | D015, D042, D074, D076, D083 |
| T3 | H1 için gösterilen “toplam etki” rakamları (%44, %101, %89) olduğundan büyük | D039, D089, D091, D092, D095, D096, D100, D107, D116, D118 |
| T4 | “Doğrudan etki” ve “bilgi birikimiyle taşınan etki” ayrımı kanıtlanmış değil | D023, D037, D041, D068, D086, D087, D090, D093, D095, D110, D115, D116, D117, D121, D122, D124, D125, D132 |
| T5 | Modelin yapısı, birinci modelin faz katsayılarını olduğundan büyük gösteriyor | D038, D039, D062, D089, D092, D100, D120, D132, D135 |
| T6 | Sahte başlangıç (plasebo) testleri eksik raporlanmış ve zayıf | D103, D104, D106 |
| T7 | İkinci fazdaki artış faz boyunca sürmüyor; 2009'da zirve yapıp sönüyor | D077, D079, D085, D086, D100, D109, D110, D112, D113, D114, D131 |
| T8 | Birleşik Krallık'ın dışarıda bırakılma gerekçesi yanlış | D024, D132 |
| T9 | Karşılaştırma döneminin son iki yılı (2003–2004) birinci faz sonucunu etkiliyor | D011, D089, D092, D100 |
| T10 | “Kurallar tümüyle AB düzeyinde belirlendi” ifadesi ilk iki faz için eksik | D012, D111, D132 |
| T11 | Karbon fiyatı tezde hiç ele alınmamış | D119, D132 |
| C1 | Ülkeler birbirinden bağımsız değil, ama hesap bağımsızlarmış gibi yapılmış | D046, D132 |
| C2 | Yöntemin anlatımı ile uygulaması birbirini tutmuyor | D008, D010, D043, D044, D135 |
| C3 | Poisson sonuçlarını büyük ölçüde tek ülke (Almanya) belirliyor | D032, D033, D065, D099 |
| C4 | Tablolardaki güven aralıkları bu veride güvenilir çalışmıyor | D009, D062, D064, D067, D071 |
| C5 | Hangi sonuç her sınamadan geçiyor? İkinci faz ve ikinci model evet, birinci faz hayır | D010, D063, D071 |
| C6 | Tablolardaki yıldızlar (anlamlılık işaretleri) biraz cömert | D046, D061, D062, D065, D073, D092, D094 |
| C7 | Yıl etkileri grafiği ve plasebo tablosu, tezin kendisinin “güvenilmez” dediği hesapla yapılmış | D043, D080, D081, D082, D084, D085, D104, D105 |
| C8 | Ticaret açıklığı sonucu abartılmış | D069 |
| C9 | Tezin kullandığı yöntem, hiçbir etki yokken de sık sık “etki var” diyor | D010, D046, D071, D132, D135 |
| M1 | “Ekonomi büyüdükçe patentler de aynı oranda artar” varsayımı veriye uymuyor | D034, D097, D098, D108 |
| M2 | Gecikme karşılaştırması anlatıldığı gibi yapılmamış | D054, D055 |
| M3 | Değişkenler arası ilişki tablosu yanlış soruya cevap veriyor | D027, D028, D029, D070 |
| M4 | Durağanlık testleri bölümünde etiket ve tutarlılık sorunları | D048, D049, D050, D053, D051, D052 |
| M5 | Yöntem için gösterilen kaynak eksik aktarılmış | D007, D031 |
| M6 | Patent sayılarının yuvarlama kuralı net yazılmamış | D016 |
| M7 | Negatif binom yönteminin bir varsayımı sağlanmıyor | D032, D047 |
| M8 | Veride sıfır yok diye özel bir model gerekmiyor | D018 |
| Y1 | “Sonuçlar hiçbir ülkeye bağlı değil” ifadesi fazla genel | D101, D102 |
| Y2 | Hipotez tablosu, kanıtın söylediğinden fazlasını söylüyor | D015, D107, D108 |
| Y3 | Üçüncü faz: “etki yok” demek ile “kanıt bulunamadı” demek aynı şey değil | D066, D067, D078, D115, D116 |
| Y4 | İki kaynak aktarımı doğrulanamadı | D056, D126, D127 |
| Y5 | “Yeşil inovasyon” aslında “yeşil patent başvurusu” olarak ölçülüyor | D017, D089, D092, D100, D131, D132 |
| Y6 | Küçük ifade ve tutarlılık hataları | D004, D005, D006, D019, D020, D021, D022, D025, D026, D040, D072, D075 |
| B1 | Belge biçimi: son nüshada düzeltilmesi gerekenler | D001, D002, D013, D020, D057, D058, D059, D060, D030, D035, D036, D088 |
| B2 | Atıf yazımı ve kaynakça biçimi | D003, D045, D135, D133, D134 |
