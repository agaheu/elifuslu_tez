# AB ETS ve Yeşil İnovasyon — 5. Bölümün Kapsamlı Yeniden İncelemesi

**İncelenen belge:** `dokumanlar/Nihai_Model_19112026.docx` (Beşinci Bölüm ve kaynakça) · **Veri:** `veri/AB14_nihai_veri.xlsx` · **Tarih:** 19.11.2026

> Bu rapor, önceki iki aşamanın (ilk inceleme ve jüri raporu analizi) sonuçları dâhil **hiçbir şeyi doğru varsaymadan**, bölümün ve veri setinin baştan sona yeniden incelenmesidir. Bütün sayılar ham veriden yeniden hesaplanmış, rapordaki tablolar ve cümle içi sayılar doğrudan hesap çıktılarından üretilmiştir (`analiz/py/rapor_uret.py`). Önceki incelemede yanlış çıkan değerlendirmelerim Kısım 11'de açıkça listelenmiştir. **Güncelleme:** İkinci jüri ekibinin raporu ayrıca değerlendirilmiş (`analiz/Juri2_Raporu_Degerlendirmesi.md`), sonuçları bu rapora işlenmiştir (Kısım 9; T5, T11, M1, M8 bulguları).

## İçindekiler

1. Kapsam ve yöntem
2. Yönetici özeti
3. Yeniden üretim: tezdeki sayılar doğru mu?
4. Hipotezlerin yeniden değerlendirilmesi
5. Bulgular
6. Tasarımın Monte Carlo sınaması
7. Çıkarsama duyarlılığı tabloları
8. Birinci jüri raporunun analizi
9. İkinci jüri raporunun analizi
10. Bağımsız hakem okumasıyla karşılaştırma
11. Önceki incelememdeki düzeltmeler
12. Yapılacaklar
13. Tez bölümlerine göre bulgu haritası ve kaynakça denetimi
14. Dosyalar ve yeniden üretilebilirlik

## 1. Kapsam ve yöntem

**Neler yapıldı**

- Bölüm metni (1.109 satır), 17 tablo, 5 şekil ve kaynakça satır satır okundu; denklemler ve yöntem anlatımı kaynaklarıyla karşılaştırıldı.
- Veri seti baştan denetlendi (denge, mükerrer, eksik, iç tutarlılık, uç değerler, stok hesabı).
- Tezdeki bütün tahminler bağımsız yazılımla (Python; kendi yazdığım Poisson IRLS ve NB2 en çok olabilirlik tahmincileri) yeniden üretildi: Model 1, Model 2, üç sağlamlık tanımı, 14 ülke dışlama tahmini, yıl etkileri, plasebo testleri, gecikme seçimi, birim kök ve yatay kesit bağımlılığı testleri. Eşli küme bootstrap B = 1999 tekrarla (tezde 1.000) uygulandı; tekrarların tamamı yakınsadı.
- Tezde olmayan ek analizler yapıldı: dört çıkarsama yöntemiyle karşılaştırma, etkin küme sayısı, stoksuz ITS, eğilimli tanımlar, beklenti kuklası, faz bölmeleri, ön-örneklem ortalamalı tahmin, ülke heterojenliği, 896 tanımlı spesifikasyon eğrisi ve tasarımın Monte Carlo sınaması.
- Önceki incelemelere demirlenmemek için, hiçbir sonuç verilmeden ayrı bir bağımsız hakem okuması yaptırıldı (`dokumanlar/Bagimsiz_Hakem_Raporu.md`); oradaki her iddia ayrıca yeniden hesaplanarak sınandı.
- Kullanıcının ilettiği iki jüri değerlendirme raporu madde madde, veriyle karşılaştırıldı; ikinci jürinin önerdiği sınamalar (ön-örneklem ortalaması tahmincisi, sıfır-kesikli model, İrlanda etkisi) uygulandı.
- Literatüre ve kurumsal olgulara ilişkin dört ifade web kaynaklarından kontrol edildi.

**Neler yapılamadı (sınırlar)**

- **Ham verinin kaynağından doğrulanması yapılamadı.** Çalışma ortamından OECD, Eurostat ve Dünya Bankası sunucularına erişim kapalıydı. Veri setinin iç tutarlılığı tam; ancak değerlerin kaynaklardaki güncel değerlerle aynı olduğu bu incelemede teyit edilmedi.
- Birleşik Krallık'ın eklenmesi, Ar-Ge harcaması kontrolü, NAP sıkılığına dayalı maruziyet tasarımı ve yeşil patent payı gibi öneriler yeni veri gerektirdiği için sınanamadı.
- Stata do-dosyası ve log çıktısı elimde yok; karşılaştırma tezde basılı değerlerle yapıldı. Pedroni testi ve Kao'nun düzeltilmiş istatistikleri yeniden üretilmedi.
- Tezin diğer bölümleri görülmedi; değerlendirme yalnızca 5. Bölüm içindir.
- Bu bir ekonometrik inceleme; nihai akademik hüküm danışman ve jüriye aittir.

## 2. Yönetici özeti

**Hesaplar doğru, yorumlar fazla iddialı.** Tezde raporlanan ve karşılaştırılan 164 sayısal değerin tamamı (katsayılar, tanımlayıcı istatistikler, VIF ve korelasyonlar) bağımsız yazılımla birebir yeniden üretildi; bootstrap standart hataları tezdekilerden medyan %2, en çok %9 farklı (farklı rassal sayı üreteci ve tekrar sayısıyla beklenen düzey). Hesaplama ya da aktarım hatası bulunmadı. Sorunlar hesapta değil; tasarımın neyi tanımlayabildiğinde, çıkarsamanın dayanıklılığında ve hipotez tablosunun kanıttan ileri gitmesinde.

**Sağlam olan.** Ülke sabit etkili tanımların hepsinde (stok, kontroller, doğrusal eğilim nasıl tanımlanırsa tanımlansın) 2006–2010 arasında yeşil patent yoğunluğunda belirgin bir yükseliş var: Faz 1 boyunca eğim artışı, Faz 2 başında düzey farkı. Bu örüntü ülkelerin tek tek dışlanmasında, 896 alternatif tanımın neredeyse tamamında ve “gerçek etki sıfır” varsayımıyla üretilen benzetimlere karşı sınandığında da ayakta kalıyor (negatif binom Faz 2 için Monte Carlo p = <0,001–0,004; Model 2 Faz 2 düzeyi p = <0,001; Faz 1 eğimi p = 0,004–0,009). Faz 3'te stok kontrol edildiğinde ek bir fark yok.

**Sağlam olmayan.**

- **T1 — Kontrol grubu yok: faz kuklaları ortak zaman kuklasıdır.** 14 ülkenin tamamı aynı tarihlerde aynı fazlara giriyor; politika değişkeni yalnızca zaman içinde değişiyor ve yıl sabit etkileri konulamıyor.
- **T2 — “ETS öncesi eğilim yok” bulgusu (H5) stok değişkeninin yan ürünü.** Model 2'de ETS öncesi eğilim katsayısının sıfırdan farksız çıkması, yeşil patent yoğunluğunda eğilim olmadığını göstermiyor; eğilimin gecikmeli stok tarafından emildiğini gösteriyor.
- **T3 — H1'in kanıtı (“toplam etki %43,8 / %101,2 / %88,8”) eğilimle kirlenmiş.** H1 için gösterilen kanıt stoksuz (a) modelinin faz katsayıları.
- **C1 — Yatay kesit bağımlılığı bulunuyor, çıkarsama yalnızca ülke kümelemesine dayanıyor.** Tezin kendi CD testi yedi değişkenin tamamında yatay kesit bağımsızlığını reddediyor.
- **Faz 1 bulgusu kırılgan.** Poisson'da küme jackknife p = 0,228, boş hipotez benzetimlerinde p = 0,215–0,326; negatif binomda analitik yöntemlerle %5 düzeyinde anlamlı, benzetimlerde sınırda (p = 0,021–0,066).
- **Model 1'in faz katsayıları yukarı yanlı ve tezin çıkarsama yöntemi fazla sık reddediyor.** Gerçek etki sıfırken bile ortalama Faz 1 ≈ +0,03, Faz 2 ≈ +0,05 tahmin ediliyor ve tezin yöntemi %5 yerine %13–21 oranında “anlamlı” buluyor (T5, C9).
- **Tanıma duyarlılık.** Ülke heterojenliği sabit etkiler yerine ön-örneklem ortalamasıyla kontrol edildiğinde Model 1'in Faz 1 ve Faz 2 katsayıları sıfıra iniyor; Model 2'nin Faz 1 eğimi (0,111) ve Faz 2 düzeyi (0,380) ise bu tahmincide de anlamlı (T5).

**Genel değerlendirme.** Birinci jüri raporundaki “önemli düzeltme gerekli” yargısı bu incelemeyle örtüşüyor; ikinci jüri raporunun “düzeltmelerle uluslararası yayına hazır” yargısı ise fazla iyimser (Kısım 9). Bölüm, “AB ETS yeşil inovasyonu artırmıştır” biçimindeki nedensel iddiayı bu tasarımla taşıyamıyor; ama “AB ETS'nin ilk iki fazına denk gelen dönemde, öncesindeki eğilimin ve bilgi stokunun açıklayamadığı bir yükseliş vardır ve bu yükseliş üçüncü fazda sürmemiştir” biçimindeki betimleyici bulgu güçlü ve yeniden üretilebilir. Aşağıdaki düzeltmeler yapılırsa bölüm savunulabilir hâle gelir; düzeltmelerin çoğu yeni veri değil, yeniden yazım ve birkaç ek tablo gerektiriyor.

|  | Kritik | Önemli | Orta | Küçük | Toplam |
|---|---|---|---|---|---|
| Bulgu sayısı | 4 | 13 | 13 | 6 | 36 |

## 3. Yeniden üretim: tezdeki sayılar doğru mu?

### 3.1 Veri seti

| Kontrol | Sonuç |
|---|---|
| Yapı | 434 satır = 14 ülke × 31 yıl (1990–2020); tam dengeli; mükerrer ülke-yıl yok |
| Tahmin örneklemi (1997–2020) | 336 gözlem; hiçbir değişkende eksik değer yok |
| Eksik değerler | Yalnızca 1990–1995: reel GSYİH ve imalat payı 1990–1994, büyüme 1990–1995 (tahmini ve gecikmeleri etkilemiyor) |
| İç tutarlılık | Büyüme oranı, GSYİH düzeylerinden hesaplananla en çok 0,05 puan farklı (yuvarlama) |
| Stok | Sıfırdan yeniden hesaplanan stok Excel sayfasındakiyle aynı (fark < 10⁻⁹); g = 0,0691 |
| Yuvarlama | Kesirli sayımlar yarım değerde yukarı yuvarlanmış; tahmin örnekleminde 62 gözlem tam ,5 |
| Sıfır gözlem | Yalnız Portekiz 1990 (stok başlangıcı) |
| Uç değerler | En yüksek başvuru Almanya 2011 (3041); en yüksek yoğunluk Danimarka 2020 (2,118); en yüksek büyüme İrlanda 2015 (%24,6); en düşük ithalat bağımlılığı Danimarka 2005 |
| Kaynak doğrulaması | **Yapılamadı** (dış veri sunucularına erişim yok) |

### 3.2 Model 1 (Tablo 5.11)

| Değişken | NB tez | NB hesap | NB SH tez | NB SH hesap | Poisson tez | Poisson hesap | P. SH tez | P. SH hesap |
|---|---|---|---|---|---|---|---|---|
| Faz 1 (2005–2007) | 0,1338 | 0,1338 | 0,0580 | 0,0568 | 0,0772 | 0,0772 | 0,0383 | 0,0378 |
| Faz 2 (2008–2012) | 0,2705 | 0,2705 | 0,0842 | 0,0849 | 0,1954 | 0,1954 | 0,0651 | 0,0654 |
| Faz 3 (2013–2020) | 0,0381 | 0,0381 | 0,1264 | 0,1266 | −0,0926 | −0,0926 | 0,1048 | 0,1063 |
| ln(1+K₍t−1₎) | 0,6278 | 0,6278 | 0,0864 | 0,0894 | 0,6127 | 0,6127 | 0,0895 | 0,0913 |
| GSYİH büyümesi₍t−1₎ | 0,0029 | 0,0029 | 0,0056 | 0,0057 | 0,0029 | 0,0029 | 0,0049 | 0,0049 |
| Yenilenebilir payı₍t−1₎ | 0,0107 | 0,0107 | 0,0093 | 0,0093 | 0,0073 | 0,0073 | 0,0079 | 0,0081 |
| Enerji ithalat bağ.₍t−1₎ | 0,0022 | 0,0022 | 0,0026 | 0,0024 | 0,0029 | 0,0029 | 0,0032 | 0,0030 |
| İmalat payı₍t−1₎ | −0,0141 | −0,0141 | 0,0197 | 0,0205 | −0,0363 | −0,0363 | 0,0246 | 0,0241 |
| Ticaret açıklığı₍t−1₎ | −0,0049 | −0,0049 | 0,0025 | 0,0025 | −0,0014 | −0,0014 | 0,0026 | 0,0026 |

α = 0,0178 [0,0137; 0,0230] (tez 0,0178 [0,0137; 0,0230]); LR = 669,77 (tez 669,77).

### 3.3 Model 2 (Tablo 5.13)

| Değişken | NB tez | NB hesap | NB SH tez | NB SH hesap | Poisson tez | Poisson hesap | P. SH tez | P. SH hesap |
|---|---|---|---|---|---|---|---|---|
| ETS öncesi eğilim (t*) | −0,0068 | −0,0068 | 0,0164 | 0,0172 | −0,0225 | −0,0225 | 0,0206 | 0,0211 |
| Faz 1 düzey (λ₁) | 0,0434 | 0,0434 | 0,0727 | 0,0707 | 0,0396 | 0,0396 | 0,0442 | 0,0421 |
| Faz 1 eğim (φ₁) | 0,1107 | 0,1107 | 0,0324 | 0,0331 | 0,0867 | 0,0867 | 0,0250 | 0,0248 |
| Faz 2 düzey (λ₂) | 0,3525 | 0,3525 | 0,0924 | 0,0899 | 0,3232 | 0,3232 | 0,0697 | 0,0631 |
| Faz 2 eğim (φ₂) | −0,0204 | −0,0204 | 0,0235 | 0,0236 | −0,0220 | −0,0220 | 0,0188 | 0,0187 |
| Faz 3 düzey (λ₃) | 0,0721 | 0,0721 | 0,1726 | 0,1690 | −0,0007 | −0,0007 | 0,1317 | 0,1223 |
| Faz 3 eğim (φ₃) | 0,0134 | 0,0134 | 0,0158 | 0,0164 | 0,0211 | 0,0211 | 0,0143 | 0,0147 |
| ln(1+K₍t−1₎) | 0,6567 | 0,6567 | 0,1623 | 0,1676 | 0,7879 | 0,7879 | 0,1921 | 0,1985 |

α = 0,0161; LR = 564,59 (tez 0,0161; 564,59). Ortak testler (bootstrap kovaryansı, χ²(2)): NB 11,85 / 21,70 / 0,70 (tez 12,27 / 21,02 / 0,73); Poisson 17,39 / 31,90 / 2,06 (tez 15,39 / 28,23 / 2,22).

### 3.4 Diğer tablolar

| Tablo / değer | Durum | Not |
|---|---|---|
| Tablo 5.2 (36 değer) | ✓ birebir |  |
| Tablo 5.3 | ✓ birebir | Kontrol sütunları eşzamanlı (t) değerler; tabloda belirtilmemiş |
| Tablo 5.4 (15 korelasyon) | ✓ birebir | Ham korelasyonlar; ülke-içi değerler çok farklı (M3) |
| Tablo 5.6 (9 VIF) | ✓ birebir |  |
| Tablo 5.7 Fisher-ADF | ✓ birebir | Yoğunluk satırı logaritmayla (M4) |
| Tablo 5.7 IPS | ✓ ±0,2 | Momentler benzetimle üretildi |
| Tablo 5.9 CD ve CIPS | ✓ birebir (3 ondalık) | Stok CIPS: −2,775 (tez −2,771) |
| Tablo 5.10 Kao | ◐ iki düzeltilmemiş istatistik birebir | Düzeltilmiş istatistikler ve Pedroni yeniden üretilmedi |
| Tablo 5.14 (18 katsayı, 18 SH) | ✓ katsayılar birebir, SH ±%4 | Esneklik testi χ²: 10,56 / 16,28 (tez 10,78 / 15,92) |
| Tablo 5.15 (42 katsayı, 42 p) | ✓ katsayılar birebir, p ±0,02 | %5'te anlamlı Faz 1 sayısı: 7 (tez 7) |
| Tablo 5.16 (plasebo) | ✓ birebir | 2003 raporlanmamış (T6) |
| Yıl etkileri (Şekil 5.5) | ✓ birebir | 0,102 / 0,156 / 0,195 / 0,308; stok 0,810 |
| Gecikme seçimi AIC | ✓ birebir | İki gecikmeli model stoku da geciktiriyor (M2) |

## 4. Hipotezlerin yeniden değerlendirilmesi

