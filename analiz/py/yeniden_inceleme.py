"""5. Bölümün sıfırdan, bağımsız yeniden incelemesi.

Çalıştırma (repo kökünden):  python analiz/py/yeniden_inceleme.py
Çıktı: analiz/cikti/sonuclar.json, analiz/cikti/panel.json  (site: docs/data/ altına kopyalanır)
"""
import json, itertools, time, sys
import numpy as np, pandas as pd
from scipy.stats import norm, chi2, t as tdist, skew
from tezlib import *
import tez_degerleri as TEZ

B = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
SEED = 12345
OUT = ROOT / "analiz" / "cikti"; OUT.mkdir(parents=True, exist_ok=True)
R = {"meta": {"B": B, "seed": SEED, "tarih": time.strftime("%Y-%m-%d")}}
C = ["lnK1"] + CTRL5
M1, M2 = PH + C, ITS + C
df = load(); est = sample(df)
G = est.country.nunique()
R["meta"].update({"N": len(est), "G": G, "g": df.attrs["g"]})


def rnd(x, k=4):
    if isinstance(x, dict): return {a: rnd(b, k) for a, b in x.items()}
    if isinstance(x, (list, tuple)): return [rnd(a, k) for a in x]
    if isinstance(x, (float, np.floating)): return None if not np.isfinite(x) else round(float(x), k)
    if isinstance(x, (np.integer,)): return int(x)
    if isinstance(x, np.ndarray): return rnd(x.tolist(), k)
    return x


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


# ------------------------------------------------------------------ 1. VERİ DENETİMİ
log("1 veri denetimi")
raw = pd.read_excel(XLSX, sheet_name="Veri")
gcalc = raw.sort_values(["country", "year"]).groupby("country").gdp_real.pct_change() * 100
xs = pd.read_excel(XLSX, sheet_name="Yesil_stok", header=None).iloc[20:, :6]
xs.columns = ["country", "year", "ccm", "K", "lnK", "lnK1"]; xs = xs.dropna(subset=["country", "year"])
xs["year"] = xs.year.astype(int)
mk = df.merge(xs[["country", "year", "K"]], on=["country", "year"], suffixes=("", "_x"))
lagwin = df[df.year.between(1996, 2019)]
ext = lambda d, v, f: [TR[d.loc[getattr(d[v], "idx" + f)(), "country"]], int(d.loc[getattr(d[v], "idx" + f)(), "year"]), float(getattr(d[v], f)())]
R["veri"] = {
    "satir": len(raw), "ulke": int(raw.country.nunique()), "yil": [int(raw.year.min()), int(raw.year.max())],
    "mukerrer": int(raw.duplicated(["country", "year"]).sum()),
    "dengeli": bool((raw.groupby("country").year.count() == 31).all()),
    "eksik_tahmin_orneklemi": int(est[["ccm", "gdp_real", "lnK1"] + CTRL5].isna().sum().sum()),
    "eksik_yillar": {c: [int(y) for y in raw[raw[c].isna()].year.unique()] for c in raw.columns if raw[c].isna().any()},
    "sifir_ccm": [[TR[r.country], int(r.year)] for r in raw[raw.ccm == 0].itertuples()],
    "buyume_tutarlilik_max_fark": float((gcalc - raw.sort_values(["country", "year"]).gdp_growth).abs().max()),
    "stok_excel_max_fark": float((mk.K - mk.K_x.astype(float)).abs().max()),
    "yuvarlama_yarim": int(((est.ccm_frac % 1) == 0.5).sum()),
    "yuvarlama_max_fark": float((raw.ccm - raw.ccm_frac).abs().max()),
    "toplam_ccm": int(est.ccm.sum()), "medyan": float(est.ccm.median()), "carpiklik": float(est.ccm.skew()),
    "pay": {TR[c]: float(est[est.country == c].ccm.sum() / est.ccm.sum() * 100) for c in est.country.unique()},
    "yillik_toplam": {int(y): int(v) for y, v in df.groupby("year").ccm.sum().items()},
    "uc": {"ccm_max": ext(est, "ccm", "max"), "ccm_min": ext(est, "ccm", "min"), "inten_max": ext(est, "inten", "max"),
           "inten_min": ext(est, "inten", "min"), "buyume_max": ext(lagwin, "gdp_growth", "max"), "buyume_min": ext(lagwin, "gdp_growth", "min"),
           "impdep_min": ext(lagwin, "impdep", "min"), "trade_max": ext(lagwin, "trade", "max")},
    "yogunluk_ulke": {TR[c]: [float(d[d.year <= 2004].inten.mean()), float(d[d.year >= 2005].inten.mean())] for c, d in est.groupby("country")},
}
panel = df[df.year >= 1990][["country", "year", "ccm", "ccm_frac", "gdp_real", "inten", "K", "lnK1", "gdp_growth", "renew_wdi", "impdep", "manuf", "trade"]].copy()
panel["country"] = panel.country.map(TR)
json.dump(json.loads(panel.round(4).to_json(orient="records")), open(OUT / "panel.json", "w"), ensure_ascii=False)

