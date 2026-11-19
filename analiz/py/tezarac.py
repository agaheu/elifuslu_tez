"""Tez metnini izlenebilir değişikliklerle güncellemek için araçlar.

Özgün metin (pandoc markdown) HTML'e çevrilir; her değişiklik özgün HTML'deki tek bir yere bağlanır,
bulgu numarasıyla işaretlenir (<del>/<ins>/<div class="ekle">), sonunda hepsi birlikte uygulanır.
"""
import subprocess, re, json, html as _html, hashlib
from tezlib import ROOT

SRC = ROOT / "dokumanlar" / "Nihai_Model_19112026_metin.md"
_CF = ROOT / "analiz" / "cikti" / ".pandoc_cache.json"
try: _C = json.load(open(_CF))
except Exception: _C = {}


def pandoc(md, frm="markdown", to="html", extra=("--mathml",)):
    k = hashlib.sha1((frm + to + "".join(extra) + md).encode()).hexdigest()
    if k not in _C:
        _C[k] = subprocess.run(["pandoc", "-f", frm, "-t", to, "--wrap=none", *extra], input=md, capture_output=True, text=True, check=True).stdout
    return _C[k]


def kaydet_cache(): json.dump(_C, open(_CF, "w"))


def I(md):
    """Satır içi markdown → HTML (sarmalayan <p> atılır)."""
    o = pandoc(md).strip()
    assert o.startswith("<p>") and o.endswith("</p>") and o.count("<p>") == 1, (md[:80], o[:120])
    return o[3:-4]


def Bk(md): return pandoc(md).strip()
def duz(h): return re.sub(r"\s+", " ", _html.unescape(re.sub(r"<annotation.*?</annotation>", "", re.sub(r"<[^>]+>", "", re.sub(r"<math.*?</math>", "[denklem]", h, flags=re.S)), flags=re.S))).strip()


H0 = pandoc(SRC.read_text(encoding="utf8"))
ED, DEG = [], []          # (bas, son, yeni_html, sira) ; değişiklik kayıtları


def _no(b, tur, ozet, eski="", yeni=""):
    no = f"D{len(DEG) + 1:03d}"
    DEG.append({"no": no, "bulgu": b.split(), "tur": tur, "ozet": ozet, "eski": duz(eski)[:600], "yeni": duz(yeni)[:900]})
    return no


def _at(no, b): return f'data-d="{no}" data-b="{b}"'
def _ekle(s, e, yeni, soft=False): ED.append((s, e, yeni, len(ED), soft))


def bul(x, ham=False, kacinci=None):
    h = x if ham else I(x)
    c = H0.count(h)
    if kacinci is None:
        assert c == 1, f"{c} eşleşme: {x[:110]!r}"
        s = H0.index(h)
    else:
        assert c >= kacinci, f"{c} eşleşme (<{kacinci}): {x[:110]!r}"
        s = -1
        for _ in range(kacinci): s = H0.index(h, s + 1)
    return s, s + len(h), h


def deg(b, eski, yeni, ozet="", kacinci=None, grup=None, tur="değişiklik"):
    s, e, eh = bul(eski, kacinci=kacinci); yh = I(yeni); no = grup or _no(b, tur, ozet, eh, yh)
    _ekle(s, e, f"<del {_at(no, b)}>{eh}</del><ins {_at(no, b)}>{yh}</ins>")
    return no


def cik(b, eski, ozet="", grup=None):
    s, e, eh = bul(eski); no = grup or _no(b, "çıkarma", ozet, eh, "")
    _ekle(s, e, f"<del {_at(no, b)}>{eh}</del>")
    return no


def ek(b, sonra, yeni, ozet="", once=False, kacinci=None, grup=None, tur="ekleme"):
    s, e, _ = bul(sonra, kacinci=kacinci); yh = I(yeni); no = grup or _no(b, tur, ozet, "", yh)
    _ekle(s, s, f"<ins {_at(no, b)}>{yh}</ins> ") if once else _ekle(e, e, f" <ins {_at(no, b)}>{yh}</ins>")
    return no


