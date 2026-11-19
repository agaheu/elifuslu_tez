# Doktora tezi – Jüri değerlendirme raporu

> **Kaynak notu:** Bu belge, kullanıcının 19.11.2026 tarihinde oturuma ilettiği dış değerlendirme metnidir; içeriğine dokunulmadan (yalnızca Markdown biçimine çevrilerek) arşivlenmiştir. Bu değerlendirmenin madde madde analizi için bkz. `analiz/Kapsamli_Yeniden_Inceleme.md`, Kısım 8.

Tezi bir doktora jürisi üyesi gözüyle değerlendirdim. İncelemeyi hem Word belgesi hem de Excel veri seti üzerinden yaptım. Özellikle ekonometrik yöntemleri, model kurulumunu, veri güvenilirliğini, sonuçların yorumlanmasını ve bilimsel katkıyı dikkate aldım.

Öncelikle önemli bir kapsam notu: Yüklediğiniz Word belgesi tezin tamamı değil, 5. Bölüm (AB ETS'nin Yeşil İnovasyon Üzerindeki Etkisinin Ekonometrik Analizi) ve kaynakçasıdır. Dolayısıyla aşağıdaki değerlendirme esas olarak bu bölüm içindir. Tezin diğer bölümlerinin kuramsal bütünlüğü ve genel akademik katkısı hakkında henüz hüküm vermek mümkün değil.

## 1. Genel jüri kanaatim

**Olumlu potansiyel, ancak önemli düzeltme gerekli**

Çalışma, konu seçimi, veri hazırlığı ve ekonometrik yöntem çeşitliliği bakımından doktora düzeyinde ciddi bir emek içeriyor.

Bununla birlikte, AB ETS'nin patent faaliyetleri üzerindeki etkisini nedensel olarak tanımlama konusunda önemli sorunlar var. Ayrıca ana modelde kullanılan GSYİH maruziyet varsayımı, çalışmanın kendi alternatif tahmin sonuçlarıyla çelişiyor.

Ben jüri üyesi olsaydım bu haliyle koşulsuz kabul yönünde oy kullanmaz, önemli yöntemsel düzeltmeler talep ederdim.

Tezin temel araştırma sorusu anlamlıdır:

> AB Emisyon Ticaret Sistemi'nin farklı uygulama fazları yeşil inovasyonu nasıl etkilemiştir ve bu etkinin zaman içindeki değişimi nasıl açıklanabilir?

Bu soru hem çevre ekonomisi hem de inovasyon ekonomisi açısından doktora çalışmasına uygun.

Ancak bir doktora tezinde yalnızca uygun model kullanılması yeterli değildir. Kullanılan modelin araştırma sorusunu gerçekten cevaplayıp cevaplamadığı ve elde edilen sonuçların hangi koşullarda nedensel yorumlanabileceği de gösterilmelidir.

Bu ayrım, benim değerlendirmemde en önemli noktadır.

## 2. Çalışmanın güçlü yönleri

### A. Ekonometrik yöntem çeşitliliği

Çalışmanın en güçlü taraflarından biri yöntemsel altyapısı. Şu yöntemler kullanılmış:

- Poisson sözde en çok olabilirlik (QML).
- Negatif binom regresyon modeli.
- Ülke sabit etkileri.
- Segmentli kesintili zaman serisi (ITS).
- Kümelenmiş bootstrap.
- Panel birim kök testleri.
- Yatay kesit bağımlılığı testleri.
- Panel eşbütünleşme testleri.
- VIF analizi.
- Plasebo kırılma testleri.
- Ülkelerin tek tek dışlandığı sağlamlık testleri.

Bu yöntemlerin aynı araştırma sorusu etrafında bir araya getirilmesi ciddi bir metodolojik çaba gerektiriyor. Özellikle sayım verilerinin özellikleri dikkate alınarak Poisson ve negatif binom modellerinin tercih edilmesi yerinde. Negatif binom modelinin aşırı yayılım testleriyle desteklenmesi de doğru bir yaklaşım.

### B. Veri setinin hazırlanması

Excel dosyasını ayrıca kontrol ettim.

| Veri setinin doğrulanması | |
|---|---|
| Ülke | 14 |
| Analiz gözlemi | 336 |
| Analiz yılı | 24 |
| Stok hesabı için veri yılı | 31 |

Veri seti dengeli panel yapısında. 1997–2020 analiz döneminde temel değişkenlerde eksik veri yok. Ülke-yıl kayıtlarında mükerrer gözlem yok. Patent stokunun Excel formüllerinde belirgin hesaplama hatası yok.

Özellikle şu sonuçları yeniden hesapladım:

| Gösterge | Tezdeki değer | Excel kontrolü |
|---|---|---|
| Patent başvurusu ortalaması | 320,71 | 320,71 |
| Standart sapma | 559,86 | 559,86 |
| Minimum | 1 | 1 |
| Maksimum | 3.041 | 3.041 |
| Patent yoğunluğu ortalaması | 0,395 | 0,395 |
| Patent yoğunluğu standart sapması | 0,341 | 0,341 |

Fazlara göre patent yoğunluğu ortalamaları da doğrulanıyor:

| Dönem | Tezdeki ortalama |
|---|---|
| ETS öncesi | 0,22 |
| Faz 1 | 0,31 |
| Faz 2 | 0,51 |
| Faz 3 | 0,53 |

Gecikmeli kontrol değişkenlerinin tanımlayıcı istatistikleri de Excel verileriyle eşleşiyor. Bu, veri hazırlığının önemli ölçüde tutarlı olduğunu gösteriyor.

Ancak burada bir ayrım yapmalıyım: Excel üzerinden veri ve tanımlayıcı istatistikleri doğruladım. Stata do-file ve tahmin çıktıları verilmediği için regresyon katsayılarını bağımsız olarak yeniden tahmin etmedim.

### C. Sağlamlık analizleri

Almanya'nın örneklemden çıkarılması, her ülkenin tek tek dışlanması ve plasebo kırılma testleri olumlu özellikler. Almanya'nın patent başvurularının yaklaşık yüzde 45'ini oluşturduğu dikkate alındığında, bu ülkenin dışlandığı analiz özellikle önemli. Bu testlerin sonuçları erken iki fazdaki pozitif ilişkinin yalnızca Almanya'nın patent üretiminden kaynaklanmadığını destekliyor.

## 3. Jüri olarak temel eleştirilerim

Burada özellikle önemli bulduğum sorunları önem sırasına göre sıralıyorum.

### 1. En önemli sorun: Nedensellik ilişkisinin tanımlanması

*Çok önemli – Esaslı düzeltme*

Tezin temel iddiası AB ETS'nin yeşil inovasyonu artırdığıdır. Ancak ana modelde ciddi bir tanımlama problemi var.

14 ülkenin tamamında AB ETS fazları aynı tarihlerde başlamaktadır: 2005 (birinci faz), 2008 (ikinci faz), 2013 (üçüncü faz). Dolayısıyla politika değişkenleri ülkeler arasında farklılaşmıyor; yalnızca zaman içinde değişiyor.

Çalışmada ülke sabit etkileri kullanılıyor. Fakat bunlar ülkeler arasındaki zamanla değişmeyen farklılıkları kontrol eder. Aynı tarihlerde bütün ülkeleri etkileyen ortak şokları kontrol etmez.

Yazar, birinci modelde yıl sabit etkilerinin faz kuklalarıyla birlikte kullanılamayacağını doğru biçimde açıklıyor. Ancak devamında şu yaklaşımı benimsiyor:

> Ortak zaman değişimi, yeşil patent stoku ve zamanla değişen kontrol değişkenleri aracılığıyla kontrol edilmektedir.

Ben jüri üyesi olarak bu açıklamayı yeterli bulmam. Çünkü 2005–2020 arasında AB ekonomisinde ETS dışında da birçok gelişme gerçekleşmiştir:

- Yenilenebilir enerji politikalarındaki değişiklikler.
- Avrupa iklim ve enerji mevzuatındaki değişiklikler.
- Enerji fiyatlarındaki değişimler.
- 2008 küresel finans krizi.
- 2011 sonrası ekonomik gelişmeler.
- Teknolojik gelişmeler.
- 2020 pandemi etkisi.

Bunların tamamının beş kontrol değişkeni ve patent stoku ile yeterince kontrol edildiği gösterilmiş değil.

Yıl etkileri modeli de bu problemi tamamen çözmüyor. Çünkü o modeldeki yıllık katsayılar ortak zaman değişimlerini gösteriyor; bunların ETS'den mi yoksa aynı dönemdeki başka gelişmelerden mi kaynaklandığını tek başına söyleyemiyoruz.

**Jüri sorum:** AB ETS tüm ülkelerde aynı tarihte uygulanıyorsa, ETS'nin etkisini aynı dönemde gerçekleşen diğer Avrupa çapındaki ekonomik ve teknolojik gelişmelerden nasıl ayırıyorsunuz?

Bu soruya güçlü bir yanıt verilmesi gerekiyor. Önerim, mümkünse karşılaştırma grubu oluşturulması veya ETS'ye maruz kalma yoğunluğuna göre farklılaşan ülkeler/sektörler üzerinden bir tasarım geliştirilmesidir. Bu mümkün değilse çalışmanın nedensel iddiaları sınırlandırılmalı ve sonuçlar daha ihtiyatlı biçimde yorumlanmalıdır.

### 2. GSYİH maruziyet değişkeni konusunda ciddi tutarsızlık

*Çok önemli – Model spesifikasyonu*

Bence çalışmanın en dikkat çekici ekonometrik problemi budur.

Ana modelde GSYİH, maruziyet değişkeni (exposure) olarak kullanılıyor. Bu durumda logaritmik GSYİH'nin katsayısı 1'e sabitlenmektedir. Bu, patent sayısının GSYİH ile orantılı olarak artması varsayımını getiriyor.

Ancak yazar, bu kısıtın sonuçları etkileyip etkilemediğini kontrol etmek için alternatif model kurmuş. Sayfa 33'teki bulgu şöyle:

| Tahminci | Tahmin edilen GSYİH esnekliği |
|---|---|
| Negatif binom | 0,393 |
| Poisson QML | 0,371 |

Her iki modelde de GSYİH esnekliğinin 1'e eşit olduğu hipotezi yüzde 1 düzeyinde reddediliyor.

Burada önemli bir çelişki ortaya çıkıyor. Ana model GSYİH esnekliğinin 1 olduğunu varsayıyor. Alternatif model ise bu varsayımın verilerle desteklenmediğini gösteriyor. Yazar, faz katsayılarının birbirine yakın olmasını gerekçe göstererek ana modeli koruyor. Ben bu gerekçeyi yeterli bulmam. Çünkü faz katsayılarının benzer olması, ana modelin dayandığı ekonomik varsayımı geçerli hâle getirmez.

**Jüri talebim:** GSYİH katsayısının serbest bırakıldığı model ana model olarak değerlendirilmeli veya birim esneklik varsayımının neden teorik olarak gerekli olduğu çok daha güçlü biçimde savunulmalı.

Bu husus yalnızca teknik bir ayrıntı değildir. Bağımlı değişkenin hangi büyüklüğü temsil ettiğiyle doğrudan ilgilidir.

### 3. Yeşil patent stoku: Kontrol değişkeni mi, aracı değişken mi?

*Çok önemli – Ekonomik yorum*

Çalışma yeşil patent stokunu kullanarak doğrudan etki ve toplam etki ayrımına gidiyor. Mantık şu: patent stoku varken doğrudan etki; patent stoku yokken bilgi birikimi kanalı dahil toplam etki. Bu yaklaşımın ekonomik açıdan anlamlı bir tarafı var.

Ancak yeşil patent stoku geçmiş yıllardaki bağımlı değişkenin birikimli hâlidir. Dolayısıyla bu değişken aynı zamanda AB ETS'nin geçmiş dönemlerde etkilediği bir sonuçtur. Bu durumda stok değişkeni basit bir kontrol değişkeni olarak değerlendirilemez. Politikanın etkisini sonraki dönemlere taşıyan bir aracı değişken niteliğindedir.

Bir aracı değişkeni modele eklemek, politikanın toplam etkisinin bir kısmını modelden çıkarmak anlamına gelebilir. Bununla birlikte, stoklu ve stoksuz iki model arasındaki farkın doğrudan nedensel aracılık etkisi olarak yorumlanabilmesi için ilave varsayımlar ve analizler gerekir.

Ayrıca tezde patent stokunun Ar-Ge kapasitesini, araştırmacı sayısını ve kurumsal altyapıyı temsil ettiği belirtiliyor. Ancak patent stoku doğrudan bir Ar-Ge girdisi değildir. Birikmiş patent çıktısını ölçmektedir.

**Jüri sorum:** Patent stoku aynı zamanda bağımlı değişkenin geçmiş değerlerinden oluşuyorsa, bu değişkenin aracılık etkisini kontrol değişkeni etkisinden nasıl ayırıyorsunuz?

Burada daha açık bir ekonometrik ve teorik gerekçe beklerim. Ayrıca Ar-Ge harcamaları ve araştırmacı sayısı gibi değişkenlerin bulunması çalışmayı güçlendirebilir.

### 4. Yatay kesit bağımlılığı ve bootstrap yöntemi

*Önemli – İstatistiksel çıkarım*

Çalışmada Pesaran CD testi uygulanmış ve yedi değişkenin tamamında yatay kesit bağımsızlığı reddedilmiştir. Bu sonuç önemlidir. Çünkü AB ülkeleri ekonomik, teknolojik ve politik olarak birbirlerinden bağımsız değildir.

Buna rağmen ana tahminlerde ülke düzeyinde kümelenmiş standart hatalar ve ülke bazlı eşli bootstrap kullanılmıştır. Ülke düzeyinde kümelenme, aynı ülkenin zaman içindeki hata bağımlılığını dikkate alır. Ancak ülkeler arasındaki ortak şokları tek başına ortadan kaldırmaz. Ayrıca yalnızca 14 küme bulunmaktadır ve Almanya çok büyük bir ağırlığa sahiptir.

Burada başka bir metodolojik ayrıntı daha var: Tezde MacKinnon ve Webb (2017) çalışmasına atıf yapılmasına rağmen uygulanan yöntem, açıklanan prosedür itibarıyla wild cluster bootstrap değil, kümeleri yerine koyarak yeniden örnekleyen pairs cluster bootstrap yöntemidir. Bu iki yöntemin aynı şey olmadığı açıkça belirtilmelidir.

**Jüri talebim:** Küme sayısının azlığı ve yatay kesit bağımlılığı birlikte düşünülerek kullanılan bootstrap yönteminin küçük örneklem performansı gerekçelendirilmeli ve mümkünse alternatif sağlam çıkarım sonuçları sunulmalıdır.

### 5. Ülke örnekleminin seçimi

*Önemli – Örneklem tasarımı*

Çalışmada şu 14 ülke kullanılıyor: Almanya, Avusturya, Belçika, Danimarka, Finlandiya, Fransa, Hollanda, İrlanda, İspanya, İsveç, İtalya, Lüksemburg, Portekiz ve Yunanistan. Bu liste, eski AB-15 ülkelerinden Birleşik Krallık çıkarıldığında kalan ülkelerden oluşuyor.

Tezde Birleşik Krallık'ın 2020 yılında AB'den ayrılması nedeniyle çalışmaya dahil edilmediği belirtiliyor. Ancak burada önemli bir tarihsel sorun var. Birleşik Krallık 31 Ocak 2020'de AB'den ayrılmış olsa da geçiş dönemi boyunca AB mevzuatı uygulanmaya devam etmiş ve Birleşik Krallık 31 Aralık 2020'ye kadar AB ETS kapsamında kalmıştır. Avrupa Komisyonu bunu açıkça doğrulamaktadır.

Dolayısıyla Birleşik Krallık'ın bütün 1997–2020 gözlemlerinin yalnızca Brexit gerekçesiyle dışlanması yeterince ikna edici değil. Ayrıca 2004 ve sonrasında AB'ye katılan ülkelerin neden örneklem dışında bırakıldığı da açıklanmalı.

**Jüri sorum:** Neden 14 ülke? Örneklem seçiminin ekonomik, istatistiksel veya veri erişimi bakımından ölçütleri nelerdir? Birleşik Krallık dahil edildiğinde sonuçlar değişiyor mu?

### 6. Panel birim kök ve eşbütünleşme analizleri

Bu bölümde yöntemsel bir uyum sorunu görüyorum. Tezde önce Fisher-ADF ve IPS testleri, daha sonra yatay kesit bağımlılığı dikkate alınarak Pesaran CIPS testleri uygulanıyor. CIPS sonuçlarına göre bazı değişkenler düzeyde durağan, bazıları ise birinci farkında durağan. Örneğin yeşil patent yoğunluğu ve yeşil patent stoku CIPS testinde düzeyde durağan görünürken bazı kontrol değişkenleri birim kök içermektedir. Buna rağmen Kao ve Pedroni testleriyle eşbütünleşme analizi yapılıyor.

Burada iki sorun var:

1. Yatay kesit bağımlılığı belirgin olduğu hâlde kullanılan geleneksel birinci nesil eşbütünleşme testleri bu bağımlılığı yeterince hesaba katmıyor.
2. I(0) ve I(1) değişkenlerin birlikte yer aldığı yapıda geleneksel eşbütünleşme yaklaşımının yorumu ayrıca gerekçelendirilmeli.

Ayrıca doğrusal panel eşbütünleşme testlerinin sonuçları, negatif binom ve Poisson QML gibi doğrusal olmayan modellerin düzeyde tahmin edilmesinin geçerliliğini kendiliğinden kanıtlamaz. Bu bölüm yeniden gözden geçirilmeli.

### 7. Üçüncü faz sonuçlarının yorumlanması

| Gösterge | Faz 1 | Faz 2 | Faz 3 |
|---|---|---|---|
| Negatif binom doğrudan etki | %14,3 | %31,1 | %3,9 |
| Poisson QML doğrudan etki | %8,0 | %21,6 | Anlamsız |

İlk iki fazda olumlu ve anlamlı bir ilişki var. Üçüncü fazda ise patent stoku kontrol edildiğinde ek doğrudan etki saptanamıyor. Ancak üçüncü fazda VIF değeri 11,83. Patent stokuyla yüksek ortak hareket söz konusu. Üstelik üçüncü faz katsayısının güven aralığı da oldukça geniş. Dolayısıyla istatistiksel anlamlılığın bulunmaması, üçüncü fazın kesinlikle etkisiz olduğunu kanıtlamaz.

Daha doğru ifade şudur: *Üçüncü fazda, patent stokunun üzerinde ek bir doğrudan etki olduğuna ilişkin yeterli istatistiksel kanıt elde edilememiştir.*

Ayrıca stokun çıkarıldığı negatif binom modelinde üçüncü fazın toplam etkisi anlamlı çıkarken Poisson modelinde anlamlı çıkmamaktadır. Bu farklılık tartışılmalıdır.

## 4. Bulguların bilimsel değerlendirilmesi

Çalışmanın sonuçlarının ekonomik olarak ilginç olduğunu düşünüyorum.

- **Birinci faz:** Ani bir sıçrama yerine kademeli bir hızlanma gözleniyor. Bu durum patent başvurularının Ar-Ge süreçlerinin sonunda ortaya çıkmasıyla uyumlu.
- **İkinci faz:** En güçlü etki bu dönemde gözleniyor. Kurumsal kuralların netleşmesi ve emisyon izin arzının sıkılaşması üzerinden yapılan açıklama ekonomik açıdan makul.
- **Üçüncü faz:** Doğrudan etki zayıflıyor. Önceki dönemlerde oluşan bilgi stokunun patent faaliyetini sürdürdüğü yönündeki açıklama ilgi çekici; ancak henüz kesin bir nedensel aracılık sonucu olarak sunulmamalı.

Bence çalışmanın en değerli bilimsel bulgusu şudur: *AB ETS'nin yeşil patentleme üzerindeki ilişkisi bütün dönemlerde aynı değildir. İlk iki fazda daha belirgin olan etki, üçüncü fazda patent stoku kontrol edildiğinde zayıflamaktadır.* Bu, araştırmanın geliştirilmesi gereken ana bilimsel hikâyesidir.

Ancak patent başvuruları inovasyonun tamamı değildir. Patent sayısı buluş faaliyetini gösterir; patent kalitesini, ekonomik olarak uygulanmasını veya çevresel faydaya dönüşmesini doğrudan göstermez. Bu nedenle çalışmanın başlığında ve sonuçlarında "yeşil inovasyon" kavramının patentleme göstergesi üzerinden operasyonelleştirildiği açıkça belirtilmelidir.

## 5. Yazım ve biçim açısından değerlendirme

Genel sayfa düzeni ve bölüm organizasyonu iyi. Başlık hiyerarşisi, şekiller ve tablolar genel olarak okunabilir. Ancak son teslimden önce şu hususlar düzeltilmeli:

- Sayfa 18 ve 21'de sarı renkle vurgulanmış metinler var. Son tez nüshasında kaldırılmalı.
- Sayfa 26 ve 29'daki bazı tablolarda alt indis/gecikme gösterimlerinin yanında küçük boş kare karakterleri görünüyor. Bunlar düzeltilmeli.
- Bazı kaynak gösterimlerinde yazım biçimi tutarsız: Bel&Joseph, Allison andWaterman, Efron&Tibshirani gibi.
- Kaynakça biçimi tek bir akademik standarda göre düzenlenmeli.
- Tabloların bazıları oldukça yoğun. Özellikle bootstrap güven aralıkları ve model katsayıları daha rahat okunabilir şekilde sunulabilir.

Bunlar ana bilimsel problemler kadar önemli değil; fakat doktora tezinin nihai nüshasında bulunmamalı.

## 6. Savunmada adaya mutlaka soracağım sorular

1. **Nedensellik** — AB ETS 14 ülkede aynı tarihlerde uygulanıyorsa, elde edilen patent artışının ETS'den kaynaklandığını nasıl kanıtlıyorsunuz? ETS ile aynı dönemde uygulanan diğer AB politikalarını nasıl ayırıyorsunuz?
2. **GSYİH maruziyet varsayımı** — Ana modelde GSYİH esnekliğini 1'e sabitlemenize rağmen alternatif modelde bu değer 0,393 bulunmuş ve 1 hipotezi reddedilmiştir. Buna rağmen neden ana modelinizi değiştirmediniz?
3. **Patent stoku** — Yeşil patent stoku geçmiş patent başvurularından hesaplanıyorsa, bu değişkenin hem kontrol hem de aracı değişken olarak kullanılması ne ölçüde doğrudur?
4. **Ülke seçimi** — Birleşik Krallık 2020 sonuna kadar AB ETS kapsamında olduğu hâlde neden 1997–2020 döneminin tamamından dışlanmıştır?
5. **İstatistiksel çıkarım** — Yatay kesit bağımlılığı testlerinde ülkelerin bağımsız olmadığı görülmesine rağmen yalnızca ülke bazında bootstrap uygulanması neden yeterlidir?
6. **Üçüncü faz** — Üçüncü fazda anlamlı bir doğrudan etki bulamamanız, AB ETS'nin etkisini kaybettiğini mi gösteriyor, yoksa geçmiş yıllarda oluşan bilgi birikiminin etkisinin devam ettiğini mi gösteriyor? Bu iki açıklamayı nasıl ayırıyorsunuz?

Bu soruların özellikle ilk üçüne verilen yanıtlar, tezin bilimsel savunulabilirliğini belirleyecektir.

## 7. Nihai jüri değerlendirmem

| Değerlendirme alanı | Kanaatim |
|---|---|
| Araştırma konusu | Çok iyi |
| Bilimsel önem | Çok iyi |
| Kuramsal çerçeve | İyi |
| Veri hazırlığı | Çok iyi |
| Ekonometrik yöntem bilgisi | İyi – Çok iyi |
| Model spesifikasyonu | Önemli düzeltme gerekli |
| Nedensel tanımlama | Yetersiz |
| Sağlamlık analizleri | İyi |
| Bulguların yorumlanması | İyi, bazı aşırı yorumlar var |
| Akademik yazım | İyi |

**Jüri kararım: Önemli düzeltmeler gerekli**

Çalışmanın konusu, veri hazırlığı ve ekonometrik altyapısı doktora çalışması için yeterli bir potansiyel taşıyor. Ancak mevcut hâliyle AB ETS'nin yeşil inovasyon üzerindeki nedensel etkisinin yeterince tanımlandığını düşünmüyorum. Özellikle nedensel tanımlama, GSYİH maruziyet varsayımı ve patent stokunun ekonomik rolü konusunda esaslı düzeltmeler yapılmasını isterdim. Bu sorunlar giderildiğinde çalışma bilimsel açıdan çok daha güçlü ve savunulabilir hâle gelebilir.

### Son olarak kişisel kanaatim

Bu çalışma basit bir regresyon çalışması değil. Yazarın ciddi bir ekonometrik altyapı kurmaya çalıştığı belli. Özellikle veri setinin düzenlenmesi, farklı sayım modellerinin kullanılması ve sağlamlık analizleri olumlu.

Fakat doktora jürisinde benim için önemli olan, kullanılan yöntemlerin sayısı değil, yöntemlerin araştırma sorusuna ne kadar doğru cevap verdiğidir. Bu tezin en büyük riski, iyi hazırlanmış ekonometrik analizlerden elde edilen ilişkileri olduğundan daha güçlü nedensel sonuçlar olarak sunmasıdır.

Ben olsam yazardan öncelikle iki konuyu yeniden çalışmasını isterdim:

1. GSYİH esnekliği serbest bırakılmış modelin ana model olarak değerlendirilmesi.
2. Ortak zaman şokları ve kontrol grubu eksikliği nedeniyle nedensel etkinin hangi varsayımlar altında tanımlandığının yeniden ele alınması.

Bu iki husus çözülmeden tezin temel sonucunu kesin bir politika etkisi olarak kabul etmezdim.

Jüri açısından en önemli ayrımım şu: Çalışma doktora düzeyinde bir araştırma emeği ortaya koyuyor; fakat mevcut haliyle metodolojik olarak tamamlanmış bir nedensel etki analizi olduğunu söylemekte zorlanıyorum.