# ------------------------------------------------------------------ 2. TANIMLAYICI
log("2 tanimlayici")
est["gdp_bn"] = est.gdp_real / 1000
t52 = {}
for v, tz in TEZ.T52.items():
    s = est[v]; mine = (s.mean(), s.std(), s.min(), s.max())
    t52[v] = {"tez": tz, "hesap": rnd(mine, 3), "uyum": bool(all(abs(a - b) <= 0.006 * max(1, abs(b)) + 0.006 for a, b in zip(mine, tz)))}
per = np.select([est.year <= 2004, est.year <= 2007, est.year <= 2012], ["pre", "F1", "F2"], "F3")
t53 = {}
for p in ["pre", "F1", "F2", "F3"]:
    d = est[per == p]
    t53[p] = {"tez": TEZ.T53[p],
              "es": dict(n=len(d), ccm=d.ccm.mean(), inten=d.inten.mean(), K=d.K.mean(), renew=d.renew_wdi.mean(), impdep=d.impdep.mean(), manuf=d.manuf.mean(), trade=d.trade.mean(), growth=d.gdp_growth.mean()),
              "gec": dict(n=len(d), K=float(np.mean(np.exp(d.lnK1) - 1)), renew=d.renew_wdi_l1.mean(), impdep=d.impdep_l1.mean(), manuf=d.manuf_l1.mean(), trade=d.trade_l1.mean(), growth=d.gdp_growth_l1.mean())}
cr = est[C].corr()
cw = (est[C] - est.groupby("country")[C].transform("mean")).corr()
t54 = [{"a": a, "b": b, "tez": v, "ham": float(cr.loc[a, b]), "ici": float(cw.loc[a, b])} for (a, b), v in TEZ.T54.items()]
Xv = est[PH + C] - est.groupby("country")[PH + C].transform("mean")
vif = {c: float(1 / (1 - sm.OLS(Xv[c], sm.add_constant(Xv.drop(columns=c))).fit().rsquared)) for c in Xv.columns}
R["tanim"] = {"t52": t52, "t53": rnd(t53, 2), "t54": rnd(t54, 2), "vif": {k: {"tez": TEZ.T56[k], "hesap": round(v, 2)} for k, v in vif.items()}}

# ------------------------------------------------------------------ 3. ANA MODELLER + ÇIKARSAMA
log("3 ana modeller")


def jack(d, cols, fam, keys, **kw):
    ctry = pd.unique(d.country); Gj = len(ctry)
    J = np.array([[fit(d[d.country != c], cols, fam, cluster=None if fam == "nb" else "country", **kw).coef(k) for k in keys] for c in ctry])
    se = np.sqrt((Gj - 1) / Gj * ((J - J.mean(0)) ** 2).sum(0))
    return se, J


