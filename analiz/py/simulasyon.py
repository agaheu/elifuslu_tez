"""Tasarımın Monte Carlo sınaması: ETS etkisi SIFIR iken tezin tahmincisi ve çıkarsama yöntemleri ne bulur?

Üç veri üretim süreci (hepsinde faz etkisi = 0, stok simüle edilen patentlerden yeniden kurulur):
  A  Tezin kendi modeli (ülke sabit etkili NB), faz kuklaları çıkarılmış kısıtlı tahminle.
  B  A + ülkeler arası ORTAK yıl şoku (AR(1); büyüklüğü ETS öncesi yıl etkilerinin eğilim etrafındaki sapmasından kalibre).
  C  Sabit etkisiz "stok ~ gecikmeli bağımlı değişken" modeli (ülke düzeyi pre-sample ortalamayla), kısıtlı tahminle.
Her tekrarda Model 1 (FE Poisson ve FE NB) tahmin edilir; faz katsayılarının ortalaması (yanlılık) ve
%5 düzeyinde ret oranları (küme-t13, iki yönlü, CV3 jackknife, eşli bootstrap-SH) kaydedilir.

Çalıştırma: python analiz/py/simulasyon.py [tekrar=300] [B=199]   Çıktı: analiz/cikti/simulasyon.json
"""
import sys, json, time
import numpy as np, pandas as pd
from multiprocessing import Pool
from scipy.stats import norm, t as tdist
from tezlib import *

NS = int(sys.argv[1]) if len(sys.argv) > 1 else 300
BB = int(sys.argv[2]) if len(sys.argv) > 2 else 199
C = ["lnK1"] + CTRL5
df = load(); est = sample(df)
psm = df[df.year.between(1990, 1996)].groupby("country").ccm.mean(); pg = df[df.year.between(1995, 1996)].groupby("country").gdp_real.mean()
est["lnpsm"] = np.log(est.country.map(psm)); est["lnpg"] = np.log(est.country.map(pg))
K0 = df[df.year == 1996].set_index("country").K
ctry = list(pd.unique(est.country)); G = len(ctry)
est = est.sort_values(["country", "year"]).reset_index(drop=True)

# kısıtlı (faz etkisiz) tahminler
rA = fit_nb(est, C, cluster=None)                       # FE'li
rC = fit_nb(est, C + ["lnpsm", "lnpg"], fe=False, cluster=None)   # FE'siz
XA, nA, off = design(est, C); XC, nC, _ = design(est, C + ["lnpsm", "lnpg"], fe=False)
iA, iC = nA.index("lnK1"), nC.index("lnK1")
baseA = XA @ rA.b[:-1] - XA[:, iA] * rA.b[iA] + off       # lnK1 katkısı hariç doğrusal öngörücü
baseC = XC @ rC.b[:-1] - XC[:, iC] * rC.b[iC] + off
gA, gC, aA, aC = rA.b[iA], rC.b[iC], rA.b[-1], rC.b[-1]
# ortak şok kalibrasyonu: ETS öncesi yıl etkilerinin (2004=0) doğrusal eğilim etrafındaki std sapması
ey = est.copy(); yrs = [y for y in range(1997, 2021) if y != 2004]
for y in yrs: ey[f"y{y}"] = (ey.year == y).astype(float)
ry = fit_poisson(ey, [f"y{y}" for y in yrs] + C)
pre = np.array([ry.coef(f"y{y}") for y in range(1997, 2004)] + [0.0])
res = pre - np.polyval(np.polyfit(np.arange(8), pre, 1), np.arange(8))
SIG, RHO = float(res.std(ddof=2)), 0.5
idx = {c: np.where(est.country.values == c)[0] for c in ctry}
years = np.arange(1997, 2021)


