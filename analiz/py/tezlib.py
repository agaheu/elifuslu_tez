"""Ortak yardımcılar: veri hazırlama, Poisson/NB tahmini, kümelenmiş çıkarsama.

Hiçbir ara sonuç dosyadan okunmaz; her şey veri/AB14_nihai_veri.xlsx'ten yeniden hesaplanır.
"""
import pathlib, warnings
import numpy as np, pandas as pd
import statsmodels.api as sm
from statsmodels.discrete.discrete_model import NegativeBinomial
from scipy.stats import norm, chi2, t as tdist

warnings.filterwarnings("ignore")
ROOT = pathlib.Path(__file__).resolve().parents[2]
XLSX = ROOT / "veri" / "AB14_nihai_veri.xlsx"
CTRL5 = ["gdp_growth_l1", "renew_wdi_l1", "impdep_l1", "manuf_l1", "trade_l1"]
PH = ["F1", "F2", "F3"]
ITS = ["tstar", "F1", "S1", "F2", "S2", "F3", "S3"]
TR = {"Austria": "Avusturya", "Belgium": "Belçika", "Denmark": "Danimarka", "Finland": "Finlandiya", "France": "Fransa",
      "Germany": "Almanya", "Greece": "Yunanistan", "Ireland": "İrlanda", "Italy": "İtalya", "Luxembourg": "Lüksemburg",
      "Netherlands": "Hollanda", "Portugal": "Portekiz", "Spain": "İspanya", "Sweden": "İsveç"}


def load(delta=0.15, lag=1):
    """Ham veriyi okur, stok ve gecikmeleri sıfırdan kurar. Tam (1990-2020) çerçeveyi döndürür."""
    df = pd.read_excel(XLSX, sheet_name="Veri").sort_values(["country", "year"]).reset_index(drop=True)
    tot = df.groupby("year").ccm.sum()
    g = float(np.mean(np.diff(np.log(tot.loc[1990:1996].values))))
    K = []
    for _, d in df.groupby("country", sort=False):
        k = None
        for v in d.ccm.values:
            k = v / (g + delta) if k is None else (1 - delta) * k + v
            K.append(k)
    df["K"] = K
    gb = df.groupby("country", sort=False)
    df["lnK1"] = np.log(1 + gb.K.shift(lag))
    df["lnK0"] = np.log(1 + df.K)
    for v in ["gdp_growth", "renew_wdi", "impdep", "manuf", "trade"]:
        df[v + "_l1"] = gb[v].shift(lag)
    df["lngdp"] = np.log(df.gdp_real)
    df["inten"] = df.ccm / (df.gdp_real / 1000.0)
    df["F1"] = df.year.between(2005, 2007).astype(float)
    df["F2"] = df.year.between(2008, 2012).astype(float)
    df["F3"] = df.year.between(2013, 2020).astype(float)
    df["ETS"] = (df.year >= 2005).astype(float)
    df["tstar"] = (df.year - 1997).astype(float)
    for k, a in enumerate([2005, 2008, 2013], 1):
        df[f"S{k}"] = np.where(df[f"F{k}"] == 1, df.year - a, 0).astype(float)
    df.attrs["g"] = g
    return df


def sample(df, y0=1997, y1=2020):
    return df[df.year.between(y0, y1)].reset_index(drop=True)


def design(d, cols, exposure="fixed", fe=True, cid=None):
    """X = [sabit, cols, ülke kuklaları]; offset = ln GSYİH (exposure='fixed')."""
    X = [np.ones(len(d))] + [d[c].values.astype(float) for c in cols]
    names = ["const"] + list(cols)
    if exposure == "free":
        X.append(d.lngdp.values); names.append("lngdp")
    if fe:
        ids = d.country.values if cid is None else cid
        u = pd.unique(ids)
        for c in u[1:]:
            X.append((ids == c).astype(float)); names.append(f"fe_{c}")
    off = d.lngdp.values if exposure == "fixed" else np.zeros(len(d))
    return np.column_stack(X), names, off


def poisson_fit(y, X, off, tol=1e-10, maxit=200):
    """Poisson (log bağlantı) IRLS. beta, mu döndürür."""
    mu = (y + y.mean()) / 2.0
    eta = np.log(np.maximum(mu, 1e-8))
    beta = np.zeros(X.shape[1]); dev_old = np.inf
    for _ in range(maxit):
        z = eta - off + (y - mu) / mu
        XtW = X.T * mu
        beta = np.linalg.solve(XtW @ X, XtW @ z)
        eta = X @ beta + off
        mu = np.exp(np.clip(eta, -30, 30))
        dev = 2 * np.sum(np.where(y > 0, y * np.log(np.maximum(y, 1e-300) / mu), 0) - (y - mu))
        if abs(dev - dev_old) < tol * (abs(dev) + 0.1):
            break
        dev_old = dev
    return beta, mu


