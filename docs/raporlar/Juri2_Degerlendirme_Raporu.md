# İkinci jüri ekibinin değerlendirme raporu

> **Kaynak notu:** Bu belge, kullanıcının 19.11.2026 tarihinde oturuma yüklediği `2nci_Juri_Degerlendirme_Raporu.docx` dosyasının metnidir; içeriğine dokunulmadan (yalnızca Markdown biçimine çevrilerek) arşivlenmiştir. Özgün dosya: `dokumanlar/Juri2_Degerlendirme_Raporu.docx`. Bu raporun madde madde, veriyle sınanmış değerlendirmesi: `analiz/Juri2_Raporu_Degerlendirmesi.md`.

Ekteki Beşinci Bölüm (Ekonometrik Analiz) metni ve AB14_nihai_veri.xlsx veri dosyası birlikte incelendiğinde; çalışmanın kuramsal çerçeve (Porter hipotezi ve yönlendirilmiş teknik değişim), ekonometrik modelleme stratejisi ve ampirik şeffaflık açısından doktora düzeyinde güçlü bir omurgaya sahip olduğu görülmektedir. Bununla birlikte, savunma jürisi perspektifinden hem nedensel tanımlama (identification) ve ekonometrik tutarlılık hem de veri sunumu ve yazım standartları bakımından giderilmesi gereken önemli metodolojik ve teknik noktalar bulunmaktadır.

## 1. Güçlü Yönler ve Özgün Katkılar

- **Veri Bütünlüğü ve Tam Tekrarlanabilirlik:** AB14_nihai_veri.xlsx dosyasındaki ham ve türetilmiş seriler üzerinden yapılan bağımsız doğrulamada; toplam başvuru sayısının (107.759), ülke paylarının (Almanya %45,3; Fransa %17,8), Tablo 5.2 tanımlayıcı istatistiklerinin, Tablo 5.4 korelasyon matrisinin, Tablo 5.6 ülke içi VIF değerlerinin ve Tablo 5.11–5.13'teki Negatif Binom (NB2) ile Poisson QML katsayılarının (α = 0,0178, LR = 669,77 vb.) virgülden sonraki hanelerine kadar birebir örtüştüğü teyit edilmiştir.

- **Doğru Tahminci ve Sabit Etki Tercihi:** Hausman, Hall ve Griliches (1984) koşullu sabit etkili negatif binom tahmincisinin gerçek birim sabit etkilerini kontrol etmediğine ilişkin Allison ve Waterman (2002) eleştirisinin dikkate alınarak ülke kuklalı koşulsuz sabit etkili NB2 ve dağılım varsayımına dayanıklı Poisson QML tahmincilerinin birlikte raporlanması yöntem bilimsel açıdan yerindedir.

- **Küçük Küme Sayısına Uygun Çıkarsama:** Küme sayısının az (N = 14) ve küme ağırlıklarının aşırı dengesiz olduğu panelde asimptotik kümelenmiş standart hatalar yerine ülke düzeyinde kümelenmiş 1000 tekrarlı eşli bootstrap ve sapma düzeltmeli (BC) güven aralıklarının kullanılması, birinci tip hata riskini başarıyla kontrol etmektedir.

- **Dinamik Ayrıştırma ve Sağlamlık Tasarımı:** Ortalama faz kuklalarının (Model 1) yanına segmentli kesintili zaman serisi tasarımının (Model 2) eklenmesi, Faz 1'deki etkinin kademeli eğim hızlanması, Faz 2'deki etkinin ise kalıcı düzey sıçraması biçiminde çalıştığını göstermektedir. Almanya'nın dışlanması, tek tek ülke dışlama testleri ve ETS öncesi plasebo kırılma testleri bulguların dayanıklılığını pekiştirmektedir.

## 2. Ekonometrik ve Yöntemsel Eleştiriler (Savunma Soruları)

Jüri değerlendirmesinde tezin savunulabilirliğini ve yayın potansiyelini doğrudan etkileyecek beş temel metodolojik eleştiri öne çıkmaktadır:

- **Yeşil Patent Stokunun Ardışık Dışsallığı ve 'Kötü Kontrol' (Mediation) Sorunu:** Sürekli envanter formülü gereği gecikmeli stok değişkeni, bağımlı değişkenin geçmiş değerlerinin doğrusal bir fonksiyonudur. Doğrusal olmayan sabit etkili Poisson QML ve NB2 tahmincilerinin tutarlılığı kesin dışsallık (strict exogeneity) varsayımına dayanır. Cari dönemdeki bir inovasyon şokunun gelecek dönemlerdeki stok değişkenine geri besleme yapması bu varsayımı mekanik olarak bozar. Ayrıca Faz 3'te ETS öncesi dönemin yaklaşık üç katına çıkan bilgi stokunu sabit tutarak Faz 3 kuklasını yorumlamak, Faz 3 katsayısını yapay biçimde aşağı çekmektedir. Başlangıç yılı öncesi bilgi stokuna dayanan ön-örneklem ortalaması (pre-sample mean) tahmincisinin ek sağlamlık testi olarak sunulması bu eleştiriyi karşılayacaktır.