def wild_score(res, keys):
    """Kline-Santos skor wild küme bootstrap'ı, Rademacher ağırlıklarının TAM sayımı (2^G)."""
    X, y, mu = res.extra["X"], res.extra["y"], res.extra["mu"]
    Ai = np.linalg.inv((X.T * mu) @ X)
    S = X * (y - mu)[:, None]
    codes, _ = pd.factorize(est.country.values if len(y) == len(est) else np.arange(len(y)))
    Gw = codes.max() + 1
    Sg = np.zeros((Gw, X.shape[1])); np.add.at(Sg, codes, S)
    W = np.array(list(itertools.product([-1.0, 1.0], repeat=Gw)))
    out = {}
    D = W @ (Sg @ Ai.T)  # her satır: beta* - beta^
    for k in keys:
        j = res.i(k)
        tstar = D[:, j] / res.stderr(k)  # Rademacher: w^2=1 => V* = V^
        that = res.coef(k) / res.stderr(k)
        out[k] = float(np.mean(np.abs(tstar) >= abs(that) - 1e-12))
    return out


def eff_clusters(res, keys, d):
    """Carter-Schnepel-Steigerwald etkin küme sayısı G* (Poisson ağırlıklı)."""
    X, mu = res.extra["X"], res.extra["mu"]
    Ai = np.linalg.inv((X.T * mu) @ X)
    out = {}
    for k in keys:
        a = Ai[res.i(k)]
        gam = np.array([a @ ((X[idx].T * mu[idx]) @ X[idx]) @ a for idx in [np.where(d.country.values == c)[0] for c in pd.unique(d.country)]])
        Gam = np.mean(((gam - gam.mean()) / gam.mean()) ** 2)
        out[k] = float(len(gam) / (1 + Gam))
    return out


def model_block(cols, keys, label):
    blk = {}
    for fam in ["poisson", "nb"]:
        r = fit(est, cols, fam)
        r2 = fit(est, cols, fam, cluster="twoway")
        ry = fit(est, cols, fam, cluster="year")
        se3, _ = jack(est, cols, fam, keys)
        o = {"coef": {}, "aic": r.extra["aic"], "bic": r.extra["bic"], "llf": r.llf}
        for j, k in enumerate(keys):
            b = r.coef(k)
            o["coef"][k] = {"b": b, "se_cl": r.stderr(k), "p_cl": r.p(k), "p_cl_t": r.p(k, "t"),
                            "se_2w": r2.stderr(k), "p_2w": r2.p(k), "se_yr": ry.stderr(k),
                            "se_cv3": float(se3[j]), "p_cv3": float(2 * tdist.sf(abs(b / se3[j]), G - 1))}
        if fam == "nb":
            a = r.coef("alpha"); sa = float(np.sqrt(r.extra["Vml"][-1, -1]))
            o["alpha"] = a; o["alpha_ci"] = [a * np.exp(-1.96 * sa / a), a * np.exp(1.96 * sa / a)]
        else:
            ws = wild_score(r, [k for k in keys])
            ge = eff_clusters(r, keys, est)
            for k in keys: o["coef"][k]["p_wild"] = ws[k]; o["coef"][k]["Gstar"] = ge[k]
        o["_res"] = r
        blk[fam] = o
    blk["LR"] = 2 * (blk["nb"]["llf"] - blk["poisson"]["llf"])
    blk["LR_p"] = float(0.5 * chi2.sf(blk["LR"], 1))
    return blk


m1 = model_block(M1, PH + C, "M1")
m2 = model_block(M2, ITS + C, "M2")
for fam in ["poisson", "nb"]:
    r = m1[fam]["_res"]; m1[fam]["wald_cl"] = {"d1=d2": r.wald_eq("F1", "F2"), "d2=d3": r.wald_eq("F2", "F3")}
    r = m2[fam]["_res"]; m2[fam]["joint_cl"] = [r.wald([f"F{k}", f"S{k}"]) for k in (1, 2, 3)]
