"""İkinci jüri raporundaki maddelerin veriyle sınanması. Çıktı: analiz/cikti/juri2.json"""
import json
import numpy as np, pandas as pd
from scipy.optimize import minimize
from scipy.special import gammaln
from scipy.stats import t as tdist, norm
from tezlib import *

df = load(); est = sample(df); C = ["lnK1"] + CTRL5
O = {}
q = lambda r, ks: {k: {"b": r.coef(k), "se": r.stderr(k), "p_t": r.p(k, "t")} for k in ks}

# ---------------------------------------------------------------- 1) Ön-örneklem ortalaması (pre-sample mean) varyantları
psm = df[df.year.between(1990, 1996)].groupby("country").ccm.mean(); pg = df[df.year.between(1995, 1996)].groupby("country").gdp_real.mean()
K96 = df[df.year == 1996].set_index("country").K
est["lnpsm"] = np.log(est.country.map(psm)); est["lnpg"] = np.log(est.country.map(pg)); est["lnK96"] = np.log(est.country.map(K96))
est["lnpsi"] = est.lnpsm - est.lnpg                       # ön-örneklem yoğunluğu
V = {"A: ön-örneklem ort. patent + GSYİH; stok var": (PH + C + ["lnpsm", "lnpg"], ["lnpsm"]),
     "B: ön-örneklem stoku (ln K1996) + GSYİH; stok var": (PH + C + ["lnK96", "lnpg"], ["lnK96"]),
     "C: ön-örneklem yoğunluğu; stok var": (PH + C + ["lnpsi"], ["lnpsi"]),
     "D: ön-örneklem stoku; zamanla değişen stok YOK": (PH + CTRL5 + ["lnK96", "lnpg"], ["lnK96"]),
     "E: ön-örneklem stoku + doğrusal eğilim; stok YOK": (PH + ["tstar"] + CTRL5 + ["lnK96", "lnpg"], ["lnK96", "tstar"]),
     "F: hiçbir ülke kontrolü yok (havuzlanmış); stok var": (PH + C, [])}
O["psm"] = {}
for nm, (cols, extra) in V.items():
    O["psm"][nm] = {fam: q(fit(est, cols, fam, fe=False), PH + (["lnK1"] if "lnK1" in cols else []) + extra) for fam in ("poisson", "nb")}
O["psm"]["Tezin sabit etkili modeli"] = {fam: q(fit(est, PH + C, fam), PH + ["lnK1"]) for fam in ("poisson", "nb")}
# ön-örneklem ortalamalı Model 2 (ITS)
O["psm_m2"] = {fam: q(fit(est, ITS + C + ["lnpsm", "lnpg"], fam, fe=False), ITS + ["lnK1"]) for fam in ("poisson", "nb")}

# ---------------------------------------------------------------- 2) Sıfır-kesikli (zero-truncated) duyarlılık
X, names, off = design(est, PH + C); y = est.ccm.values.astype(float)
bP, muP = poisson_fit(y, X, off); bN, aN, muN, _ = nb_fit(y, X, off)
p0P = np.exp(-muP); p0N = (1 + aN * muN) ** (-1 / aN)
small = est.country.isin(["Greece", "Portugal", "Ireland", "Luxembourg"]).values
O["sifir"] = {"gozlenen_sifir": int((y == 0).sum()), "beklenen_sifir_poisson": float(p0P.sum()), "beklenen_sifir_nb": float(p0N.sum()),
              "y_le_3": int((y <= 3).sum()), "y_le_5": int((y <= 5).sum()), "min_mu_nb": float(muN.min()),
              "en_kucukler": est.assign(mu=muN, p0=p0N).nsmallest(6, "mu")[["country", "year", "ccm", "mu", "p0"]].assign(country=lambda d: d.country.map(TR)).round(3).values.tolist(),
              "sifir_olasiligi_0_01_ustu": int((p0N > 0.01).sum())}


def ztp_nll(b):
    mu = np.exp(np.clip(X @ b + off, -30, 30)); return -np.sum(y * np.log(mu) - mu - np.log1p(-np.exp(-mu)))


def ztp_grad(b):
    mu = np.exp(np.clip(X @ b + off, -30, 30)); e = np.exp(-mu)
    return -(X.T @ (y - mu - mu * e / (1 - e)))


def ztnb_nll(th):
    b, a = th[:-1], np.exp(th[-1]); mu = np.exp(np.clip(X @ b + off, -30, 30)); r = 1 / a
    ll = gammaln(y + r) - gammaln(y + 1) - gammaln(r) + r * np.log(r / (r + mu)) + y * np.log(mu / (r + mu))
    return -np.sum(ll - np.log1p(-(1 + a * mu) ** (-r)))