- **Ortak Zaman Şokları, Karıştırıcı Politikalar ve Karbon Fiyatı Dinamiği:** Faz kuklaları tüm ülkeler için eşzamanlı tanımlandığından modelde yıl sabit etkileri kullanılamamaktadır. Faz 2 (2008–2012) AB 2020 Paketi ve kriz sonrası yeşil teşviklerle örtüşmektedir. Faz 3'te ise 2013-2017 arası EUA karbon fiyatlarının 3-8 €/ton bandına çökmesi, etkinin kaybolmasının temel iktisadi mekanizmasıdır ve tartışılmalıdır. Plasebo kontrol olarak yeşil olmayan (non-green) EPO patent başvurularının kullanılması nedensel iddiayı güçlendirecektir.

- **Maruziyet Kısıtı ve Aykırı Makroekonomik Gözlemler:** Tablo 5.14(b)'de reel GSYİH esnekliği serbest bırakıldığında katsayı 0,393 (NB) tahmin edilmiş ve birim esneklik kısıtı %1 düzeyinde reddedilmiştir. Özellikle İrlanda'nın 2015'teki %24,6'lık reel GSYİH sıçraması yeşil patent yoğunluğunu suni biçimde düşürmektedir. Kısıtsız modelin yalnızca ek test değil, ana bulgularla birlikte sunulması daha sağlıklıdır.

- **Panel Birim Kök ve Eşbütünleşme Analizindeki Yöntemsel Tutarsızlık:** Yatay kesit bağımlılığı (CD) testi ile bağımlılık tespit edilip ikinci nesil CIPS testine geçilmişken, hemen ardından birinci nesil Kao ve Pedroni eşbütünleşme testlerinin kullanılması yöntemsel bir çelişkidir. Üstel sayım modelinde değişkenlerin durağanlık derecelerinin uyumuna ilişkin daha tutarlı bir açıklama gerekmektedir.

- **Sıfır-Kesikli (Zero-Truncated) Sayım Dağılımı:** Örneklemde hiçbir sıfır patent başvurusu bulunmadığı belirtilmiştir. Gözlemlerin 1 değerine yaklaştığı ülkeler (Yunanistan, Portekiz vb.) bulunduğundan, bulguların sıfır-kesikli negatif binom (ZTNB) tahmincisine duyarlılığının kısa bir notla kontrol edilmesi teknik titizliği artıracaktır.

## 3. Veri Seti ve Metin İçi Tutarlılık Denetimi

Veri seti ve word metni karşılaştırıldığında tespit edilen ve baskı öncesinde düzeltilmesi gereken teknik hatalar aşağıda özetlenmiştir:

| Konu / Konum | Tespit Edilen Uyumsuzluk veya Eksiklik | Önerilen Düzeltme |
|---|---|---|
| Tablo 5.2 ve Tablo 5.3 Dönem Uyuşmazlığı | Tablo 5.2'de kontrol değişkenleri ve stok bir dönem gecikmeli (t-1) raporlanırken, Tablo 5.3'teki dönem ortalamaları cari (t) değerlerle hesaplanmıştır. | Tablo 5.3 başlığına 'Değişkenler cari dönem (t) değerleriyle raporlanmıştır' notu eklenmeli ya da t-1 ortalamaları verilmelidir. |
| Tablo Numarası Çapraz Referansı (5.6.4) | 5.6.4 bölümünün son cümlesinde VIF değerleri için (Tablo 5.5) ifadesine atıf yapılmış, ancak altındaki tablo Tablo 5.6 olarak numaralandırılmıştır. | Metin içindeki atıf (Tablo 5.6) olarak düzeltilmelidir. |
| Örneklem Başlangıç Yılı Gerekçesi (5.5) | Şekil 5.1'de seri 1990'dan başlatıldığı halde tahmin örnekleminin neden 1997'den başladığı yeterince açıklanmamıştır. | 1990–1995 yılları arasında Eurostat makro verilerinde 10–12 ülkeye ait eksik gözlem bulunduğu açıkça belirtilmelidir. |
| Parametre Kaynak Atıfları (5.4.4) | Sürekli envanter formülündeki eskime oranı (0,15) için kaynakçada yer alan Noailly & Smeets (2015) vd. çalışmalara metinde atıf yapılmamıştır. | Formülün hemen ardından ilgili kaynaklara metin içi atıf eklenmelidir. |
| Değişken Adı ve APA 7 Biçim Tutarlılığı | Aynı değişken tablolarda farklı adlandırılmış; metinde İngilizce '&' bağlacı, bitişik yazımlar ve kaynakçada mükerrer girdi mevcuttur. | Tüm tablolarda ortak adlar kullanılmalı, metin içi atıflarda 've' bağlacı ile boşluk kuralları (APA 7) standardize edilmelidir. |

Bu düzeltmelerin eklenmesiyle çalışma; yalnızca ampirik bulguları sağlam bir doktora tezi bölümü olmakla kalmayıp, doğrudan uluslararası dergilere gönderilebilecek olgunluğa ulaşacaktır.