# Poisson / NB örtük ağırlık payları (Almanya)
mu = m1["poisson"]["_res"].extra["mu"]; a = m1["nb"]["alpha"]
wP = pd.Series(mu).groupby(est.country.values).sum(); wN = pd.Series(mu / (1 + a * mu)).groupby(est.country.values).sum()
R["agirlik"] = {TR[c]: [float(wP[c] / wP.sum() * 100), float(wN[c] / wN.sum() * 100)] for c in wP.index}

# ------------------------------------------------------------------ 4. BOOTSTRAP
log("4 bootstrap")


def boot(d, cols, fam, keys, exposure="fixed", Bn=B, seed=SEED, tstat=False):
    rng = np.random.default_rng(seed)
    full = fit(d, cols, fam, exposure=exposure)
    bhat = np.array([full.coef(k) for k in keys]); sehat = np.array([full.stderr(k) for k in keys])
    draws, ts, nde, fail = [], [], [], 0
    for _ in range(Bn):
        db, cid, picked = resample(d, rng)
        try:
            if fam == "poisson":
                rb = fit_poisson(db, cols, exposure=exposure, cid=cid)
            else:
                rb = fit_nb(db, cols, exposure=exposure, cid=cid, cluster=None)
                if not rb.extra["conv"]: fail += 1; continue
            bb = np.array([rb.coef(k) for k in keys])
            if not np.all(np.isfinite(bb)) or np.max(np.abs(bb)) > 50: fail += 1; continue
            draws.append(bb); nde.append(picked.count("Germany"))
            if tstat and fam == "poisson":
                ts.append((bb - bhat) / np.array([rb.stderr(k) for k in keys]))
        except Exception:
            fail += 1
    D = np.array(draws); nde = np.array(nde)
    out = {"B_ok": len(D), "fail": fail, "coef": {}}
    Vb = np.cov(D.T, ddof=1)
    for j, k in enumerate(keys):
        x = D[:, j]; se = x.std(ddof=1)
        lo, hi, z0 = bc_interval(x, bhat[j]); plo, phi = np.quantile(x, [.025, .975])
        o = {"b": bhat[j], "se": se, "p": float(2 * norm.sf(abs(bhat[j] / se))), "bc": [lo, hi], "pct": [float(plo), float(phi)], "z0": z0,
             "mean": float(x.mean()), "median": float(np.median(x)), "skew": float(skew(x)),
             "mean_noDE": float(x[nde == 0].mean()), "mean_DE": float(x[nde > 0].mean())}
        if tstat and fam == "poisson":
            T = np.array(ts)[:, j]; q = np.quantile(T, [.025, .975])
            o["pt"] = [float(bhat[j] - q[1] * sehat[j]), float(bhat[j] - q[0] * sehat[j])]
            o["p_pt"] = float(np.mean(np.abs(T) >= abs(bhat[j] / sehat[j])))
        out["coef"][k] = o
    out["share_noDE"] = float(np.mean(nde == 0))
    out["_D"], out["_V"], out["_b"], out["_keys"] = D, Vb, bhat, keys
    return out


def bwald(bo, ks, r=None):
    idx = [bo["_keys"].index(k) for k in ks]
    b = bo["_b"][idx] - (0 if r is None else np.asarray(r))
    w = float(b @ np.linalg.solve(bo["_V"][np.ix_(idx, idx)], b))
    return {"chi2": w, "df": len(ks), "p": float(chi2.sf(w, len(ks)))}


def bwald_eq(bo, a, b_):
    ia, ib = bo["_keys"].index(a), bo["_keys"].index(b_); V = bo["_V"]
    w = float((bo["_b"][ia] - bo["_b"][ib]) ** 2 / (V[ia, ia] + V[ib, ib] - 2 * V[ia, ib]))
    return {"chi2": w, "df": 1, "p": float(chi2.sf(w, 1))}


