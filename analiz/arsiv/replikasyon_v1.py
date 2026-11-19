"""Beşinci bölüm replikasyonu — AB14_nihai_veri.xlsx

Çalıştırma (repo kökünden):
    pip install pandas numpy scipy statsmodels openpyxl
    python analiz/py/replikasyon.py            # ana modeller + tanılar
    python analiz/py/replikasyon.py --boot 1000  # + ülke düzeyinde kümelenmiş eşli bootstrap
"""
import argparse, warnings, pathlib
import numpy as np, pandas as pd, patsy
import statsmodels.api as sm
from statsmodels.discrete.discrete_model import NegativeBinomial
from scipy.stats import chi2, norm, t as tdist

warnings.filterwarnings("ignore")
ROOT = pathlib.Path(__file__).resolve().parents[2]
XLSX = ROOT / "veri" / "AB14_nihai_veri.xlsx"
DELTA = 0.15
CTRL = "lnK1 + gdp_growth_l1 + renew_wdi_l1 + impdep_l1 + manuf_l1 + trade_l1"
KEYS1 = ["F1", "F2", "F3", "lnK1", "gdp_growth_l1", "renew_wdi_l1", "impdep_l1", "manuf_l1", "trade_l1"]
KEYS2 = ["tstar", "F1", "S1", "F2", "S2", "F3", "S3", "lnK1", "trade_l1"]


def load():
    df = pd.read_excel(XLSX, sheet_name="Veri").sort_values(["country", "year"]).reset_index(drop=True)
    tot = df.groupby("year").ccm.sum()
    g = np.mean(np.diff(np.log(tot.loc[1990:1996].values)))
    K = []
    for _, d in df.groupby("country"):
        k = None
        for _, r in d.iterrows():
            k = r.ccm / (g + DELTA) if k is None else (1 - DELTA) * k + r.ccm
            K.append(k)
    df["K"] = K
    df["lnK1"] = np.log(1 + df.groupby("country").K.shift(1))
    for v in ["gdp_growth", "renew_wdi", "impdep", "manuf", "trade"]:
        df[v + "_l1"] = df.groupby("country")[v].shift(1)
    df["lngdp"] = np.log(df.gdp_real)
    df["F1"] = df.year.between(2005, 2007).astype(int)
    df["F2"] = df.year.between(2008, 2012).astype(int)
    df["F3"] = df.year.between(2013, 2020).astype(int)
    df["ETS"] = (df.year >= 2005).astype(int)
    df["tstar"] = df.year - 1997
    for k, a in enumerate([2005, 2008, 2013], 1):
        df[f"S{k}"] = np.where(df[f"F{k}"] == 1, df.year - a, 0)
    est = df[df.year.between(1997, 2020)].copy()
    est["cid"] = est.country
    return est, g


def design(formula, d, exposure=True):
    y, X = patsy.dmatrices(formula, d, return_type="dataframe")
    D = pd.get_dummies(d["cid"].astype(str), prefix="c", drop_first=True, dtype=float).set_index(X.index)
    X = pd.concat([X, D], axis=1)
    off = np.log(d.gdp_real.values) if exposure else None
    return y, X, off


def fit(formula, d, fam="poisson", cov="cluster", exposure=True):
    y, X, off = design(formula, d, exposure)
    groups = pd.factorize(d.country)[0]
    kw = dict(cov_type="cluster", cov_kwds={"groups": groups}) if cov == "cluster" else {}
    if fam == "poisson":
        return sm.GLM(y, X, family=sm.families.Poisson(), offset=off).fit(**kw)
    return NegativeBinomial(y, X, offset=off).fit(disp=0, maxiter=1000, **kw)


def show(r, keys, title=None):
    if title:
        print(title)
    for k in keys:
        if k in r.params:
            b, s = r.params[k], r.bse[k]
            print(f"  {k:14s} {b: .4f} ({s:.4f})  p={2 * norm.sf(abs(b / s)):.3f}")


def wald_eq(r, a, b):
    V = r.cov_params(); d = r.params[a] - r.params[b]
    w = d * d / (V.loc[a, a] + V.loc[b, b] - 2 * V.loc[a, b])
    return round(w, 2), round(chi2.sf(w, 1), 3)


def wald_joint(r, ks):
    b = r.params[ks].values; V = r.cov_params().loc[ks, ks].values
    w = b @ np.linalg.solve(V, b)
    return round(w, 2), round(chi2.sf(w, len(ks)), 3)


def twoway_se(formula, d, keys):
    y, X, off = design(formula, d)
    m = sm.GLM(y, X, family=sm.families.Poisson(), offset=off)
    Vc = m.fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(d.country)[0]}).cov_params()
    Vt = m.fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(d.year)[0]}).cov_params()
    Vh = m.fit(cov_type="HC0").cov_params()
    V = Vc + Vt - Vh
    b = m.fit().params
    print("İki yönlü kümeleme (ülke & yıl), Poisson:")
    for k in keys:
        se = np.sqrt(V.loc[k, k])
        print(f"  {k:10s} b={b[k]: .4f} SE_ülke={np.sqrt(Vc.loc[k, k]):.4f} SE_yıl={np.sqrt(Vt.loc[k, k]):.4f} SE_2y={se:.4f} p={2 * norm.sf(abs(b[k] / se)):.3f}")


