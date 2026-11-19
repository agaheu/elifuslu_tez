# Bağımsız hakem raporu (kör ikinci okuma)

> **Kaynak notu:** Bu rapor, yeniden inceleme sırasında (19.11.2026) ayrı bir yapay zekâ ajanına, önceki incelemelerin hiçbir sonucu verilmeden, yalnızca bölüm metni + şekiller + veri seti verilerek yaptırılan bağımsız okumanın çıktısıdır. Amaç, ana incelemenin kendi önyargılarına demirlenmemiş bir kontrol elde etmekti. Rapor İngilizce üretilmiş ve burada olduğu gibi arşivlenmiştir. Buradaki her iddia ana incelemede ayrıca yeniden hesaplanarak sınanmıştır (bkz. `analiz/Kapsamli_Yeniden_Inceleme.md` ve `analiz/py/ek_dogrulama.py`). Satır numaraları `dokumanlar/Nihai_Model_19112026_metin.md` dosyasına göredir.

---

# Referee report — Chapter 5 vs AB14_nihai_veri.xlsx

The chapter's numbers are reproducible; its problems are in identification, inference and what the hypotheses table claims. I re-estimated everything except the IPS, CIPS, Kao and Pedroni statistics (statsmodels; pairs cluster bootstrap, 1000 reps, own RNG).

## A. Verified correct

- **Descriptives:** Table 5.2 (all cells, lagged controls), Table 5.3, Table 5.4 and Figs 5.1–5.3 match the data. So do the text figures: 107,759 total, Germany 45.3%, France 17.8%, 1,707 / 6,414 / 7,381, range 1–3,041, median 142.5, skew 3.1, variance/mean 977, Denmark −50.6, Ireland 24.6 (2015).
- **Stock:** reproduces the Yesil_stok sheet to 1e-10 (g = 0.069148).
- **Point estimates:** every coefficient in Tables 5.11, 5.13, 5.14 and 5.15 reproduces to 4 decimals. So do α (0.0178 / 0.0161), LR (669.77 / 564.59), AIC (2958.25 / 2999.78), the VIFs in Table 5.6, the year effects (0.102, 0.156, 0.195, 0.308; stock 0.810) and the placebo χ² in Table 5.16.
- **Bootstrap:** SEs, BC intervals and Wald tests are close to the reported ones (e.g. Poisson F1 SE 0.0375 vs 0.0383; NB joint tests 12.27 / 21.83 / 0.72). Leave-one-out counts (7 of 14 at 5%, 13 at 10%) reproduce.
- **Arithmetic:** all percent/IRR conversions, yearly ITS deviations (4.4 / 16.7 / 30.3 / 42.3; 31–42), 1+αμ ≈ 6.7, χ² p-values (one exception, item 16), Fisher χ²(28) p-values, significance stars under normal critical values.
- **Unit-root tables:** Fisher-ADF and CD statistics reproduce exactly (one labelling caveat, item 12c).
- **Equations:** (1)–(13), NB2 pmf and variance, the ½χ²(0)+½χ²(1) boundary result, BC formulas, Wald formula, Maddala–Wu and Choi statistics are all correct.
- **Citations:** every in-text citation has a reference-list entry; no author/year mismatches.

## B. Problems

### Identification and hypothesis logic

1. **H1 evidence is trend-contaminated — critical, high.** L772: "Toplam etki üç fazda pozitif ve anlamlı (NB: %43,8; %101,2; %88,8)"; also L695.
   - The no-stock model has no trend term. Model 2 without the stock gives a pre-ETS trend of +0.035/yr (Poisson, bootstrap SE 0.013, p=0.006) and +0.049/yr (NB, SE 0.013).
   - Extrapolated, that trend alone yields about 0.27 / 0.46 / 0.78 log points against the reported 0.363 / 0.699 / 0.635.
   - Phase-3 deviation from trend is not positive (Poisson λ3 = −0.044, φ3 = −0.025/yr).
   - The Poisson no-stock F3 is itself insignificant (L682: 0.2687, SE 0.2006).
   - H1 and H5 are "supported" from mutually incompatible specifications; the main model shows no Phase-3 effect.