BO = {}
for fam in ["poisson", "nb"]:
    b1 = boot(est, M1, fam, PH + C, tstat=True); b2 = boot(est, M2, fam, ITS + C, tstat=True)
    b1["wald"] = {"d1=d2": bwald_eq(b1, "F1", "F2"), "d2=d3": bwald_eq(b1, "F2", "F3")}
    b2["joint"] = [bwald(b2, [f"F{k}", f"S{k}"]) for k in (1, 2, 3)]
    b1s = boot(est, M1, fam, PH + C, seed=2026)  # Monte Carlo duyarlılığı
    b1["seed2"] = {k: {"se": b1s["coef"][k]["se"], "bc": b1s["coef"][k]["bc"]} for k in PH + C}
    BO[fam] = {"m1": b1, "m2": b2}
    log("  boot", fam, "ok", b1["B_ok"], b2["B_ok"])
    m1[fam]["boot"] = b1; m2[fam]["boot"] = b2
hist = {}
for fam in ["poisson", "nb"]:
    D = BO[fam]["m1"]["_D"]
    hist[fam] = {k: rnd(D[:, j].tolist(), 4) for j, k in enumerate(PH + C)}
json.dump(hist, open(OUT / "bootstrap_m1.json", "w"))

# ------------------------------------------------------------------ 5. TEZDEKİ SAĞLAMLIK TABLOLARI
log("5 saglamlik")
SAG = {}
noK = [c for c in M1 if c != "lnK1"]
specs = {"a": (est, noK, "fixed"), "b": (est, M1, "free"), "c": (est[est.country != "Germany"].reset_index(drop=True), M1, "fixed")}
for nm, (d, cols, expo) in specs.items():
    SAG[nm] = {}
    for fam in ["poisson", "nb"]:
        keys = PH + (["lngdp"] if expo == "free" else [])
        bo = boot(d, cols, fam, keys, exposure=expo)
        r = fit(d, cols, fam, exposure=expo)
        SAG[nm][fam] = {k: {"b": r.coef(k), "se_cl": r.stderr(k), "se_boot": bo["coef"][k]["se"], "p_boot": bo["coef"][k]["p"]} for k in keys}
        SAG[nm][fam]["tez"] = TEZ.T514[nm][fam]
        if expo == "free":
            e, s = r.coef("lngdp"), bo["coef"]["lngdp"]["se"]
            SAG[nm][fam]["elast_test_boot"] = {"chi2": float(((e - 1) / s) ** 2), "p": float(chi2.sf(((e - 1) / s) ** 2, 1)), "tez": TEZ.T514["elast"][fam]}
            SAG[nm][fam]["elast_test_cl"] = float(((e - 1) / r.stderr("lngdp")) ** 2)
            base = fit(est, M1, fam)
            SAG[nm][fam]["aic"] = {"sabit": base.extra["aic"], "serbest": r.extra["aic"], "bic_sabit": base.extra["bic"], "bic_serbest": r.extra["bic"]}
            SAG[nm][fam]["lnK1"] = r.coef("lnK1")
log("  loo")
LOO = {}
for c in pd.unique(est.country):
    d = est[est.country != c].reset_index(drop=True)
    bo = boot(d, M1, "poisson", PH)
    LOO[TR[c]] = {"hesap": [[bo["coef"][k]["b"], bo["coef"][k]["p"], bo["coef"][k]["bc"]] for k in PH], "tez": TEZ.T515[c]}
    rn = fit_nb(d, M1, cluster=None); LOO[TR[c]]["nb"] = [rn.coef(k) for k in PH]
