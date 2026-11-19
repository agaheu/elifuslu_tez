"""Monte Carlo bölümünün yorum metni (rapor ve site ortak kullanır); sayılar sonuç dosyalarından çekilir."""
import json
from tezlib import ROOT


def metin(S, tr):
    SP = json.load(open(ROOT / "analiz" / "cikti" / "simulasyon_p.json"))
    R = json.load(open(ROOT / "analiz" / "cikti" / "sonuclar.json"))
    P, N = "poisson", "nb"
    rng = lambda key, g: f"%{tr(100 * min(min(S[g][f][key]) for f in (P, N)), 0)}–{tr(100 * max(max(S[g][f][key]) for f in (P, N)), 0)}"
    b = lambda fam, k: R["m1"][fam]["coef"][k]["b"]
    return "\n".join([
        "**Ne öğreniyoruz?**",
        "",
        f"1. **Model 1'in faz katsayıları yukarı yanlı.** Veri tezin kendi modelinden gelse ve gerçek etki sıfır olsa bile, sabit etkili tahminci stok katsayısını küçük tahmin ediyor (gerçek {tr(S['ayar']['gamma_A'], 2)}; ortalama tahmin {tr(SP['A'][N]['ort_gamma'], 2)}) ve aradaki farkı faz kuklalarına yüklüyor: negatif binomda ortalama Faz 1 +{tr(SP['A'][N]['ort'][0], 3)}, Faz 2 +{tr(SP['A'][N]['ort'][1], 3)}, Faz 3 +{tr(SP['A'][N]['ort'][2], 3)}. Tezdeki “Nickell sapması ihmal edilebilir” savı (L373) bu yüzden doğru değil. Karşılaştırma: tezin tahminleri {tr(b(N, 'F1'), 3)} / {tr(b(N, 'F2'), 3)} / {tr(b(N, 'F3'), 3)}. Yanlılık Faz 2'yi açıklamıyor, Faz 1'in dörtte biri kadar, Faz 3 tahmininden büyük.",
        f"2. **Model 2'nin katsayıları neredeyse yansız.** Aynı benzetimlerde Faz 1 eğiminin ortalaması {tr(SP['A'][N]['ort'][4], 3)}, Faz 2 düzeyinin {tr(SP['A'][N]['ort'][5], 3)}. Kesintili zaman serisi tanımı bu açıdan Model 1'den daha güvenilir.",
        f"3. **Tezin çıkarsama yöntemi fazla sık “anlamlı” buluyor.** Eşli bootstrap SH + normal kritik değer, gerçek etki sıfırken %5 yerine {rng('rej_boot', 'A')} oranında reddediyor; küçük bir ortak yıl şokuyla {rng('rej_boot', 'B')}. Sınanan yöntemler içinde nominal düzeye en yakını küme jackknife ({rng('rej_cv3', 'A')}); **en kötüsü iki yönlü kümeleme** ({rng('rej_2w', 'A')}). İlk incelemede önerdiğim iki yönlü kümeleme bu boyuttaki bir panelde çözüm değil.",
        f"4. **Hangi bulgu “sıfır etki” dünyasında nadir?** Tezin gözlenen katsayılarının boş hipotez altındaki dağılımda aşılma olasılığı (tek yönlü Monte Carlo p, dört senaryonun en küçüğü–en büyüğü): negatif binom Faz 2 {_r(SP, N, 1, tr)}, Model 2 Faz 2 düzeyi {_r(SP, N, 5, tr)}, Model 2 Faz 1 eğimi {_r(SP, N, 4, tr)}: bunlar yanlılık ve örnekleme gürültüsüyle açıklanamıyor. Negatif binom Faz 1 {_r(SP, N, 0, tr)}: sınırda. Poisson Faz 1 {_r(SP, P, 0, tr)}: sıfır etkiyle tamamen uyumlu. Poisson Faz 2 {_r(SP, P, 1, tr)}.",
        "",
        "**Sınırlar.** Benzetimler tezin model ailesi içinde kurulmuştur; boş hipotez senaryoları yalnızca *küçük* (ETS öncesi dalgalanmadan kalibre) ortak şok içerir. Kyoto dönemi ya da enerji fiyatı gibi büyük ve kalıcı ortak şoklar (T1) bu sınamanın dışındadır: buradaki “anlamlı” sözcüğü “tahminci yanlılığı ve örnekleme gürültüsüyle açıklanamıyor” demektir, “AB ETS'den kaynaklanıyor” demek değildir. Negatif binom üretim süreci ortak ya da ülkeye özgü aşırı yayılım varsayar; gerçek hata yapısı (seri korelasyon dâhil) farklıysa oranlar değişir."])


def _r(SP, fam, j, tr):
    ps = [SP[g][fam]["p_tek"][j] for g in ("A", "A2", "B", "C")]
    f = lambda p: "<0,001" if p < 0.0005 else tr(p, 3)
    return f(min(ps)) if f(min(ps)) == f(max(ps)) else f"{f(min(ps))}–{f(max(ps))}"