2. **H5 "ETS öncesi eğilim anlamsız" is a by-product of the stock — critical, high.** L645, L780.
   - Within-country correlation of ln(1+K_{t−1}) with time is 0.95. Model-2 within-VIFs (not reported) are 42.8 for the trend, 25.4 for F3 and 12.0 for the stock.
   - The trend's sign flips by specification: −0.007 / −0.023 (Model 2), +0.035 / +0.049 (no stock), +0.057 / +0.059 (pre-ETS sample only, cluster SE 0.023 / 0.028).
   - Fig 5.5: all seven pre-ETS coefficients are positive and decay to zero, which is not "istikrarlı bir seyir" (L663).
   - Phase 3 fails the joint test, so "Desteklenmektedir" is at most partial.
3. **No control group; phase dummies are time dummies — major, high.** L351.
   - Nothing in the model absorbs common shocks.
   - Coincident confounders: the 2004–08 energy-price surge (Popp 2002 is cited, prices are omitted); Kyoto's first commitment period, which is exactly Phase 2; the 2009 renewables package; the global CCMT patent boom and bust.
   - L801 attributes the Phase-3 decline to a "küresel eğilim" (Probst 2021) but the Phase 1–2 rise to the ETS.
   - Exogenous timing (L125) is not identification; the causal wording at L127 and L761 over-claims.
4. **"Direct vs stock-carried effect" is not identified — major, high.** L371, L695, L799–805.
   - The stock is a function of lagged outcomes and would have grown without the ETS.
   - Within-country, F3 correlates 0.74 with the stock and 0.79 with renewables (VIF 11.83).
   - L403 compares the *mean* VIF with the threshold of 10, which is meaningless.
5. **Table 5.4 uses the wrong correlations — major, high.** L271.
   - These are pooled correlations. Within-country (what FE uses): stock–renewables 0.81, stock–trade 0.64, stock–manufacturing −0.53.
   - The maximum is 0.3510, so it does exceed 0.35 (cosmetic).
6. **Phase-2 "korunmaktadır" contradicts the chapter's own year effects — major, high.** L647, L651, L795.
   - Year coefficients: 0.195, 0.308, 0.226, 0.135 (n.s.), 0.050 (n.s.). The effect peaks in 2009 and is gone by 2012.
   - That is right after Directive 2009/29, which L793 credits with creating certainty.
7. **Placebo tests are selective and low-powered — major, high.** L745–761.
   - An unreported break at 2003 rejects: Poisson χ²(2) = 9.51, p = 0.009; NB 5.45, p = 0.066.
   - N = 112 with 14 clusters and about 22 parameters.
   - "AB ETS'nin faaliyete geçtiği dönemle sınırlı olduğunu göstermektedir" is not supported.
8. **Exposure restriction is rejected and kept — major, high.** L697: elasticity 0.393 / 0.371, χ² = 10.78 / 15.92. NB F1 moves from 0.1338 to 0.1654 (+24%), which is not "yakın".
9. **Leave-one-out over-claim — major, high.** L741.
   - F1 loses 5% significance in 7 of 14 runs (France dropped: p = 0.141).
   - Dropping Denmark or Germany raises F2 by about 0.07 and flips the sign of F3.
   - H2 is fragile under Poisson, and λ1 in Model 2 is insignificant.

### Inference

10. **Bootstrap justification is mis-attributed — major, high.** L103.
    - Cameron et al. (2008) and MacKinnon–Webb (2017) recommend wild cluster bootstrap-t; pairs-bootstrap SEs give no refinement with few clusters.
    - L407 "küme büyüklüklerindeki farklılık": every cluster has 24 observations. Germany's 45% outcome share is not cluster size.
    - Stars use normal critical values. With t(13): Poisson F1 p = 0.065; NB trade openness z = −1.96, p = 0.050 (normal) / 0.072.
11. **BC intervals are unstable; inference methods are mixed — major, high.**
    - The bootstrap distribution is median-biased. For Poisson F1 the bootstrap mean is 0.097 against an estimate of 0.077, so the "95% BC" interval is the 0.2nd–83.6th percentiles.
    - Visible symptom at L550: import dependency 0.0022, SE 0.0026, BC [−0.0000; 0.0241], an upper bound 8.4 SEs out.
    - Trade openness: percentile CI [−0.0066; 0.0035] includes zero.
    - Year effects and placebo tests (L407, L661) use the asymptotic cluster SEs that L103 calls unreliable. With bootstrap SEs, z for 2006–2010 is 1.88 / 1.79 / 1.91 / 2.36 / 1.48, so only 2009 passes 5%. "2006'dan itibaren anlamlı" (L663) is method-dependent.