log("  yil etkileri, plasebo, gecikme")
yrs = [y for y in range(1997, 2021) if y != 2004]
ey = est.copy()
for y in yrs: ey[f"y{y}"] = (ey.year == y).astype(float)
YE = {}
for fam in ["poisson", "nb"]:
    ry = fit(ey, [f"y{y}" for y in yrs] + C, fam)
    YE[fam] = {"yil": {y: [ry.coef(f"y{y}"), ry.stderr(f"y{y}")] for y in yrs}, "lnK1": ry.coef("lnK1")}
# stoksuz yıl etkileri
ry0 = fit(ey, [f"y{y}" for y in yrs] + CTRL5, "poisson"); YE["poisson_stoksuz"] = {"yil": {y: [ry0.coef(f"y{y}"), ry0.stderr(f"y{y}")] for y in yrs}}
pre = est[est.year <= 2004].reset_index(drop=True)
PL = {}
for tau in [1999, 2000, 2001, 2002, 2003]:
    d = pre.copy(); d["PF"] = (d.year >= tau).astype(float); d["PS"] = d.PF * (d.year - tau)
    PL[tau] = {}
    for fam in ["poisson", "nb"]:
        try:
            r = fit(d, ["tstar", "PF", "PS"] + C, fam)
            w = r.wald(["PF", "PS"])
            PL[tau][fam] = {"chi2": w["chi2"], "p": w["p"], "PF": [r.coef("PF"), r.stderr("PF")], "PS": [r.coef("PS"), r.stderr("PS")],
                            "tez": TEZ.T516.get(tau, {}).get(fam)}
        except Exception as ex:
            PL[tau][fam] = {"hata": str(ex)}
# gecikme seçimi
df2 = load(lag=2); e1 = sample(df, 1998, 2020); e2 = sample(df2, 1998, 2020)
e_mix = e1.copy(); e_mix[CTRL5] = e2[CTRL5].values  # yalnız kontroller 2 gecikmeli, stok 1
LAG = {"nb": {"lag1": fit_nb(e1, M1, cluster=None).extra["aic"], "lag2_hepsi": fit_nb(e2, M1, cluster=None).extra["aic"],
              "lag2_yalniz_kontrol": fit_nb(e_mix, M1, cluster=None).extra["aic"]},
       "poisson": {"lag1": fit_poisson(e1, M1).extra["aic"], "lag2_hepsi": fit_poisson(e2, M1).extra["aic"]},
       "tez": TEZ.AIC, "N": len(e1)}
r2l = fit(e2, M1, "nb"); LAG["lag2_coef"] = {k: [r2l.coef(k), r2l.stderr(k)] for k in PH}

# ------------------------------------------------------------------ 6. EK ANALİZLER
log("6 ek analizler")
EK = {}


def quick(d, cols, keys, exposure="fixed", fe=True):
    o = {}
    for fam in ["poisson", "nb"]:
        r = fit(d, cols, fam, exposure=exposure, fe=fe)
        o[fam] = {k: {"b": r.coef(k), "se": r.stderr(k), "p": r.p(k), "p_t": r.p(k, "t")} for k in keys}
        o[fam]["_aic"] = r.extra["aic"]
    return o


