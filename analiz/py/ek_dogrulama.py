"""Bağımsız hakem incelemesinin iddialarının ayrıca doğrulanması + Kao istatistiği.
Çıktı: analiz/cikti/ek_dogrulama.json
"""
import json
import numpy as np, pandas as pd
import statsmodels.api as sm
from scipy.stats import norm, chi2, t as tdist
from tezlib import *

rng = np.random.default_rng(12345)
df = load(); est = sample(df)
C = ["lnK1"] + CTRL5
out = {}

# 1) Model 2 ülke-içi VIF ve stok-zaman korelasyonu
cols = ITS + C
Xw = est[cols] - est.groupby("country")[cols].transform("mean")
out["vif_m2"] = {c: float(1 / (1 - sm.OLS(Xw[c], sm.add_constant(Xw.drop(columns=c))).fit().rsquared)) for c in cols}
w = est[["lnK1", "tstar", "F3", "renew_wdi_l1", "lngdp"]] - est.groupby("country")[["lnK1", "tstar", "F3", "renew_wdi_l1", "lngdp"]].transform("mean")
out["ici_kor"] = {"lnK1~zaman": float(w.lnK1.corr(w.tstar)), "F3~lnK1": float(w.F3.corr(w.lnK1)), "F3~yenilenebilir": float(w.F3.corr(w.renew_wdi_l1)),
                  "lngdp~lnK1": float(w.lngdp.corr(w.lnK1)), "lngdp~zaman": float(w.lngdp.corr(w.tstar))}

# 2) Stoksuz Model 2'nin eğilimi tek başına faz farklarını ne kadar üretir?
noK = [c for c in ITS + C if c != "lnK1"]
tr = {fam: fit(est, noK, fam).coef("tstar") for fam in ["poisson", "nb"]}
mid = {"pre": 3.5, "F1": 9.0, "F2": 13.0, "F3": 19.5}
a_nb = fit(est, [c for c in PH + C if c != "lnK1"], "nb"); a_p = fit(est, [c for c in PH + C if c != "lnK1"], "poisson")
out["egilim_katkisi"] = {fam: {f: {"egilimden": float(tr[fam] * (mid[f] - mid["pre"])), "stoksuz_faz_katsayisi": float((a_nb if fam == "nb" else a_p).coef(f))} for f in PH} for fam in ["poisson", "nb"]}
out["egilim_katkisi"]["egim"] = tr

# 3) Yıl etkileri: bootstrap SH ile anlamlılık
yrs = [y for y in range(1997, 2021) if y != 2004]
ey = est.copy()
for y in yrs: ey[f"y{y}"] = (ey.year == y).astype(float)
ycols = [f"y{y}" for y in yrs]
full = fit_poisson(ey, ycols + C)
D = []
for _ in range(1999):
    db, cid, _p = resample(ey, rng)
    r = fit_poisson(db, ycols + C, cid=cid)
    D.append([r.coef(c) for c in ycols])
D = np.array(D)
ye = {}
for j, y in enumerate(yrs):
    b = full.coef(f"y{y}"); se_b = D[:, j].std(ddof=1); lo, hi = np.quantile(D[:, j], [.025, .975]); bl, bh, z0 = bc_interval(D[:, j], b)
    ye[y] = {"b": b, "se_cl": full.stderr(f"y{y}"), "p_cl": full.p(f"y{y}"), "p_cl_t13": full.p(f"y{y}", "t"), "se_boot": float(se_b), "p_boot": float(2 * norm.sf(abs(b / se_b))),
             "pct": [float(lo), float(hi)], "bc": [bl, bh]}
out["yil_boot"] = ye

