# İkinci Jüri Raporunun Değerlendirmesi

**Değerlendirilen belge:** `dokumanlar/Juri2_Degerlendirme_Raporu.docx` (metni: `dokumanlar/Juri2_Degerlendirme_Raporu.md`) · **Tarih:** 19.11.2026

> İkinci jüri ekibinin raporundaki her madde (4 güçlü yön, 5 yöntemsel eleştiri, 5 tutarlılık notu ve kapanış yargısı) tek tek ele alındı. Her madde için jürinin ifadesi, benim değerlendirmem ve bu değerlendirmenin dayandığı hesap verilmiştir. Jürinin önerdiği sınamalar (ön-örneklem ortalaması tahmincisi, sıfır-kesikli model, İrlanda'nın etkisi) uygulanmıştır: `analiz/py/juri2.py` → `analiz/cikti/juri2.json`. Bulgu numaraları (T1, C9 …) ana rapora, `analiz/Kapsamli_Yeniden_Inceleme.md` Kısım 5'e atıftır. Sayılar hesap çıktılarından otomatik çekilir.

## 1. Özet

İkinci jüri raporu kısa, isabetli ve yapıcı; beş eleştirisinin dördü birinci jüri raporu ve benim incelememle örtüşüyor, üç yeni öneri getiriyor (ön-örneklem ortalaması tahmincisi, karbon fiyatı, yeşil olmayan patentlerle plasebo). Üç noktada veriyle çelişiyor ya da fazla iyimser:

1. **Çıkarsama övgüsü veriyle çelişiyor (G3).** Rapor, eşli bootstrap ve BC aralıklarının birinci tip hatayı “başarıyla kontrol ettiğini” söylüyor. Gerçek etkinin sıfır olduğu benzetimlerde bu yöntem %5 yerine %13–21 oranında reddediyor.
2. **Önerilen çare sorunu çözmüyor (E1).** Stok eleştirisini “karşılayacağı” söylenen ön-örneklem ortalaması tahmincisi uygulandığında Model 1'in faz katsayıları sıfıra iniyor (negatif binom Faz 2: 0,017). Tezi ayakta tutan Model 2: Faz 1 eğimi ve Faz 2 düzeyi bu tahmincide de anlamlı.
3. **Kapanış yargısı fazla iyimser (S).** Listelenen düzeltmeler gerekli ama yeterli değil; raporun değinmediği altı kritik/önemli nokta var (Kısım 6).

| Değerlendirme | Madde sayısı | Maddeler |
|---|---|---|
| Katılıyorum | 5 | G1, K1, K2, K4, K5 |
| Büyük ölçüde katılıyorum | 1 | G2 |
| Katılmıyorum | 2 | G3, S |
| Kısmen katılıyorum | 2 | G4, K3 |
| Tanıya katılıyorum; önerilen çare sorunu çözmüyor | 1 | E1 |
| Katılıyorum; fiyat mekanizması hükmüne kısmen | 1 | E2 |
| Katılıyorum; İrlanda etkisi sonuçlar için önemsiz | 1 | E3 |
| Katılıyorum; ek bulgular var | 1 | E4 |
| Kavramsal olarak katılmıyorum; yine de sınandı | 1 | E5 |

İkinci jürinin iki küçük önerisi (sıfır-kesikli model, İrlanda) sınandı ve sonuçları değiştirmediği görüldü; tezde birer dipnot yeterli.

## 2. Madde madde değerlendirme

### 2.1 Güçlü yönler ve özgün katkılar

#### G1 · Veri bütünlüğü ve tam tekrarlanabilirlik

**Jürinin ifadesi.** Toplam, paylar, Tablo 5.2, 5.4, 5.6 ve Tablo 5.11–5.13 katsayılarının birebir örtüştüğü belirtiliyor.

**Değerlendirme: Katılıyorum.** Bağımsız yeniden üretimimle aynı sonuç: karşılaştırılan 164 değerin tamamı birebir. İkinci jüri bunu benden bağımsız doğrulamış oluyor. Bir kayıt: “tam tekrarlanabilirlik” hesapların doğruluğunu gösterir, yorumların doğruluğunu göstermez.

#### G2 · Doğru tahminci ve sabit etki tercihi

**Jürinin ifadesi.** Koşullu sabit etkili NB yerine ülke kuklalı NB2 ve Poisson QML'in birlikte raporlanması yerinde bulunuyor.

**Değerlendirme: Büyük ölçüde katılıyorum.** Tercih savunulabilir. İki kayıt: (i) negatif binomun ortak aşırı yayılım varsayımı sağlanmıyor (ülke bazında α: Lüksemburg 0,26, Almanya 0,009); (ii) iki tahminci farklı ağırlıklandırıyor (Almanya'nın payı Poisson'da %45, NB'de %11), bu yüzden “birlikte raporlama” farkın nedenini açıklamayı da gerektirir.

**Ana rapordaki ilgili bulgular:** M5, M7, C3

#### G3 · Küçük küme sayısına uygun çıkarsama: eşli bootstrap ve BC aralıkları “birinci tip hata riskini başarıyla kontrol etmektedir”

**Jürinin ifadesi.** 14 küme ve dengesiz ağırlıklar altında eşli bootstrap + BC aralıklarının birinci tip hatayı kontrol ettiği söyleniyor.

**Değerlendirme: Katılmıyorum.** Bu, raporun veriyle çelişen tek güçlü iddiası. Gerçek etkinin sıfır olduğu benzetimlerde tezin yöntemi %5 yerine %13–21 oranında reddediyor; küçük bir ortak şokla %17–23. BC aralıkları kararsız: Poisson Faz 1 için “%95 BC aralığı” fiilen bootstrap dağılımının %0,2–%84,6 yüzdelikleri. Eşli bootstrap asimptotik kümelenmiş SH'den daha ihtiyatlı ama yeterli değil. Birinci jüri raporu da aynı noktada ikinci jüriden ayrışıyor (wild ↔ eşli bootstrap uyumsuzluğu).

**Ana rapordaki ilgili bulgular:** C2, C4, C9

#### G4 · Dinamik ayrıştırma ve sağlamlık tasarımı: Faz 1'de eğim hızlanması, Faz 2'de “kalıcı düzey sıçraması”; dışlama ve plasebo testleri dayanıklılığı pekiştiriyor

**Jürinin ifadesi.** Model 2'nin katkısı ve sağlamlık testleri olumlu bulunuyor.

**Değerlendirme: Kısmen katılıyorum.** Model 2 gerçekten bölümün en sağlam kısmı: Faz 1 eğimi ve Faz 2 düzeyi benzetimlerde yansız ve nadir (NB Monte Carlo p = 0,004–0,009; <0,001), ön-örneklem tahmincisinde de anlamlı. Üç kayıt: (i) “kalıcı” nitelemesi yıl etkileriyle çelişiyor: fark 2009'da zirve yapıp 2012'de sıfıra iniyor; (ii) plasebo testleri seçici: raporlanmayan 2003 kırılması tezin kendi yöntemiyle reddediyor (χ² = 9,51); (iii) ülke dışlamada Faz 1 on dört tahminin yalnız 7'sinde %5 düzeyinde anlamlı.

**Ana rapordaki ilgili bulgular:** T6, T7, Y1

### 2.2 Ekonometrik ve yöntemsel eleştiriler

#### E1 · Stokun ardışık dışsallığı ve “kötü kontrol” sorunu; ön-örneklem ortalaması tahmincisi “bu eleştiriyi karşılayacaktır”

**Jürinin ifadesi.** Stok geçmiş bağımlı değişkenin fonksiyonu; sabit etkili sayım tahmincileri kesin dışsallık ister; Faz 3'te stoku sabit tutmak Faz 3 katsayısını yapay biçimde aşağı çeker; ön-örneklem ortalaması tahmincisi önerilir.

**Değerlendirme: Tanıya katılıyorum; önerilen çare sorunu çözmüyor.** Tanı doğru ve benzetimle ölçüldü: gerçek etki sıfırken bile stok katsayısı 0,72 yerine ortalama 0,63 tahmin ediliyor, faz katsayıları yukarı kayıyor (+0,032 / +0,046 / +0,065). İki noktada ayrışıyorum. (1) “Faz 3 yapay biçimde aşağı çekiliyor” ifadesi yön olarak desteklenmiyor: dinamik yanlılık Faz 3 katsayısını yukarı iter; stok çıkarıldığında büyüyen Faz 3 katsayısı (0,64) eğilimi de içerir, eğilim eklenince 0,18 (p = 0,175) kalır. (2) Önerilen ön-örneklem tahmincisi uygulandı ve Model 1'i kurtarmıyor: Faz 1 0,003, Faz 2 0,017, Faz 3 −0,300 (NB; stok katsayısı 0,92); ön-örneklem stokuyla da aynı. Sonuç ön-örneklem bilgisinin biçimine çok duyarlı (tek yoğunluk değişkeniyle Faz 2 0,40). İyi haber: Model 2 bu tahmincide de ayakta (Faz 1 eğimi 0,111, Faz 2 düzeyi 0,380).

**Ana rapordaki ilgili bulgular:** T4, T5

#### E2 · Ortak zaman şokları, karıştırıcı politikalar ve karbon fiyatı; yeşil olmayan patentlerle plasebo

**Jürinin ifadesi.** Yıl sabit etkileri kullanılamıyor; Faz 2 AB 2020 Paketi ve kriz sonrası teşviklerle örtüşüyor; Faz 3'te EUA fiyatının 3–8 €/ton'a çökmesi etkinin kaybolmasının temel mekanizması; yeşil olmayan EPO başvuruları plasebo olarak önerilir.

**Değerlendirme: Katılıyorum; fiyat mekanizması hükmüne kısmen.** Tanımlama eleştirisi bu incelemenin birinci kritik bulgusuyla aynı; en somut çakışma Kyoto 1. taahhüt dönemi (2008–2012 = Faz 2). Yeşil olmayan patentlerle plasebo önerisi yerinde ve güçlü; veri setinde olmadığı için sınanamadı. Fiyat konusunda: tartışılması gerektiğine katılıyorum (tezde hiç yok); “temel mekanizma” hükmüne katılmak için kanıt yok. Yıl etkileri basit bir fiyat–inovasyon ilişkisi göstermiyor: Faz 1 izin fiyatı 2007'de sıfıra yaklaşırken etki artıyor; fiyat 2008 ortasından sonra gerilerken etki 2009'da zirve yapıyor; 2018–2019'da fiyat 15,5 → 24,7 €'ya çıkarken Faz 3 yıl etkileri sıfırın altında (−0,16).

**Ana rapordaki ilgili bulgular:** T1, T11

#### E3 · Maruziyet kısıtı ve İrlanda 2015

**Jürinin ifadesi.** Birim esneklik reddediliyor; İrlanda'nın 2015'teki %24,6'lık GSYİH sıçraması yoğunluğu suni düşürüyor; kısıtsız model ana bulgularla birlikte sunulmalı.

**Değerlendirme: Katılıyorum; İrlanda etkisi sonuçlar için önemsiz.** Kısıtsız modelin ana tabloda yer alması önerisine katılıyorum (birinci jüri de istiyor; AIC ve BIC serbest modeli seçiyor). İrlanda sınandı: ülke çıkarıldığında NB 0,140 / 0,264 / 0,025 (tam örneklem 0,134 / 0,271 / 0,038); İrlanda × 2015 sonrası kuklası anlamsız; serbest esneklik İrlanda'sız 0,401 (tam 0,393). İrlanda'nın Poisson ağırlığı %0,8. Ayrıca 2015'te İrlanda'nın başvurusu da sıçradığı için (31 → 83) o yıl yoğunluk düşmüyor, yükseliyor (0,142 → 0,305).

**Ana rapordaki ilgili bulgular:** M1

#### E4 · Birim kök ve eşbütünleşme analizindeki yöntemsel tutarsızlık

**Jürinin ifadesi.** CD ile bağımlılık bulunup CIPS'e geçildikten sonra birinci nesil Kao ve Pedroni testlerinin kullanılması çelişki; üstel sayım modelinde durağanlık uyumu açıklanmalı.

**Değerlendirme: Katılıyorum; ek bulgular var.** Aynı eleştiri birinci jüride ve bağımsız hakemde de var. Bu incelemenin eklediği: (i) “yeşil patent yoğunluğu” satırları aslında logaritmayla hesaplanmış; düzeyle CIPS −2,09 olup birim kökü reddedemiyor; (ii) birim kök testleri 1996–2020, Kao 1997–2020 dönemiyle; (iii) Pedroni'nin +2,255'lik istatistiğinin ret sayılması şüpheli.

**Ana rapordaki ilgili bulgular:** M4

#### E5 · Sıfır-kesikli sayım dağılımı: ZTNB duyarlılığı

**Jürinin ifadesi.** Örneklemde sıfır yok; Yunanistan ve Portekiz'de değerler 1'e yaklaşıyor; sıfır-kesikli negatif binoma duyarlılık kontrol edilmeli.

**Değerlendirme: Kavramsal olarak katılmıyorum; yine de sınandı.** Sıfır-kesikli model, sıfırın gözlenemediği tasarımlar içindir; burada sıfır gözlenebilir, yalnızca gerçekleşmemiştir ve model bunu olağan buluyor (beklenen sıfır sayısı 0,42). Kontrol yapıldı: sıfır-kesikli NB katsayıları 0,1342 / 0,2709 / 0,0385, olağan NB 0,1338 / 0,2705 / 0,0381. Fark dördüncü ondalıkta. Bir dipnot yeterli.

**Ana rapordaki ilgili bulgular:** M8

### 2.3 Veri seti ve metin içi tutarlılık denetimi

#### K1 · Tablo 5.2 (t−1) ↔ Tablo 5.3 (t) dönem uyuşmazlığı

**Jürinin ifadesi.** Tablo 5.3 dönem ortalamaları cari değerlerle hesaplanmış; not eklenmeli.

**Değerlendirme: Katılıyorum.** Doğrulandı: Tablo 5.3'ün kontrol sütunları eşzamanlı değerlerle birebir (ör. ETS öncesi yenilenebilir payı 11,90; gecikmeliyle 11,81). Stok sütunu da K₍t₎.

**Ana rapordaki ilgili bulgular:** Y6

#### K2 · 5.6.4'te “Tablo 5.5” atfı Tablo 5.6 olmalı

**Jürinin ifadesi.** VIF tablosuna yanlış numarayla atıf.

**Değerlendirme: Katılıyorum.** Doğrulandı (metin satırı L375).

**Ana rapordaki ilgili bulgular:** Y6

#### K3 · Tahmin döneminin neden 1997'de başladığı açıklanmamış

**Jürinin ifadesi.** 1990–1995'te Eurostat makro verilerinde 10–12 ülke eksik; açıkça belirtilmeli.

**Değerlendirme: Kısmen katılıyorum.** Veriyle doğrulandı: reel GSYİH 1995'ten, büyüme oranı 1996'dan itibaren tam (1990–1995'te 10–12 ülke eksik); bir dönem gecikmeyle ilk yıl 1997. “Açıklanmamış” demek biraz ağır: L193 “veriler 1996 yılından itibaren eksiksiz temin edilebilmiştir” diyor; ama hangi değişkenlerin kısıtlayıcı olduğu yazılmamış. Bir cümle eklenmeli.

**Ana rapordaki ilgili bulgular:** Y6

#### K4 · Eskime oranı (0,15) için metin içi atıf yok

**Jürinin ifadesi.** Noailly ve Smeets (2015) vd. kaynakçada var, metinde atıf yok.

**Değerlendirme: Katılıyorum.** Doğrulandı; veri dosyası Noailly–Smeets, Hall–Mairesse ve Popp/Verdolini–Galeotti'yi anıyor, metin (L179) anmıyor.

**Ana rapordaki ilgili bulgular:** Y6

#### K5 · Değişken adları ve APA 7 biçim tutarlılığı

**Jürinin ifadesi.** Farklı adlandırmalar, “&” bağlacı, bitişik yazımlar, mükerrer kaynakça girdisi.

**Değerlendirme: Katılıyorum.** Doğrulandı; ayrıntılı liste Kaynakça sayfasında ve B1–B2 bulgularında.

**Ana rapordaki ilgili bulgular:** B1, B2

### 2.4 Kapanış yargısı

#### S · “Bu düzeltmelerle çalışma doğrudan uluslararası dergilere gönderilebilecek olgunluğa ulaşacaktır”

**Jürinin ifadesi.** Önerilen düzeltmeler yapıldığında yayın olgunluğuna ulaşılacağı söyleniyor.

**Değerlendirme: Katılmıyorum.** İkinci jürinin listesi gerekli ama yeterli değil. Listede olmayan ve hakem sürecinde belirleyici olacak noktalar: “ETS öncesi eğilim yok” bulgusunun stok yan ürünü olması (T2), H1 kanıtının eğilimle kirlenmesi (T3), çıkarsama yönteminin aşırı reddetmesi (C9), plasebo testlerinin seçiciliği (T6), Faz 2 zamanlaması (T7), Birleşik Krallık gerekçesi (T8). Kontrol grubu sorunu (T1) çözülmeden nedensel bir makale olarak yayımlanması güç; betimleyici bir makale olarak ise bulgular güçlü.

**Ana rapordaki ilgili bulgular:** T1, T2, T3, C9, T6, T7, T8

## 3. Önerilen sınamaların tam sonuçları

### 3.1 Ön-örneklem ortalaması tahmincisi (E1)

Ülke kuklaları çıkarılıp ülke heterojenliği ön-örneklem dönemi bilgisiyle kontrol edildi (Blundell, Griffith ve Windmeijer, 2002). Ön-örneklem: patent için 1990–1996, GSYİH için 1995–1996. Hücreler: katsayı (ülke-kümeli t(13) p değeri).

| Tanım | Tahminci | Faz 1 | Faz 2 | Faz 3 | Stok katsayısı |
|---|---|---|---|---|---|
| A: ön-örneklem ort. patent + GSYİH; stok var | Negatif binom | 0,003 (0,955) | 0,017 (0,870) | −0,300 (0,050) | 0,917 (<0,001) |
| A: ön-örneklem ort. patent + GSYİH; stok var | Poisson QML | 0,004 (0,906) | 0,025 (0,768) | −0,337 (0,005) | 0,960 (<0,001) |
| B: ön-örneklem stoku (ln K1996) + GSYİH; stok var | Negatif binom | −0,000 (0,994) | 0,009 (0,931) | −0,311 (0,048) | 0,925 (<0,001) |
| B: ön-örneklem stoku (ln K1996) + GSYİH; stok var | Poisson QML | 0,005 (0,894) | 0,026 (0,753) | −0,335 (0,005) | 0,958 (<0,001) |
| C: ön-örneklem yoğunluğu; stok var | Negatif binom | 0,218 (0,013) | 0,402 (0,035) | 0,184 (0,503) | 0,285 (0,023) |
| C: ön-örneklem yoğunluğu; stok var | Poisson QML | 0,126 (0,239) | 0,280 (0,155) | 0,014 (0,960) | 0,357 (0,011) |
| D: ön-örneklem stoku; zamanla değişen stok YOK | Negatif binom | 0,403 (<0,001) | 0,790 (<0,001) | 0,790 (0,007) | – |
| D: ön-örneklem stoku; zamanla değişen stok YOK | Poisson QML | 0,347 (<0,001) | 0,745 (<0,001) | 0,709 (0,003) | – |
| E: ön-örneklem stoku + doğrusal eğilim; stok YOK | Negatif binom | 0,203 (0,020) | 0,453 (<0,001) | 0,227 (0,134) | – |
| E: ön-örneklem stoku + doğrusal eğilim; stok YOK | Poisson QML | 0,144 (0,001) | 0,390 (<0,001) | 0,101 (0,300) | – |
| F: hiçbir ülke kontrolü yok (havuzlanmış); stok var | Negatif binom | 0,060 (0,530) | 0,053 (0,614) | −0,373 (0,106) | 0,484 (<0,001) |
| F: hiçbir ülke kontrolü yok (havuzlanmış); stok var | Poisson QML | 0,054 (0,524) | 0,121 (0,313) | −0,226 (0,195) | 0,475 (<0,001) |
| Tezin sabit etkili modeli | Negatif binom | 0,134 (0,027) | 0,271 (0,004) | 0,038 (0,757) | 0,628 (<0,001) |
| Tezin sabit etkili modeli | Poisson QML | 0,077 (0,001) | 0,195 (0,002) | −0,093 (0,217) | 0,613 (<0,001) |

Okuma: (A) ve (B) tanımlarında stok katsayısı bire yaklaşıyor ve faz farkları kayboluyor; (C) tanımında stok katsayısı düşüyor ve faz farkları geri geliyor; stoksuz tanımlar (D, E) sabit etkili stoksuz tahminlere benziyor. 14 ülkelik yatay kesitte ülke heterojenliğini tek ya da iki değişkenle kontrol etmek kararsız; bu tahminci Model 1 için net bir hüküm vermiyor, ama sabit etkili tahminin tek doğru olmadığını gösteriyor.

**Model 2 (kesintili zaman serisi), ön-örneklem ortalamalı (A tanımı):**

| Katsayı | Negatif binom | Poisson QML | Tezin sabit etkili tahmini (NB) |
|---|---|---|---|
| ETS öncesi eğilim | −0,046 (0,011) | −0,046 (0,005) | −0,007 |
| Faz 1 düzey | 0,091 (0,281) | 0,072 (0,057) | 0,043 |
| Faz 1 eğim | 0,111 (0,013) | 0,103 (<0,001) | 0,111 |
| Faz 2 düzey | 0,380 (0,003) | 0,356 (<0,001) | 0,352 |
| Faz 2 eğim | −0,019 (0,357) | −0,015 (0,181) | −0,020 |
| Faz 3 düzey | 0,121 (0,474) | 0,038 (0,686) | 0,072 |
| Faz 3 eğim | 0,046 (0,014) | 0,044 (0,002) | 0,013 |
| Stok | 1,012 (<0,001) | 1,096 (<0,001) | 0,657 |

Faz 1 eğimi ve Faz 2 düzeyi iki tahmincide de sabit etkili tahminlere çok yakın ve anlamlı. Bu, tezin en dayanıklı bulgusunun Model 2'de olduğunu bir kez daha gösteriyor.

### 3.2 Sıfır-kesikli model (E5)

|  | Faz 1 | Faz 2 | Faz 3 | Stok |
|---|---|---|---|---|
| Poisson (tezdeki) | 0,0772 | 0,1954 | −0,0926 | 0,6127 |
| Sıfır-kesikli Poisson | 0,0772 | 0,1954 | −0,0926 | 0,6130 |
| Negatif binom (tezdeki) | 0,1338 | 0,2705 | 0,0381 | 0,6278 |
| Sıfır-kesikli negatif binom | 0,1342 | 0,2709 | 0,0385 | 0,6286 |

Modele göre beklenen sıfır sayısı 0,34 (Poisson) ve 0,42 (NB); gözlenen 0. En küçük beklenen değer 2,9 (Portekiz 1997). 3 ve altında 12, 5 ve altında 19 gözlem var. Yunanistan ve Portekiz çıkarıldığında: NB 0,119 / 0,277 / 0,027; Poisson 0,076 / 0,198 / −0,091.

### 3.3 İrlanda 2015 (E3)

| Tanım | Tahminci | Faz 1 | Faz 2 | Faz 3 | GSYİH esnekliği / kukla |
|---|---|---|---|---|---|
| Tezin ana modeli | Negatif binom | 0,134 (0,027) | 0,271 (0,004) | 0,038 (0,757) | – |
| Tezin ana modeli | Poisson QML | 0,077 (0,002) | 0,195 (0,002) | −0,093 (0,216) | – |
| İrlanda hariç | Negatif binom | 0,140 (0,054) | 0,264 (0,011) | 0,025 (0,847) | – |
| İrlanda hariç | Poisson QML | 0,076 (0,004) | 0,191 (0,006) | −0,099 (0,226) | – |
| İrlanda × 2015 sonrası kuklası eklenmiş | Negatif binom | 0,133 (0,031) | 0,270 (0,005) | 0,037 (0,763) | −0,143 (0,522) (kukla) |
| İrlanda × 2015 sonrası kuklası eklenmiş | Poisson QML | 0,079 (0,002) | 0,198 (0,003) | −0,088 (0,259) | 0,085 (0,640) (kukla) |
| Serbest GSYİH esnekliği, tam örneklem | Negatif binom | 0,165 (0,018) | 0,274 (0,004) | 0,035 (0,758) | 0,393 (0,024) |
| Serbest GSYİH esnekliği, tam örneklem | Poisson QML | 0,101 (<0,001) | 0,204 (<0,001) | −0,069 (0,281) | 0,371 (0,005) |
| Serbest GSYİH esnekliği, İrlanda hariç | Negatif binom | 0,168 (0,028) | 0,271 (0,009) | 0,026 (0,828) | 0,401 (0,037) |
| Serbest GSYİH esnekliği, İrlanda hariç | Poisson QML | 0,107 (<0,001) | 0,210 (0,002) | −0,059 (0,437) | 0,294 (0,027) |

İrlanda'nın reel GSYİH'si 2014'te 218,3, 2015'te 272,1 milyar €. Aynı yıl başvuru sayısı 31 → 83 → 43 seyrettiği için yoğunluk 2015'te düşmedi (0,142 → 0,305 → 0,156); GSYİH düzeyindeki kalıcı sıçrama sonraki yıllarda yoğunluğu mekanik olarak düşürüyor. İrlanda'nın Poisson tahminindeki ağırlığı %0,8.

### 3.4 Tahmin döneminin başlangıcı (K3)

| Değişken | 14 ülke için tam olduğu ilk yıl | Eksik ülke sayısı (yıl: adet) |
|---|---|---|
| Reel GSYİH | 1995 | 1990: 12, 1991: 11, 1992: 11, 1993: 10, 1994: 10 |
| GSYİH büyüme oranı | 1996 | 1990: 12, 1991: 12, 1992: 11, 1993: 11, 1994: 10, 1995: 10 |
| İmalat payı | 1995 | 1990: 7, 1991: 6, 1992: 6, 1993: 6, 1994: 6 |
| Patent, ithalat bağımlılığı, yenilenebilir payı, ticaret | 1990 | eksik yok |

Büyüme oranı 1996'dan itibaren tam olduğundan, bir dönem gecikmeyle tahmin 1997'de başlayabiliyor. Jürinin açıklaması doğru; teze bir cümleyle eklenmeli.

## 4. Karbon fiyatı üzerine (E2)

İkinci jüri raporu, 2013–2017'de izin (EUA) fiyatının 3–8 €/ton bandına gerilemesini Faz 3'te etkinin kaybolmasının “temel iktisadi mekanizması” olarak gösteriyor ve tartışılmasını istiyor. Fiyatın tartışılması gerektiği doğru: tezde karbon fiyatı değişken olarak da, tartışma konusu olarak da yok; oysa ETS'nin inovasyon teşviki fiyat üzerinden işler. Ancak “temel mekanizma” hükmü bu veriyle sınanmış değil ve tezin kendi yıl etkileriyle basit bir fiyat–inovasyon örtüşmesi görülmüyor.

Fiyat ve yıl etkilerinin (Poisson, 2004 = 0) yan yana okunması: (i) Faz 1 izinlerinin fiyatı 2007'de sıfıra yaklaştı (Ellerman ve Buchner, 2007; Ellerman ve diğ., 2010; ikisi de tezin kaynakçasında), yıl etkisi ise 2006–2007'de yükseliyor (0,102 → 0,156); (ii) fiyat 2008 ortasındaki ≈30 €'dan sonra ≈10–15 €'ya geriledi, yıl etkisi 2009'da zirve yapıyor (0,308); (iii) Avrupa Çevre Ajansı'na göre yıllık ortalama fiyat 2018'de 15,5 €, 2019'da 24,7 €; Faz 3 yıl etkileri 2020'ye kadar sıfırın altında ya da çevresinde (−0,186; −0,160; −0,104). Patentlerin fiyata gecikmeli tepki vermesi bu tabloyu kısmen açıklayabilir, ama fiyat kanalı kanıtlanmış değil. Yıllık EUA fiyat serisi veri setinde yok; doğrulanmış tam bir seri bu incelemede elde edilemedi, bu yüzden fiyat kontrollü tahmin yapılmadı.

Fiyat verileri için dayanak: 2008 ortasındaki ≈30 € zirvesi ve sonrasındaki gerileme, 2016'daki ≈5 € düzeyi ile 2018 (15,5 €) ve 2019 (24,7 €) yıllık ortalamaları Avrupa Çevre Ajansı ve Hollanda İstatistik Kurumu yayınlarından; Faz 1 fiyat çöküşü tezin kaynakçasındaki Ellerman çalışmalarından. Tam yıllık seri elimde olmadığı için sayısal bir tahmin yapmadım; bu, tezde yapılması gereken bir ek analizdir.

## 5. İki jüri raporunun karşılaştırması

| Konu | 1. jüri raporu | 2. jüri raporu | Ana rapordaki karşılığı |
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

İki rapor dört temel eleştiride birleşiyor (ortak şoklar, stok, maruziyet, birim kök). Ayrıştıkları tek esaslı nokta bootstrap: birinci jüri yöntemi sorguluyor, ikinci jüri övüyor; benzetim sonuçları birinci jüriyi destekliyor. Genel hükümde birinci jüri daha temkinli (“nedensel tanımlama yetersiz”), ikinci jüri daha iyimser (“düzeltmelerle yayına hazır”); bu incelemenin vardığı sonuç birinci jürinin hükmüne daha yakın.

## 6. İkinci jüri raporunun değinmediği noktalar

- **T2 (kritik).** “ETS öncesi eğilim yok” bulgusu (H5) stok değişkeninin yan ürünü.
- **T3 (kritik).** H1'in kanıtı (“toplam etki %43,8 / %101,2 / %88,8”) eğilimle kirlenmiş.
- **C9 (önemli).** Tezin çıkarsama yöntemi, gerçek etki sıfırken nominal düzeyin üç-dört katı “anlamlı” sonuç üretiyor.
- **T6 (önemli).** Plasebo kırılma testleri seçici raporlanmış ve gücü düşük.
- **T7 (önemli).** Faz 2 etkisi “faz boyunca korunuyor” iddiası tezin kendi yıl etkileriyle çelişiyor.
- **T8 (önemli).** Örneklem gerekçesi hatalı: Birleşik Krallık 2020 sonuna kadar AB ETS içindeydi.
- **C3 (önemli).** Etkin küme sayısı 4–5: Poisson tahminleri fiilen Almanya ağırlıklı.
- **M3 (orta).** Tablo 5.4 ham korelasyonları veriyor; sabit etkili model için ilgili olan ülke-içi korelasyonlar çok daha yüksek.
- **Y1 (önemli).** Ülke dışlama sonuçlarının yorumu fazla iddialı.

Bunların ilk altısı savunmada ya da hakem sürecinde belirleyici olabilecek nitelikte; ayrıntıları ana raporun 5. kısmında.

## 7. Savunma için cevap taslakları

**Soru: Stok kesin dışsallığı bozuyor; tahminleriniz tutarlı mı?**

İhlal tanım gereği var. Büyüklüğünü benzetimle ölçtüm: gerçek etki sıfırken Model 1 ortalama +0,03 / +0,05 / +0,06 tahmin ediyor. Bu, Faz 2 tahminini (0,27) açıklamıyor. Asıl kanıtım Model 2: orada yanlılık yok denecek kadar küçük ve Faz 1 eğimi ile Faz 2 düzeyi hem sabit etkili hem ön-örneklem ortalamalı tahmincide anlamlı.

**Soru: Ön-örneklem ortalaması tahmincisi ne veriyor?**

Model 1'de faz katsayıları sıfıra iniyor (Faz 2: 0,017), stok katsayısı 0,92'ye çıkıyor; sonuç ön-örneklem bilgisinin biçimine çok duyarlı. Model 2'de bulgular korunuyor. Bu yüzden iki tahmini aralık olarak sunuyor, yorumu Model 2'ye dayandırıyorum.

**Soru: Faz 3'te etki neden yok? Karbon fiyatı mı?**

Fiyat makul bir aday, ama bu veriyle sınanmadı ve yıl etkileri fiyatla birebir hareket etmiyor (2007'de fiyat sıfıra yaklaşırken etki artıyor; 2018–2019'da fiyat yükselirken etki yok). Dürüst cevap: üçüncü fazda ek doğrudan etkiye ilişkin kanıt yok; nedeni ayrıştırılamıyor. Gecikmeli EUA fiyatını modele ekleyen tahmin yapılmalı.

**Soru: Ortak şokları nasıl ayırıyorsunuz? Yeşil olmayan patentler?**

Bu tasarımla ayrılamıyor; bulgular “AB ETS dönemleriyle ilişkili fark” olarak sunulmalı. Yeşil olmayan EPO başvurularıyla plasebo ve NAP sıkılığına dayalı maruziyet tasarımı en güçlü iki ek sınama; ikisi de yeni veri gerektiriyor.

**Soru: İrlanda sonuçları bozuyor mu? Sıfır-kesikli model gerekli mi?**

İkisi de sınandı, sonuç değişmiyor: İrlanda'sız NB 0,140 / 0,264; sıfır-kesikli NB 0,1342 / 0,2709.

## 8. Bu değerlendirme sonucunda ana raporda yapılan güncellemeler

- **Yeni bulgu T11** (karbon fiyatı): ikinci jürinin fiyat eleştirisi ve yıl etkileriyle karşılaştırması.
- **Yeni bulgu M8** (sıfır-kesikli model): önerinin sınanması; sonuç değişmiyor.
- **T5 genişletildi:** kesin dışsallık çerçevesi; ön-örneklem ortalaması tahmincisinin altı varyantı; Model 2'nin bu tahmincide de ayakta kaldığı.
- **T1 güncellendi:** yeşil olmayan EPO başvurularıyla plasebo sonuç önerisi.
- **M1 güncellendi:** İrlanda 2015 sınaması.
- **C9 ve T7'ye not eklendi:** ikinci jürinin “birinci tip hata kontrol ediliyor” ve “kalıcı düzey sıçraması” nitelemelerinin veriyle karşılaştırması.
- **Y6 güncellendi:** tahmin döneminin 1997'de başlama gerekçesi.
- **Kaynak etiketleri:** T1, T4, T5, M1, M4, Y6, B1, B2 bulgularına “2. jüri raporu” kaynağı eklendi.
- **Yeni Kısım 9** (ikinci jüri raporunun analizi) ve **Kısım 13** (tez bölümlerine göre bulgu haritası, kaynakça denetimi) eklendi; yapılacaklar listesine üç madde eklendi; “önceki incelememdeki düzeltmeler” tablosuna ön-örneklem tahmincisi notu eklendi.

## 9. Yeniden üretim

```bash
python analiz/py/juri2.py
```

```bash
python analiz/py/rapor_uret.py
```