def jackknife(formula, d, fam, keys):
    ctry = list(d.country.unique()); G = len(ctry)
    full = fit(formula, d, fam, cov="none").params[keys]
    J = np.array([fit(formula, d[d.country != c], fam, cov="none").params[keys].values for c in ctry])
    se = np.sqrt((G - 1) / G * ((J - J.mean(0)) ** 2).sum(0))
    print(f"Küme jackknife (CV3) SH, t({G - 1}) p — {fam}:")
    for i, k in enumerate(keys):
        print(f"  {k:10s} b={full[k]: .4f} SE={se[i]:.4f} p={2 * tdist.sf(abs(full[k] / se[i]), G - 1):.3f}")


def bootstrap(formula, d, fam, keys, B, seed=12345):
    bhat = fit(formula, d, fam, cov="none").params[keys]
    rng = np.random.default_rng(seed); ctry = d.country.unique(); out = []
    for _ in range(B):
        pick = rng.choice(ctry, size=len(ctry), replace=True)
        db = pd.concat([d[d.country == c].assign(cid=f"{c}_{j}") for j, c in enumerate(pick)])
        try:
            out.append(fit(formula, db, fam, cov="none").params[keys].values)
        except Exception:
            pass
    bs = np.array(out); se = bs.std(axis=0, ddof=1)
    print(f"Kümelenmiş eşli bootstrap — {fam}, B={len(bs)}:")
    for i, k in enumerate(keys):
        z0 = norm.ppf((bs[:, i] < bhat[k]).mean())
        a1, a2 = norm.cdf(2 * z0 + norm.ppf(.025)), norm.cdf(2 * z0 + norm.ppf(.975))
        lo, hi = np.quantile(bs[:, i], [a1, a2]); plo, phi = np.quantile(bs[:, i], [.025, .975])
        print(f"  {k:14s} b={bhat[k]: .4f} SE={se[i]:.4f} p={2 * norm.sf(abs(bhat[k] / se[i])):.3f} BC[{lo: .4f};{hi: .4f}] pct[{plo: .4f};{phi: .4f}] z0={z0: .2f}")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--boot", type=int, default=0); a = ap.parse_args()
    est, g = load()
    print(f"N={len(est)}  g={g:.4f}")
    M1 = f"ccm ~ F1 + F2 + F3 + {CTRL}"
    M2 = f"ccm ~ tstar + F1 + S1 + F2 + S2 + F3 + S3 + {CTRL}"

    p1 = fit(M1, est, "poisson"); n1 = fit(M1, est, "nb")
    show(p1, KEYS1, "\n== Model 1 Poisson QML (cluster SH)"); show(n1, KEYS1, "== Model 1 NB (ülke kuklaları, cluster SH)")
    print("  alpha =", round(n1.params["alpha"], 4), " LR(alpha=0) =", round(2 * (fit(M1, est, "nb", "none").llf - fit(M1, est, "poisson", "none").llf), 2))
    print("  Wald d1=d2 / d2=d3: P", wald_eq(p1, "F1", "F2"), wald_eq(p1, "F2", "F3"), " NB", wald_eq(n1, "F1", "F2"), wald_eq(n1, "F2", "F3"))

    p2 = fit(M2, est, "poisson"); n2 = fit(M2, est, "nb")
    show(p2, KEYS2, "\n== Model 2 Poisson"); show(n2, KEYS2, "== Model 2 NB")
    print("  Ortak faz testleri: P", [wald_joint(p2, [f"F{k}", f"S{k}"]) for k in (1, 2, 3)], " NB", [wald_joint(n2, [f"F{k}", f"S{k}"]) for k in (1, 2, 3)])

    M2a = M2.replace("lnK1 + ", "")
    show(fit(M2a, est, "poisson"), KEYS2, "\n== Model 2 STOKSUZ Poisson (tezde yok)"); show(fit(M2a, est, "nb"), KEYS2, "== Model 2 STOKSUZ NB")

    Ma = M1.replace("lnK1 + ", "")
    show(fit(Ma, est, "poisson"), ["F1", "F2", "F3"], "\n== (a) stoksuz Poisson"); show(fit(Ma, est, "nb"), ["F1", "F2", "F3"], "== (a) stoksuz NB")
    show(fit(M1 + " + lngdp", est, "poisson", exposure=False), ["F1", "F2", "F3", "lngdp"], "== (b) GSYİH serbest Poisson")
    show(fit(M1 + " + lngdp", est, "nb", exposure=False), ["F1", "F2", "F3", "lngdp"], "== (b) GSYİH serbest NB")
    e2 = est[est.country != "Germany"]
    show(fit(M1, e2, "poisson"), ["F1", "F2", "F3"], "== (c) Almanya hariç Poisson"); show(fit(M1, e2, "nb"), ["F1", "F2", "F3"], "== (c) Almanya hariç NB")

    Mh = f"ccm ~ ETS + {CTRL}"
    show(fit(Mh, est, "poisson"), ["ETS"], "\n== Tek ETS kuklası (H1) Poisson"); show(fit(Mh, est, "nb"), ["ETS"], "== Tek ETS kuklası NB")

    print()
    twoway_se(M1, est, ["F1", "F2", "F3", "lnK1"])
    jackknife(M1, est, "poisson", ["F1", "F2", "F3", "lnK1"]); jackknife(M1, est, "nb", ["F1", "F2", "F3", "lnK1"])

    if a.boot:
        print()
        bootstrap(M1, est, "poisson", KEYS1, a.boot); bootstrap(M1, est, "nb", KEYS1, a.boot)


if __name__ == "__main__":
    main()