# 4) Plasebo kırılmaları: tüm olası yıllar, küme ve bootstrap çıkarsaması
pre = est[est.year <= 2004].reset_index(drop=True)
pl = {}
for tau in [1999, 2000, 2001, 2002, 2003]:
    d = pre.copy(); d["PF"] = (d.year >= tau).astype(float); d["PS"] = d.PF * (d.year - tau)
    pl[tau] = {}
    for fam in ["poisson", "nb"]:
        r = fit(d, ["tstar", "PF", "PS"] + C, fam)
        wj = r.wald(["PF", "PS"])
        Db = []
        for _ in range(999):
            db, cid, _p = resample(d, rng)
            try:
                rb = fit(db, ["tstar", "PF", "PS"] + C, fam, cid=cid, cluster=None) if fam == "nb" else fit_poisson(db, ["tstar", "PF", "PS"] + C, cid=cid)
                Db.append([rb.coef("PF"), rb.coef("PS")])
            except Exception:
                pass
        Db = np.array(Db); b = np.array([r.coef("PF"), r.coef("PS")]); Vb = np.cov(Db.T)
        wb = float(b @ np.linalg.solve(Vb, b))
        pl[tau][fam] = {"chi2_kume": wj["chi2"], "p_kume": wj["p"], "chi2_boot": wb, "p_boot": float(chi2.sf(wb, 2)), "PF": float(b[0]), "PS": float(b[1])}
out["plasebo"] = pl

# 5) Kao (1999) düzeltilmemiş istatistikleri — tezin hangi tanımı kullandığını bulmak için
def kao(d, dep, regs):
    d = d.sort_values(["country", "year"]).copy()
    Z = d[[dep] + regs]; Zd = Z - Z.groupby(d.country).transform("mean")
    y, X = Zd[dep].values, Zd[regs].values
    e = y - X @ np.linalg.lstsq(X, y, rcond=None)[0]
    d["e"] = e; d["e1"] = d.groupby("country").e.shift(1); dd = d.dropna(subset=["e1"])
    N = d.country.nunique(); T = int(dd.groupby("country").size().iloc[0])
    rho = (dd.e * dd.e1).sum() / (dd.e1 ** 2).sum(); v = dd.e - rho * dd.e1
    t_rho = (rho - 1) * np.sqrt((dd.e1 ** 2).sum()) / np.sqrt((v ** 2).sum() / len(dd))
    return {"DF_rho": float((np.sqrt(N) * T * (rho - 1) + 3 * np.sqrt(N)) / np.sqrt(10.2)), "DF_t": float(np.sqrt(1.25) * t_rho + np.sqrt(1.875 * N)), "rho": float(rho), "T": T}
k = {}
for y0 in (1996, 1997):
    d = df[df.year.between(y0, 2020)].copy(); d["lninten"] = np.log(d.ccm / d.gdp_real); d["lnK"] = np.log(1 + d.K)
    for dep in ("lninten", "inten"):
        k[f"{y0}-2020 | {dep}"] = kao(d, dep, ["lnK", "impdep", "manuf", "renew_wdi", "trade"])
out["kao"] = {"tez": {"DF_rho_duzeltilmemis": -18.260, "DF_t_duzeltilmemis": -11.434}, "hesap": k}

# 6) Küçük kontroller
tot = df.groupby("year").ccm.sum()
out["kucuk"] = {"g_log": float(np.mean(np.diff(np.log(tot.loc[1990:1996])))), "g_aritmetik": float(tot.loc[1990:1996].pct_change().mean()),
                "g_bilesik": float((tot[1996] / tot[1990]) ** (1 / 6) - 1), "max_ham_korelasyon": float(est[C].corr().abs().where(~np.eye(6, dtype=bool)).max().max()),
                "faz2_faz1_orani": {"nb": 0.2705 / 0.1338, "poisson": 0.1954 / 0.0772}}
json.dump(out, open(ROOT / "analiz" / "cikti" / "ek_dogrulama.json", "w"), ensure_ascii=False, indent=1, default=float)
print(json.dumps({k: out[k] for k in ["vif_m2", "ici_kor", "egilim_katkisi", "kao", "kucuk"]}, indent=1, default=float))
print("PLASEBO", json.dumps(pl, indent=0, default=float))
print("YIL", {y: (round(v["b"], 3), round(v["p_cl"], 3), round(v["p_boot"], 3)) for y, v in ye.items()})