def kontrol(b, eski, not_, ozet):
    s, e, eh = bul(eski); no = _no(b, "kontrol", ozet, eh, not_)
    _ekle(s, e, f'<span class="kontrol" {_at(no, b)} title="{_html.escape(not_)}">{eh}</span>')


def ham(b, eski_html, yeni_html, tur, ozet="", kayit_eski="", kayit_yeni="", grup=None):
    s, e, _ = bul(eski_html, ham=True); no = grup or _no(b, tur, ozet, kayit_eski or eski_html, kayit_yeni or yeni_html)
    _ekle(s, e, yeni_html.replace("@AT@", _at(no, b)))
    return no


def blok(b, sonra, md, ozet, once=False, ham_anchor=False):
    """Yeni blok (paragraf, tablo, başlık): çapanın içinde bulunduğu paragrafın/tablonun ardına (ya da önüne)."""
    if isinstance(sonra, tuple) and sonra[0] == "tablo": pos = tablo(sonra[1])[1]
    else:
        s, e, _ = bul(sonra, ham=ham_anchor)
        if once:
            pos = max(H0.rfind("<p>", 0, s + 3), H0.rfind("<h", 0, s + 2))
        else:
            ks = [k for k in (H0.find("</p>", e), H0.find("</h", e)) if k >= 0]; k = min(ks); pos = H0.index(">", k) + 1
    yh = Bk(md); no = _no(b, "ekleme", ozet, "", yh)
    _ekle(pos, pos, f'\n<div class="ekle" {_at(no, b)}>\n{yh}\n</div>\n')


# ------------------------------------------------------------------ tablolar
def tablo(no):
    cap = f"<strong>Tablo {no}.</strong>"; assert H0.count(cap) == 1, (no, H0.count(cap))
    ts = H0.index("<table", H0.index(cap)); te = H0.index("</table>", ts) + 8
    return ts, te


def _satirlar(no):
    ts, te = tablo(no)
    return [(ts + m.start(), ts + m.end(), m.group(0)) for m in re.finditer(r"<tr[^>]*>.*?</tr>", H0[ts:te], re.S)]


def _hucreler(rs, rtxt):
    return [(rs + m.start(3), rs + m.end(3), m.group(3), m.group(2)) for m in re.finditer(r"<(td|th)([^>]*)>(.*?)</\1>", rtxt, re.S)]


def _satir_bul(no, anahtar, kacinci=1):
    n = 0
    for rs, re_, rt in _satirlar(no):
        hs = _hucreler(rs, rt)
        if hs and anahtar in duz(hs[0][2]):
            n += 1
            if n == kacinci: return rs, re_, rt, hs
    raise AssertionError(f"Tablo {no}: satır bulunamadı: {anahtar} #{kacinci}")


def hucre(b, no, satir, sutun, yeni, ozet, kacinci=1, grup=None):
    """Tek hücrenin içeriğini değiştirir. grup: aynı değişiklik numarasını paylaşan hücreler için önceki kayıt no."""
    rs, re_, rt, hs = _satir_bul(no, satir, kacinci); s, e, eski, _ = hs[sutun]; yh = I(yeni) if yeni else ""
    dno = grup or _no(b, "tablo", ozet, f"Tablo {no}, {satir}: {duz(eski)}", duz(yh))
    _ekle(s, e, (f"<del {_at(dno, b)}>{eski}</del>" if eski.strip() else "") + (f"<ins {_at(dno, b)}>{yh}</ins>" if yh else ""))
    return dno


def satir_ekle(b, no, sonra, hucreler, ozet, kacinci=1, grup=None):
    rs, re_, rt, hs = _satir_bul(no, sonra, kacinci)
    dno = grup or _no(b, "tablo", ozet, "", f"Tablo {no}, yeni satır: " + " | ".join(hucreler))
    tds = "".join(f"<td{hs[min(i, len(hs) - 1)][3]}>{I(c) if c else ''}</td>" for i, c in enumerate(hucreler))
    _ekle(re_, re_, f'\n<tr class="ekle" {_at(dno, b)}>{tds}</tr>')
    return dno


