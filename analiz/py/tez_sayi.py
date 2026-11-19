"""Güncellenmiş tez metninde kullanılan sayılar ve biçimlendirme yardımcıları (hepsi hesap çıktılarından)."""
import json
from scipy.stats import t as tdist
from icerik import R, E, S, SP, J, U, tr, pv, pct, c, bo, P, N, yb, pl, ALFA_I, vif2, ici, eg, SG, mcr, simrg, loo
from icerik import ek as ekc, ik
from tezlib import ROOT, TR, PH, ITS
import tez_degerleri as TZ

TG = json.load(open(ROOT / "analiz" / "cikti" / "tez_guncel.json"))
FAM = {N: "NB", P: "Poisson"}


def g(ad, fam, k, f="b"): return TG[ad][fam][k][f]
def yz(p): return r"\*\*\*" if p < .01 else r"\*\*" if p < .05 else r"\*" if p < .10 else ""
def pt(b, se, df=13): return float(2 * tdist.sf(abs(b / se), df))
def kh(ad, fam, k):
    v = TG[ad][fam][k]
    return f"{tr(v['b'], 4)}{yz(v['p_boot_t'])} ({tr(v['se_boot'], 4)})"


def tezh(b, se):
    """Tezin kendi katsayı ve standart hatasıyla, t(13)'e göre yıldızlı hücre."""
    return f"{tr(b, 4)}{yz(pt(b, se))}"


def duzey(p): return "yüzde 1" if p < .01 else "yüzde 5" if p < .05 else "yüzde 10" if p < .10 else None
def a2(x): return f"{x:.2f}".replace(".", ",").replace("-", "−")
def yuzde(b): return tr(100 * (2.718281828459045 ** b - 1), 1)
def yaral(lo, hi):
    f = lambda x: ("−%" if x < 0 else "%") + tr(abs(100 * (2.718281828459045 ** x - 1)), 1)
    return rf"\[{f(lo)}; {f(hi)}\]"