EK["m2_stoksuz"] = quick(est, [c for c in M2 if c != "lnK1"], ITS)
EK["m2_stoksuz_boot"] = {fam: {k: {"se": v["se"], "p": v["p"], "bc": v["bc"]} for k, v in boot(est, [c for c in M2 if c != "lnK1"], fam, ITS)["coef"].items()} for fam in ["poisson", "nb"]}
EK["ets_tek"] = quick(est, ["ETS"] + C, ["ETS", "lnK1"])
EK["ets_tek_stoksuz"] = quick(est, ["ETS"] + CTRL5, ["ETS"])
EK["ets_tek_boot"] = {fam: boot(est, ["ETS"] + C, fam, ["ETS"])["coef"]["ETS"] for fam in ["poisson", "nb"]}
EK["m1_trend"] = quick(est, PH + ["tstar"] + C, PH + ["tstar", "lnK1"])
EK["m1_trend_stoksuz"] = quick(est, PH + ["tstar"] + CTRL5, PH + ["tstar"])
est["t2"] = est.tstar ** 2
EK["m1_trend2"] = quick(est, PH + ["tstar", "t2"] + C, PH)
est["ANT"] = est.year.between(2003, 2004).astype(float)
EK["beklenti"] = quick(est, ["ANT"] + M1, ["ANT"] + PH)
est["F2a"] = est.year.between(2008, 2009).astype(float); est["F2b"] = est.year.between(2010, 2012).astype(float)
EK["faz2_bolunmus"] = quick(est, ["F1", "F2a", "F2b", "F3"] + C, ["F1", "F2a", "F2b", "F3"])
est["F3a"] = est.year.between(2013, 2016).astype(float); est["F3b"] = est.year.between(2017, 2020).astype(float)
EK["faz3_bolunmus"] = quick(est, ["F1", "F2", "F3a", "F3b"] + C, ["F1", "F2", "F3a", "F3b"])
EK["kontrolsuz"] = quick(est, PH + ["lnK1"], PH + ["lnK1"])
EK["yalniz_faz"] = quick(est, PH, PH)
EK["kesirli"] = {k: v for k, v in zip(PH + ["lnK1"], [fit_poisson(est, M1, depvar="ccm_frac").coef(k) for k in PH + ["lnK1"]])}
for nm, d in {"2020_haric": est[est.year <= 2019], "2018_2020_haric": est[est.year <= 2017], "irlanda_haric": est[est.country != "Ireland"],
              "luksemburg_haric": est[est.country != "Luxembourg"], "DE_FR_haric": est[~est.country.isin(["Germany", "France"])]}.items():
    EK[nm] = quick(d.reset_index(drop=True), M1, PH + ["lnK1"])
for dl in [0.05, 0.10, 0.20, 0.25]:
    EK[f"delta_{dl}"] = quick(sample(load(delta=dl)), M1, PH + ["lnK1"])
# pre-sample mean (BGW 2002): ülke kuklası yerine ln(1990-96 ort. ccm) ve ln(1995-96 ort. GSYİH)
psm = df[df.year.between(1990, 1996)].groupby("country").ccm.mean(); pg = df[df.year.between(1995, 1996)].groupby("country").gdp_real.mean()
est["lnpsm"] = np.log(est.country.map(psm)); est["lnpg"] = np.log(est.country.map(pg))
EK["presample"] = quick(est, M1 + ["lnpsm", "lnpg"], PH + ["lnK1", "lnpsm"], fe=False)
# ülke heterojenliği: ülke x faz (ortak stok ve kontroller)
eh = est.copy(); hk = []
for c in pd.unique(est.country):
    for f in PH:
        eh[f"{f}_{c}"] = eh[f] * (eh.country == c); hk.append(f"{f}_{c}")
rh = fit_poisson(eh, hk + C)
EK["heterojen"] = {TR[c]: [rh.coef(f"{f}_{c}") for f in PH] for c in pd.unique(est.country)}
# ülke bazında basit önce-sonra (ham yoğunluk log farkı)
EK["ham_log_fark"] = {TR[c]: [float(np.log(d[d[f] == 1].inten.mean() / d[d.year <= 2004].inten.mean())) for f in PH] for c, d in est.groupby("country")}
# plasebo gücü: en küçük saptanabilir etki (MDE ~ 2.8 x SH)
EK["plasebo_guc"] = {tau: {fam: {"se_PF": v[fam]["PF"][1], "se_PS": v[fam]["PS"][1], "mde_PS": 2.8 * v[fam]["PS"][1], "mde_PF": 2.8 * v[fam]["PF"][1]} for fam in ["poisson", "nb"] if "PF" in v[fam]} for tau, v in PL.items()}
# Model 2'nin ETS-öncesi eğilimi yalnızca 8 yıldan tanımlanıyor: alt örneklem
EK["pre_egilim"] = {"stoklu": quick(pre, ["tstar"] + C, ["tstar", "lnK1"]), "stoksuz": quick(pre, ["tstar"] + CTRL5, ["tstar"])}