12. **Unit-root and cointegration section — major.**
    - (a) CD rejects independence, yet Kao and Pedroni assume it (high).
    - (b) Under CIPS the dependent variable is I(0) and four regressors are I(1); "her iki test grubunun sonuçları altında da geçerlidir" (L519) does not follow (high).
    - (c) Rows labelled "Yeşil Patent Yoğunluğu" are actually ln(density): logs give 22.94 / 34.65 / 207.86 and CD 36.913, raw density gives 15.65 / 31.42 / 151.46 and 34.68 (high).
    - (d) L512: Pedroni modified PP = +2.255, p = 0.012. The rho-type statistic rejects in the left tail, so "üç istatistiğin tamamı" is doubtful (medium).
    - (e) Table 5.8 calls trade openness trend-stationary; CIPS finds a unit root (p = 0.570 / 0.997). L491 passes over the reversal.
13. **Nickell argument — minor, medium.** L373: "hata terimiyle ilişkisi çok daha zayıftır" is unsupported. K_{t−1} contains y_{t−1} with weight 1 and is highly persistent; FE Poisson needs strict exogeneity.

### EU ETS facts

14. **UK exclusion rationale is wrong — major, high.** L193. The UK stayed in the EU ETS until 31 December 2020 (UK ETS from 2021), so it was a participant in all three phases. The EU-15-minus-UK sample and the exclusion of post-2004 members are unjustified.
15. **Phase rules were not all EU-level — minor, medium.** L125. Phase 1–2 caps and allocations came from National Allocation Plans; only Phase 3 is EU-wide. L793 "2020 yılına kadar": the linear reduction factor had no 2020 sunset. Banking from Phase 2 to 3 and the NAP-II cuts are correct.

### Internal consistency (minor / cosmetic)

16. L636: Poisson Phase-1 joint test "15,39 (0,001)". χ²(2) = 15.39 gives p = 0.0005, i.e. 0,000.
17. L375: "(Tablo 5.5)" should be Tablo 5.6.
18. Table 5.3 uses unlagged controls and the level K_t, while Table 5.2 uses lags; neither is labelled.
19. L179: 0.0691 is the mean *log* growth (arithmetic 0.0769, CAGR 0.0716).
20. L523: the "two-lag" model also lags the stock twice. Lagging only the controls gives AIC 2966.65 (gap 8, not 42).
21. L593: "yaklaşık iki katı" holds for NB (2.02), not Poisson (2.53).
22. L161: the highest-density list holds for 2005–2020 only. Pre-ETS, Luxembourg is top (0.517), probably an artefact of counting by applicant country (L149).
23. L645: "%11,7 yükselmiştir" is percentage points of annual growth.
24. L173 "altı kontrol" vs Table 5.5 "beş"; "ticaret hacmi" vs "açıklığı"; equations after (13) are unnumbered.
25. L13 (log link "yalnızca pozitif"), L49 (NB2 not named) and L57 ("daha etkin" holds only if the variance function is right) are imprecise.
26. L741: the BC claim "on üç tahminde" is not in Table 5.15.

### Citations

27. (a) None missing. (b) No mismatches.
    - (c) Formatting is inconsistent: "Allison&Waterman", "Allison andWaterman" (L81, L331), "Efron&Tibshirani" (L109), "Bel&Joseph" (L335, L525), "Pakes&Griliches(1984)", "(OECD,2026)", "Haščič ve Migotto 2015".
    - The Dechezleprêtre (2011) entry uses "&" and a quoted title. The OECD dataset appears twice (L1005 dated 2024 in another style; L1101 dated 2026).
    - δ = 0.15 and the K₀ formula (L179) carry no citation, though the data file credits Noailly–Smeets, Hall–Mairesse and Verdolini–Galeotti, all in the list.
    - Wooldridge (1999) is the proper source for L81 and is listed but uncited.
    - L193: the cited works do not claim patent data are reliable "from 1990" (low–medium).

## C. Not verified

- IPS, CIPS, Kao and Pedroni statistics.
- Content attributed to Yu (2022), Andreou (2026), Pakes–Griliches ("1,6 yıl") and Bel–Joseph.
- Exact bootstrap digits (different RNG; magnitudes agree).
- Whether Stata reports the Pedroni p-value two-sided or by absolute value (item 12d rests on this).