rz = minimize(ztp_nll, bP, jac=ztp_grad, method="BFGS", options={"gtol": 1e-8, "maxiter": 2000})
rzn = minimize(ztnb_nll, np.r_[bN, np.log(aN)], method="BFGS", options={"gtol": 1e-6, "maxiter": 5000})
ix = [names.index(k) for k in PH + ["lnK1"]]
O["sifir"]["zt_poisson"] = {k: float(rz.x[i]) for k, i in zip(PH + ["lnK1"], ix)}; O["sifir"]["zt_nb"] = {k: float(rzn.x[i]) for k, i in zip(PH + ["lnK1"], ix)}
O["sifir"]["zt_nb_alpha"] = float(np.exp(rzn.x[-1])); O["sifir"]["yakinsama"] = [bool(rz.success or rz.status == 2), bool(rzn.success or rzn.status == 2)]
O["sifir"]["normal_poisson"] = {k: float(bP[i]) for k, i in zip(PH + ["lnK1"], ix)}; O["sifir"]["normal_nb"] = {k: float(bN[i]) for k, i in zip(PH + ["lnK1"], ix)}
# küçük ülkeler (Yunanistan, Portekiz) dışarıda
d2 = est[~est.country.isin(["Greece", "Portugal"])].reset_index(drop=True)
O["sifir"]["GR_PT_haric"] = {fam: q(fit(d2, PH + C, fam), PH) for fam in ("poisson", "nb")}

# ---------------------------------------------------------------- 3) İrlanda 2015 GSYİH sıçraması
ie = est[est.country == "Ireland"].set_index("year")
O["irlanda"] = {"gsyih_2014_2015": [float(ie.gdp_real[2014]), float(ie.gdp_real[2015])], "yogunluk_2014_2016": [float(ie.inten[y_]) for y_ in (2014, 2015, 2016)], "ccm_2014_2016": [int(ie.ccm[y_]) for y_ in (2014, 2015, 2016)]}
dI = est[est.country != "Ireland"].reset_index(drop=True)
e3 = est.copy(); e3["IE15"] = ((e3.country == "Ireland") & (e3.year >= 2015)).astype(float)
O["irlanda"]["haric"] = {fam: q(fit(dI, PH + C, fam), PH) for fam in ("poisson", "nb")}
O["irlanda"]["kukla_2015_sonrasi"] = {fam: q(fit(e3, PH + C + ["IE15"], fam), PH + ["IE15"]) for fam in ("poisson", "nb")}
O["irlanda"]["serbest_haric"] = {fam: q(fit(dI, PH + C, fam, exposure="free"), PH + ["lngdp"]) for fam in ("poisson", "nb")}
O["irlanda"]["serbest_tam"] = {fam: q(fit(est, PH + C, fam, exposure="free"), PH + ["lngdp"]) for fam in ("poisson", "nb")}
mu = fit_poisson(est, PH + C).extra["mu"]; O["irlanda"]["poisson_agirlik"] = float(mu[est.country.values == "Ireland"].sum() / mu.sum() * 100)

# ---------------------------------------------------------------- 4) Örneklem başlangıç yılı: eksik veri
raw = pd.read_excel(XLSX, sheet_name="Veri")
O["eksik"] = {c: {int(y_): int(n) for y_, n in raw[raw[c].isna()].groupby("year").size().items()} for c in ["gdp_real", "gdp_growth", "manuf"]}
O["eksik"]["ilk_tam_yil"] = {c: int(raw.groupby("year")[c].apply(lambda s: s.notna().all()).pipe(lambda s: s[s].index.min())) for c in ["gdp_real", "gdp_growth", "manuf", "impdep", "renew_wdi", "trade", "ccm"]}

# ---------------------------------------------------------------- 5) Faz 3 "aşağı çekilme": stok koşullu / koşulsuz / eğilimli
O["faz3"] = {"stoklu": {fam: q(fit(est, PH + C, fam), ["F3"]) for fam in ("poisson", "nb")},
             "stoksuz": {fam: q(fit(est, PH + CTRL5, fam), ["F3"]) for fam in ("poisson", "nb")},
             "stoksuz_egilimli": {fam: q(fit(est, PH + ["tstar"] + CTRL5, fam), ["F3", "tstar"]) for fam in ("poisson", "nb")}}
json.dump(O, open(ROOT / "analiz" / "cikti" / "juri2.json", "w"), ensure_ascii=False, indent=1, default=float)
r3 = lambda d: {k: (round(v["b"], 3), round(v["p_t"], 3)) for k, v in d.items()}
for nm, v in O["psm"].items(): print(nm, "| P", r3(v["poisson"]), "| NB", r3(v["nb"]))
print("PSM M2", {f: r3(v) for f, v in O["psm_m2"].items()})
print("SIFIR", {k: v for k, v in O["sifir"].items() if k != "en_kucukler"}); print(O["sifir"]["en_kucukler"])
print("IRLANDA", json.dumps(O["irlanda"], default=float)[:1500])
print("EKSIK", O["eksik"]); print("FAZ3", {k: {f: r3(v) for f, v in d.items()} for k, d in O["faz3"].items()})