|  | Hipotez | Tezin sonucu | Yeniden değerlendirme | Gerekçe |
|---|---|---|---|---|
| H1 | AB ETS, ETS öncesine göre yeşil patent yoğunluğunu artırmıştır | Desteklenmektedir | **Koşullu** | Ana modelde tek ETS kuklası pozitif ve anlamlı (0,26; ≈ %29,1). Ancak tasarım önce–sonra karşılaştırması; ETS öncesinden gelen eğilimden ve ortak şoklardan ayrıştırılamıyor. Tezin gösterdiği kanıt (“toplam etki”) eğilimle kirli (T1, T3). |
| H2 | Faz 1 pozitif etki yaratmıştır | Desteklenmektedir | **Kısmen** | Negatif binomda analitik yöntemlerin hepsinde %5 düzeyinde anlamlı (p = 0,018–0,042); ancak boş hipotez altındaki benzetimlerde tek yönlü p = 0,021–0,066 (sınırda). Poisson'da jackknife ile p = 0,228, benzetimle p = 0,215–0,326 (anlamsız); referans dönem 1997–2002 alındığında da anlamsız (C5, C9, T9). Daha sağlam kanıt Model 2'de: Faz 1 boyunca eğim artışı negatif binomda her sınamada anlamlı (benzetim p = 0,004–0,009). |
| H3 | Faz 2'nin etkisi Faz 1'den güçlüdür | Desteklenmektedir | **Destekleniyor** | δ₁ = δ₂ her iki tahmincide reddediliyor (bootstrap p = 0,012; 0,039); Faz 2 farkı negatif binomda her yöntemde, 896 tanımın neredeyse tamamında ve boş hipotez benzetimlerinde (p = <0,001–0,004; Model 2 düzeyi p = <0,001) anlamlı. Poisson'da daha zayıf: küme jackknife p = 0,068, benzetim p = 0,024–0,097. Kayıt: fark 2008–2010'da yoğunlaşıyor, faz boyunca korunmuyor (T7); ETS'ye atfı ayrı bir konu (T1). |
| H4 | Faz 3'ün etkisi Faz 2'den güçlüdür | Desteklenmemektedir | **Desteklenmiyor** | Tezle aynı sonuç: Faz 3 katsayısı her tanımda Faz 2'den küçük; δ₂ = δ₃ p < 0,001. |
| H5 | Fazların etkisi ETS öncesi eğilimden bağımsızdır | Desteklenmektedir | **Bu hâliyle desteklenmiyor** | “Eğilim yok” bulgusu stok kontrolünün yan ürünü; stoksuz tanımda anlamlı pozitif eğilim var (T2). Savunulabilir daraltılmış hâli: “Faz 1 eğim ve Faz 2 düzey farkları, ETS öncesi doğrusal eğilim kontrol edildiğinde de (stoklu ve stoksuz) anlamlıdır.” Faz 3 için geçerli değil. |

## 5. Bulgular

Her bulgu için: önem derecesi, tezdeki yeri (satır numaraları `dokumanlar/Nihai_Model_19112026_metin.md` dosyasına göre), hangi incelemede ortaya çıktığı, tespit, sayısal kanıt ve öneri. Etkileşimli, süzülebilir sürümü sitededir.

### 5.1 Tanımlama

#### T1 · Kontrol grubu yok: faz kuklaları ortak zaman kuklasıdır

**Önem:** kritik · **Yer:** 5.2, 5.6.3 (L125–127, L351, L761) · **Kaynak:** İlk inceleme, 1. jüri raporu, Bağımsız hakem, Yeniden inceleme, 2. jüri raporu · **Durum:** doğrulandı