def tablo_degistir(b, no, md, ozet):
    ts, te = tablo(no); yh = Bk(md); dno = _no(b, "tablo", ozet, f"Tablo {no} (tamamı)", duz(yh))
    _ekle(ts, te, f'<div class="cik" {_at(dno, b)}>{H0[ts:te]}</div><!--/cik--><div class="ekle" {_at(dno, b)}>\n{yh}\n</div>')


def hepsi(b, desen, yeni, ozet, tur="biçim"):
    """Düzenli ifadeyle eşleşen bütün yerleri (yalnız metin içinde) tek değişiklik numarasıyla değiştirir."""
    ms = [m for m in re.finditer(desen, H0) if H0.rfind("<", 0, m.start()) <= H0.rfind(">", 0, m.start())]
    assert ms, desen
    dno = _no(b, tur, ozet + f" ({len(ms)} yer)", ms[0].group(0), yeni if isinstance(yeni, str) else yeni(ms[0]))
    for m in ms:
        y = yeni if isinstance(yeni, str) else yeni(m)
        _ekle(m.start(), m.end(), f"<del {_at(dno, b)}>{m.group(0)}</del><ins {_at(dno, b)}>{y}</ins>", soft=True)
    return len(ms)


def uygula():
    sert = [x for x in ED if not x[4]]
    es = sorted([x for x in ED if not x[4] or not any(x[0] < h[1] and h[0] < x[1] for h in sert)], key=lambda x: (x[0], x[3])); out, pos = [], 0
    for s, e, y, _, _s in es:
        assert s >= pos, f"çakışan değişiklik: {H0[s:s + 90]!r} / {y[:90]!r}"
        out.append(H0[pos:s]); out.append(y); pos = e
    out.append(H0[pos:])
    return "".join(out)


def bolum_ata(H):
    """Her değişikliğe, metinde ilk göründüğü yerin bölüm başlığını yazar."""
    cur, gor = "5 (giriş)", {}
    for m in re.finditer(r'<h[1-6][^>]*>(.*?)</h[1-6]>|<p>(?:<strong>)?(5\.\d+(?:\.\d+)? [^<]{3,80})(?:</strong>)?</p>|data-d="(D\d+)"', H, re.S):
        if m.group(3):
            gor.setdefault(m.group(3), cur)
        else:
            ic = re.findall(r'data-d="(D\d+)"', m.group(0))
            t = duz(re.sub(r"<del[^>]*>.*?</del>", "", m.group(1) or m.group(2) or "", flags=re.S))
            t = re.sub(r"^(ins|del)$", "", t)
            mm = re.match(r"(5\.\d+(?:\.\d+)?)\s", t)
            if mm: cur = mm.group(1)
            elif "KAYNAKÇA" in t: cur = "Kaynakça"
            elif "Veri Kaynakları" in t: cur = "Kaynakça"
            for x in ic: gor.setdefault(x, cur)
    for d in DEG: d["bolum"] = gor.get(d["no"], "?")


def temiz(H):
    """Değişiklik işaretlerini kaldırır: güncel (temiz) metin."""
    H = re.sub(r'<div class="cik"[^>]*>.*?</div><!--/cik-->', "", H, flags=re.S)
    H = re.sub(r"<del [^>]*>.*?</del>", "", H, flags=re.S)
    H = re.sub(r"<ins [^>]*>(.*?)</ins>", r"\1", H, flags=re.S)
    H = re.sub(r'<span class="(?:kontrol|bicim)"[^>]*>(.*?)</span>', r"\1", H, flags=re.S)
    H = re.sub(r'\n?<div class="ekle"[^>]*>\n?', "\n", H); H = re.sub(r"\n</div>\n", "\n", H)
    H = re.sub(r' class="ekle" data-d="[^"]*" data-b="[^"]*"', "", H)
    H = re.sub(r' data-d="[^"]*" data-b="[^"]*"', "", H)
    return H