def poisson_llf(y, mu):
    from scipy.special import gammaln
    return float(np.sum(y * np.log(mu) - mu - gammaln(y + 1)))


def sandwich(y, X, mu, groups, groups2=None, stata=True):
    """Kümelenmiş (tek veya iki yönlü) Poisson QML kovaryansı.
    stata=True: yalnızca G/(G-1) düzeltmesi (Stata ML kuralı)."""
    A = (X.T * mu) @ X
    Ai = np.linalg.inv(A)
    S = X * (y - mu)[:, None]

    def meat(g):
        codes, _ = pd.factorize(g)
        G = codes.max() + 1
        Sg = np.zeros((G, X.shape[1]))
        np.add.at(Sg, codes, S)
        c = G / (G - 1) if stata else G / (G - 1) * (len(y) - 1) / (len(y) - X.shape[1])
        return c * Sg.T @ Sg, G

    M, G = meat(groups)
    if groups2 is not None:
        M2, G2 = meat(groups2)
        M12 = S.T @ S * (1.0 if stata else len(y) / (len(y) - X.shape[1]))
        M = M + M2 - M12
        G = min(G, G2)
    return Ai @ M @ Ai, G


class Res:
    def __init__(self, names, b, V, G, llf=None, extra=None, n=None):
        self.names, self.b, self.V, self.G, self.llf, self.n = list(names), np.asarray(b), np.asarray(V), G, llf, n
        self.se = np.sqrt(np.clip(np.diag(self.V), 0, None))
        self.extra = extra or {}

    def i(self, k): return self.names.index(k)
    def coef(self, k): return float(self.b[self.i(k)])
    def stderr(self, k): return float(self.se[self.i(k)])
    def p(self, k, dist="z"):
        if not self.stderr(k) > 0: return float("nan")  # iki yönlü kümelemede varyans pozitif tanımlı olmayabilir
        z = abs(self.coef(k) / self.stderr(k))
        return float(2 * norm.sf(z) if dist == "z" else 2 * tdist.sf(z, self.G - 1))
    def has(self, k): return k in self.names
    def row(self, k):
        return {"b": self.coef(k), "se": self.stderr(k), "p": self.p(k), "p_t": self.p(k, "t")}
    def wald(self, ks, r=None):
        idx = [self.i(k) for k in ks]
        b = self.b[idx] - (0 if r is None else np.asarray(r))
        w = float(b @ np.linalg.solve(self.V[np.ix_(idx, idx)], b))
        return {"chi2": w, "df": len(ks), "p": float(chi2.sf(w, len(ks)))}
    def wald_eq(self, a, b_):
        ia, ib = self.i(a), self.i(b_)
        d = self.b[ia] - self.b[ib]
        v = self.V[ia, ia] + self.V[ib, ib] - 2 * self.V[ia, ib]
        w = float(d * d / v)
        return {"chi2": w, "df": 1, "p": float(chi2.sf(w, 1))}


def fit_poisson(d, cols, exposure="fixed", fe=True, depvar="ccm", cluster="country", cid=None):
    X, names, off = design(d, cols, exposure, fe, cid)
    y = d[depvar].values.astype(float)
    b, mu = poisson_fit(y, X, off)
    if cluster == "twoway":
        V, G = sandwich(y, X, mu, d.country.values, d.year.values)
    elif cluster == "year":
        V, G = sandwich(y, X, mu, d.year.values)
    else:
        V, G = sandwich(y, X, mu, d.country.values if cid is None else cid)
    k = X.shape[1]
    llf = poisson_llf(y, mu)
    return Res(names, b, V, G, llf, {"mu": mu, "X": X, "y": y, "off": off, "aic": -2 * llf + 2 * k, "bic": -2 * llf + k * np.log(len(y)), "k": k}, len(y))


def nb_llf(y, mu, a):
    from scipy.special import gammaln
    r = 1.0 / a
    return float(np.sum(gammaln(y + r) - gammaln(y + 1) - gammaln(r) + r * np.log(r / (r + mu)) + y * np.log(mu / (r + mu))))