def simulate(dgp, rng):
    base, gam, alpha = (baseC, gC, aC) if dgp == "C" else (baseA, gA, aA)
    shock = np.zeros(len(years))
    if dgp == "B":
        e = rng.standard_normal(len(years)) * SIG * np.sqrt(1 - RHO ** 2); shock[0] = rng.standard_normal() * SIG
        for t in range(1, len(years)): shock[t] = RHO * shock[t - 1] + e[t]
    y = np.zeros(len(est)); lnK1 = np.zeros(len(est))
    for c in ctry:
        k = K0[c]
        for j, i in enumerate(idx[c]):
            lnK1[i] = np.log(1 + k)
            mu = np.exp(base[i] + gam * lnK1[i] + shock[j])
            y[i] = rng.poisson(rng.gamma(1 / alpha, alpha * mu))
            k = 0.85 * k + y[i]
    d = est.copy(); d["ccm"] = y; d["lnK1"] = lnK1
    return d


def one(args):
    dgp, seed = args
    rng = np.random.default_rng(seed)
    d = simulate(dgp, rng)
    out = {}
    try:
        for fam in ["poisson", "nb"]:
            r = fit(d, PH + C, fam); r2 = fit(d, PH + C, fam, cluster="twoway")
            J = np.array([[fit(d[d.country != c], PH + C, fam, cluster=None if fam == "nb" else "country").coef(k) for k in PH] for c in ctry])
            se3 = np.sqrt((G - 1) / G * ((J - J.mean(0)) ** 2).sum(0))
            D = []
            for _ in range(BB):
                db, cid, _p = resample(d, rng)
                rb = fit_poisson(db, PH + C, cid=cid) if fam == "poisson" else fit_nb(db, PH + C, cid=cid, cluster=None)
                D.append([rb.coef(k) for k in PH])
            seb = np.array(D).std(axis=0, ddof=1)
            b = np.array([r.coef(k) for k in PH])
            out[fam] = {"b": b.tolist(), "g": r.coef("lnK1"),
                        "rej_cl": [float(r.p(k, "t") < .05) for k in PH], "rej_2w": [float(r2.p(k) < .05) if r2.stderr(k) > 0 else float("nan") for k in PH],
                        "rej_cv3": (2 * tdist.sf(np.abs(b / se3), G - 1) < .05).astype(float).tolist(),
                        "rej_boot": (2 * norm.sf(np.abs(b / seb)) < .05).astype(float).tolist(),
                        "rej_boot_t": (2 * tdist.sf(np.abs(b / seb), G - 1) < .05).astype(float).tolist()}
    except Exception as ex:
        import traceback
        return "HATA", traceback.format_exc()[-600:]
    return dgp, out


if __name__ == "__main__":
    t0 = time.time()
    jobs = [(g, 1000 * (i + 1) + j) for j, g in enumerate("ABC") for i in range(NS)]
    with Pool(4) as pool:
        allr = list(pool.imap_unordered(one, jobs, chunksize=4))
    hatalar = [r[1] for r in allr if r[0] == "HATA"]
    resl = [r for r in allr if r[0] != "HATA"]
    R = {"hata_sayisi": len(hatalar), "hata_ornek": hatalar[:2], "ayar": {"tekrar": NS, "B": BB, "sigma_ortak_sok": SIG, "rho": RHO, "gamma_A": float(gA), "gamma_C": float(gC), "alpha_A": float(aA), "alpha_C": float(aC)}}
    for g in "ABC":
        rs = [o for d_, o in resl if d_ == g]
        R[g] = {"n": len(rs)}
        for fam in ["poisson", "nb"]:
            B_ = np.array([o[fam]["b"] for o in rs])
            R[g][fam] = {"ort_b": B_.mean(0).tolist(), "sd_b": B_.std(0, ddof=1).tolist(), "medyan_b": np.median(B_, 0).tolist(), "ort_gamma": float(np.mean([o[fam]["g"] for o in rs])),
                         **{k: np.nanmean(np.array([o[fam][k] for o in rs], dtype=float), 0).tolist() for k in ["rej_cl", "rej_2w", "rej_cv3", "rej_boot", "rej_boot_t"]},
                         "ikiyonlu_gecersiz_pay": float(np.mean(np.isnan(np.array([o[fam]["rej_2w"] for o in rs], dtype=float))))}
    json.dump(R, open(ROOT / "analiz" / "cikti" / "simulasyon.json", "w"), indent=1)
    print(json.dumps(R, indent=1)); print("sure (sn):", round(time.time() - t0))
