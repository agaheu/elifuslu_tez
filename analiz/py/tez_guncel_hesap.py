"""Güncellenmiş tez metnine eklenen tablo satırları için bootstrap ve küme jackknife çıkarsaması.

Çıktı: analiz/cikti/tez_guncel.json
Kullanım: python analiz/py/tez_guncel_hesap.py [B]
"""
import json, sys, time
from multiprocessing import Pool
import numpy as np, pandas as pd
from scipy.stats import norm, t as tdist
from tezlib import *

B = int(sys.argv[1]) if len(sys.argv) > 1 else 1999
SEED = 12345
C = ["lnK1"] + CTRL5
M1 = PH + C


def veri():
    df = load(); est = sample(df)
    est["ANT"] = est.year.between(2003, 2004).astype(float)
    est["F2a"] = est.year.between(2008, 2009).astype(float); est["F2b"] = est.year.between(2010, 2012).astype(float)
    est["ETS"] = (est.year >= 2005).astype(float)
    psm = df[df.year.between(1990, 1996)].groupby("country").ccm.mean(); pg = df[df.year.between(1995, 1996)].groupby("country").gdp_real.mean()
    est["lnpsm"] = np.log(est.country.map(psm)); est["lnpg"] = np.log(est.country.map(pg))
    return est


TANIM = {
    "stoksuz_egilim": dict(cols=PH + ["tstar"] + CTRL5, keys=PH + ["tstar"]),
    "referans_1997_2002": dict(cols=["ANT"] + M1, keys=["ANT"] + PH + ["lnK1"]),
    "faz2_bolunmus": dict(cols=["F1", "F2a", "F2b", "F3"] + C, keys=["F1", "F2a", "F2b", "F3", "lnK1"]),
    "2018_2020_haric": dict(cols=M1, keys=PH + ["lnK1"], filt="y2017"),
    "ets_tek": dict(cols=["ETS"] + C, keys=["ETS", "lnK1"]),
    "m2_stoksuz": dict(cols=ITS + CTRL5, keys=ITS),
    "psm_m1": dict(cols=M1 + ["lnpsm", "lnpg"], keys=PH + ["lnK1"], fe=False),
    "psm_m2": dict(cols=ITS + C + ["lnpsm", "lnpg"], keys=ITS + ["lnK1"], fe=False),
    "irlanda_haric": dict(cols=M1, keys=PH + ["lnK1"], filt="ie"),
}


def is_(arg):
    ad, fam = arg
    t0 = time.time()
    tn = TANIM[ad]; cols, keys, fe = tn["cols"], tn["keys"], tn.get("fe", True)
    d = veri()
    if tn.get("filt") == "y2017": d = d[d.year <= 2017].reset_index(drop=True)
    if tn.get("filt") == "ie": d = d[d.country != "Ireland"].reset_index(drop=True)
    full = fit(d, cols, fam, fe=fe)
    bhat = np.array([full.coef(k) for k in keys])
    ctry = pd.unique(d.country); G = len(ctry)
    Jk = np.array([[fit(d[d.country != c].reset_index(drop=True), cols, fam, fe=fe, cluster=None if fam == "nb" else "country").coef(k) for k in keys] for c in ctry])
    se_j = np.sqrt((G - 1) / G * ((Jk - Jk.mean(0)) ** 2).sum(0))
    rng = np.random.default_rng(SEED); draws, fail = [], 0
    for _ in range(B):
        db, cid, _p = resample(d, rng)
        try:
            if fam == "poisson": rb = fit_poisson(db, cols, fe=fe, cid=cid)
            else:
                rb = fit_nb(db, cols, fe=fe, cid=cid, cluster=None)
                if not rb.extra["conv"]: fail += 1; continue
            bb = np.array([rb.coef(k) for k in keys])
            if not np.all(np.isfinite(bb)) or np.max(np.abs(bb)) > 50: fail += 1; continue
            draws.append(bb)
        except Exception:
            fail += 1
    D = np.array(draws); o = {"_B_ok": len(D), "_fail": fail, "_N": len(d), "_G": G}
    for j, k in enumerate(keys):
        x = D[:, j]; se = float(x.std(ddof=1)); lo, hi, _z = bc_interval(x, bhat[j]); pl, ph = np.quantile(x, [.025, .975])
        o[k] = {"b": float(bhat[j]), "se_kume": full.stderr(k), "se_boot": se, "p_boot": float(2 * norm.sf(abs(bhat[j] / se))), "p_boot_t": float(2 * tdist.sf(abs(bhat[j] / se), G - 1)),
                "se_cv3": float(se_j[j]), "p_cv3": float(2 * tdist.sf(abs(bhat[j] / se_j[j]), G - 1)), "bc": [lo, hi], "pct": [float(pl), float(ph)]}
    print(ad, fam, "bitti", round(time.time() - t0), "sn", "basarisiz:", fail, flush=True)
    return ad, fam, o


if __name__ == "__main__":
    isler = [(a, f) for a in TANIM for f in ("poisson", "nb")]
    with Pool(4) as p: sonuc = p.map(is_, isler, chunksize=1)
    O = {"meta": {"B": B, "seed": SEED}}
    for ad, fam, o in sonuc: O.setdefault(ad, {})[fam] = o
    json.dump(O, open(ROOT / "analiz" / "cikti" / "tez_guncel.json", "w"), ensure_ascii=False, indent=1)
    print("yazildi")