def nb_fit(y, X, off, tol=1e-9, maxit=200):
    """NB2 en çok olabilirlik: beta için IRLS (alpha sabitken), alpha için tek boyutlu profil arama; dönüşümlü."""
    from scipy.optimize import minimize_scalar
    beta, mu = poisson_fit(y, X, off)
    a, ll_old = 0.05, -np.inf
    for _ in range(maxit):
        a = float(np.exp(minimize_scalar(lambda la: -nb_llf(y, mu, np.exp(la)), bounds=(-14, 3), method="bounded", options={"xatol": 1e-10}).x))
        for _ in range(50):
            w = mu / (1 + a * mu)
            z = np.log(mu) - off + (y - mu) / mu
            XtW = X.T * w
            bnew = np.linalg.solve(XtW @ X, XtW @ z)
            munew = np.exp(np.clip(X @ bnew + off, -30, 30))
            done = np.max(np.abs(bnew - beta)) < 1e-10
            beta, mu = bnew, munew
            if done: break
        ll = nb_llf(y, mu, a)
        if abs(ll - ll_old) < tol * (abs(ll) + 1): break
        ll_old = ll
    return beta, a, mu, ll


def fit_nb(d, cols, exposure="fixed", fe=True, depvar="ccm", cluster="country", cid=None, start=None):
    X, names, off = design(d, cols, exposure, fe, cid)
    y = d[depvar].values.astype(float)
    beta, a, mu, llf = nb_fit(y, X, off)
    n, k = len(y), X.shape[1] + 1
    names = names + ["alpha"]
    params = np.r_[beta, a]
    extra = {"aic": -2 * llf + 2 * k, "bic": -2 * llf + k * np.log(n), "k": k, "conv": True, "mu": mu}
    if cluster is None:
        return Res(names, params, np.full((k, k), np.nan), n, llf, extra, n)
    mod = NegativeBinomial(y, X, offset=off)
    r0 = mod.fit(start_params=params, disp=0, maxiter=0, method="bfgs", warn_convergence=False)
    extra["Vml"] = np.asarray(r0.cov_params())
    extra["grad_max"] = float(np.max(np.abs(mod.score(params))))

    def cl(gr):
        rc = mod.fit(start_params=params, disp=0, maxiter=0, method="bfgs", cov_type="cluster",
                     cov_kwds={"groups": pd.factorize(gr)[0], "use_correction": True}, warn_convergence=False)
        return np.asarray(rc.cov_params()) * (n - k) / (n - 1)  # Stata kuralı: yalnızca G/(G-1)
    if cluster == "twoway":
        rh = mod.fit(start_params=params, disp=0, maxiter=0, method="bfgs", cov_type="HC0", warn_convergence=False)
        V = cl(d.country.values) + cl(d.year.values) - np.asarray(rh.cov_params()); G = min(d.country.nunique(), d.year.nunique())
    elif cluster == "year":
        V, G = cl(d.year.values), d.year.nunique()
    else:
        ids = d.country.values if cid is None else cid
        V, G = cl(ids), len(pd.unique(ids))
    return Res(names, params, V, G, llf, extra, n)


def fit(d, cols, fam="poisson", **kw):
    return fit_poisson(d, cols, **kw) if fam == "poisson" else fit_nb(d, cols, **kw)


def resample(d, rng):
    """Ülkeleri yerine koyarak yeniden örnekler; yinelenen ülke ayrı küme (kendi sabit etkisi) olur."""
    ctry = pd.unique(d.country)
    pick = rng.choice(len(ctry), size=len(ctry), replace=True)
    parts, cid = [], []
    for j, p in enumerate(pick):
        blk = d[d.country == ctry[p]]
        parts.append(blk); cid += [f"{ctry[p]}#{j}"] * len(blk)
    return pd.concat(parts, ignore_index=True), np.array(cid), [ctry[p] for p in pick]


def bc_interval(draws, bhat, level=0.95):
    a = (1 - level) / 2
    frac = np.mean(draws < bhat)
    frac = min(max(frac, 1e-6), 1 - 1e-6)
    z0 = norm.ppf(frac)
    a1, a2 = norm.cdf(2 * z0 + norm.ppf(a)), norm.cdf(2 * z0 + norm.ppf(1 - a))
    lo, hi = np.quantile(draws, [a1, a2])
    return float(lo), float(hi), float(z0)


def stars(p):
    return "***" if p < 0.01 else "**" if p < 0.05 else "*" if p < 0.10 else ""
