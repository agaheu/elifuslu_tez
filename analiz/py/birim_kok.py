"""Tablo 5.7 ve 5.9'un bağımsız yeniden üretimi: Fisher-ADF, IPS, Pesaran CD ve CIPS.

IPS W-istatistiği için E[t], Var[t] momentleri ve CIPS için kritik değerler Monte Carlo ile üretilir
(T=25 ve T=24, gecikme=1). Çıktı: analiz/cikti/birim_kok.json
"""
import json
import numpy as np, pandas as pd
from scipy.stats import chi2, norm
from statsmodels.tsa.stattools import adfuller
from tezlib import load, ROOT
import tez_degerleri as TEZ

rng = np.random.default_rng(12345)
df = load()
d = df[df.year.between(1996, 2020)].copy()
d["lnK"] = np.log(1 + d.K)
d["lninten"] = np.log(d.ccm / d.gdp_real)
VARS = {"lninten": "Ln yeşil patent yoğunluğu (tezin kullandığı)", "inten": "Yeşil patent yoğunluğu (düzey)", "lnK": "Ln yeşil patent stoku", "gdp_growth": "GSYİH büyüme oranı", "renew_wdi": "Yenilenebilir enerji payı",
        "impdep": "Enerji ithalat bağımlılığı", "manuf": "İmalat payı", "trade": "Ticaret açıklığı"}


def wide(v, diff=False):
    w = d.pivot(index="year", columns="country", values=v)
    return w.diff().dropna() if diff else w


def adf_t(x, p, reg):
    r = adfuller(x, maxlag=p, autolag=None, regression=reg)
    return r[0], r[1]


def fisher(W, p, reg):
    ps = [adf_t(W[c].values, p, reg)[1] for c in W]
    P = -2 * np.sum(np.log(np.clip(ps, 1e-300, 1)))
    return float(P), float(chi2.sf(P, 2 * len(ps)))


def adf_reg(x, p, reg, start=None):
    """ADF regresyonu; start verilirse AIC karşılaştırması için ortak örneklem kullanılır."""
    dx = np.diff(x); T = len(dx); s0 = p if start is None else start
    rows, Y = [], []
    for t in range(s0, T):
        rows.append([x[t], 1.0] + ([t] if reg == "ct" else []) + [dx[t - j] for j in range(1, p + 1)]); Y.append(dx[t])
    Xm = np.array(rows); Y = np.array(Y)
    b = np.linalg.lstsq(Xm, Y, rcond=None)[0]; e = Y - Xm @ b; n, k = len(Y), Xm.shape[1]
    tstat = b[0] / np.sqrt(e @ e / (n - k) * np.linalg.inv(Xm.T @ Xm)[0, 0])
    return tstat, n * np.log(e @ e / n) + 2 * k


_mom = {}


def ips_moments(T, p, reg, nsim=20000):
    key = (T, p, reg)
    if key not in _mom:
        ts = [adf_reg(np.cumsum(rng.standard_normal(T)), p, reg)[0] for _ in range(nsim)]
        _mom[key] = (np.mean(ts), np.var(ts))
    return _mom[key]


def ips(W, pmax, reg):
    """IPS W_tbar; ülke bazında gecikme, ortak örneklemde AIC ile (en fazla pmax) — Stata xtunitroot ips, lags(aic #) mantığı."""
    ts, Es, Vs = [], [], []
    for c in W:
        x = W[c].values
        best = min(range(pmax + 1), key=lambda p: adf_reg(x, p, reg, start=pmax)[1])
        E, V = ips_moments(len(x), best, reg)
        ts.append(adf_reg(x, best, reg)[0]); Es.append(E); Vs.append(V)
    Wst = np.sqrt(len(ts)) * (np.mean(ts) - np.mean(Es)) / np.sqrt(np.mean(Vs))
    return float(Wst), float(norm.cdf(Wst))


def cd_test(W):
    X = W.values; T, N = X.shape
    Rm = np.corrcoef(X.T)
    s = Rm[np.triu_indices(N, 1)].sum()
    cd = np.sqrt(2 * T / (N * (N - 1))) * s
    return float(cd), float(2 * norm.sf(abs(cd)))


def cadf_t(y, ybar, p, trend):
    dy, dyb = np.diff(y), np.diff(ybar)
    T = len(dy)
    rows = []
    for t in range(p, T):
        r = [y[t], ybar[t], dyb[t], 1.0]
        for j in range(1, p + 1): r += [dy[t - j], dyb[t - j]]
        if trend: r.append(t)
        rows.append(r)
    Xm = np.array(rows); Y = dy[p:]
    b, *_ = np.linalg.lstsq(Xm, Y, rcond=None)
    e = Y - Xm @ b
    s2 = e @ e / (len(Y) - Xm.shape[1])
    se = np.sqrt(s2 * np.linalg.inv(Xm.T @ Xm)[0, 0])
    return b[0] / se


def cips(W, p, trend):
    X = W.values; ybar = X.mean(1)
    return float(np.mean([cadf_t(X[:, i], ybar, p, trend) for i in range(X.shape[1])]))


_cv = {}


def cips_pvalue(stat, T, N, p, trend, nsim=3000):
    key = (T, N, p, trend)
    if key not in _cv:
        sims = np.empty(nsim)
        for s in range(nsim):
            f = np.cumsum(rng.standard_normal(T))
            Xs = np.cumsum(rng.standard_normal((T, N)), axis=0) + f[:, None]
            yb = Xs.mean(1)
            sims[s] = np.mean([cadf_t(Xs[:, i], yb, p, trend) for i in range(N)])
        _cv[key] = np.sort(sims)
    sims = _cv[key]
    return float(np.mean(sims <= stat)), [float(np.quantile(sims, q)) for q in (.01, .05, .10)]


out = {}
for v, lab in VARS.items():
    W, dW = wide(v), wide(v, True)
    tk = "inten" if v == "lninten" else v
    o = {"etiket": lab, "tez57": TEZ.T57[tk] if v != "inten" else None, "tez59": TEZ.T59[tk] if v != "inten" else None}
    o["fisher_c"] = fisher(W, 1, "c"); o["fisher_ct"] = fisher(W, 1, "ct"); o["fisher_d"] = fisher(dW, 1, "c")
    o["ips_c"] = ips(W, 2, "c"); o["ips_ct"] = ips(W, 2, "ct"); o["ips_d"] = ips(dW, 2, "c")
    o["cd"] = cd_test(W)
    T, N = W.shape
    for nm, (WW, tr) in {"cips_c": (W, False), "cips_ct": (W, True), "cips_d": (dW, False)}.items():
        st = cips(WW, 1, tr); pv, cv = cips_pvalue(st, len(WW), N, 1, tr)
        o[nm] = {"stat": st, "p_sim": pv, "kd": cv}
    out[v] = o
    print(lab, "| Fisher", np.round(o["fisher_c"], 3), "| IPS", np.round(o["ips_c"], 3), "| CD", np.round(o["cd"][0], 3), "| CIPS", round(o["cips_c"]["stat"], 3), "p_sim", o["cips_c"]["p_sim"], flush=True)
(ROOT / "analiz" / "cikti").mkdir(exist_ok=True, parents=True)
json.dump(out, open(ROOT / "analiz" / "cikti" / "birim_kok.json", "w"), ensure_ascii=False, indent=1)