# spesifikasyon eğrisi
log("  spesifikasyon egrisi")
SC = []
dcache = {}
for dl, lg in itertools.product([0.10, 0.15, 0.20], [1, 2]):
    dcache[(dl, lg)] = load(delta=dl, lag=lg)
samples = {"tam": lambda d: d, "Almanya hariç": lambda d: d[d.country != "Germany"], "İrlanda hariç": lambda d: d[d.country != "Ireland"],
           "Lüksemburg hariç": lambda d: d[d.country != "Luxembourg"], "Danimarka hariç": lambda d: d[d.country != "Denmark"],
           "2020 hariç": lambda d: d[d.year <= 2019], "1998–2017": lambda d: d[d.year <= 2017]}
for fam, stok, expo, ctrl, smp, lg, trend in itertools.product(["poisson", "nb"], [True, False], ["fixed", "free"], ["tam", "yok"], samples, [1, 2], [False, True]):
    for dl in ([0.10, 0.15, 0.20] if stok else [0.15]):
        d = samples[smp](sample(dcache[(dl, lg)], 1998 if lg == 2 else 1997, 2020)).reset_index(drop=True)
        cols = PH + (["tstar"] if trend else []) + (["lnK1"] if stok else []) + (CTRL5 if ctrl == "tam" else [])
        try:
            r = fit(d, cols, fam, exposure=expo)
            Gs = d.country.nunique()
            SC.append({"fam": fam, "stok": stok, "expo": expo, "ctrl": ctrl, "smp": smp, "lag": lg, "trend": trend, "delta": dl,
                       "b": [round(r.coef(k), 4) for k in PH], "se": [round(r.stderr(k), 4) for k in PH],
                       "p": [round(float(2 * tdist.sf(abs(r.coef(k) / r.stderr(k)), Gs - 1)), 4) for k in PH]})
        except Exception:
            pass
json.dump(SC, open(OUT / "spec_egrisi.json", "w"), ensure_ascii=False)
EK["spec_ozet"] = {"n": len(SC)}
for j, f in enumerate(PH):
    b = np.array([s["b"][j] for s in SC]); p = np.array([s["p"][j] for s in SC])
    EK["spec_ozet"][f] = {"medyan": float(np.median(b)), "min": float(b.min()), "max": float(b.max()), "pozitif_pay": float(np.mean(b > 0)),
                          "poz_anlamli5": float(np.mean((b > 0) & (p < .05))), "neg_anlamli5": float(np.mean((b < 0) & (p < .05)))}
    for key, lab in [("stok", "stok"), ("trend", "trend")]:
        for val in [True, False]:
            m = np.array([s[key] == val for s in SC])
            EK["spec_ozet"][f][f"{lab}_{int(val)}"] = {"medyan": float(np.median(b[m])), "poz_anlamli5": float(np.mean((b[m] > 0) & (p[m] < .05)))}

# ------------------------------------------------------------------ KAYDET
log("kaydet")


def clean(o):
    if isinstance(o, dict): return {str(k): clean(v) for k, v in o.items() if not str(k).startswith("_")}
    if isinstance(o, (list, tuple)): return [clean(v) for v in o]
    return o


R.update({"m1": m1, "m2": m2, "saglamlik": SAG, "loo": LOO, "yil": YE, "plasebo": PL, "gecikme": LAG, "ek": EK,
          "tez": {"t511": TEZ.T511, "t513": TEZ.T513, "yil": {str(k): v for k, v in TEZ.YIL.items()}}})
json.dump(rnd(clean(R), 4), open(OUT / "sonuclar.json", "w"), ensure_ascii=False, indent=1)
log("bitti ->", OUT / "sonuclar.json")
