"""Parametrik bootstrap: "ETS etkisi sıfır" boş hipotezi altında tezin katsayılarının dağılımı ve Monte Carlo p değerleri.

Senaryolar (hepsinde faz etkisi = 0; stok simüle patentlerden yeniden kurulur):
  A   tezin kendi modeli (sabit etkili NB, ortak alpha)
  A2  A, ancak aşırı yayılım ülkeye özgü (veriden moment tahmini)
  B   A2 + ortak yıl şoku
  C   sabit etkisiz stok modeli
Çalıştırma: python analiz/py/simulasyon_p.py [tekrar=1000]   Çıktı: analiz/cikti/simulasyon_p.json
"""
import sys, json
NSP = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
sys.argv = [sys.argv[0], "1", "1"]
import numpy as np, pandas as pd
from multiprocessing import Pool
import simulasyon as S
from tezlib import *

C = S.C; est = S.est; ctry = S.ctry
muA = S.rA.extra["mu"]; y = est.ccm.values.astype(float)
a_i = pd.Series(((y - muA) ** 2 - muA) / muA ** 2).groupby(est.country.values).mean().clip(lower=0.002)
KEYS1, KEYS2 = PH, ["tstar", "S1", "F2", "S3"]


def simulate(dgp, rng):
    base, gam = (S.baseC, S.gC) if dgp == "C" else (S.baseA, S.gA)
    shock = np.zeros(len(S.years))
    if dgp == "B":
        e = rng.standard_normal(len(S.years)) * S.SIG * np.sqrt(1 - S.RHO ** 2); shock[0] = rng.standard_normal() * S.SIG
        for t in range(1, len(S.years)): shock[t] = S.RHO * shock[t - 1] + e[t]
    yy = np.zeros(len(est)); lnK1 = np.zeros(len(est))
    for c in ctry:
        k = S.K0[c]; al = S.aC if dgp == "C" else (S.aA if dgp == "A" else a_i[c])
        for j, i in enumerate(S.idx[c]):
            lnK1[i] = np.log(1 + k)
            mu = np.exp(base[i] + gam * lnK1[i] + shock[j])
            yy[i] = rng.poisson(rng.gamma(1 / al, al * mu))
            k = 0.85 * k + yy[i]
    d = est.copy(); d["ccm"] = yy; d["lnK1"] = lnK1
    return d


def one(args):
    dgp, seed = args
    rng = np.random.default_rng(seed); d = simulate(dgp, rng); out = {}
    try:
        for fam in ["poisson", "nb"]:
            r1 = fit(d, PH + C, fam, cluster=None if fam == "nb" else "country"); r2 = fit(d, ITS + C, fam, cluster=None if fam == "nb" else "country")
            out[fam] = [r1.coef(k) for k in KEYS1] + [r2.coef(k) for k in KEYS2] + [r1.coef("lnK1")]
    except Exception:
        return None
    return dgp, out


if __name__ == "__main__":
    R = json.load(open(ROOT / "analiz" / "cikti" / "sonuclar.json"))
    obs = {fam: [R["m1"][fam]["coef"][k]["b"] for k in KEYS1] + [R["m2"][fam]["coef"][k]["b"] for k in KEYS2] for fam in ["poisson", "nb"]}
    jobs = [(g, 50000 + 10 * i + j) for j, g in enumerate(["A", "A2", "B", "C"]) for i in range(NSP)]
    with Pool(4) as pool:
        res = [r for r in pool.imap_unordered(one, jobs, chunksize=16) if r]
    names = ["M1 Faz 1", "M1 Faz 2", "M1 Faz 3", "M2 ETS öncesi eğilim", "M2 Faz 1 eğim", "M2 Faz 2 düzey", "M2 Faz 3 eğim"]
    O = {"ayar": {"tekrar": NSP, "alpha_i": {TR[c]: float(a_i[c]) for c in ctry}, "gamma_A": float(S.gA), "gamma_C": float(S.gC)}, "katsayilar": names, "gozlenen": obs}
    for g in ["A", "A2", "B", "C"]:
        O[g] = {"n": sum(1 for x, _ in res if x == g)}
        for fam in ["poisson", "nb"]:
            M = np.array([o[fam] for x, o in res if x == g]); ob = np.array(obs[fam])
            D = M[:, :7]
            O[g][fam] = {"ort": D.mean(0).tolist(), "sd": D.std(0, ddof=1).tolist(), "q025": np.quantile(D, .025, 0).tolist(), "q975": np.quantile(D, .975, 0).tolist(),
                         "p_tek": ((D >= ob).mean(0)).tolist(), "p_cift": ((np.abs(D - D.mean(0)) >= np.abs(ob - D.mean(0))).mean(0)).tolist(),
                         "ort_gamma": float(M[:, 7].mean()), "f1_orneklem": np.round(D[:400, 0], 4).tolist(), "f2_orneklem": np.round(D[:400, 1], 4).tolist()}
    json.dump(O, open(ROOT / "analiz" / "cikti" / "simulasyon_p.json", "w"), indent=1, ensure_ascii=False)
    for g in ["A", "A2", "B", "C"]:
        for fam in ["poisson", "nb"]:
            o = O[g][fam]; print(g, fam, "n", O[g]["n"], "| ort", np.round(o["ort"], 3), "| sd", np.round(o["sd"], 3), "| p_tek", np.round(o["p_tek"], 3), "| p_cift", np.round(o["p_cift"], 3), "| gamma", round(o["ort_gamma"], 3))
    print("gozlenen", {f: np.round(v, 3).tolist() for f, v in obs.items()})