**Tespit.** 14 ülkenin tamamı aynı tarihlerde aynı fazlara giriyor; politika değişkeni yalnızca zaman içinde değişiyor ve yıl sabit etkileri konulamıyor. Bu yapıda faz katsayıları, o yıllarda bütün ülkeleri birlikte etkileyen her şeyi (yalnızca AB ETS'yi değil) ölçer. Metindeki “ortak zaman değişimi stok ve kontrollerle kontrol edilmektedir” (L351) ve “etkiler AB ETS'den kaynaklanmaktadır” (L127, L761) ifadeleri bu tasarımın verebileceğinden fazlasını iddia ediyor. Fazların dışsal belirlenmesi (ters nedensellik yokluğu) tanımlama için yeterli değildir.

**Kanıt.** Aynı dönemlere denk gelen ortak gelişmeler: Kyoto Protokolü 1. taahhüt dönemi (2008–2012) Faz 2 ile birebir aynı yılları kapsıyor; 2004–2008 enerji fiyatı yükselişi (tez Popp, 2002'yi anıyor ama enerji fiyatı modelde yok); 2009/28/AT Yenilenebilir Enerji Direktifi; küresel düşük-karbon patent dalgası ve 2012 sonrası gerilemesi (Probst ve diğ., 2021). Tez, Faz 3'teki düşüşü “küresel eğilim”e (L801), Faz 1–2'deki yükselişi ise ETS'ye bağlıyor: asimetrik atıf. Monte Carlo sınaması (Kısım 6): gerçek etki sıfırken tezin çıkarsama yöntemi (eşli bootstrap SH, normal kritik değer) nominal %5 yerine %13–21 oranında “anlamlı etki” buluyor; ETS öncesi yıl etkilerinden kalibre edilen küçük bir ortak yıl şoku (std ≈ 0,038 log puan) eklendiğinde oran %17–23. Gerçek ortak şoklar bu kalibrasyondan büyükse oran daha da yükselir.

**Öneri.** (1) Bölüme “Sınırlılıklar” alt başlığı ekleyin ve nedensel dili daraltın: “AB ETS'nin etkisi” yerine “AB ETS dönemleriyle ilişkili fark”. (2) Ülkeler arası değişen bir maruziyet ölçüsüyle etkileşim tasarımı kurun: Faz 1–2'de üst sınırlar Ulusal Tahsis Planlarıyla (NAP) ülke bazında belirlendi; NAP sıkılığı ya da ETS kapsamındaki emisyon payı × faz etkileşimi, yıl sabit etkilerinin eklenmesine izin verir. (3) İkinci jürinin önerdiği plasebo sonuç sınamasını yapın: aynı modeli yeşil olmayan EPO başvurularıyla tahmin edin (ya da bağımlı değişken olarak yeşil patentlerin toplam EPO başvurularındaki payını kullanın); ortak patentleme eğilimlerini ayıklar. (4) Enerji fiyatı kontrolü ekleyin.

#### T2 · “ETS öncesi eğilim yok” bulgusu (H5) stok değişkeninin yan ürünü

**Önem:** kritik · **Yer:** 5.7.2 (L645), Tablo 5.13, Tablo 5.17 H5 · **Kaynak:** İlk inceleme, Bağımsız hakem, Yeniden inceleme · **Durum:** doğrulandı

**Tespit.** Model 2'de ETS öncesi eğilim katsayısının sıfırdan farksız çıkması, yeşil patent yoğunluğunda eğilim olmadığını göstermiyor; eğilimin gecikmeli stok tarafından emildiğini gösteriyor. Stok, geçmiş patentlerin birikimi olduğundan zamanla neredeyse eşdoğrusal. Eğilim katsayısının işareti tanıma göre değişiyor.

**Kanıt.** Ülke-içi korelasyon: ln(1+K₍t−1₎) ile zaman 0,95. Model 2'nin (tezde raporlanmayan) ülke-içi VIF değerleri: eğilim 42,8, Faz 3 düzey 25,4, stok 12,0. Eğilim katsayısı: stoklu Model 2'de −0,0225 (Poisson) / −0,0068 (NB); stoksuz Model 2'de 0,0354 / 0,0486 (bootstrap p = 0,007 / <0,001); yalnız 1997–2004 örnekleminde stoklu 0,057 / 0,059, stoksuz 0,077 / 0,073. Stoksuz yıl etkilerinde 1997 katsayısı −0,28 olup 2004'e kadar düzenli yükseliyor. Şekil 5.5'te ETS öncesi yedi katsayının tamamı pozitif ve sıfıra doğru azalıyor; bu “istikrarlı seyir” (L663) değil.

**Öneri.** Stoksuz Model 2'yi tabloya ekleyin. H5'i “stok kontrol edildiğinde” diye sınırlayın ya da kaldırın; eğilimden bağımsızlık iddiasını stoksuz ITS'deki Faz 1 eğim ve Faz 2 düzey katsayılarına dayandırın (bunlar stoksuz da anlamlı). Model 2 için de VIF raporlayın.

#### T3 · H1'in kanıtı (“toplam etki %43,8 / %101,2 / %88,8”) eğilimle kirlenmiş

**Önem:** kritik · **Yer:** 5.8.1 (a) (L695), Tablo 5.17 H1 (L772) · **Kaynak:** İlk inceleme, Bağımsız hakem, Yeniden inceleme · **Durum:** doğrulandı

**Tespit.** H1 için gösterilen kanıt stoksuz (a) modelinin faz katsayıları. Bu modelde ne stok ne de zaman eğilimi var; dolayısıyla faz kuklaları ETS öncesinden beri süren yükseliş eğilimini de taşıyor. H1 (stoksuz, eğilimsiz model) ile H5 (stoklu, eğilimli model) birbiriyle bağdaşmayan iki tanımdan destekleniyor.

**Kanıt.** Stoksuz Model 2'nin ETS öncesi eğilimi (NB: yılda 0,049) tek başına, dönem ortalarına uzatıldığında fazlar için 0,27 / 0,46 / 0,78 log puan üretiyor; raporlanan “toplam etki” katsayıları 0,36 / 0,70 / 0,64. Faz 3'ün “toplam etkisi” eğilimin öngördüğünün altında. Stoksuz modele doğrusal eğilim eklenince: Faz 1 0,188, Faz 2 0,420, Faz 3 0,178 (p = 0,175) (NB); Poisson'da 0,139 / 0,356 / 0,101 (p = 0,198). Stoksuz Poisson'da Faz 3 zaten anlamsız (0,2687; bootstrap p = 0,184).

**Öneri.** H1'i “ilk iki fazda” diye daraltın ya da ana modelde tek bir ETS kuklasıyla (2005–2020 = 1) doğrudan sınayın: katsayı 0,248 (Poisson) / 0,255 (NB), bootstrap SH 0,034 / 0,050. “Toplam etki” yüzdelerini H1 kanıtı olarak kullanmayın; kullanılacaksa eğilimli stoksuz modeli raporlayın.

#### T4 · “Doğrudan etki / stokla taşınan etki” ayrıştırması tanımlı değil

**Önem:** önemli · **Yer:** 5.6.4 (L371), 5.8.1, 5.10.3–5.10.4 · **Kaynak:** 1. jüri raporu, Bağımsız hakem, İlk inceleme, Yeniden inceleme, 2. jüri raporu · **Durum:** doğrulandı

**Tespit.** Stok geçmiş bağımlı değişkenin birikimi; ETS olmasaydı da büyüyecekti. Stoklu ve stoksuz model arasındaki farkı “ETS'nin bilgi birikimi yoluyla taşınan etkisi” olarak okumak nedensel aracılık varsayımları (ardışık yoksayılabilirlik) gerektirir; bunlar ne tartışılmış ne sınanmış. Ayrıca stok, metinde söylendiği gibi Ar-Ge girdisi değil, birikmiş çıktıdır (jüri notu). “Üçüncü fazdaki yüksek düzey önceki fazların bilgi birikimiyle sürüyor” sonucu bu veriyle “ETS'siz de sürecek eğilim” açıklamasından ayırt edilemiyor.

**Kanıt.** Ülke-içi korelasyonlar: Faz 3 kuklası ile stok 0,74, yenilenebilir enerji payı ile 0,79; Faz 3 VIF 11,83. Tez (L403) ortalama VIF'i (4,08) 10 eşiğiyle karşılaştırıyor; ortalama VIF için böyle bir eşik yorumu yok.

**Öneri.** “Nedensel aracılık” dilinden vazgeçin; stoklu ve stoksuz tahminleri “stok koşullu” ve “stok koşulsuz” ilişkiler olarak adlandırın. Ar-Ge harcaması/GSYİH (Eurostat rd_e_gerdtot) gibi gerçek bir girdi kontrolü eklemeyi deneyin.

#### T5 · Sabit etki + gecikmeli stok: Model 1'in faz katsayıları yukarı yanlı ve ön-örneklem tahmincisinde kayboluyor; Model 2'ninkiler korunuyor

**Önem:** önemli · **Yer:** 5.6.4 (L373) · **Kaynak:** Yeniden inceleme, Bağımsız hakem, 2. jüri raporu · **Durum:** yeni

**Tespit.** Stok, y₍t−1₎'i içeren bir gecikmeli bağımlı değişken birikimi. Ülke sabit etkileriyle birlikte kullanıldığında stok katsayısı aşağı, onunla ilişkili faz kuklaları yukarı yanlı olabilir (Nickell tipi sapma); sabit etkiler yerine ön-örneklem ortalaması kullanıldığında ise tersi beklenir. Tezdeki “sapma ihmal edilebilir” savunması (T = 24, stok ‘çok daha zayıf’ ilişkili) bir iddia; sınanmamış. İkinci jüri raporu aynı sorunu kesin dışsallık (strict exogeneity) ihlali olarak adlandırıyor ve ön-örneklem ortalaması tahmincisini öneriyor: ihlal tartışmasız, çünkü stok tanım gereği cari patentleri bir sonraki dönemin açıklayıcısına taşıyor (K₍t₎ = 0,85·K₍t−1₎ + y₍t₎).

**Kanıt.** Ülke kuklaları yerine 1990–1996 ortalama patent sayısı (Blundell, Griffith ve Windmeijer, 2002 tarzı ön-örneklem ortalaması) kullanıldığında: stok katsayısı 0,96 / 0,92'ye yükseliyor, Faz 1 0,004 / 0,003, Faz 2 0,025 / 0,017 (ikisi de anlamsız), Faz 3 −0,337 / −0,300. Yani faz etkisinin varlığı, ülke heterojenliğinin nasıl kontrol edildiğine bağlı. Ön-örneklem bilgisinin biçimine duyarlılık (ikinci jürinin önerisi üzerine altı varyant): ön-örneklem stoku ln K₁₉₉₆ ile sonuç aynı (Faz 1 0,005 / −0,000; Faz 2 0,026 / 0,009); tek bir ön-örneklem yoğunluğu değişkeniyle ise Faz 1 0,126 / 0,218, Faz 2 0,280 / 0,402. 14 ülkelik yatay kesitte bu tahminci kararsız. Buna karşılık Model 2 ön-örneklem tahmincisinde de ayakta: Faz 1 eğimi 0,103 (p = <0,001) / 0,111 (p = 0,013), Faz 2 düzeyi 0,356 (p = <0,001) / 0,380 (p = 0,003). Monte Carlo (Kısım 6): tezin kendi modeli doğru ve gerçek etki sıfır olsa bile sabit etkili tahminci stok katsayısını aşağı (gerçek 0,72 → ortalama 0,63), Model 1'in faz katsayılarını yukarı yanlı tahmin ediyor: Faz 1 +0,032, Faz 2 +0,046, Faz 3 +0,065 (NB). Veri sabit etkisiz stok modelinden geliyorsa yanlılık +0,047 / +0,077 / +0,117. Yani “sapma ihmal edilebilir” savı doğru değil. Ölçek: yanlılık Faz 2 tahminini (0,271) açıklamaya yetmiyor; Faz 1 tahmininin (0,134) dörtte biri ile üçte biri arasında; Faz 3 tahmininden (0,038) büyük. Model 2'nin eğim ve düzey katsayılarında yanlılık çok küçük (Faz 1 eğimi −0,003, Faz 2 düzeyi −0,006).

**Öneri.** İki tanımı birlikte raporlayın ve bulguları aralık olarak sunun (sabit etkili tahmin üst, ön-örneklem ortalamalı tahmin alt uç); yanlılığı benzetimle raporlayıp katsayıları buna göre yorumlayın; 5.6.4'teki Nickell paragrafını yeniden yazın. Blundell-Griffith-Windmeijer (2002) ve Blundell-Griffith-Van Reenen (1999) atıflarıyla tartışın. Bu, jürinin “stok kontrol mü aracı mı” sorusunun ekonometrik karşılığıdır.

#### T6 · Plasebo kırılma testleri seçici raporlanmış ve gücü düşük

**Önem:** önemli · **Yer:** 5.8.3, Tablo 5.16 (L745–761) · **Kaynak:** İlk inceleme, Bağımsız hakem, Yeniden inceleme · **Durum:** doğrulandı

**Tespit.** Tez 2000, 2001 ve 2002 için sahte kırılma raporluyor. Aynı yöntemle (ülke-kümeli SH) 2003 kırılması test edildiğinde ret çıkıyor. Ayrıca 112 gözlem, 14 küme ve ~22 parametreyle testin gücü, ana bulgu büyüklüğündeki bir etkiyi bile saptamaya yetmiyor. “Faz etkileri AB ETS'nin faaliyete geçtiği dönemle sınırlıdır” (L761) sonucu bu testlerden çıkmaz.

**Kanıt.** 2003 sahte kırılması: Poisson χ²(2) = 9,51 (p = 0,009), NB 5,45 (p = 0,066); bootstrap kovaryansıyla p = 0,129 / 0,128 (reddedilmiyor). 2003 sonrası eğim katsayısı negatif (−0,077): 2003–2004 eğilimin altında. Güç: plasebo eğim teriminin SH'si 0,028–0,070; %80 güçle saptanabilir en küçük eğim ≈ 0,08–0,20, oysa ana bulgu olan Faz 1 eğimi 0,087–0,111. Tezde raporlanan dört χ² değeri birebir yeniden üretildi.

**Öneri.** 1999–2003'ün tamamını raporlayın; plasebo ve ana tahminlerde aynı çıkarsama yöntemini kullanın; sonucu “kırılma kanıtı bulunamamıştır, ancak testin gücü sınırlıdır” diye yazın. 2003 sonucunu beklenti etkisi bağlamında tartışın.

#### T7 · Faz 2 etkisi “faz boyunca korunuyor” iddiası tezin kendi yıl etkileriyle çelişiyor

**Önem:** önemli · **Yer:** 5.7.2 (L647, L651), 5.10.2 (L793–795), Şekil 5.5 · **Kaynak:** Bağımsız hakem, Yeniden inceleme · **Durum:** yeni

**Tespit.** Model 2'de Faz 2 eğiminin anlamsız çıkması “ulaşılan düzey korunuyor” diye yorumlanmış. Yıl etkileri ise etkinin 2009'da zirve yapıp 2012'ye kadar sıfıra indiğini gösteriyor. Tartışma bölümündeki “kurumsal kesinlik” açıklaması (2009/29/AT'nin Nisan 2009'da kabulüyle kuralların kesinleşmesi) zamanlamayla uyuşmuyor: etki tam da kesinliğin sağlandığı tarihten sonra sönüyor; öncelik tarihli 2008–2009 başvuruları ise 2006–2008'in Ar-Ge kararlarını yansıtır.

**Kanıt.** Yıl katsayıları (Poisson, 2004 = 0): 2008 0,195, 2009 0,308, 2010 0,226, 2011 0,135, 2012 0,050 (son ikisi her yöntemde anlamsız). Faz 2 ikiye bölündüğünde: 2008–2009 katsayısı 0,208 / 0,290 (p = 0,001 / 0,001), 2010–2012 katsayısı 0,098 / 0,187 (p = 0,187 / 0,102). İkinci jüri raporu da Faz 2'yi “kalıcı düzey sıçraması” olarak niteliyor; yıl etkileri bu nitelemeyi desteklemiyor.

**Öneri.** “Korunmaktadır” ifadesini düzeltin: etki 2008–2010'da yoğunlaşıyor, sonra zayıflıyor. Tartışmada alternatif açıklamaları (2008 enerji fiyatı zirvesi, kriz öncesi Ar-Ge dalgası, Kyoto dönemi başlangıcı, kriz sonrası Ar-Ge kısıntısı) ele alın.

#### T8 · Örneklem gerekçesi hatalı: Birleşik Krallık 2020 sonuna kadar AB ETS içindeydi

**Önem:** önemli · **Yer:** 5.5 (L193) · **Kaynak:** 1. jüri raporu, Bağımsız hakem, İlk inceleme · **Durum:** doğrulandı

**Tespit.** Birleşik Krallık'ın “2020'de AB üyeliğinden çıktığı için” dışlandığı yazılmış. Oysa geçiş dönemi boyunca, 31.12.2020'ye kadar AB ETS'ye tabiydi (UK ETS 1.1.2021'de başladı); yani üç fazın tamamında katılımcıydı. Örneklem fiilen “AB-15 eksi Birleşik Krallık”; 2004 ve sonrasında üye olan ülkelerin neden dışlandığı da açıklanmamış.

**Kanıt.** Olgu web kaynaklarından teyit edildi (ICAP; Avrupa Komisyonu duyurusu). Veri setinde Birleşik Krallık yok; bu yüzden dahil edildiğinde sonuçların değişip değişmediği sınanamadı.

**Öneri.** Gerekçeyi düzeltin. Birleşik Krallık verisini (OECD, Eurostat/WDI) ekleyip 15 ülkeli tahmini sağlamlık testi olarak raporlayın. 2004 sonrası üyeler için dışlama ölçütünü yazın (ETS öncesi dönemde AB üyesi olmama, erken yıllarda sıfıra yakın EPO başvurusu vb.).

#### T9 · Referans dönem ve beklenti etkisi: 2003–2004 ayrıldığında Poisson Faz 1 anlamsızlaşıyor

**Önem:** orta · **Yer:** 5.2, 5.4.3 · **Kaynak:** İlk inceleme, Yeniden inceleme · **Durum:** yeni

**Tespit.** Direktif 2003/87/AT Ekim 2003'te kabul edildi (Yeşil Kitap 2000, Komisyon önerisi 2001). Referans dönemin son yılları beklenti etkisi taşıyabilir. İlk incelemede bunun etkileri aşağı yanlı yapacağını (tez lehine) varsaymıştım; veri tersini gösteriyor: 2003–2004 eğilimin altında kalıyor ve referans dönemi aşağı çekerek Faz 1 katsayısını büyütüyor.

**Kanıt.** 2003–2004 için ayrı kukla eklendiğinde (referans 1997–2002): kukla −0,070 / −0,030; Faz 1 0,044 (p = 0,267) Poisson, 0,121 (p = 0,067) NB; Faz 2 0,147 / 0,251 (p = 0,028 / 0,012).

**Öneri.** Referans dönem seçimine duyarlılığı raporlayın; Faz 1 bulgusunu buna göre ihtiyatla yorumlayın.

#### T10 · “Faz kuralları AB düzeyinde, ülkelerden bağımsız belirlendi” ifadesi Faz 1–2 için tam doğru değil

**Önem:** orta · **Yer:** 5.2 (L125), 5.10.2 (L793) · **Kaynak:** Bağımsız hakem · **Durum:** doğrulandı (orta güven)

**Tespit.** Faz 1 ve 2'de üst sınırlar ve tahsisler üye devletlerin Ulusal Tahsis Planlarıyla belirlendi (Komisyon onayıyla); AB çapında tek üst sınır Faz 3'te geldi. Dolayısıyla ilk iki fazın sıkılığı kısmen ülke kararıydı. Ayrıca “2020 yılına kadar geçerli olacak… doğrusal indirim faktörü” ifadesi yanıltıcı; faktörün 2020'de bitiş tarihi yoktu.

**Kanıt.** Tezin kendi atıf yaptığı Schleich ve diğ. (2009) NAP-II kesintilerini anlatıyor. Bu ayrıntı bir fırsat da sunuyor: ülkeler arası NAP sıkılığı farkı, T1'de önerilen maruziyet tasarımının değişkeni olabilir.

**Öneri.** İfadeyi düzeltin; dışsallık savını “faz takvimi” ile sınırlayın.

#### T11 · Karbon fiyatı ne modelde ne tartışmada var; “Faz 3'te etki fiyat çöktüğü için kayboldu” açıklaması sınanmalı

**Önem:** orta · **Yer:** 5.4.4, 5.10.2–5.10.3 · **Kaynak:** 2. jüri raporu, Yeniden inceleme · **Durum:** kısmen doğrulandı

**Tespit.** İkinci jüri raporu, 2013–2017'de izin (EUA) fiyatının 3–8 €/ton bandına gerilemesini Faz 3'te etkinin kaybolmasının “temel iktisadi mekanizması” olarak gösteriyor ve tartışılmasını istiyor. Fiyatın tartışılması gerektiği doğru: tezde karbon fiyatı değişken olarak da, tartışma konusu olarak da yok; oysa ETS'nin inovasyon teşviki fiyat üzerinden işler. Ancak “temel mekanizma” hükmü bu veriyle sınanmış değil ve tezin kendi yıl etkileriyle basit bir fiyat–inovasyon örtüşmesi görülmüyor.

**Kanıt.** Fiyat ve yıl etkilerinin (Poisson, 2004 = 0) yan yana okunması: (i) Faz 1 izinlerinin fiyatı 2007'de sıfıra yaklaştı (Ellerman ve Buchner, 2007; Ellerman ve diğ., 2010; ikisi de tezin kaynakçasında), yıl etkisi ise 2006–2007'de yükseliyor (0,102 → 0,156); (ii) fiyat 2008 ortasındaki ≈30 €'dan sonra ≈10–15 €'ya geriledi, yıl etkisi 2009'da zirve yapıyor (0,308); (iii) Avrupa Çevre Ajansı'na göre yıllık ortalama fiyat 2018'de 15,5 €, 2019'da 24,7 €; Faz 3 yıl etkileri 2020'ye kadar sıfırın altında ya da çevresinde (−0,186; −0,160; −0,104). Patentlerin fiyata gecikmeli tepki vermesi bu tabloyu kısmen açıklayabilir, ama fiyat kanalı kanıtlanmış değil. Yıllık EUA fiyat serisi veri setinde yok; doğrulanmış tam bir seri bu incelemede elde edilemedi, bu yüzden fiyat kontrollü tahmin yapılmadı.

**Öneri.** Gecikmeli yıllık ortalama EUA fiyatını modele ekleyin (faz kuklalarıyla birlikte faz içi fiyat değişiminden tanımlanır) ve sonucu raporlayın; 5.10'da fiyat dinamiğini tartışın, ancak Faz 3 için tek açıklama olarak sunmayın.

### 5.2 Çıkarsama

#### C1 · Yatay kesit bağımlılığı bulunuyor, çıkarsama yalnızca ülke kümelemesine dayanıyor

**Önem:** kritik · **Yer:** 5.6.5, 5.6.7 (Tablo 5.9) · **Kaynak:** İlk inceleme, 1. jüri raporu, Bağımsız hakem, Yeniden inceleme · **Durum:** doğrulandı

**Tespit.** Tezin kendi CD testi yedi değişkenin tamamında yatay kesit bağımsızlığını reddediyor. Ülke kümelemesi (ve ülke bazlı eşli bootstrap) ülke içi zaman korelasyonunu hesaba katar; aynı yılın ülkeler arası ortak şoklarını katmaz. Faz kuklaları yalnızca zaman boyutunda değiştiği için asıl belirsizlik tam da bu boyuttadır.

**Kanıt.** CD istatistikleri birebir yeniden üretildi (4,36–46,56). Ülke ve yıl için iki yönlü kümelemeyle Model 1: Poisson Faz 1 p = 0,069 (ülke kümeli 0,002), NB Faz 1 p = 0,042; Faz 2 p = 0,003 / 0,002. Uyarı: 14 × 24'lük panelde iki yönlü tahminci güvenilir değil: Monte Carlo'da boş hipotez altında %21–31 ret oranıyla sınanan yöntemlerin en kötüsü oldu ve tekrarların bir bölümünde pozitif tanımlı çıkmadı. İlk incelemedeki “iki yönlü kümelemeyle yeniden raporlayın” önerimi bu yüzden geri çekiyorum.

**Öneri.** Ana tabloya küme jackknife (CV3) ve parametrik bootstrap p değerlerini ekleyin; hangi bulguların her yöntemde ayakta kaldığını açıkça yazın (bkz. C5, C9). Ortak şoklar çıkarsamayla değil tasarımla ele alınmalı (T1).

#### C2 · Bootstrap gerekçesi ile uygulanan yöntem uyuşmuyor

**Önem:** önemli · **Yer:** 5.1.8 (L103), 5.6.5 (L407) · **Kaynak:** İlk inceleme, 1. jüri raporu, Bağımsız hakem · **Durum:** doğrulandı

**Tespit.** Kuramsal kısım wild küme bootstrap çalışmalarına (Cameron ve diğ., 2008; MacKinnon ve Webb, 2017) dayanıyor, uygulanan yöntem ise eşli (pairs) küme bootstrap standart hatası. Bu kaynaklar az kümede wild küme bootstrap-t'yi önerir; eşli bootstrap SH'sinin asimptotik iyileştirme sağlamadığını gösterir. “Küme büyüklüklerindeki farklılık” gerekçesi de yerinde değil: her kümede 24 gözlem var; farklı olan Almanya'nın sonuçtaki payı.

**Kanıt.** Bootstrap SH'leri yeniden üretildi (B = 1999): NB Faz 1 0,0568 (tez 0,0580), Faz 2 0,0849 (0,0842); Poisson 0,0378 (0,0383), 0,0654 (0,0651). Uygulama doğru, gerekçelendirme yanlış.

**Öneri.** 5.1.8'i uygulanan yönteme göre yeniden yazın; yöntemin az kümedeki sınırlarını belirtin; alternatif olarak küme jackknife (CV3; MacKinnon, Nielsen ve Webb, 2023) sonuçlarını ekleyin.

#### C3 · Etkin küme sayısı 4–5: Poisson tahminleri fiilen Almanya ağırlıklı

**Önem:** önemli · **Yer:** 5.6.5, 5.8.1 (c) · **Kaynak:** Yeniden inceleme · **Durum:** yeni

**Tespit.** Poisson tahmincisi gözlemleri beklenen patent sayısıyla ağırlıklandırır; NB ağırlıkları çok daha eşittir. Bu yüzden iki tahminci farklı sorulara cevap verir: Poisson “patent ağırlıklı (Almanya ağırlıklı) ortalama etki”, NB “ülkelerin daha eşit ağırlıklı ortalama etkisi”. Tezdeki Poisson–NB katsayı farkı bundan kaynaklanıyor; metinde açıklanmamış.

**Kanıt.** Almanya'nın örtük ağırlık payı: Poisson'da %45,3, NB'de %11,3. Carter-Schnepel-Steigerwald etkin küme sayısı (Poisson, Model 1): Faz 1 için 4,3, Faz 2 için 5,3 (nominal 14). Almanya çıkarılınca Poisson Faz 1 katsayısı 0,1323'e çıkıp NB'nin tam örneklem değerine (0,1338) eşitleniyor. Eşli bootstrap tekrarlarının %34'inde Almanya örneklemde hiç yok.

**Öneri.** İki tahmincinin neyi ağırlıklandırdığını metinde açıklayın; Poisson sonuçlarını “Almanya ağırlıklı” diye nitelendirin; ülke heterojenliğini (ülke × faz) bir ek tabloda gösterin.

#### C4 · Sapma düzeltmeli (BC) güven aralıkları bu veride kararsız

**Önem:** önemli · **Yer:** 5.1.8, Tablo 5.11–5.13 · **Kaynak:** İlk inceleme, Bağımsız hakem, Yeniden inceleme · **Durum:** doğrulandı

**Tespit.** Bootstrap dağılımları nokta tahmine göre belirgin biçimde kaymış (medyan sapması büyük). BC yöntemi bu kaymayı yüzdelikleri aşırı öteleyerek “düzeltiyor”; sonuçta aralıklar nokta tahmine göre çok asimetrik ve SH ile bağdaşmaz hâle geliyor. İlk incelemede yazım hatası sandığım enerji ithalat bağımlılığı aralığı bunun görünür belirtisi.

**Kanıt.** Poisson Faz 1: nokta tahmin 0,0772, bootstrap ortalaması 0,0975, z₀ = −0,47; “%95 BC aralığı” fiilen bootstrap dağılımının %0,2–%84,6 yüzdelikleri. Aynı katsayı için üç aralık: BC [0,013; 0,135], yüzdelik [0,036; 0,181], bootstrap-t [0,012; 0,118]. Stok katsayısında z₀ = 0,52. Enerji ithalat bağımlılığı (NB): katsayı 0,0022, bootstrap SH 0,0024, BC [−0,0000; 0,0192] (tez: [−0,0000; 0,0241]). Farklı tohumla (Monte Carlo hatası) BC sınırları: Faz 1 NB [0,049; 0,274].

**Öneri.** BC aralıklarını ana çıkarsama aracı yapmayın; yüzdelik ve bootstrap-t aralıklarını da verin ya da küme jackknife SH + t(13) kullanın. Tablo 5.12'de Faz 3 için “Anlamsız” yerine aralığı yazın.

#### C5 · Hangi bulgu hangi çıkarsama yönteminde ayakta kalıyor? Faz 2 ve Model 2 dayanıklı; Faz 1 kırılgan

**Önem:** önemli · **Yer:** Tablo 5.11, 5.13, 5.17 (H2, H3) · **Kaynak:** İlk inceleme, Yeniden inceleme · **Durum:** doğrulandı

**Tespit.** Tez tek bir çıkarsama yöntemi (eşli bootstrap SH + normal kritik değer) raporluyor. Dört analitik yöntem ve boş hipotez altındaki benzetim yan yana konduğunda tablo netleşiyor.

**Kanıt.** Model 1, p değerleri (ülke-küme t(13) | iki yönlü | küme jackknife CV3 | eşli bootstrap z): Poisson Faz 1 0,002 | 0,069 | 0,228 | 0,041; NB Faz 1 0,027 | 0,042 | 0,041 | 0,018; Poisson Faz 2 0,002 | 0,003 | 0,068 | 0,003; NB Faz 2 0,004 | 0,002 | 0,022 | 0,001. Model 2'nin iki ana bulgusu her yöntemde güçlü: Faz 1 eğimi CV3 p = 0,004 / 0,007, Faz 2 düzeyi <0,001 / 0,002. Parametrik bootstrap (gerçek etki sıfırken 1.000 benzetim × dört senaryo; tek yönlü p, en küçük–en büyük): Faz 1 Poisson 0,215–0,326, NB 0,021–0,066; Faz 2 Poisson 0,024–0,097, NB <0,001–0,004; Model 2 Faz 1 eğimi Poisson 0,048–0,115, NB 0,004–0,009; Faz 2 düzeyi Poisson <0,001–0,019, NB <0,001. Fazlar arası fark (δ₁ = δ₂): bootstrap Wald p = 0,012 / 0,039 (tez 0,013 / 0,037).

**Öneri.** Bu tabloyu teze ekleyin. H2 için “negatif binomda sınırda, Poisson'da anlamsız; çıkarsama yöntemine duyarlı” deyin; ana kanıtı Faz 2 ve Model 2 katsayılarına dayandırın.

#### C6 · Anlamlılık yıldızları normal dağılım kritik değerleriyle verilmiş; 14 kümede t(13) daha uygun

**Önem:** orta · **Yer:** Tablo 5.11, 5.13, 5.14 · **Kaynak:** Bağımsız hakem, Yeniden inceleme · **Durum:** doğrulandı

**Tespit.** Az kümede küme sayısı − 1 serbestlik dereceli t dağılımı standart öneridir. Sınırdaki sonuçların yıldızı değişiyor.

**Kanıt.** Bootstrap SH ile t(13): Poisson Faz 1 p = 0,062 (normal: 0,041); NB ticaret açıklığı p = 0,072 (normal: 0,049); NB Faz 1 p = 0,035.

**Öneri.** Yıldızları t(13) ile verin ya da tablo notunda kritik değer seçimini belirtin.

#### C7 · Yıl etkileri ve plasebo testlerinde, tezin kendisinin güvenilmez dediği asimptotik SH kullanılmış

**Önem:** orta · **Yer:** 5.6.5 (L407), 5.7.3 (L663), Şekil 5.5 · **Kaynak:** İlk inceleme, Bağımsız hakem, Yeniden inceleme · **Durum:** doğrulandı

**Tespit.** 5.1.8'de az kümede asimptotik kümelenmiş SH'nin güvenilmez olduğu söyleniyor; yıl etkileri ve plasebo testleri ise tam bu SH ile raporlanıyor. “Katsayılar 2006'dan itibaren anlamlı” ifadesi yönteme bağlı.

**Kanıt.** Yıl katsayılarının p değerleri (ülke-küme z | eşli bootstrap z): 2006 0,003 | 0,066; 2007 0,001 | 0,074; 2008 0,001 | 0,062; 2009 <0,001 | 0,021; 2010 0,003 | 0,146. Bootstrap SH ile %5 düzeyini yalnızca 2009 geçiyor (yüzdelik aralıklar 2006–2010 için sıfırı dışlıyor: yöntemler arasında yine tutarsızlık).

**Öneri.** Şekil 5.5 ve Tablo 5.16'yı ana tablolarla aynı çıkarsama yöntemiyle yeniden üretin ya da farkı gerekçelendirin.

#### C8 · Ticaret açıklığının “**” işareti savunulamıyor

**Önem:** orta · **Yer:** Tablo 5.11, 5.13 (L554, L595) · **Kaynak:** İlk inceleme, Bağımsız hakem · **Durum:** doğrulandı

**Tespit.** Tek anlamlı kontrol değişkeni olarak yorumlanan ticaret açıklığı (NB) sınırda.

**Kanıt.** z = −1,96, bootstrap p = 0,049; yüzdelik aralık [−0,0066; 0,0021] sıfırı içeriyor; küme jackknife p = 0,102; Poisson'da anlamsız (p = 0,585).

**Öneri.** “Sınırda anlamlı” deyin; L595'teki yorumu yumuşatın.

#### C9 · Tezin çıkarsama yöntemi, gerçek etki sıfırken nominal düzeyin üç-dört katı “anlamlı” sonuç üretiyor

**Önem:** önemli · **Yer:** 5.1.8, 5.6.5, Tablo 5.11–5.14 · **Kaynak:** Yeniden inceleme · **Durum:** yeni

**Tespit.** Tezin tasarımı ve çıkarsama yöntemi, etkinin sıfır olduğu bilinen yapay veriyle sınandı (stok her tekrarda üretilen patentlerden yeniden kuruldu). En elverişli durumda bile (veri tezin kendi modelinden geliyor, ortak şok yok) eşli bootstrap SH + normal kritik değer %5 yerine çok daha sık reddediyor. Nedeni iki katmanlı: Model 1'in faz katsayıları yukarı yanlı (T5) ve 14 küme / birkaç baskın ülke ile standart hatalar küçük kalıyor.

**Kanıt.** Boş hipotez altında ret oranları (300 benzetim, Model 1, üç faz katsayısı, iki tahminci): eşli bootstrap SH + z (tezin yöntemi) %13–21; ülke-küme t(13) %10–26; iki yönlü küme %21–31; küme jackknife CV3 + t(13) %8–12. Küçük ortak yıl şokuyla tezin yöntemi %17–23, jackknife %11–15. Sınananlar içinde nominal düzeye en yakın yöntem küme jackknife. İkinci jüri raporu bu yöntemin “birinci tip hata riskini başarıyla kontrol ettiğini” belirtiyor; benzetim sonuçları bu değerlendirmeyi desteklemiyor.

**Öneri.** Anlamlılık yargılarını küme jackknife + t(13) ve/veya parametrik bootstrap p değerleriyle verin; yıldızları buna göre güncelleyin. Tek yöntemle raporlanan sınırdaki sonuçları (Faz 1, ticaret açıklığı) “anlamlı” diye sunmayın.

### 5.3 Model

#### M1 · GSYİH maruziyet kısıtı veriyle reddediliyor; serbest esneklikli model daha iyi uyum veriyor

**Önem:** önemli · **Yer:** 5.6.2, 5.8.1 (b) (L697) · **Kaynak:** 1. jüri raporu, Bağımsız hakem, İlk inceleme, Yeniden inceleme, 2. jüri raporu · **Durum:** güncellendi

**Tespit.** Ana model ln GSYİH katsayısını 1'e sabitliyor; tezin kendi (b) modeli bu kısıtı reddediyor. İlk incelemede jürinin bu maddesini “abartılı” bulmuştum; yeniden değerlendirmede jürinin ilkesel olarak haklı olduğunu kabul ediyorum: kısıt bir normalizasyon olarak savunulabilir, ama veriyle reddedilen ve bilgi ölçütlerinin tercih etmediği bir tanımı “faz katsayıları yakın” gerekçesiyle ana model tutmak zayıf bir savunma. Öte yandan faz etkilerinin işareti ve anlamlılığı iki tanımda aynı; yani bu sorun bulguları değiştirmiyor, sunumu değiştiriyor.

**Kanıt.** Esneklik 0,371 (Poisson) / 0,393 (NB); H₀: esneklik = 1 için bootstrap χ² = 16,28 / 10,56 (tez 15,92 / 10,78). AIC: sabit 3.069,2 → serbest 3.058,6 (NB); 3.736,9 → 3.671,9 (Poisson); BIC de serbest modeli seçiyor. Faz katsayıları (NB): Faz 1 0,1338 → 0,1654 (%24 artış; “yakın” denmesi tartışılır), Faz 2 0,2705 → 0,2743, Faz 3 0,0381 → 0,0349. Uyarı: ln GSYİH ülke içinde stokla 0,77, zamanla 0,75 korelasyonlu; esneklik tahmini büyük ölçüde ortak eğilimden geliyor. İkinci jürinin işaret ettiği İrlanda etkisi sınandı: 2015'te reel GSYİH 218,3 → 272,1 milyar € (+%24,6). İrlanda çıkarıldığında faz katsayıları değişmiyor (NB 0,140 / 0,264; Poisson 0,076 / 0,191); İrlanda × 2015 sonrası kuklası anlamsız (0,085; p = 0,640); İrlanda'nın Poisson ağırlığı %0,8. Sorun ilkesel olarak doğru, sonuçlar için önemsiz.

**Öneri.** İki tanımı ana tabloda yan yana verin ya da serbest esneklikli modeli ana model yapıp hipotezleri “GSYİH'ye koşullu patent sayısı” üzerinden yazın. 5.6.2'de maruziyetin bir normalizasyon olduğunu, kısıtın reddedildiğini ve bulguların buna duyarsız olduğunu açıkça belirtin.

#### M2 · Gecikme seçimi karşılaştırması stoku da iki dönem geciktiriyor

**Önem:** orta · **Yer:** 5.6.9 (L523) · **Kaynak:** Bağımsız hakem, Yeniden inceleme · **Durum:** doğrulandı

**Tespit.** Metin “kontrol değişkenlerinin gecikme yapısı”nı karşılaştırdığını söylüyor; raporlanan iki gecikmeli AIC değeri ancak stok da iki dönem geciktirildiğinde elde ediliyor.

**Kanıt.** NB, 1998–2020, N = 322: bir gecikme AIC = 2.958,25 (tez 2958,25); stok dahil hepsi iki gecikme 2.999,78 (tez 2999,78); yalnız kontroller iki gecikme 2.966,65 (fark 41,5 değil 8,4). İki gecikmeli modelde faz katsayıları büyüyor (NB: 0,185 / 0,413 / 0,195).

**Öneri.** Karşılaştırmanın neyi içerdiğini doğru yazın; sonuç (bir gecikme tercih edilir) değişmiyor.

#### M3 · Tablo 5.4 ham korelasyonları veriyor; sabit etkili model için ilgili olan ülke-içi korelasyonlar çok daha yüksek

**Önem:** orta · **Yer:** 5.5.1 (L271), Tablo 5.4 · **Kaynak:** İlk inceleme, Bağımsız hakem, Yeniden inceleme · **Durum:** doğrulandı

**Tespit.** “Korelasyonlar 0,35'i aşmıyor, ciddi çoklu doğrusallık yok” sonucu havuzlanmış korelasyonlara dayanıyor. Model ülke-içi değişimden tahmin ediliyor.

**Kanıt.** Ülke-içi korelasyonlar: stok–yenilenebilir 0,81, stok–ticaret 0,64, stok–imalat −0,53. Ham korelasyonların en büyüğü 0,3510; yani “0,35'i aşmamaktadır” ifadesi de harfiyen doğru değil. Tablo 5.4'ün 15 değeri ve Tablo 5.6'nın 9 VIF değeri birebir yeniden üretildi.

**Öneri.** Tablo 5.4'ü ülke-içi korelasyonlarla verin (ya da iki panel); sonucu VIF tablosuyla tutarlı yazın.

#### M4 · Birim kök / eşbütünleşme bölümü: etiket, dönem ve yorum sorunları

**Önem:** orta · **Yer:** 5.6.7–5.6.8, Tablo 5.7–5.10 · **Kaynak:** 1. jüri raporu, Bağımsız hakem, Yeniden inceleme, 2. jüri raporu · **Durum:** doğrulandı

**Tespit.** (a) “Yeşil Patent Yoğunluğu” satırları aslında yoğunluğun logaritmasıyla hesaplanmış; düzeyle sonuçlar farklı ve CIPS sonucu tersine dönüyor. (b) Birim kök testleri 1996–2020, Kao testi 1997–2020 dönemiyle yapılmış; metinde belirtilmemiş. (c) CD bağımsızlığı reddederken Kao ve Pedroni bağımsızlık varsayıyor. (d) CIPS'e göre bağımlı değişken I(0), dört açıklayıcı I(1); “düzey tahmini her iki test grubunda da geçerli” (L519) sonucu buradan çıkmaz. (e) Pedroni'nin değiştirilmiş Phillips-Perron istatistiği +2,255; rho tipi istatistik sol kuyrukta reddeder, bu yüzden “üç istatistiğin tamamı reddediyor” ifadesi şüpheli (orta güven; Stata'nın p değeri kuralına bağlı). (f) Tablo 5.8 ticaret açıklığını trend durağan sayıyor, CIPS birim kök buluyor.

**Kanıt.** Log yoğunlukla: Fisher-ADF 22,94 (tez 22,94), CD 36,913 (36,913), CIPS −3,092 (−3,092). Düzey yoğunlukla: Fisher-ADF 15,65, CD 34,675, CIPS −2,091 (benzetimle p ≈ 0,13; %5 kritik değer ≈ −2,25: birim kök reddedilemiyor). Diğer altı değişkende Fisher-ADF, CD ve CIPS istatistikleri üç ondalığa kadar, IPS istatistikleri ±0,2 içinde yeniden üretildi. Kao'nun düzeltilmemiş iki istatistiği log yoğunluk ve 1997–2020 ile birebir çıkıyor (−18,260; −11,433). Pedroni ve Kao'nun düzeltilmiş istatistikleri yeniden üretilmedi.

**Öneri.** Satır etiketini “ln(yeşil patent yoğunluğu)” yapın; dönemleri yazın; bölümü kısaltıp eke alın ya da yatay kesit bağımlılığına dayanıklı bir test (Westerlund, 2007) ekleyin; Pedroni yorumunu kontrol edin; L519'daki genellemeyi çıkarın.

#### M5 · Koşulsuz sabit etkili NB için kaynak okuması eksik

**Önem:** küçük · **Yer:** 5.1.5, 5.6.1 (L331) · **Kaynak:** Yeniden inceleme · **Durum:** doğrulandı (orta güven)

**Tespit.** Allison ve Waterman (2002) katsayılarda tesadüfi parametre yanlılığı bulmuyor; ancak sonraki literatür (Allison'ın kendi kitabı; Greene, 2007; Guimarães, 2008) bu tahmincinin güven aralıklarının dar kaldığını ve yanlılık tartışmasının kapanmadığını belirtiyor. Tez bootstrap kullandığı için pratik etkisi sınırlı. Ayrıca sabit etkili Poisson'un dağılım varsayımına dayanıklılığı için doğru kaynak Wooldridge (1999); kaynakçada var, metinde yok.

**Kanıt.** Web kaynaklarından teyit (Statalist tartışmaları, Guimarães 2008 özeti).

**Öneri.** Bir cümleyle bu tartışmaya değinin; Wooldridge (1999) atfını ekleyin.

#### M6 · Kesirli sayımların yuvarlanması: sonuçları etkilemiyor, ifade netleştirilmeli

**Önem:** küçük · **Yer:** 5.4.1 (L149) · **Kaynak:** İlk inceleme, Yeniden inceleme · **Durum:** doğrulandı

**Tespit.** Metin “en yakın tam sayıya yuvarlandı” diyor; veri dosyası “0,5 yukarı yuvarlandı” diyor.

**Kanıt.** Tahmin örnekleminde tam yarım değerli 62 gözlem var. Yuvarlanmamış seriyle Poisson: 0,0774 / 0,1955 / −0,0927 (yuvarlanmış: 0,0772 / 0,1954 / −0,0926).

**Öneri.** Kuralı yazın ve sonuçların değişmediğini bir cümleyle belirtin.

#### M7 · Negatif binomun ortak aşırı yayılım varsayımı sağlanmıyor

**Önem:** orta · **Yer:** 5.1.4, 5.6.6 (L417) · **Kaynak:** Yeniden inceleme · **Durum:** yeni

**Tespit.** NB2 modeli tek bir α ile varyansı μ + αμ² olarak tanımlar. Veride yayılım ülkeden ülkeye çok farklı ve varyans ortalamayla NB2'nin öngördüğünden yavaş büyüyor. Bu, katsayıların tutarlılığını bozmaz; ama “negatif binom verinin yayılım yapısıyla uyumludur ve daha etkindir” (L417) gerekçesini ve α'ya dayalı LR testinin yorumunu zayıflatır.

**Kanıt.** Ülke bazında moment tahmini α (Model 1): Lüksemburg 0,257, Portekiz 0,080, Danimarka 0,037, Almanya 0,009, Fransa 0,006 (ortak tahmin 0,0178). Kalıntı varyansının logaritmasının beklenen değerin logaritmasına göre eğimi 1,29 (Poisson 1, büyük ortalamada NB2 2 öngörür).

**Öneri.** Bir cümleyle belirtin; ana tahminci gerekçesini etkinlik yerine “ülkelere daha eşit ağırlık verme” (C3) üzerine kurun ya da Poisson QML'i eş-ana tahminci olarak sunun.

#### M8 · Sıfır-kesikli (zero-truncated) model önerisi: kavramsal olarak gerekli değil; sınandı, sonuç değişmiyor

**Önem:** küçük · **Yer:** 5.4.1 (L153), 5.6.1 · **Kaynak:** 2. jüri raporu, Yeniden inceleme · **Durum:** sınandı — sorun yok

**Tespit.** İkinci jüri, örneklemde sıfır bulunmadığı için bulguların sıfır-kesikli negatif binoma duyarlılığının kontrol edilmesini öneriyor. Sıfır-kesikli modeller, sıfırın örnekleme tasarımı gereği gözlenemediği veriler içindir; burada sıfır gözlenebilir (Portekiz 1990'da sıfır), yalnızca tahmin döneminde gerçekleşmemiştir. Model de bunu olağan buluyor. Yine de öneri uygulandı.

**Kanıt.** Tahmin edilen modele göre beklenen sıfır sayısı 0,34 (Poisson) / 0,42 (NB); hiç sıfır gözlenmemesi şaşırtıcı değil. En küçük beklenen değer 2,9; 3 ve altında 12 gözlem var. Sıfır-kesikli Poisson: 0,0772 / 0,1954 / −0,0926 (olağan: 0,0772 / 0,1954 / −0,0926). Sıfır-kesikli NB: 0,1342 / 0,2709 / 0,0385 (olağan: 0,1338 / 0,2705 / 0,0381). Yunanistan ve Portekiz çıkarıldığında NB 0,119 / 0,277.

**Öneri.** Dipnotla belirtmek yeterli: “örneklemde sıfır yoktur; sıfır-kesikli tahminler katsayıları dördüncü ondalıkta değiştirmektedir.”

### 5.4 Yorum

#### Y1 · Ülke dışlama sonuçlarının yorumu fazla iddialı

**Önem:** önemli · **Yer:** 5.8.2 (L741), Tablo 5.15 · **Kaynak:** Bağımsız hakem, Yeniden inceleme · **Durum:** doğrulandı

**Tespit.** “Bulgular herhangi bir ülkenin örneklemde bulunmasına bağlı değildir” deniyor. Faz 2 için doğru; Faz 1 ve Faz 3 için değil.

**Kanıt.** Faz 1, 14 tahminin 7'sinde %5 düzeyinde anlamlı (Fransa çıkınca p = 0,127). Danimarka ya da Almanya çıkarıldığında Faz 2 katsayısı ≈0,07 büyüyor (0,270; 0,260) ve Faz 3'ün işareti pozitife dönüyor (0,032; 0,036). Tablo 5.15'in 42 katsayısı birebir, p değerleri ±0,02 içinde yeniden üretildi. “BC aralığı on üç tahminde sıfırı içermiyor” ifadesinin tabloda karşılığı yok.

**Öneri.** Cümleyi “Faz 2 bulgusu hiçbir ülkeye bağlı değildir; Faz 1 bulgusu Poisson'da ülke bileşimine duyarlıdır” diye değiştirin.

#### Y2 · Hipotez tablosu (Tablo 5.17) kanıtın taşıdığından fazlasını söylüyor

**Önem:** önemli · **Yer:** 5.9, Tablo 5.17 · **Kaynak:** İlk inceleme, Bağımsız hakem, Yeniden inceleme · **Durum:** doğrulandı

**Tespit.** H1 ve H5 bağdaşmayan tanımlardan destekleniyor (T2, T3); H2 Poisson'da çıkarsama yöntemine ve referans döneme duyarlı (C5, T9); H3 ve H4'ün sonuçları sağlam. Tüm hipotezler için “etki” sözcüğü önce–sonra tasarımının taşıyamayacağı bir nedensellik içeriyor.

**Kanıt.** H3: bootstrap Wald p = 0,039 (NB), 0,012 (Poisson). “İkinci fazın etkisi birincinin yaklaşık iki katı” NB için doğru (2,02 kat), Poisson için 2,53 kat. H4: δ₂ = δ₃ bootstrap p < 0,001; Faz 3 katsayısı her tanımda Faz 2'den küçük.

**Öneri.** Tabloyu Özet sayfasındaki yeniden değerlendirmeye göre güncelleyin: H1 koşullu, H2 kısmen, H3 destekleniyor, H4 desteklenmiyor, H5 bu hâliyle desteklenmiyor.

#### Y3 · Üçüncü faz: “etki yok” değil “kanıt yok”; stoksuz ITS'de Faz 3 eğimi negatif

**Önem:** orta · **Yer:** 5.7.1–5.7.2, 5.10.3 · **Kaynak:** 1. jüri raporu, İlk inceleme, Yeniden inceleme · **Durum:** doğrulandı

**Tespit.** Faz 3 kuklası stokla yüksek eşdoğrusal ve güven aralığı geniş; anlamsızlık etkisizlik kanıtı değil. “Önceki fazların bilgi birikimi düzeyi sürdürüyor” yorumunu zayıflatan bir bulgu da var.

**Kanıt.** Faz 3 (NB) %95 yüzdelik aralığı [−0,18; 0,31]: hem −%16 hem +%37 ile bağdaşıyor. Stoksuz Model 2'de Faz 3 eğimi Poisson'da −0,0249 (bootstrap p = 0,035), NB'de −0,0192 (p = 0,309).

**Öneri.** Jürinin önerdiği ifadeyi kullanın: “üçüncü fazda stokun üzerinde ek bir doğrudan etkiye ilişkin yeterli kanıt elde edilememiştir.” İki tahminci arasındaki farkı (C3) tartışın.

#### Y4 · Literatür aktarımlarında doğrulanamayan iki ifade

**Önem:** orta · **Yer:** 5.6.9 (L525), 5.10.5 (L811) · **Kaynak:** Yeniden inceleme, Bağımsız hakem · **Durum:** doğrulanamadı

**Tespit.** (a) “Pakes ve Griliches (1984) Ar-Ge ile patent arasındaki ortalama gecikmeyi yaklaşık 1,6 yıl bulmuştur”: birincil kaynakta bu rakam teyit edilemedi; kaynak, patentlerin Ar-Ge'ye hızlı tepki verdiğini ve geçmiş Ar-Ge'nin küçük ama kalıcı etkisini raporluyor. (b) “Bel ve Joseph'in (2018) ana modeli enerji teknolojilerine dayanırken bu çalışma iklim değişikliği azaltım teknolojilerinin tamamını kapsamaktadır”: makalenin özeti hem genel CCMT hem enerji patentlerini kullandığını ve 28 ülkeyi kapsadığını söylüyor; “katkı” ifadesi buna göre düzeltilmeli. “Rassal etkili model” nitelemesi de kaynaktan teyit edilemedi.

**Kanıt.** Web araması (NBER bölüm kaydı; Energy Policy 117, 434–444 özeti). Tam metinlere erişilemedi; bu yüzden hüküm değil, kontrol çağrısı.

**Öneri.** İki ifadeyi birincil kaynaktan kontrol edin; sayfa numarasıyla atıf verin ya da ifadeyi değiştirin.

#### Y5 · “Yeşil inovasyon” yalnızca EPO patent başvurusuyla ölçülüyor

**Önem:** orta · **Yer:** Başlık, 5.4.1, 5.10 · **Kaynak:** 1. jüri raporu · **Durum:** doğrulandı

**Tespit.** Patent başvurusu buluş faaliyetinin bir göstergesi; kaliteyi, uygulamayı ya da çevresel faydayı ölçmez. Öncelik tarihine göre son yılların (2018–2020) verisi çekim tarihine bağlı olarak eksik olabilir.

**Kanıt.** 2018–2020 çıkarıldığında bulgular güçleniyor (NB Faz 1 0,168, Faz 2 0,333); yani olası kesilme ana sonuçları yaratmıyor.

**Öneri.** Başlıkta/sonuçta operasyonel tanımı belirtin; OECD'nin son yıllara ilişkin uyarısına atıf yapın.

#### Y6 · Küçük ifade ve tutarlılık sorunları

**Önem:** küçük · **Yer:** çeşitli · **Kaynak:** İlk inceleme, Bağımsız hakem, Yeniden inceleme, 2. jüri raporu · **Durum:** doğrulandı

**Tespit.** Ayrı ayrı küçük, toplamda dikkat çeken ifade hataları.

**Kanıt.** • L645 “yıllık artış hızı … %11,7 yükselmiştir”: bu, yıllık büyüme oranına eklenen yüzde puandır. • L161 “en yüksek yoğunluk Danimarka, Almanya, Finlandiya, İsveç”: yalnız ETS dönemi için doğru; ETS öncesinde en yüksek Lüksemburg (0,517), muhtemelen başvuru sahibi ülkesine göre sayımın (holdingler) etkisi. • L179 g = 0,0691 ortalama log büyümedir (aritmetik ortalama 0,0769, bileşik 0,0716). • Tablo 5.3 kontrolleri eşzamanlı, Tablo 5.2 gecikmeli veriyor; ikisi de etiketsiz. • L173 “altı kontrol değişkeni” ↔ Tablo 5.5 “stok ve beş kontrol”. • L636 Poisson Faz 1 ortak testi: χ²(2) = 15,39 için p = 0,000 (0,001 değil). • L375 “Tablo 5.5” → Tablo 5.6. • L13 “bağımlı değişken yalnızca pozitif” (sayım verisi negatif olmayandır; log bağlantı ortalamayı pozitif tutar); L49 NB2 adı verilmemiş; L57 “daha etkin” ancak varyans fonksiyonu doğruysa. • δ = 0,15 ve başlangıç stoku formülü için metinde atıf yok (veri dosyasında var). • İrlanda'nın 2015 GSYİH sıçraması (%24,6) yoğunluğu mekanik düşürür; İrlanda hariç sonuç değişmiyor (0,140 / 0,264). • Tahmin döneminin neden 1997'de başladığı metinde yalnız dolaylı söyleniyor (L193): reel GSYİH 1995'ten, büyüme oranı 1996'dan itibaren 14 ülkenin tamamı için mevcut (1990–1995'te 10–12 ülke eksik); bir dönem gecikmeyle ilk kullanılabilir yıl 1997 (ikinci jüri notu; veriyle doğrulandı).

**Öneri.** Tek tek düzeltin.

### 5.5 Biçim

#### B1 · Belge yapısı ve biçim hataları

**Önem:** küçük · **Yer:** tüm bölüm · **Kaynak:** İlk inceleme, 1. jüri raporu, Bağımsız hakem, 2. jüri raporu · **Durum:** doğrulandı

**Tespit.** Son nüshada bulunmaması gereken biçim sorunları.

**Kanıt.** • L127'deki paragrafın tamamı Başlık 2 stilinde (içindekilere girer). • İki boş başlık paragrafı (L323, L783). • 5.8 “Sağlamlık Testleri” başlık stilinde değil. • Başlıkların bir kısmı kalın paragraf, bir kısmı gerçek başlık stili. • Denklemler (13)'ten sonra numarasız. • Üç yerde sarı vurgu kalmış (L351, L363, L403). • α sembolü üç anlamda: ülke sabit etkisi, aşırı yayılım parametresi, BC yüzdelik düzeyi. • Tablo 5.11/5.13'te alt indisler tabanı boş denklem nesnesi olarak girilmiş; Word bunu küçük kesikli kare olarak gösteriyor (jürinin gördüğü “boş kareler”). • Tablo 5.12 “Anlamsız” hücreleri; Tablo 5.13'te kontrol değişkenlerinin güven aralıkları boş. • Terim tutarsızlığı: “dış ticaret hacmi / dış ticaret açıklığı / ticaret açıklığı”.

**Öneri.** Word başlık stillerini tutarlı uygulayın; denklem numaralarını tamamlayın; sembolleri ayırın (sabit etki için c_i gibi).

### 5.6 Kaynakça

#### B2 · Atıf yazımı ve kaynakça biçimi

**Önem:** küçük · **Yer:** metin içi atıflar, KAYNAKÇA · **Kaynak:** İlk inceleme, 1. jüri raporu, Bağımsız hakem, Yeniden inceleme, 2. jüri raporu · **Durum:** doğrulandı

**Tespit.** Metin içi atıfların tamamının kaynakçada karşılığı var (programla eşleştirildi; eksik ya da yıl/yazar uyuşmazlığı yok). Sorun biçimde.

**Kanıt.** • Boşluk/bağlaç hataları: “Allison&Waterman”, “Allison andWaterman”, “Efron&Tibshirani”, “Bel&Joseph”, “Pakes&Griliches(1984)”, “Hausman ve diğ.(1984)”, “(OECD,2026)”, “Haščič ve Migotto 2015”. • Dechezleprêtre ve diğ. (2011) kaydı “&” ve tırnaklı başlıkla, OECD veri seti kaydı farklı bir atıf stiliyle yazılmış; OECD veri seti iki kez, iki farklı yılla (2024 / 2026) listelenmiş. • Wooldridge (1999) listede var, metinde kullanılmamış. • Stata 19 için kaynak kaydı yok. • L193'te 1990 başlangıcı için gösterilen kaynakların “veriler 1990'dan itibaren güvenilir” dediği kontrol edilmeli.

**Öneri.** Tez yazım kılavuzuna göre tek biçime getirin.

### 5.7 Doğrulanan (sorun bulunmayan) noktalar

- **Veri seti bütünlüğü.** 434 satır, 14 ülke × 31 yıl, tam dengeli; mükerrer yok; tahmin örnekleminde eksik değer yok; GSYİH büyüme oranı GSYİH düzeyleriyle tutarlı (en büyük fark 0,05 puan, yuvarlama); stok Excel formülleriyle aynı (fark < 10⁻⁹).
- **Tanımlayıcı tablolar.** Tablo 5.2 (36 değer), Tablo 5.3 (patent, yoğunluk, stok sütunları), Tablo 5.4 (15 korelasyon), Tablo 5.6 (9 VIF) birebir; metindeki toplam (107.759), paylar (%45,3; %17,8), medyan (142,5), çarpıklık (3,1), uç değerlerin ülke/yılları doğru.
- **Nokta tahminleri.** Tablo 5.11, 5.13, 5.14, 5.15'teki bütün katsayılar dört ondalığa kadar; α (0,0178; 0,0161) ve güven aralığı; LR (669,77; 564,59); AIC (2958,25; 2999,78); yıl etkileri (0,102; 0,156; 0,195; 0,308; stok 0,810); GSYİH esnekliği (0,371; 0,393).
- **Bootstrap ve testler.** Bootstrap standart hataları tezdekilerle çoğunlukla ±%4 içinde, en çok %10 farklı (farklı rassal sayı üreteci ve tekrar sayısı); Wald testleri: δ₁=δ₂ χ² = 4,26 (tez 4,33), δ₂=δ₃ 15,96 (15,34); Model 2 ortak testleri 11,85 / 21,70 / 0,70 (12,27 / 21,02 / 0,73); plasebo χ² değerleri birebir.
- **Birim kök ve yatay kesit bağımlılığı.** Fisher-ADF, CD ve CIPS istatistikleri üç ondalığa kadar (yoğunluk için logaritma kullanıldığı anlaşılınca); IPS ±0,2 içinde; Kao'nun düzeltilmemiş iki istatistiği birebir.
- **Denklemler ve aritmetik.** (1)–(13) numaralı denklemler, NB2 olasılık fonksiyonu ve varyansı, sınırdaki LR dağılımı, BC ve Wald formülleri doğru. Yüzde etkiler, olay hızı oranları, yıllık sapmalar (4,4 / 16,7 / 30,3 / 42,3), 1 + αμ ≈ 6,7 ve p değerleri (bir istisna dışında) doğru.
- **Atıf–kaynakça eşleşmesi.** Bölümdeki yaklaşık 40 farklı atfın tamamı kaynakçada bulunuyor; yazar/yıl uyuşmazlığı yok.
- **Sağlam kalan bulgu.** 896 farklı tanımın (tahminci × stok × maruziyet × kontroller × örneklem × gecikme × eğilim × eskime oranı) %99,9'inde Faz 2, %97,9'inde Faz 1 katsayısı pozitif ve %5 düzeyinde anlamlı (ülke-kümeli t(13)). Eskime oranı (0,05–0,25), son yılların çıkarılması, İrlanda/Lüksemburg/Almanya+Fransa dışlamaları sonucu değiştirmiyor. Uyarı: bu tanımların hepsi aynı önce–sonra tasarımını ve ülke sabit etkilerini paylaşıyor; T1 ve T5'teki sorunlara cevap vermiyor.

## 6. Tasarımın Monte Carlo sınaması

Soru: **AB ETS'nin gerçek etkisi sıfır olsaydı, tezin tahmincisi ve çıkarsama yöntemi ne bulurdu?** Bunu görmek için üç senaryoda yapay veri üretildi (`analiz/py/simulasyon.py`).

Her senaryoda 300 yapay veri seti üretildi; hepsinde gerçek faz etkisi sıfır. Stok, üretilen patentlerden yeniden kuruldu (δ = 0,15). Her veri setinde tezin Model 1'i tahmin edildi; eşli bootstrap için B = 199. Ortak yıl şokunun standart sapması (0,038 log puan; AR(1) ρ = 0,5), ETS öncesi yıl etkilerinin doğrusal eğilim etrafındaki sapmasından kalibre edildi.

**Yanlılık — gerçek etki 0 iken tahmin edilen faz katsayılarının ortalaması**

| Senaryo | Tahminci | Faz 1 | Faz 2 | Faz 3 | Stok katsayısı (ort.) |
|---|---|---|---|---|---|
| A — tezin kendi modeli (sabit etkili NB), etki = 0 | Poisson QML | 0,034 | 0,042 | 0,079 | 0,57 |
| A — tezin kendi modeli (sabit etkili NB), etki = 0 | Negatif binom | 0,028 | 0,045 | 0,067 | 0,63 |
| B — A + ortak yıl şoku | Poisson QML | 0,029 | 0,039 | 0,069 | 0,58 |
| B — A + ortak yıl şoku | Negatif binom | 0,032 | 0,049 | 0,072 | 0,63 |
| C — sabit etkisiz stok modeli, etki = 0 | Poisson QML | 0,034 | 0,063 | 0,116 | 0,63 |
| C — sabit etkisiz stok modeli, etki = 0 | Negatif binom | 0,053 | 0,084 | 0,127 | 0,68 |

**Boyut — gerçek etki 0 iken %5 düzeyinde “anlamlı” bulma oranı (ideal: %5)**

| Senaryo | Tahminci | Çıkarsama yöntemi | Faz 1 | Faz 2 | Faz 3 |
|---|---|---|---|---|---|
| A | Poisson QML | Ülke-küme t(13) | %22 | %21 | %26 |
| A | Poisson QML | İki yönlü küme | %31 | %25 | %31 |
| A | Poisson QML | Küme jackknife (CV3) | %9 | %10 | %12 |
| A | Poisson QML | Eşli bootstrap SH, z (tezin yöntemi) | %17 | %15 | %21 |
| A | Poisson QML | Eşli bootstrap SH, t(13) | %11 | %11 | %18 |
| A | Negatif binom | Ülke-küme t(13) | %10 | %17 | %18 |
| A | Negatif binom | İki yönlü küme | %21 | %24 | %23 |
| A | Negatif binom | Küme jackknife (CV3) | %8 | %10 | %9 |
| A | Negatif binom | Eşli bootstrap SH, z (tezin yöntemi) | %13 | %17 | %17 |
| A | Negatif binom | Eşli bootstrap SH, t(13) | %9 | %13 | %11 |
| B | Poisson QML | Ülke-küme t(13) | %30 | %27 | %31 |
| B | Poisson QML | İki yönlü küme | %32 | %27 | %29 |
| B | Poisson QML | Küme jackknife (CV3) | %15 | %11 | %14 |
| B | Poisson QML | Eşli bootstrap SH, z (tezin yöntemi) | %23 | %17 | %19 |
| B | Poisson QML | Eşli bootstrap SH, t(13) | %19 | %14 | %14 |
| B | Negatif binom | Ülke-küme t(13) | %17 | %21 | %19 |
| B | Negatif binom | İki yönlü küme | %21 | %24 | %24 |
| B | Negatif binom | Küme jackknife (CV3) | %15 | %14 | %13 |
| B | Negatif binom | Eşli bootstrap SH, z (tezin yöntemi) | %20 | %22 | %19 |
| B | Negatif binom | Eşli bootstrap SH, t(13) | %18 | %16 | %15 |
| C | Poisson QML | Ülke-küme t(13) | %24 | %24 | %26 |
| C | Poisson QML | İki yönlü küme | %27 | %31 | %33 |
| C | Poisson QML | Küme jackknife (CV3) | %10 | %11 | %12 |
| C | Poisson QML | Eşli bootstrap SH, z (tezin yöntemi) | %18 | %15 | %20 |
| C | Poisson QML | Eşli bootstrap SH, t(13) | %13 | %12 | %14 |
| C | Negatif binom | Ülke-küme t(13) | %15 | %20 | %25 |
| C | Negatif binom | İki yönlü küme | %27 | %30 | %31 |
| C | Negatif binom | Küme jackknife (CV3) | %13 | %16 | %19 |
| C | Negatif binom | Eşli bootstrap SH, z (tezin yöntemi) | %17 | %20 | %26 |
| C | Negatif binom | Eşli bootstrap SH, t(13) | %15 | %18 | %22 |

**Parametrik bootstrap — tezin gözlenen katsayıları “sıfır etki” dağılımının neresinde?**

Her senaryoda 1000 benzetim. Senaryo A2, A'nın ülkeye özgü aşırı yayılımlı hâlidir (M7). “Sıfır etki ort.” sütunu yanlılığı, p sütunu gözlenen değerin aşılma olasılığını (tek yönlü) verir.

| Katsayı | Tahminci | Tezdeki değer | A: ort. (p) | A2: ort. (p) | B: ort. (p) | C: ort. (p) |
|---|---|---|---|---|---|---|
| M1 Faz 1 | Negatif binom | 0,134 | 0,032 (0,027) | 0,038 (0,021) | 0,040 (0,061) | 0,047 (0,066) |
| M1 Faz 1 | Poisson QML | 0,077 | 0,025 (0,232) | 0,025 (0,215) | 0,027 (0,259) | 0,029 (0,326) |
| M1 Faz 2 | Negatif binom | 0,271 | 0,046 (<0,001) | 0,057 (<0,001) | 0,061 (0,002) | 0,077 (0,004) |
| M1 Faz 2 | Poisson QML | 0,195 | 0,034 (0,030) | 0,036 (0,024) | 0,040 (0,055) | 0,051 (0,097) |
| M1 Faz 3 | Negatif binom | 0,038 | 0,065 (0,638) | 0,082 (0,698) | 0,086 (0,674) | 0,117 (0,782) |
| M1 Faz 3 | Poisson QML | −0,093 | 0,059 (0,883) | 0,061 (0,916) | 0,066 (0,882) | 0,099 (0,884) |
| M2 ETS öncesi eğilim | Negatif binom | −0,007 | 0,012 (0,936) | 0,014 (0,969) | 0,014 (0,936) | 0,018 (0,958) |
| M2 ETS öncesi eğilim | Poisson QML | −0,022 | 0,019 (0,980) | 0,018 (0,992) | 0,018 (0,983) | 0,023 (0,979) |
| M2 Faz 1 eğim | Negatif binom | 0,111 | −0,003 (0,004) | −0,001 (0,004) | −0,005 (0,007) | 0,000 (0,009) |
| M2 Faz 1 eğim | Poisson QML | 0,087 | −0,009 (0,062) | −0,008 (0,048) | −0,009 (0,063) | −0,006 (0,115) |
| M2 Faz 2 düzey | Negatif binom | 0,352 | −0,006 (<0,001) | −0,004 (<0,001) | −0,001 (<0,001) | 0,009 (<0,001) |
| M2 Faz 2 düzey | Poisson QML | 0,323 | −0,036 (<0,001) | −0,027 (0,001) | −0,022 (0,008) | −0,012 (0,019) |
| M2 Faz 3 eğim | Negatif binom | 0,013 | −0,005 (0,089) | −0,006 (0,070) | −0,006 (0,128) | −0,003 (0,139) |
| M2 Faz 3 eğim | Poisson QML | 0,021 | −0,008 (0,085) | −0,007 (0,068) | −0,007 (0,087) | −0,001 (0,181) |

**Ne öğreniyoruz?**

1. **Model 1'in faz katsayıları yukarı yanlı.** Veri tezin kendi modelinden gelse ve gerçek etki sıfır olsa bile, sabit etkili tahminci stok katsayısını küçük tahmin ediyor (gerçek 0,72; ortalama tahmin 0,63) ve aradaki farkı faz kuklalarına yüklüyor: negatif binomda ortalama Faz 1 +0,032, Faz 2 +0,046, Faz 3 +0,065. Tezdeki “Nickell sapması ihmal edilebilir” savı (L373) bu yüzden doğru değil. Karşılaştırma: tezin tahminleri 0,134 / 0,271 / 0,038. Yanlılık Faz 2'yi açıklamıyor, Faz 1'in dörtte biri kadar, Faz 3 tahmininden büyük.
2. **Model 2'nin katsayıları neredeyse yansız.** Aynı benzetimlerde Faz 1 eğiminin ortalaması −0,003, Faz 2 düzeyinin −0,006. Kesintili zaman serisi tanımı bu açıdan Model 1'den daha güvenilir.
3. **Tezin çıkarsama yöntemi fazla sık “anlamlı” buluyor.** Eşli bootstrap SH + normal kritik değer, gerçek etki sıfırken %5 yerine %13–21 oranında reddediyor; küçük bir ortak yıl şokuyla %17–23. Sınanan yöntemler içinde nominal düzeye en yakını küme jackknife (%8–12); **en kötüsü iki yönlü kümeleme** (%21–31). İlk incelemede önerdiğim iki yönlü kümeleme bu boyuttaki bir panelde çözüm değil.
4. **Hangi bulgu “sıfır etki” dünyasında nadir?** Tezin gözlenen katsayılarının boş hipotez altındaki dağılımda aşılma olasılığı (tek yönlü Monte Carlo p, dört senaryonun en küçüğü–en büyüğü): negatif binom Faz 2 <0,001–0,004, Model 2 Faz 2 düzeyi <0,001, Model 2 Faz 1 eğimi 0,004–0,009: bunlar yanlılık ve örnekleme gürültüsüyle açıklanamıyor. Negatif binom Faz 1 0,021–0,066: sınırda. Poisson Faz 1 0,215–0,326: sıfır etkiyle tamamen uyumlu. Poisson Faz 2 0,024–0,097.

**Sınırlar.** Benzetimler tezin model ailesi içinde kurulmuştur; boş hipotez senaryoları yalnızca *küçük* (ETS öncesi dalgalanmadan kalibre) ortak şok içerir. Kyoto dönemi ya da enerji fiyatı gibi büyük ve kalıcı ortak şoklar (T1) bu sınamanın dışındadır: buradaki “anlamlı” sözcüğü “tahminci yanlılığı ve örnekleme gürültüsüyle açıklanamıyor” demektir, “AB ETS'den kaynaklanıyor” demek değildir. Negatif binom üretim süreci ortak ya da ülkeye özgü aşırı yayılım varsayar; gerçek hata yapısı (seri korelasyon dâhil) farklıysa oranlar değişir.

## 7. Çıkarsama duyarlılığı tabloları

### Model 1: p değerleri

| Tahminci | Katsayı | b | Ülke-küme t(13) | İki yönlü | Jackknife CV3 | Bootstrap z (tez) | Bootstrap t(13) | %95 yüzdelik | %95 BC |
|---|---|---|---|---|---|---|---|---|---|
| Negatif binom | Faz 1 (2005–2007) | 0,1338 | 0,027 | 0,042 | 0,041 | 0,018 | 0,035 | [0,042; 0,270] | [0,050; 0,282] |
| Negatif binom | Faz 2 (2008–2012) | 0,2705 | 0,004 | 0,002 | 0,022 | 0,001 | 0,007 | [0,123; 0,452] | [0,110; 0,439] |
| Negatif binom | Faz 3 (2013–2020) | 0,0381 | 0,757 | 0,763 | 0,824 | 0,764 | 0,768 | [−0,180; 0,314] | [−0,205; 0,276] |
| Negatif binom | ln(1+K₍t−1₎) | 0,6278 | <0,001 | <0,001 | <0,001 | <0,001 | <0,001 | [0,412; 0,764] | [0,474; 0,797] |
| Poisson QML | Faz 1 (2005–2007) | 0,0772 | 0,002 | 0,069 | 0,228 | 0,041 | 0,062 | [0,036; 0,181] | [0,013; 0,135] |
| Poisson QML | Faz 2 (2008–2012) | 0,1954 | 0,002 | 0,003 | 0,068 | 0,003 | 0,010 | [0,120; 0,368] | [0,070; 0,297] |
| Poisson QML | Faz 3 (2013–2020) | −0,0926 | 0,216 | 0,336 | 0,603 | 0,384 | 0,399 | [−0,208; 0,200] | [−0,262; 0,072] |
| Poisson QML | ln(1+K₍t−1₎) | 0,6127 | <0,001 | <0,001 | <0,001 | <0,001 | <0,001 | [0,371; 0,738] | [0,477; 0,829] |

### Model 2: p değerleri

| Tahminci | Katsayı | b | Ülke-küme t(13) | İki yönlü | Jackknife CV3 | Bootstrap z (tez) | Bootstrap t(13) | %95 yüzdelik | %95 BC |
|---|---|---|---|---|---|---|---|---|---|
| Negatif binom | ETS öncesi eğilim (t*) | −0,0068 | 0,604 | 0,568 | 0,730 | 0,692 | 0,699 | [−0,035; 0,033] | [−0,040; 0,027] |
| Negatif binom | Faz 1 düzey (λ₁) | 0,0434 | 0,542 | 0,375 | 0,566 | 0,539 | 0,550 | [−0,079; 0,196] | [−0,072; 0,208] |
| Negatif binom | Faz 1 eğim (φ₁) | 0,1107 | 0,004 | <0,001 | 0,007 | 0,001 | 0,005 | [0,049; 0,179] | [0,053; 0,185] |
| Negatif binom | Faz 2 düzey (λ₂) | 0,3525 | 0,001 | <0,001 | 0,002 | <0,001 | 0,002 | [0,203; 0,551] | [0,207; 0,564] |
| Negatif binom | Faz 2 eğim (φ₂) | −0,0204 | 0,417 | 0,418 | 0,495 | 0,387 | 0,403 | [−0,059; 0,032] | [−0,071; 0,018] |
| Negatif binom | Faz 3 düzey (λ₃) | 0,0721 | 0,676 | 0,654 | 0,723 | 0,670 | 0,677 | [−0,204; 0,470] | [−0,230; 0,433] |
| Negatif binom | Faz 3 eğim (φ₃) | 0,0134 | 0,338 | 0,390 | 0,425 | 0,414 | 0,429 | [−0,021; 0,044] | [−0,022; 0,042] |
| Negatif binom | ln(1+K₍t−1₎) | 0,6567 | <0,001 | <0,001 | 0,006 | <0,001 | 0,002 | [0,195; 0,870] | [0,321; 0,945] |
| Poisson QML | ETS öncesi eğilim (t*) | −0,0225 | 0,112 | 0,092 | 0,519 | 0,286 | 0,306 | [−0,045; 0,033] | [−0,056; 0,015] |
| Poisson QML | Faz 1 düzey (λ₁) | 0,0396 | 0,271 | 0,101 | 0,330 | 0,346 | 0,364 | [−0,063; 0,107] | [−0,055; 0,113] |
| Poisson QML | Faz 1 eğim (φ₁) | 0,0867 | <0,001 | <0,001 | 0,004 | 0,001 | 0,004 | [0,062; 0,160] | [0,062; 0,163] |
| Poisson QML | Faz 2 düzey (λ₂) | 0,3232 | <0,001 | <0,001 | <0,001 | <0,001 | <0,001 | [0,204; 0,459] | [0,203; 0,453] |
| Poisson QML | Faz 2 eğim (φ₂) | −0,0220 | 0,111 | 0,201 | 0,263 | 0,241 | 0,261 | [−0,047; 0,029] | [−0,065; 0,008] |
| Poisson QML | Faz 3 düzey (λ₃) | −0,0007 | 0,993 | 0,994 | 0,994 | 0,995 | 0,996 | [−0,173; 0,338] | [−0,233; 0,201] |
| Poisson QML | Faz 3 eğim (φ₃) | 0,0211 | 0,043 | 0,107 | 0,316 | 0,152 | 0,175 | [−0,015; 0,042] | [−0,007; 0,048] |
| Poisson QML | ln(1+K₍t−1₎) | 0,7879 | <0,001 | <0,001 | 0,018 | <0,001 | 0,002 | [0,181; 0,938] | [0,507; 1,030] |

Notlar: ülke-küme ve iki yönlü kovaryanslar Stata'nın en çok olabilirlik kuralıyla (yalnız G/(G−1) düzeltmesi) hesaplandı. **İki yönlü sütunu ihtiyatla okuyun:** Kısım 6'daki benzetimde bu tahminci boş hipotez altında %21–31 ret oranıyla en kötü performansı gösterdi; burada yalnız şeffaflık için raporlanıyor. Nominal düzeye en yakın yöntem küme jackknife (CV3; MacKinnon, Nielsen ve Webb, 2023). Parametrik bootstrap p değerleri Kısım 6'dadır.

### Spesifikasyon eğrisi özeti (896 tanım)

|  | Medyan katsayı | En küçük | En büyük | Pozitif pay | Pozitif ve %5'te anlamlı | Negatif ve %5'te anlamlı |
|---|---|---|---|---|---|---|
| Faz 1 (2005–2007) | 0,160 | 0,052 | 0,459 | %100,0 | %97,9 | %0,0 |
| Faz 2 (2008–2012) | 0,340 | 0,143 | 0,919 | %100,0 | %99,9 | %0,0 |
| Faz 3 (2013–2020) | 0,099 | −0,158 | 1,023 | %73,7 | %22,8 | %0,6 |

Tanımlar: tahminci (2) × stok var/yok × eskime oranı (0,10/0,15/0,20) × maruziyet sabit/serbest × kontroller tam/yok × örneklem (7) × gecikme 1/2 × doğrusal eğilim var/yok. Faz 3'ün pozitif ve anlamlı çıktığı tanımların neredeyse tamamı stoksuz olanlar (stoklu tanımlarda %6,2, stoksuzlarda %72,3). Bu eğri, bulguların *tanım seçimine* dayanıklılığını gösterir; ortak şoklara (T1) ve sabit etki/stok yapısına (T5) dayanıklılığını göstermez.

### Seçilmiş ek tahminler (faz katsayıları; ülke-kümeli SH, t(13) p değeri)

| Tanım | Tahminci | Faz 1 | Faz 2 | Faz 3 |
|---|---|---|---|---|
| Ana model + doğrusal eğilim | Negatif binom | 0,130 (0,012) | 0,265 (0,003) | 0,028 (0,794) |
| Ana model + doğrusal eğilim | Poisson QML | 0,087 (<0,001) | 0,208 (0,001) | −0,063 (0,304) |
| Ana model + karesel eğilim | Negatif binom | 0,156 (0,035) | 0,291 (0,003) | 0,037 (0,734) |
| Ana model + karesel eğilim | Poisson QML | 0,138 (<0,001) | 0,264 (<0,001) | −0,025 (0,636) |
| Yalnız stok (kontrolsüz) | Negatif binom | 0,113 (0,062) | 0,254 (0,017) | 0,013 (0,917) |
| Yalnız stok (kontrolsüz) | Poisson QML | 0,059 (0,053) | 0,171 (0,012) | −0,137 (0,114) |
| 2003–2004 beklenti kuklası eklenmiş | Negatif binom | 0,121 (0,067) | 0,251 (0,012) | 0,015 (0,911) |
| 2003–2004 beklenti kuklası eklenmiş | Poisson QML | 0,044 (0,267) | 0,147 (0,028) | −0,152 (0,132) |
| 2020 hariç | Negatif binom | 0,148 (0,029) | 0,296 (0,004) | 0,059 (0,662) |
| 2020 hariç | Poisson QML | 0,093 (0,003) | 0,228 (0,001) | −0,056 (0,500) |
| 2018–2020 hariç | Negatif binom | 0,168 (0,030) | 0,333 (0,002) | 0,094 (0,463) |
| 2018–2020 hariç | Poisson QML | 0,117 (0,003) | 0,283 (<0,001) | 0,019 (0,772) |
| İrlanda hariç | Negatif binom | 0,140 (0,054) | 0,264 (0,011) | 0,025 (0,847) |
| İrlanda hariç | Poisson QML | 0,076 (0,004) | 0,191 (0,006) | −0,099 (0,226) |
| Lüksemburg hariç | Negatif binom | 0,097 (0,039) | 0,207 (0,009) | −0,038 (0,745) |
| Lüksemburg hariç | Poisson QML | 0,062 (0,001) | 0,171 (0,004) | −0,120 (0,117) |
| Almanya ve Fransa hariç | Negatif binom | 0,167 (0,033) | 0,321 (0,003) | 0,119 (0,372) |
| Almanya ve Fransa hariç | Poisson QML | 0,125 (0,022) | 0,274 (0,005) | 0,063 (0,576) |
| Eskime oranı 0,05 | Negatif binom | 0,153 (0,014) | 0,325 (0,001) | 0,071 (0,601) |
| Eskime oranı 0,05 | Poisson QML | 0,090 (0,002) | 0,245 (0,001) | −0,065 (0,479) |
| Eskime oranı 0,25 | Negatif binom | 0,127 (0,030) | 0,240 (0,007) | 0,037 (0,740) |
| Eskime oranı 0,25 | Poisson QML | 0,077 (0,001) | 0,173 (0,004) | −0,083 (0,204) |
| Sabit etki yerine ön-örneklem ortalaması | Negatif binom | 0,003 (0,955) | 0,017 (0,870) | −0,300 (0,050) |
| Sabit etki yerine ön-örneklem ortalaması | Poisson QML | 0,004 (0,906) | 0,025 (0,768) | −0,337 (0,005) |

## 8. Birinci jüri raporunun analizi

Jüri raporunun tam metni: `dokumanlar/Juri1_Degerlendirme_Raporu.md`. Jüri, kendi ifadesiyle, regresyonları yeniden tahmin edememişti; aşağıdaki değerlendirme her maddeyi veriyle sınıyor.

| Jüri maddesi | Değerlendirmem | Veriyle desteklenen cevap |
|---|---|---|
| 1. Nedensellik: ETS'nin etkisini aynı dönemdeki diğer gelişmelerden nasıl ayırıyorsunuz? | Tamamen katılıyorum | Dürüst cevap: bu veriyle ayrılamıyor. Jüri listesine en somut çakışma eklenmeli: Kyoto 1. taahhüt dönemi (2008–2012) = Faz 2. Savunulabilir konum: (i) bulguları “AB ETS dönemleriyle ilişkili farklar” olarak sunmak; (ii) fazlara göre farklılaşan profilin (Faz 1'de eğim, Faz 2 başında düzey, Faz 3'te yok) tek bir ortak şokla açıklanmasının güç olduğunu, ama dışlanamadığını söylemek; (iii) NAP sıkılığı gibi ülkeler arası değişen bir maruziyet ölçüsüyle ek tahmin yapmak. Monte Carlo sonucu (Kısım 6) bu riskin büyüklüğünü sayısal gösteriyor. |
| 2. GSYİH esnekliği 0,39 çıktığı hâlde neden ana modeli değiştirmediniz? | Katılıyorum (ilk görüşümü güncelledim) | Kısıt reddediliyor ve AIC/BIC serbest modeli seçiyor (NB: 3.069,2 → 3.058,6). Savunma: maruziyet, bağımlı büyüklüğü “GSYİH başına patent” olarak tanımlayan bir normalizasyondur; hipotezler yoğunluk üzerine kuruludur; ve faz bulguları iki tanımda aynıdır (Faz 1 0,134 ↔ 0,165; Faz 2 0,271 ↔ 0,274). En temiz çözüm: iki tanımı ana tabloda yan yana vermek. |
| 3. Patent stoku hem kontrol hem aracı olabilir mi? | Katılıyorum | Stok geçmiş bağımlı değişkenin birikimi; hem ortak eğilimi emiyor (zamanla ülke-içi korelasyon 0,95) hem de olası etkiyi taşıyor. İki model arasındaki fark nedensel aracılık etkisi olarak okunamaz. Ek risk (jürinin sormadığı): sabit etki + gecikmeli stok yapısında tahminler tanıma duyarlı; sabit etkisiz ön-örneklem tanımında faz etkileri sıfıra iniyor (T5). Cevap: iki tanımı aralık olarak sunmak, “doğrudan/toplam” yerine “stok koşullu/koşulsuz” demek, mümkünse Ar-Ge harcaması kontrolü eklemek. |
| 4. Birleşik Krallık neden dışlandı? | Katılıyorum | Gerekçe olgusal olarak hatalı: Birleşik Krallık 31.12.2020'ye kadar AB ETS içindeydi. Hatayı kabul edip 15 ülkeli sağlamlık tahmini eklemek gerekir (veri setinde Birleşik Krallık yok; bu inceleme sınayamadı). |
| 5. Yatay kesit bağımlılığı varken yalnız ülke bazlı bootstrap neden yeterli? | Katılıyorum | Yeterli değil. Benzetim, tezin yönteminin gerçek etki sıfırken %5 yerine %13–21 oranında reddettiğini gösteriyor (C9). Yine de hangi sonucun dayanıklı olduğu gösterilebilir. Faz 2: küme jackknife ile p = 0,068 / 0,022, parametrik bootstrapla p = 0,024–0,097 / <0,001–0,004 (Poisson / NB). Faz 1: jackknife 0,228 / 0,041, parametrik bootstrap 0,215–0,326 / 0,021–0,066. İki yönlü kümeleme bu boyutta işe yaramıyor (benzetimde en kötü yöntem). Wild/pairs bootstrap ayrımı da metinde düzeltilmeli. |
| 6. Faz 3: etki mi kayboldu, stok mu taşıyor? | Katılıyorum | Bu veriyle ayrıştırılamıyor. “Stok taşıyor” lehine: stoksuz NB'de Faz 3 düzeyi yüksek (0,64). Aleyhine: bu düzey ETS öncesi eğilimin öngördüğünün altında (T3) ve stoksuz ITS'de Faz 3 eğimi negatif (Poisson −0,025). Doğru ifade: “üçüncü fazda ek doğrudan etkiye ilişkin kanıt yok; düzeyin neden yüksek kaldığı ayrıştırılamıyor.” |
| Birim kök / eşbütünleşme bölümü | Katılıyorum; ek bulgu var | Jürinin iki eleştirisi yerinde. Ek olarak: yoğunluk testleri logaritmayla yapılmış ama etiket düzey; düzeyle CIPS birim kökü reddedemiyor; Pedroni'nin +2,255'lik istatistiğinin “ret” sayılması şüpheli (M4). |
| Jürinin veri kontrolü | Doğrulandı ve genişletildi | Jüri yalnızca tanımlayıcı istatistikleri doğrulayabilmişti. Bu incelemede bütün regresyon katsayıları, bootstrap standart hataları ve testler bağımsız yazılımla yeniden üretildi: hesaplama hatası yok. Bu, tezin savunmada kullanabileceği güçlü bir nokta. |

**Jüri raporunda bulunmayan, bu incelemede ortaya çıkan başlıca noktalar:** H5'in stok yan ürünü olması (T2), H1 kanıtının eğilimle kirlenmesi (T3), sabit etki/stok tanımına duyarlılık (T5), 2003 plasebosu ve plasebo gücü (T6), Faz 2'nin zamanlaması (T7), etkin küme sayısı ve Poisson–NB ağırlık farkı (C3), BC aralıklarının kararsızlığı (C4), birim kök tablosunda log/düzey etiketi (M4), gecikme seçimi tanımı (M2).

## 9. İkinci jüri raporunun analizi

İkinci jüri ekibinin raporu (`dokumanlar/Juri2_Degerlendirme_Raporu.md`) ayrı bir belgede madde madde değerlendirildi: **`analiz/Juri2_Raporu_Degerlendirmesi.md`**. Burada özeti ve bu rapora etkisi verilmiştir.

|  | İkinci jürinin maddesi | Değerlendirmem | Gerekçe (özet) | İlgili bulgular |
|---|---|---|---|---|
| G1 | Veri bütünlüğü ve tam tekrarlanabilirlik | **Katılıyorum** | Yeniden üretimimle aynı sonuç: 164 değer birebir. | – |
| G2 | Doğru tahminci ve sabit etki tercihi | **Büyük ölçüde katılıyorum** | Tercih savunulabilir; negatif binomun ortak yayılım varsayımı ve iki tahmincinin farklı ağırlıklandırması not edilmeli. | M5, M7, C3 |
| G3 | Küçük küme sayısına uygun çıkarsama: eşli bootstrap ve BC aralıkları “birinci tip hata riskini başarıyla kontrol etmektedir” | **Katılmıyorum** | Benzetimde yöntem %5 yerine %13–21 oranında reddediyor; BC aralıkları kararsız. | C2, C4, C9 |
| G4 | Dinamik ayrıştırma ve sağlamlık tasarımı: Faz 1'de eğim hızlanması, Faz 2'de “kalıcı düzey sıçraması”; dışlama ve plasebo testleri dayanıklılığı pekiştiriyor | **Kısmen katılıyorum** | Model 2 gerçekten en sağlam kısım; ancak “kalıcı” nitelemesi yıl etkileriyle, plasebo övgüsü 2003 sonucuyla çelişiyor. | T6, T7, Y1 |
| E1 | Stokun ardışık dışsallığı ve “kötü kontrol” sorunu; ön-örneklem ortalaması tahmincisi “bu eleştiriyi karşılayacaktır” | **Tanıya katılıyorum; önerilen çare sorunu çözmüyor** | Kesin dışsallık ihlali doğru ve ölçüldü; önerilen tahminci Model 1'i kurtarmıyor, Model 2'yi doğruluyor. | T4, T5 |
| E2 | Ortak zaman şokları, karıştırıcı politikalar ve karbon fiyatı; yeşil olmayan patentlerle plasebo | **Katılıyorum; fiyat mekanizması hükmüne kısmen** | Tanımlama eleştirisi birinci kritik bulguyla aynı; fiyatın “temel mekanizma” olduğu sınanmış değil. | T1, T11 |
| E3 | Maruziyet kısıtı ve İrlanda 2015 | **Katılıyorum; İrlanda etkisi sonuçlar için önemsiz** | Kısıtsız model ana tabloda yer almalı; İrlanda sınandı, sonuç değişmiyor. | M1 |
| E4 | Birim kök ve eşbütünleşme analizindeki yöntemsel tutarsızlık | **Katılıyorum; ek bulgular var** | Aynı eleştiri diğer incelemelerde de var; ek olarak log/düzey etiketi ve dönem farkı bulundu. | M4 |
| E5 | Sıfır-kesikli sayım dağılımı: ZTNB duyarlılığı | **Kavramsal olarak katılmıyorum; yine de sınandı** | Sıfır gözlenebilir, yalnız gerçekleşmemiş; sıfır-kesikli tahminler dördüncü ondalıkta aynı. | M8 |
| K1 | Tablo 5.2 (t−1) ↔ Tablo 5.3 (t) dönem uyuşmazlığı | **Katılıyorum** | Doğrulandı. | Y6 |
| K2 | 5.6.4'te “Tablo 5.5” atfı Tablo 5.6 olmalı | **Katılıyorum** | Doğrulandı. | Y6 |
| K3 | Tahmin döneminin neden 1997'de başladığı açıklanmamış | **Kısmen katılıyorum** | Veriyle doğrulandı; metin bunu dolaylı söylüyor, bir cümle eklenmeli. | Y6 |
| K4 | Eskime oranı (0,15) için metin içi atıf yok | **Katılıyorum** | Doğrulandı. | Y6 |
| K5 | Değişken adları ve APA 7 biçim tutarlılığı | **Katılıyorum** | Doğrulandı. | B1, B2 |
| S | “Bu düzeltmelerle çalışma doğrudan uluslararası dergilere gönderilebilecek olgunluğa ulaşacaktır” | **Katılmıyorum** | Liste gerekli ama yeterli değil; değinilmeyen altı kritik ya da önemli nokta var. | T1, T2, T3, C9, T6, T7, T8 |

**Üç ana sonuç.** (1) Raporun çıkarsama övgüsü veriyle çelişiyor: eşli bootstrap + BC, gerçek etki sıfırken %5 yerine %13–21 oranında reddediyor (C9). (2) Stok eleştirisi için önerilen ön-örneklem ortalaması tahmincisi uygulandı: Model 1'in faz katsayıları sıfıra iniyor (NB Faz 2: 0,017), Model 2'nin Faz 1 eğimi (0,111) ve Faz 2 düzeyi (0,380) ise anlamlı kalıyor (T5). (3) Karbon fiyatı ve yeşil olmayan patentlerle plasebo önerileri yerinde ve yeni; ilki için kanıt sınırlı (T11), ikincisi yeni veri gerektiriyor (T1).

**İki jüri raporunun karşılaştırması**

| Konu | 1. jüri raporu | 2. jüri raporu | Bu rapordaki karşılığı |
|---|---|---|---|
| Kontrol grubu / ortak zaman şokları | Var (en önemli madde) | Var | T1 |
| Stokun kontrol / aracı rolü | Var | Var (kesin dışsallık çerçevesiyle) | T4, T5 |
| GSYİH maruziyet kısıtı | Var (ana model değişsin) | Var (birlikte sunulsun) | M1 |
| Birim kök / eşbütünleşme tutarsızlığı | Var | Var | M4 |
| Bootstrap yöntemi | Eleştiriyor (wild ↔ eşli uyumsuzluğu, az küme) | Övüyor (“birinci tip hatayı kontrol ediyor”) | C2, C4, C9 — veri birinci jüriyi destekliyor |
| Birleşik Krallık ve örneklem seçimi | Var | Yok | T8 |
| Üçüncü faz yorumu (“etki yok” ↔ “kanıt yok”) | Var | Kısmen (fiyat mekanizması) | Y3, T11 |
| Karbon fiyatı | Yok | Var | T11 |
| Yeşil olmayan patentlerle plasebo | Yok (genel olarak karşılaştırma grubu) | Var | T1 |
| Ön-örneklem ortalaması tahmincisi | Yok | Var | T5 |
| İrlanda 2015 | Yok | Var | M1 |
| Sıfır-kesikli model | Yok | Var | M8 |
| “Yeşil inovasyon = patent” sınırı | Var | Yok | Y5 |
| Regresyonların yeniden tahmini | Yapılmamış (yalnız tanımlayıcılar) | Yapılmış (katsayılar doğrulanmış) | Kısım 3 |
| Genel hüküm | Önemli düzeltme gerekli; nedensel tanımlama yetersiz | Güçlü omurga; düzeltmelerle yayına hazır | Bu inceleme birinci jürinin hükmüne daha yakın |

## 10. Bağımsız hakem okumasıyla karşılaştırma

Hiçbir ön bilgi verilmeden yaptırılan ikinci okuma (`dokumanlar/Bagimsiz_Hakem_Raporu.md`) 27 madde üretti. Hepsi ayrıca yeniden hesaplandı (`analiz/py/ek_dogrulama.py`):

| Hakemin iddiası | Benim hesabım | Sonuç |
|---|---|---|
| Model 2 ülke-içi VIF: eğilim 42,8; Faz 3 25,4; stok 12,0 | 42,8; 25,4; 12,0 | ✓ doğrulandı |
| Stok–zaman ülke-içi korelasyonu 0,95 | 0,945 | ✓ |
| Eğilim tek başına 0,27 / 0,46 / 0,78 log puan üretir (NB) | 0,27 / 0,46 / 0,78 | ✓ |
| 2003 plasebo kırılması reddediyor: Poisson χ² = 9,51 (p = 0,009); NB 5,45 (p = 0,066) | 9,51 (0,009); 5,45 (0,066) | ✓ (bootstrap kovaryansıyla reddedilmiyor: ek bilgi) |
| Bootstrap SH ile yıl etkilerinden yalnız 2009 %5'i geçiyor | p: 0,066 / 0,074 / 0,062 / 0,021 / 0,146 | ✓ |
| Yalnız kontroller 2 gecikmeli: AIC 2966,65 | 2.966,65 | ✓ |
| Yoğunluk birim kök testleri logaritmayla yapılmış | Fisher 22,94 ↔ 15,65; CD 36,913 ↔ 34,675 | ✓ (ek: CIPS ve Kao da; düzeyle CIPS reddetmiyor) |
| En büyük ham korelasyon 0,3510 | 0,3510 | ✓ |
| g ortalama log büyüme (aritmetik 0,0769; bileşik 0,0716) | 0,0769; 0,0716 | ✓ |
| Faz 2 / Faz 1 oranı NB 2,02; Poisson 2,53 | 2,02; 2,53 | ✓ |
| Pedroni değiştirilmiş PP +2,255'in “ret” sayılması şüpheli | Yeniden üretilmedi | Orta güvenle aktarıldı (M4) |
| Birleşik Krallık 31.12.2020'ye kadar AB ETS'de | Web kaynaklarından teyit | ✓ |

İki bağımsız okumanın (benim ilk incelemem ve hakem okuması) birbirinden habersiz aynı kritik noktalara ulaşması (kontrol grubu, H5'in stoka bağlılığı, bootstrap gerekçesi, Tablo 5.4, BC aralıkları) bu bulguların güvenilirliğini artırıyor. Hakemin bulup benim ilk incelememde kaçırdıklarım: H1 kanıtının eğilimle kirlenmesi, 2003 plasebosu, Faz 2 zamanlaması, log/düzey etiketi, gecikme seçimi tanımı, NAP ayrıntısı.

## 11. Önceki incelememdeki düzeltmeler

İlk incelemede (`analiz/arsiv/01_Ilk_Inceleme_ve_Juri_Analizi.md`) yazdığım ve bu aşamada yanlış ya da eksik çıkan değerlendirmeler:

| Önceki ifadem | Şimdiki durum |
|---|---|
| Tablo 5.11'de enerji ithalat bağımlılığı güven aralığı “yazım hatası” demiştim | Geri çekildi. Aynı aralık veriyle yeniden üretiliyor; hata değil, BC yönteminin kararsızlığı (C4). |
| Jürinin GSYİH maruziyeti eleştirisini “abartılı” bulmuştum | Güncellendi. Kısıt reddediliyor ve AIC/BIC serbest modeli seçiyor; jüri ilkesel olarak haklı. Faz bulgularının değişmediği tespiti geçerli (M1). |
| “Beklenti etkisi faz etkilerini aşağı yanlı yapar (tez lehine)” demiştim | Düzeltildi. Veri tersini gösteriyor: 2003–2004 eğilimin altında; ayrıldığında Poisson Faz 1 anlamsızlaşıyor (T9). |
| İki yönlü kümelemede Poisson Faz 1 p = 0,084; Wald δ₁=δ₂ (NB, küme) p = 0,052 yazmıştım | Stata'nın serbestlik düzeltmesi kuralıyla yeniden hesaplandı: 0,069 ve 0,044. Yorum değişmiyor. |
| Yatay kesit bağımlılığına çare olarak “iki yönlü kümeleme ile yeniden raporlayın” önermiştim | Geri çekildi. Monte Carlo'da iki yönlü kümeleme boş hipotez altında %21–31 ret oranıyla sınanan yöntemlerin en kötüsü çıktı. Yerine küme jackknife ve parametrik bootstrap öneriyorum (C1, C9). |
| “Faz 1 negatif binomda her yöntemde sağlam” izlenimi vermiştim | Yumuşatıldı. Boş hipotez benzetimlerinde negatif binom Faz 1 için tek yönlü p = 0,021–0,066 (sınırda); Poisson'da 0,215–0,326 (C5). |
| “Birim kök/eşbütünleşme testleri yeniden üretilmedi” demiştim | Fisher-ADF, IPS, CD, CIPS ve Kao'nun iki istatistiği yeniden üretildi; bu sırada log/düzey etiket sorunu bulundu (M4). |
| “Stata nbreg kesirli bağımlı değişken kabul etmez” imasında bulunmuştum | Doğrulanmadı; rapordan çıkarıldı. |
| “2007 İklim-Enerji Paketi” yazmıştım | Düzeltildi: hedefler Mart 2007 zirvesinde benimsendi; paket 2008'de önerildi, 2009'da kabul edildi. |
| NB bootstrap'ında ilk yeniden yazımda tekrarların ~%20'si yakınsamadı | Tahminci IRLS + profil olabilirlik algoritmasıyla yeniden yazıldı; 1.999 tekrarın tamamı yakınsıyor, katsayılar Stata sonuçlarıyla dört ondalıkta aynı. |
| Ön-örneklem ortalaması için tek bir tanım raporlayıp “faz etkisi kayboluyor” demiştim | Ayrıntılandırıldı. Altı varyantın sonucu ön-örneklem bilgisinin biçimine çok duyarlı (Model 1 Faz 2: 0,02 ile 0,40 arasında); Model 2'nin Faz 1 eğimi ve Faz 2 düzeyi ise bu tahmincide de anlamlı (T5). |

## 12. Yapılacaklar

### A — Savunmadan önce şart

1. Sınırlılıklar alt bölümü yazın: kontrol grubu yokluğu, ortak şoklar (Kyoto 2008–2012, enerji fiyatları, küresel patent dalgası), 14 küme / etkin 4–5 küme, yatay kesit bağımlılığı, plasebo gücü, patentin inovasyon ölçüsü olarak sınırları. *(bkz. T1, C1, C3, T6)*
2. Nedensel dili daraltın: “AB ETS'nin etkisi” → “AB ETS dönemleriyle ilişkili fark”; L127, L351, L761 ve 5.10'daki kesin ifadeleri yumuşatın. *(bkz. T1)*
3. H5'i yeniden yazın; stoksuz Model 2'yi ve Model 2 VIF değerlerini raporlayın. *(bkz. T2)*
4. H1 kanıtını değiştirin: tek ETS kuklalı ana model ya da eğilimli stoksuz model; “toplam etki” yüzdelerini H1 için kullanmayın. *(bkz. T3)*
5. Çıkarsama duyarlılığı tablosu ekleyin (küme jackknife, parametrik bootstrap, eşli bootstrap); H2'yi “negatif binomda sınırda, Poisson'da anlamsız” diye güncelleyin; ana kanıtı Faz 2 ve Model 2'ye dayandırın. *(bkz. C1, C5, C6, C9)*
6. 5.1.8'i uygulanan yönteme göre yeniden yazın (eşli bootstrap ≠ wild bootstrap); BC aralıklarının yanında yüzdelik ve bootstrap-t aralıklarını verin. *(bkz. C2, C4)*

### B — Güçlü biçimde önerilir

1. Sabit etkisiz / ön-örneklem ortalamalı tanımı raporlayın ve faz etkilerini aralık olarak sunun; Nickell paragrafını benzetim sonucuna göre yeniden yazın; Blundell-Griffith-Windmeijer (2002) atfı. *(bkz. T5)*
2. GSYİH esnekliği serbest modeli ana tabloya ekleyin (ya da ana model yapın); 5.6.2'yi buna göre yeniden yazın. *(bkz. M1)*
3. Birleşik Krallık gerekçesini düzeltin; 15 ülkeli sağlamlık tahmini için veriyi ekleyin; 2004 sonrası üyelerin dışlanma ölçütünü yazın. *(bkz. T8)*
4. Plasebo testlerini 1999–2003 için eksiksiz ve ana tablolarla aynı çıkarsama yöntemiyle raporlayın; güç sınırını belirtin. *(bkz. T6, C7)*
5. “Faz 2 boyunca korunuyor” yorumunu yıl etkilerine göre düzeltin; 5.10.2'deki zamanlama anlatısını gözden geçirin. *(bkz. T7)*
6. Ülke dışlama yorumunu düzeltin; Poisson–NB farkını ağırlıklandırmayla açıklayın. *(bkz. Y1, C3)*
7. Tablo 5.17'yi yeniden değerlendirmeye göre güncelleyin. *(bkz. Y2)*
8. Karbon fiyatını tartışmaya ve modele ekleyin: gecikmeli yıllık ortalama EUA fiyatı; Faz 3 için fiyat açıklamasını sınanmış biçimde sunun. *(bkz. T11)*

### C — Önerilir

1. Tablo 5.4'ü ülke-içi korelasyonlarla verin; ortalama VIF yorumunu çıkarın. *(bkz. M3, T4)*
2. Birim kök tablolarında “ln” etiketini ve dönemleri düzeltin; Pedroni yorumunu kontrol edin; bölümü kısaltın. *(bkz. M4)*
3. Gecikme seçimi karşılaştırmasının tanımını düzeltin; negatif binom tercihinin gerekçesini yayılım heterojenliğine göre yeniden yazın. *(bkz. M2, M7)*
4. Pakes–Griliches (1,6 yıl) ve Bel–Joseph (kapsam, tahminci) ifadelerini birincil kaynaktan doğrulayın. *(bkz. Y4)*
5. NAP ve doğrusal indirim faktörü ifadelerini düzeltin. *(bkz. T10)*
6. Maruziyet tasarımı (NAP sıkılığı × faz), enerji fiyatı kontrolü ve yeşil patent payı bağımlı değişkeniyle ek tahminler (yeni veri gerekir). *(bkz. T1)*
7. Yeşil olmayan EPO başvurularıyla plasebo sonuç sınaması yapın (ikinci jüri önerisi; yeni veri gerekir). *(bkz. T1)*

### D — Son okuma düzeltmeleri

1. Küçük ifade düzeltmeleri: yüzde puan, Lüksemburg, g tanımı, Tablo 5.3 notu, “altı/beş kontrol”, p = 0,000, Tablo 5.6 atfı, yuvarlama kuralı. *(bkz. Y6, M6)*
2. Biçim: başlık stilleri, boş başlıklar, sarı vurgular, denklem numaraları, α sembolü, boş tabanlı alt indisler, tablo boşlukları. *(bkz. B1)*
3. Atıf yazımı ve kaynakça biçimi; Wooldridge (1999) ve StataCorp kayıtları. *(bkz. B2, M5)*
4. Dipnotlar: tahmin döneminin 1997'de başlama nedeni; sıfır-kesikli tahminlerin sonucu değiştirmediği; İrlanda 2015 sıçramasının etkisizliği. *(bkz. Y6, M8, M1)*

## 13. Tez bölümlerine göre bulgu haritası ve kaynakça denetimi

### 13.1 Bölümlere göre bulgular

| Tez bölümü | Kapsam | Genel durum | İlgili bulgular |
|---|---|---|---|
| 5.1 Modeller ve yöntemler | Genelleştirilmiş doğrusal modeller, sayım verisi, Poisson QML, negatif binom, sabit etkili panel sayım modeli, kukla değişkenli model, segmentli kesintili zaman serisi ve kümelenmiş bootstrap'ın kuramsal anlatımı. | Denklemler (1)–(13), NB2 olasılık fonksiyonu ve varyansı, sınırdaki LR dağılımı, BC ve Wald formülleri doğru. Sorunlar anlatımın uygulamayla uyumunda: bootstrap gerekçesi (wild ↔ eşli), BC aralıklarının bu verideki davranışı ve negatif binomun varsayımları. | C2, C4, C9, M5, M7 |
| 5.2–5.3 Model tanımı ve hipotezler | İki modelin amacı, referans dönem (1997–2004), tanımlama savı (fazların dışsallığı) ve Porter hipotezine dayanan H1–H5. | Faz takvimi doğru (Faz 3: 2013–2020; Faz 4 dışarıda). Temel sorun tanımlama savında: fazların dışsal olması ters nedenselliği dışlar, ortak zaman şoklarını dışlamaz. Hipotezlerin yeniden değerlendirmesi Özet sayfasında. | T1, T9, T10 |
| 5.4–5.5 Değişkenler ve veri | Bağımlı değişken (EPO iklim azaltım patent başvuruları), maruziyet (reel GSYİH), faz kuklaları, stok ve beş kontrol; örneklem, kaynaklar, tanımlayıcı istatistikler, korelasyonlar. | Veri seti tam dengeli ve iç tutarlı; Tablo 5.2–5.4'ün bütün değerleri, toplamlar, paylar, uç değerler ve stok hesabı birebir yeniden üretildi. Kaynak verilerle karşılaştırma yapılamadı (erişim yok). Sorunlar örneklem gerekçesinde ve tabloların sunumunda. | T8, T9, M3, M6, M8, Y5, Y6 |
| 5.6 Modelin kurulması | Tahminci seçimi, maruziyet, Model 1 ve Model 2 denklemleri, stokun rolü ve Nickell tartışması, VIF, bootstrap uygulaması, aşırı yayılım testi, birim kök ve eşbütünleşme testleri, gecikme seçimi. | α, LR, VIF, AIC değerleri ve birim kök / CD / CIPS istatistikleri yeniden üretildi. Bölümün en yoğun sorun alanı burası: çıkarsama yöntemi, dinamik yapı (stok), maruziyet kısıtı, birim kök bölümünün tutarlılığı. | T1, T4, T5, C1, C2, C3, C7, C9, M1, M2, M4, M5, M7, M8, Y4 |
| 5.7 Bulgular | Model 1 faz katsayıları (Tablo 5.11–5.12), Model 2 düzey ve eğim katsayıları (Tablo 5.13), yıl etkileri (Şekil 5.5). | Bütün katsayılar dört ondalığa kadar, bootstrap standart hataları birkaç yüzde içinde yeniden üretildi; yüzde dönüşümleri ve yıllık sapmalar doğru. Sorunlar katsayıların yorumunda ve anlamlılık yargılarında. | T2, T7, C4, C5, C6, C7, C8, Y3, Y6 |
| 5.8 Sağlamlık testleri | Stoksuz model, serbest GSYİH esnekliği, Almanya hariç, ülkelerin tek tek dışlanması, plasebo kırılma testleri. | Tablo 5.14–5.16'nın bütün değerleri yeniden üretildi. Sorunlar testlerin seçici raporlanmasında (2003 plasebosu), gücünde ve sonuçların yorumunda. | T3, T4, T6, C3, C7, M1, Y1 |
| 5.9–5.10 Hipotez değerlendirmesi ve tartışma | Tablo 5.17 (hipotez sonuçları), fazlara göre tartışma, bilgi stoku ve yol bağımlılığı, literatürle karşılaştırma. | H3 ve H4'ün sonuçları sağlam. H1 ve H5 bağdaşmayan tanımlardan destekleniyor; tartışmadaki nedensel anlatı (beklenti kanalı, kurumsal kesinlik, stokla taşınan etki) tasarımın taşıyabileceğinden güçlü; bölümde sınırlılıklar tartışması yok. | T1, T2, T3, T4, T7, T10, T11, C5, Y2, Y3, Y4, Y5 |

### 13.2 Kaynakça ve atıf denetimi

Bölümdeki bütün metin içi atıflar programla çıkarılıp kaynakçayla eşleştirildi: eksik kayıt ya da yazar/yıl uyuşmazlığı yok. Sorunlar biçimde, birkaç eksik atıfta ve doğrulanamayan iki literatür aktarımında. Bölümde 38 farklı yazar–yıl atfı var; kaynakçada 125 kayıt bulunuyor (liste tezin tamamı için).

**Atıf yazım hataları**

| Satır | Metindeki yazım | Sorun |
|---|---|---|
| L81 | Hausman ve diğ.(1984) | parantezden önce boşluk |
| L81 | (Allison&Waterman, 2002) | “ve” bağlacı, boşluk |
| L109 | (Efron&Tibshirani, 1993) | “ve” bağlacı, boşluk |
| L153 | (OECD,2026) | virgülden sonra boşluk; kaynakçadaki yıl 2024 |
| L183 | sağlamaktadır(Bel ve Joseph,2018) | boşluklar |
| L193 | (Dechezleprêtre ve diğ.,2011; … Haščič ve Migotto 2015) | boşluk, virgül |
| L331 | (Allison andWaterman, 2002) | “and” → “ve”, boşluk |
| L335 | etkilemektedir(Bel&Joseph,2018) | “ve” bağlacı, boşluklar |
| L525 | Pakes&Griliches(1984); Bel&Joseph(2018) | “ve” bağlacı, boşluklar |

**Kaynakça kayıtları**

| Kayıt | Sorun |
|---|---|
| Dechezleprêtre ve diğ. (2011) | “&” bağlacı ve tırnak içinde başlık; diğer kayıtlarla aynı biçime getirilmeli |
| OECD veri seti | İki kez, iki farklı yıl ve biçimle listelenmiş (2024, başka bir atıf stiliyle; 2026, veri kaynakları altında) |
| StataCorp | Stata 19 kullanıldığı yazılıyor, kaynakça kaydı yok |
| Wooldridge (1999) | Kaynakçada var; sabit etkili Poisson'un dağılım varsayımına dayanıklılığı (5.1.5) için metinde atıf yapılmalı |

**Eksik metin içi atıflar**

| Yer | Konu | Not |
|---|---|---|
| 5.4.4 (L179) | Eskime oranı δ = 0,15 ve başlangıç stoku formülü | Noailly ve Smeets (2015); Hall ve Mairesse (1995); Popp (2002); Verdolini ve Galeotti (2011) — hepsi kaynakçada, metinde atıf yok |
| 5.5 (L193) | 1990 başlangıcı için gösterilen kaynaklar | Atıf yapılan çalışmaların “veriler 1990'dan itibaren güvenilir” dediği kontrol edilmeli |

**Birincil kaynaktan doğrulanması gereken aktarımlar**

| Yer | İfade | Durum |
|---|---|---|
| 5.6.9 (L525) | “Pakes ve Griliches (1984) … ortalama gecikme yaklaşık 1,6 yıl” | Birincil kaynakta bu rakam teyit edilemedi; sayfa numarasıyla atıf verilmeli ya da ifade değiştirilmeli |
| 5.10.5 (L811) | “Bel ve Joseph'in (2018) ana modeli enerji teknolojilerine dayanırken…” | Makalenin özeti genel iklim azaltım teknolojilerini de kullandığını ve 28 ülkeyi kapsadığını belirtiyor; “rassal etkili model” nitelemesi de teyit edilemedi |

**Eklenmesi önerilen kaynaklar**

| Kaynak | Neden |
|---|---|
| Blundell, Griffith ve Windmeijer (2002); Blundell, Griffith ve Van Reenen (1999) | Sayım verili dinamik panel, ön-örneklem ortalaması tahmincisi (T5) |
| MacKinnon, Nielsen ve Webb (2023) | Az kümede çıkarsama, küme jackknife (C1, C9) |
| Carter, Schnepel ve Steigerwald (2017) | Etkin küme sayısı (C3) |
| Westerlund (2007) | Yatay kesit bağımlılığına dayanıklı eşbütünleşme testi (M4) |
| Guimarães (2008); Greene (2007) | Sabit etkili negatif binom tartışması (M5) |

## 14. Dosyalar ve yeniden üretilebilirlik

| Dosya | İçerik |
|---|---|
| `veri/AB14_nihai_veri.xlsx` | Ham panel, stok sayfası, kaynaklar |
| `dokumanlar/` | Tez bölümü (docx + metin), şekiller, iki jüri raporu, bağımsız hakem raporu |
| `analiz/Juri2_Raporu_Degerlendirmesi.md` | İkinci jüri raporunun madde madde değerlendirmesi |
| `analiz/py/juri2.py` | İkinci jürinin önerdiği sınamalar → `analiz/cikti/juri2.json` |
| `analiz/py/tezlib.py` | Veri hazırlama, Poisson IRLS, NB2 en çok olabilirlik, kümelenmiş kovaryanslar, bootstrap yardımcıları |
| `analiz/py/yeniden_inceleme.py` | Tüm tabloların yeniden üretimi ve ek analizler → `analiz/cikti/sonuclar.json` |
| `analiz/py/birim_kok.py` | Fisher-ADF, IPS, CD, CIPS |
| `analiz/py/ek_dogrulama.py` | Hakem iddialarının sınanması, yıl etkisi bootstrap'ı, plasebo, Kao |
| `analiz/py/simulasyon.py`, `simulasyon_p.py` | Monte Carlo sınaması (çıkarsama boyutu; parametrik bootstrap) |
| `analiz/py/icerik.py`, `rapor_uret.py` | Bulgular ve bu raporun üretimi (sayılar çıktılardan çekilir) |
| `analiz/arsiv/` | İlk inceleme raporu ve ilk replikasyon betiği |
| `docs/` | Etkileşimli site (GitHub Pages) |

```bash
pip install pandas numpy scipy statsmodels openpyxl
python analiz/py/yeniden_inceleme.py 1999
python analiz/py/birim_kok.py
python analiz/py/ek_dogrulama.py
python analiz/py/simulasyon.py 300 199
python analiz/py/simulasyon_p.py 1000
python analiz/py/juri2.py
python analiz/py/rapor_uret.py
```
