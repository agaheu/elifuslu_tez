/* Küçük, bağımlılıksız SVG grafik yardımcıları. Renkler CSS değişkenlerinden gelir (açık/koyu tema). */
(function () {
  const NS = "http://www.w3.org/2000/svg";
  const el = (tag, attrs, parent) => {
    const e = document.createElementNS(NS, tag);
    for (const k in attrs || {}) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  };
  const fmt = (v, d = 2) => (v == null || !isFinite(v) ? "–" : Number(v).toLocaleString("tr-TR", { minimumFractionDigits: d, maximumFractionDigits: d }));

  let tip;
  function tooltip() {
    if (!tip) { tip = document.createElement("div"); tip.className = "tip"; tip.setAttribute("role", "status"); document.body.appendChild(tip); }
    return tip;
  }
  function showTip(evt, title, rows) {
    const t = tooltip(); t.replaceChildren();
    if (title) { const h = document.createElement("div"); h.className = "tip-h"; h.textContent = title; t.appendChild(h); }
    for (const r of rows) {
      const row = document.createElement("div"); row.className = "tip-r";
      if (r.cls) { const k = document.createElement("span"); k.className = "tip-k " + r.cls; row.appendChild(k); }
      const v = document.createElement("strong"); v.textContent = r.value; row.appendChild(v);
      const l = document.createElement("span"); l.textContent = r.label; row.appendChild(l);
      t.appendChild(row);
    }
    t.style.display = "block";
    const pad = 14, w = t.offsetWidth, h = t.offsetHeight;
    let x = evt.clientX + pad, y = evt.clientY + pad;
    if (x + w > innerWidth - 8) x = evt.clientX - w - pad;
    if (y + h > innerHeight - 8) y = evt.clientY - h - pad;
    t.style.left = Math.max(8, x) + "px"; t.style.top = Math.max(8, y) + "px";
  }
  function hideTip() { if (tip) tip.style.display = "none"; }

  function ticks(min, max, n = 5) {
    if (min === max) { min -= 1; max += 1; }
    const span = max - min, step0 = Math.pow(10, Math.floor(Math.log10(span / n)));
    const err = span / n / step0;
    const step = step0 * (err >= 7.5 ? 10 : err >= 3.5 ? 5 : err >= 1.5 ? 2 : 1);
    const out = [];
    for (let v = Math.ceil(min / step) * step; v <= max + step * 1e-9; v += step) out.push(Math.abs(v) < step * 1e-9 ? 0 : v);
    return { out, step };
  }
  const dec = (step) => Math.max(0, Math.min(4, -Math.floor(Math.log10(step) + 1e-9)));

  function frame(host, o) {
    host.replaceChildren();
    const W = Math.max(320, host.clientWidth || 720), H = o.height || 320;
    const two = (o.catLabels || []).some((c) => String(c).includes("\n"));
    const ncat = (o.cats || []).length, narrow = ncat && !o.numericX && (W - 82) / ncat < 58;
    const maxlab = Math.max(0, ...(o.catLabels || o.cats || []).map((c) => String(c).length));
    const m = Object.assign({ t: 14, r: 16, b: (o.xLabel ? 46 : 30) + (narrow ? Math.min(70, maxlab * 4.2) : two ? 14 : 0), l: o.yLabel ? 66 : 52 }, o.margin || {});
    const svg = el("svg", { viewBox: `0 0 ${W} ${H}`, width: "100%", height: H, role: "img", "aria-label": o.aria || "" }, host);
    const g = el("g", {}, svg);
    return { svg, g, W, H, m, iw: W - m.l - m.r, ih: H - m.t - m.b };
  }
  function yAxis(f, y0, y1, o) {
    const { out, step } = ticks(y0, y1, o.yTicks || 5), d = o.yDec != null ? o.yDec : dec(step);
    const sy = (v) => f.m.t + f.ih - ((v - y0) / (y1 - y0)) * f.ih;
    for (const v of out) {
      el("line", { x1: f.m.l, x2: f.m.l + f.iw, y1: sy(v), y2: sy(v), class: v === 0 && o.zero ? "axis0" : "grid" }, f.g);
      const t = el("text", { x: f.m.l - 8, y: sy(v) + 4, class: "tick", "text-anchor": "end" }, f.g); t.textContent = fmt(v, d) + (o.ySuffix || "");
    }
    if (o.yLabel) { const t = el("text", { x: 13, y: f.m.t + f.ih / 2, class: "axlab", transform: `rotate(-90 13 ${f.m.t + f.ih / 2})`, "text-anchor": "middle" }, f.g); t.textContent = o.yLabel; }
    return sy;
  }
  function xLab(f, o) {
    if (o.xLabel) { const t = el("text", { x: f.m.l + f.iw / 2, y: f.H - 6, class: "axlab", "text-anchor": "middle" }, f.g); t.textContent = o.xLabel; }
  }
  function bands(f, sx, list) {
    for (const b of list || []) {
      const x0 = sx(b.x0), x1 = sx(b.x1);
      el("rect", { x: x0, y: f.m.t, width: Math.max(0, x1 - x0), height: f.ih, class: "band " + (b.cls || "") }, f.g);
      if (b.label) { const t = el("text", { x: (x0 + x1) / 2, y: f.m.t + 13, class: "bandlab", "text-anchor": "middle" }, f.g); t.textContent = b.label; }
    }
  }
  const PHASES = [{ x0: 2004.5, x1: 2007.5, label: "Faz 1", cls: "b1" }, { x0: 2007.5, x1: 2012.5, label: "Faz 2", cls: "b2" }, { x0: 2012.5, x1: 2020.5, label: "Faz 3", cls: "b3" }];

  /* Çizgi grafik: series=[{name, cls, points:[[x,y],...]}] */
  function line(host, o) {
    const f = frame(host, o);
    const all = o.series.flatMap((s) => s.points.filter((p) => p[1] != null));
    if (!all.length) return;
    const xs = all.map((p) => p[0]), ys = all.map((p) => p[1]);
    const x0 = o.xMin != null ? o.xMin : Math.min(...xs), x1 = o.xMax != null ? o.xMax : Math.max(...xs);
    let y0 = o.yMin != null ? o.yMin : Math.min(...ys), y1 = Math.max(...ys);
    const padY = (y1 - y0) * 0.06 || 1; if (o.yMin == null) y0 -= padY; y1 += padY;
    const sx = (v) => f.m.l + ((v - x0) / (x1 - x0 || 1)) * f.iw;
    bands(f, sx, o.bands);
    const sy = yAxis(f, y0, y1, o);
    const xt = ticks(x0, x1, Math.min(8, Math.floor(f.iw / 70))).out.filter((v) => Number.isInteger(v));
    for (const v of xt) { const t = el("text", { x: sx(v), y: f.m.t + f.ih + 18, class: "tick", "text-anchor": "middle" }, f.g); t.textContent = v; }
    el("line", { x1: f.m.l, x2: f.m.l + f.iw, y1: f.m.t + f.ih, y2: f.m.t + f.ih, class: "axis" }, f.g);
    xLab(f, o);
    for (const s of o.series) {
      const pts = s.points.filter((p) => p[1] != null);
      el("path", { d: pts.map((p, i) => (i ? "L" : "M") + sx(p[0]).toFixed(1) + " " + sy(p[1]).toFixed(1)).join(""), class: "ln " + s.cls, fill: "none" }, f.g);
      if (o.series.length <= 4 && pts.length) {
        const last = pts[pts.length - 1];
        el("circle", { cx: sx(last[0]), cy: sy(last[1]), r: 4, class: "dot " + s.cls }, f.g);
      }
    }
    const cross = el("line", { y1: f.m.t, y2: f.m.t + f.ih, class: "cross", visibility: "hidden" }, f.g);
    const hit = el("rect", { x: f.m.l, y: f.m.t, width: f.iw, height: f.ih, fill: "transparent", tabindex: 0 }, f.g);
    const xsU = [...new Set(xs)].sort((a, b) => a - b);
    const at = (evt) => {
      const r = f.svg.getBoundingClientRect(), px = ((evt.clientX - r.left) / r.width) * f.W;
      const xv = x0 + ((px - f.m.l) / f.iw) * (x1 - x0);
      const near = xsU.reduce((a, b) => (Math.abs(b - xv) < Math.abs(a - xv) ? b : a));
      cross.setAttribute("x1", sx(near)); cross.setAttribute("x2", sx(near)); cross.setAttribute("visibility", "visible");
      const rows = o.series.map((s) => { const p = s.points.find((q) => q[0] === near); return p && p[1] != null ? { cls: s.cls, value: fmt(p[1], o.dec != null ? o.dec : 2), label: s.name } : null; }).filter(Boolean);
      rows.sort((a, b) => parseFloat(b.value.replace(/\./g, "").replace(",", ".")) - parseFloat(a.value.replace(/\./g, "").replace(",", ".")));
      showTip(evt, String(near), rows.slice(0, 15));
    };
    hit.addEventListener("pointermove", at); hit.addEventListener("pointerleave", () => { cross.setAttribute("visibility", "hidden"); hideTip(); });
  }

  /* Nokta + güven aralığı: cats=[etiket], series=[{name, cls, pts:[{b,lo,hi,note}]}]; numericX ise cats sayısal */
  function dotci(host, o) {
    const f = frame(host, o);
    const all = o.series.flatMap((s) => s.pts.filter(Boolean).flatMap((p) => [p.b, p.lo, p.hi].filter((v) => v != null && isFinite(v))));
    let y0 = Math.min(0, ...all), y1 = Math.max(0, ...all); const pad = (y1 - y0) * 0.08 || 0.1; y0 -= pad; y1 += pad;
    const n = o.cats.length, ns = o.series.length;
    let sx;
    if (o.numericX) { const a = Math.min(...o.cats) - 0.7, b = Math.max(...o.cats) + 0.7; sx = (v) => f.m.l + ((v - a) / (b - a)) * f.iw; bands(f, sx, o.bands); }
    else { const bw = f.iw / n; sx = (i) => f.m.l + bw * (i + 0.5); }
    const sy = yAxis(f, y0, y1, Object.assign({ zero: true }, o));
    const off = (j) => (ns === 1 ? 0 : (j - (ns - 1) / 2) * Math.min(22, (f.iw / n) * 0.28));
    o.cats.forEach((c, i) => {
      const cx = o.numericX ? sx(c) : sx(i);
      if (!o.numericX || o.cats.length < 14 || c % 5 === 0) {
        const lab = String(o.catLabels ? o.catLabels[i] : c);
        if (!o.numericX && f.iw / n < 58) {
          const t = el("text", { x: cx + 4, y: f.m.t + f.ih + 12, class: "tick", "text-anchor": "end", transform: `rotate(-40 ${cx + 4} ${f.m.t + f.ih + 12})` }, f.g); t.textContent = lab.replace("\n", " ");
        } else {
          lab.split("\n").forEach((ln, k) => { const t = el("text", { x: cx, y: f.m.t + f.ih + 18 + k * 13, class: "tick", "text-anchor": "middle" }, f.g); t.textContent = ln; });
        }
      }
      o.series.forEach((s, j) => {
        const p = s.pts[i]; if (!p || p.b == null) return;
        const x = cx + off(j);
        const gg = el("g", { class: "mark", tabindex: 0 }, f.g);
        if (p.lo != null && p.hi != null) {
          el("line", { x1: x, x2: x, y1: sy(p.lo), y2: sy(p.hi), class: "whisk " + s.cls }, gg);
          el("line", { x1: x - 4, x2: x + 4, y1: sy(p.lo), y2: sy(p.lo), class: "whisk " + s.cls }, gg);
          el("line", { x1: x - 4, x2: x + 4, y1: sy(p.hi), y2: sy(p.hi), class: "whisk " + s.cls }, gg);
        }
        el("circle", { cx: x, cy: sy(p.b), r: 5, class: "dot " + s.cls + (p.hollow ? " hollow" : "") }, gg);
        el("rect", { x: x - 12, y: Math.min(sy(p.hi != null ? p.hi : p.b), sy(p.b) - 12), width: 24, height: Math.max(24, Math.abs(sy(p.lo != null ? p.lo : p.b) - sy(p.hi != null ? p.hi : p.b))), fill: "transparent" }, gg);
        const show = (evt) => showTip(evt, (o.catLabels ? o.catLabels[i] : String(c)).replace("\n", " ") + " · " + s.name, [
          { cls: s.cls, value: fmt(p.b, 4), label: "katsayı" + (o.pct ? ` (≈ %${fmt(100 * (Math.exp(p.b) - 1), 1)})` : "") },
          ...(p.lo != null ? [{ value: `[${fmt(p.lo, 4)}; ${fmt(p.hi, 4)}]`, label: o.ciLabel || "%95 GA" }] : []),
          ...(p.note ? [{ value: p.note, label: "" }] : [])]);
        gg.addEventListener("pointermove", show); gg.addEventListener("focus", (e) => { const r = gg.getBoundingClientRect(); show({ clientX: r.right, clientY: r.top }); });
        gg.addEventListener("pointerleave", hideTip); gg.addEventListener("blur", hideTip);
      });
    });
    xLab(f, o);
  }

  /* Histogram: groups=[{name, cls, values}] üst üste yığılı; markers=[{x,label}] */
  function hist(host, o) {
    const f = frame(host, o);
    const all = o.groups.flatMap((g) => g.values);
    const lo = o.min != null ? o.min : Math.min(...all), hi = o.max != null ? o.max : Math.max(...all), nb = o.bins || 40, bw = (hi - lo) / nb;
    const counts = o.groups.map((g) => { const c = new Array(nb).fill(0); for (const v of g.values) { const k = Math.min(nb - 1, Math.max(0, Math.floor((v - lo) / bw))); c[k]++; } return c; });
    const tot = counts[0].map((_, k) => counts.reduce((a, c) => a + c[k], 0)), ymax = Math.max(...tot) * 1.08;
    const sx = (v) => f.m.l + ((v - lo) / (hi - lo)) * f.iw;
    const sy = yAxis(f, 0, ymax, Object.assign({ yDec: 0 }, o));
    const xt = ticks(lo, hi, Math.min(8, Math.floor(f.iw / 80)));
    for (const v of xt.out) { const t = el("text", { x: sx(v), y: f.m.t + f.ih + 18, class: "tick", "text-anchor": "middle" }, f.g); t.textContent = fmt(v, dec(xt.step)); }
    for (let k = 0; k < nb; k++) {
      let base = 0;
      const gg = el("g", { class: "mark" }, f.g);
      o.groups.forEach((g, j) => {
        const c = counts[j][k]; if (!c) return;
        const y1 = sy(base + c), y0 = sy(base);
        el("rect", { x: sx(lo + k * bw) + 1, y: y1, width: Math.max(1, sx(lo + (k + 1) * bw) - sx(lo + k * bw) - 2), height: Math.max(0, y0 - y1 - (j < o.groups.length - 1 ? 0 : 0)), class: "bar " + g.cls }, gg);
        base += c;
      });
      el("rect", { x: sx(lo + k * bw), y: f.m.t, width: sx(lo + (k + 1) * bw) - sx(lo + k * bw), height: f.ih, fill: "transparent" }, gg);
      gg.addEventListener("pointermove", (evt) => showTip(evt, `${fmt(lo + k * bw, 3)} – ${fmt(lo + (k + 1) * bw, 3)}`, o.groups.map((g, j) => ({ cls: g.cls, value: String(counts[j][k]), label: g.name }))));
      gg.addEventListener("pointerleave", hideTip);
    }
    el("line", { x1: f.m.l, x2: f.m.l + f.iw, y1: f.m.t + f.ih, y2: f.m.t + f.ih, class: "axis" }, f.g);
    (o.markers || []).forEach((mk, i) => {
      if (mk.x < lo || mk.x > hi) return;
      el("line", { x1: sx(mk.x), x2: sx(mk.x), y1: f.m.t, y2: f.m.t + f.ih, class: "marker " + (mk.cls || "") }, f.g);
      const t = el("text", { x: sx(mk.x) + (mk.left ? -5 : 5), y: f.m.t + 12 + i * 14, class: "bandlab", "text-anchor": mk.left ? "end" : "start" }, f.g); t.textContent = mk.label;
    });
    xLab(f, o);
  }

  /* Dumbbell / yatay çubuk: rows=[{label, a, b}] */
  function dumbbell(host, o) {
    const rows = o.rows, rh = 26;
    const f = frame(host, Object.assign({}, o, { height: rows.length * rh + 56, margin: { l: 104, t: 8, r: 24, b: 44 } }));
    const mx = Math.max(...rows.flatMap((r) => [r.a, r.b])) * 1.05, sx = (v) => f.m.l + (v / mx) * f.iw;
    const xt = ticks(0, mx, 5);
    for (const v of xt.out) {
      el("line", { x1: sx(v), x2: sx(v), y1: f.m.t, y2: f.m.t + f.ih, class: "grid" }, f.g);
      const t = el("text", { x: sx(v), y: f.m.t + f.ih + 16, class: "tick", "text-anchor": "middle" }, f.g); t.textContent = fmt(v, dec(xt.step));
    }
    rows.forEach((r, i) => {
      const y = f.m.t + i * rh + rh / 2;
      const t = el("text", { x: f.m.l - 10, y: y + 4, class: "tick", "text-anchor": "end" }, f.g); t.textContent = r.label;
      const gg = el("g", { class: "mark", tabindex: 0 }, f.g);
      el("line", { x1: sx(r.a), x2: sx(r.b), y1: y, y2: y, class: "conn" }, gg);
      el("circle", { cx: sx(r.a), cy: y, r: 5, class: "dot " + o.clsA }, gg); el("circle", { cx: sx(r.b), cy: y, r: 5, class: "dot " + o.clsB }, gg);
      el("rect", { x: f.m.l, y: y - rh / 2, width: f.iw, height: rh, fill: "transparent" }, gg);
      const show = (evt) => showTip(evt, r.label, [{ cls: o.clsA, value: fmt(r.a, 3), label: o.nameA }, { cls: o.clsB, value: fmt(r.b, 3), label: o.nameB }, { value: "×" + fmt(r.b / r.a, 1), label: "artış katı" }]);
      gg.addEventListener("pointermove", show); gg.addEventListener("pointerleave", hideTip);
    });
    xLab(f, o);
  }

  /* Spesifikasyon eğrisi: pts=[{b, lo, hi, cls, sig, tipTitle, tipRows}] (sıralı) */
  function spec(host, o) {
    const f = frame(host, o);
    const all = o.pts.flatMap((p) => [p.lo, p.hi]);
    let y0 = Math.min(0, ...all), y1 = Math.max(0, ...all); const pad = (y1 - y0) * 0.05; y0 -= pad; y1 += pad;
    const sy = yAxis(f, y0, y1, Object.assign({ zero: true }, o));
    const n = o.pts.length, sx = (i) => f.m.l + ((i + 0.5) / n) * f.iw;
    o.pts.forEach((p, i) => { el("line", { x1: sx(i), x2: sx(i), y1: sy(p.lo), y2: sy(p.hi), class: "specw " + p.cls }, f.g); });
    o.pts.forEach((p, i) => { el("circle", { cx: sx(i), cy: sy(p.b), r: n > 500 ? 1.6 : 2.4, class: "dot nr " + p.cls + (p.sig ? "" : " faint") }, f.g); });
    if (o.ref != null) {
      el("line", { x1: f.m.l, x2: f.m.l + f.iw, y1: sy(o.ref), y2: sy(o.ref), class: "marker" }, f.g);
      const t = el("text", { x: f.m.l + f.iw - 4, y: sy(o.ref) - 5, class: "bandlab", "text-anchor": "end" }, f.g); t.textContent = o.refLabel || "";
    }
    const cross = el("line", { y1: f.m.t, y2: f.m.t + f.ih, class: "cross", visibility: "hidden" }, f.g);
    const hit = el("rect", { x: f.m.l, y: f.m.t, width: f.iw, height: f.ih, fill: "transparent" }, f.g);
    hit.addEventListener("pointermove", (evt) => {
      const r = f.svg.getBoundingClientRect(), px = ((evt.clientX - r.left) / r.width) * f.W;
      const i = Math.max(0, Math.min(n - 1, Math.floor(((px - f.m.l) / f.iw) * n))), p = o.pts[i];
      cross.setAttribute("x1", sx(i)); cross.setAttribute("x2", sx(i)); cross.setAttribute("visibility", "visible");
      showTip(evt, p.tipTitle, p.tipRows);
    });
    hit.addEventListener("pointerleave", () => { cross.setAttribute("visibility", "hidden"); hideTip(); });
    xLab(f, o);
  }

  window.Viz = { line, dotci, hist, dumbbell, spec, fmt, PHASES, hideTip };
})();
