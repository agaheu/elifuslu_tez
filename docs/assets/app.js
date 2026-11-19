/* AB ETS & Yeşil İnovasyon — inceleme sitesi. Tüm sayılar data/*.json dosyalarından okunur. */
(async function () {
  const REPO = "https://github.com/agaheu/elifuslu_tez/blob/HEAD/";
  const $ = (s, r = document) => r.querySelector(s);
  const h = (tag, props, ...kids) => {
    const e = document.createElement(tag);
    for (const k in props || {}) {
      if (k === "class") e.className = props[k]; else if (k === "html") e.innerHTML = props[k];
      else if (k.startsWith("on")) e.addEventListener(k.slice(2), props[k]); else if (props[k] != null && props[k] !== false) e.setAttribute(k, props[k]);
    }
    for (const c of kids.flat()) if (c != null && c !== false) e.append(c.nodeType ? c : document.createTextNode(String(c)));
    return e;
  };
  const tr = (v, d = 3) => (v == null || !isFinite(v) ? "–" : Number(v).toLocaleString("tr-TR", { minimumFractionDigits: d, maximumFractionDigits: d }).replace("-", "−"));
  const pv = (p) => (p == null || !isFinite(p) ? "–" : p < 0.0005 ? "<0,001" : tr(p, 3));
  const pcls = (p) => (p == null || !isFinite(p) ? "pn" : p < 0.01 ? "p1" : p < 0.05 ? "p5" : p < 0.1 ? "p10" : "pn");
  const pcell = (p) => h("td", { class: "pcell" }, h("span", { class: "pp " + pcls(p) }, pv(p)));
  const pctEff = (b) => tr(100 * (Math.exp(b) - 1), 1);
  const load = (f) => fetch("data/" + f).then((r) => { if (!r.ok) throw new Error(f); return r.json(); });

  let R, IC, PANEL, SPEC, BOOT, UR, EKD, SIM, SIMP, J2D;
  try {
    [R, IC, PANEL, SPEC, BOOT, UR, EKD, SIM, SIMP, J2D] = await Promise.all(["sonuclar.json", "icerik.json", "panel.json", "spec_egrisi.json", "bootstrap_m1.json", "birim_kok.json", "ek_dogrulama.json", "simulasyon.json", "simulasyon_p.json", "juri2.json"].map(load));
  } catch (e) {
    $("#yukleniyor").textContent = "Veri dosyaları yüklenemedi (" + e.message + "). Sayfayı bir web sunucusu üzerinden açın.";
    return;
  }
  const P = "poisson", N = "nb", FAM = { poisson: "Poisson QML", nb: "Negatif binom" };
  const AD = { F1: "Faz 1", F2: "Faz 2", F3: "Faz 3", lnK1: "Stok ln(1+K)", gdp_growth_l1: "GSYİH büyümesi", renew_wdi_l1: "Yenilenebilir payı", impdep_l1: "Enerji ithalat bağ.", manuf_l1: "İmalat payı", trade_l1: "Ticaret açıklığı", tstar: "ETS öncesi eğilim", S1: "Faz 1 eğim", S2: "Faz 2 eğim", S3: "Faz 3 eğim" };
  const AD2 = Object.assign({}, AD, { F1: "Faz 1 düzey", F2: "Faz 2 düzey", F3: "Faz 3 düzey" });
  const ONEM = { kritik: "b-kritik", "önemli": "b-onemli", orta: "b-orta", "küçük": "b-kucuk" };
  const badge = (t, cls) => h("span", { class: "badge " + (cls || "") }, t);
  const legend = (items) => h("div", { class: "legend" }, items.map(([cls, t]) => h("span", null, h("i", { class: "key " + cls }), t)));
  const table = (head, rows, opt = {}) => {
    const t = h("table", null, h("thead", null, h("tr", null, head.map((x) => h("th", { class: opt.num && opt.num.includes(head.indexOf(x)) ? "num" : null }, x)))));
    const tb = h("tbody"); t.append(tb);
    for (const r of rows) tb.append(h("tr", null, r.map((x, i) => (x && x.nodeType ? (x.tagName === "TD" ? x : h("td", null, x)) : h("td", { class: opt.num && opt.num.includes(i) ? "num" : null }, x == null ? "–" : x)))));
    return h("div", { class: "tw" + (opt.tall ? " tall" : "") }, t);
  };
  const redraws = [];
  /* Grafik kartı: çizim + tablo görünümü ikizi */
  function chartCard(title, sub, leg, draw, tbl, note) {
    const host = h("div", { class: "chart" }), tw = h("div", { style: "display:none" });
    const btn = h("button", { type: "button", onclick: () => { const on = tw.style.display === "none"; tw.style.display = on ? "" : "none"; host.style.display = on ? "none" : ""; btn.textContent = on ? "Grafik" : "Tablo olarak göster"; if (on) { tw.replaceChildren(tbl()); } else draw(host); } }, "Tablo olarak göster");
    const card = h("div", { class: "card" }, h("h3", null, title), sub ? h("div", { class: "sub" }, sub) : null, leg ? legend(leg) : null, host, tw, tbl ? h("div", { class: "chart-tools" }, btn) : null, note ? h("div", { class: "takeaway", html: note }) : null);
    const rd = () => { if (host.isConnected && host.offsetParent !== null) draw(host); };
    redraws.push(rd); requestAnimationFrame(rd);
    card.redraw = rd;
    return card;
  }
  const seg = (opts, cur, on) => { const d = h("div", { class: "seg", role: "group" }); opts.forEach(([v, t]) => d.append(h("button", { type: "button", class: v === cur ? "on" : "", onclick: (e) => { [...d.children].forEach((b) => b.classList.remove("on")); e.target.classList.add("on"); on(v); } }, t))); return d; };
  const sel = (opts, cur, on) => { const s = h("select", { onchange: (e) => on(e.target.value) }); opts.forEach(([v, t]) => s.append(h("option", Object.assign({ value: v }, v === cur ? { selected: "" } : {}), t))); return s; };

  const say = (o) => IC.bulgular.filter((b) => b.onem === o).length;
  const PAGES = [
    ["ozet", "◎", "Özet"], ["rapor", "❡", "Rapor (tam metin)"], ["bolumler", "☰", "Tez bölümleri"], ["veri", "▤", "Veri"], ["replikasyon", "⟳", "Yeniden üretim"], ["modeller", "ƒ", "Modeller"], ["cikarsama", "±", "Çıkarsama"],
    ["saglamlik", "≋", "Sağlamlık"], ["bulgular", "⚑", "Bulgular", IC.bulgular.length], ["kaynakca", "❞", "Kaynakça"], ["juri", "§", "Jüri raporları"], ["yapilacak", "☑", "Yapılacaklar", IC.yapilacak.length], ["belgeler", "▣", "Belgeler"]];
  const para = (t) => { const parts = t.split(" • "); if (parts.length < 3) return h("p", null, t.replace(/^• /, "")); return h("ul", null, parts.map((x) => h("li", null, x.replace(/^• /, "")))); };
  const durumCls = (d) => (d.startsWith("yeni") ? "b-info" : d.includes("doğrulanamadı") || d.includes("kısmen") ? "b-orta" : "b-ok");
  let ANL = "sade"; try { ANL = localStorage.getItem("anlatim") === "teknik" ? "teknik" : "sade"; } catch (e) {}
  document.documentElement.setAttribute("data-anlatim", ANL);
  const anlSegs = [];
  const anlatimSeg = () => { const d = h("div", { class: "seg anl", role: "group", "aria-label": "Anlatım düzeyi" });
    [["sade", "Sade anlatım"], ["teknik", "Teknik anlatım"]].forEach(([v, t]) => d.append(h("button", { type: "button", "data-v": v, class: v === ANL ? "on" : "", "aria-pressed": v === ANL ? "true" : "false", onclick: () => { ANL = v; document.documentElement.setAttribute("data-anlatim", v); try { localStorage.setItem("anlatim", v); } catch (e) {}
      anlSegs.forEach((g) => [...g.children].forEach((x) => { const on = x.dataset.v === v; x.classList.toggle("on", on); x.setAttribute("aria-pressed", on ? "true" : "false"); })); } }, t)));
    anlSegs.push(d); return d; };
  const anlatimBar = () => h("div", { class: "anlbar" }, h("span", { class: "small" }, "Bulguların anlatımı:"), anlatimSeg(), h("span", { class: "small v-sade" }, "Günlük dille: sorun ne, neden önemli, ne yapılmalı."), h("span", { class: "small v-teknik" }, "Ekonometri diliyle: tespit, sayısal kanıt, öneri."));
  const kopyala = (t) => h("button", { type: "button", class: "kopya", onclick: (e) => { const b = e.currentTarget; const ok = () => { b.textContent = "Kopyalandı"; setTimeout(() => (b.textContent = "Metni kopyala"), 1600); };
    try { navigator.clipboard.writeText(t).then(ok, () => (b.textContent = "Kopyalanamadı")); } catch (x) { b.textContent = "Kopyalanamadı"; } } }, "Metni kopyala");
  const findingEl = (b, pre) => { const s = b.sade;
    return h("details", { class: "finding", id: (pre || "b-") + b.id }, h("summary", null, badge(b.onem, ONEM[b.onem]), h("span", null, h("span", { class: "id" }, b.id + " · " + b.kat), h("br"), h("span", { class: "ttl v-sade" }, s.baslik), h("span", { class: "ttl v-teknik" }, b.baslik)), h("span", { class: "small" }, b.yer)),
      h("div", { class: "body" }, h("div", { class: "meta" }, b.kaynak.map((k) => badge(k)), badge(b.durum, durumCls(b.durum))),
        h("div", { class: "v-sade" }, h("h4", null, "Sorun ne?"), para(s.sorun), h("h4", null, "Neden önemli?"), para(s.neden)),
        h("div", { class: "v-teknik" }, h("h4", null, "Tespit"), para(b.tespit), h("h4", null, "Kanıt"), para(b.kanit), h("h4", null, "Öneri"), para(b.oneri)),
        h("h4", null, "Ne yapılmalı? Adım adım düzeltme"), h("ol", { class: "adim" }, s.adimlar.map((x) => h("li", null, x))),
        s.ornek ? h("div", { class: "ornek" }, h("h4", null, "Teze yazılabilecek örnek metin"), h("p", null, s.ornek), kopyala(s.ornek)) : null)); };
  const bulguLink = (id) => h("a", { href: "#bulgular", class: "small", style: "margin-right:8px", onclick: () => setTimeout(() => { const d = document.getElementById("b-" + id); if (d) { d.open = true; d.scrollIntoView({ block: "center" }); } }, 80) }, id);
  const mdView = async (view, f) => { view.textContent = "Yükleniyor…"; try { const t = await fetch("raporlar/" + f).then((r) => { if (!r.ok) throw 0; return r.text(); }); view.innerHTML = marked.parse(t); view.querySelectorAll("table").forEach((t_) => { const w = h("div", { class: "tw" }); t_.replaceWith(w); w.append(t_); }); } catch (e) { view.textContent = "Belge yüklenemedi."; } };
  const main = $("#main"); main.replaceChildren();
  const nav = $("#nav");
  const built = {};
  const pages = {};
  PAGES.forEach(([id, ic, t, cnt]) => {
    nav.append(h("a", { href: "#" + id, "data-p": id }, h("span", { class: "ic", "aria-hidden": "true" }, ic), t, cnt ? h("span", { class: "cnt" }, cnt) : null));
    pages[id] = h("section", { class: "page", id: "p-" + id }); main.append(pages[id]);
  });
  $("#foot").replaceChildren(h("div", null, "İnceleme tarihi: " + IC.ozet.tarih), h("div", null, "Bootstrap B = " + R.meta.B + " · N = " + R.meta.N), h("div", { style: "margin-top:6px" }, h("a", { href: "https://github.com/agaheu/elifuslu_tez" }, "GitHub deposu")));
  $("#tema").addEventListener("click", () => {
    const cur = document.documentElement.getAttribute("data-theme") || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    const nx = cur === "dark" ? "light" : "dark"; document.documentElement.setAttribute("data-theme", nx); try { localStorage.setItem("tema", nx); } catch (e) {}
  });

  const C = (m, f, k) => R[m][f].coef[k], B = (m, f, k) => R[m][f].boot.coef[k];
  const T13 = 2.1604;
  const SEN = ["A", "A2", "B", "C"];
  const mcr = (f, j) => { const ps = SEN.map((g) => SIMP[g][f].p_tek[j]); const a = pv(Math.min(...ps)), b = pv(Math.max(...ps)); return a === b ? a : a + "–" + b; };
  const simr = (key, g) => { const xs = [P, N].flatMap((f) => SIM[g][f][key]); return "%" + tr(100 * Math.min(...xs), 0) + "–" + tr(100 * Math.max(...xs), 0); };

  // ================================================================ ÖZET
  function ozet(el) {
    const u = IC.ozet.uyum;
    el.append(h("h1", null, "AB ETS'nin yeşil inovasyona etkisi: 5. bölümün kapsamlı yeniden incelemesi"),
      h("p", { class: "lede" }, "Doktora tezinin ekonometri bölümü ve veri seti, önceki incelemeler dâhil hiçbir şey doğru varsayılmadan baştan sona yeniden incelendi. Bütün tahminler ham veriden bağımsız yazılımla yeniden üretildi; tezde olmayan çıkarsama, tanım ve benzetim sınamaları eklendi."));
    el.append(h("div", { class: "hero" },
      h("div", { class: "verdict" }, h("h3", null, "Sonuç: hesaplar doğru, yorumlar fazla iddialı"),
        h("p", null, "Tezde raporlanan sayılar yeniden üretilebiliyor; hesaplama hatası yok. Sorunlar, tasarımın neyi tanımlayabildiğinde ve hipotez tablosunun kanıttan ileri gitmesinde. “AB ETS yeşil inovasyonu artırmıştır” nedensel iddiası bu tasarımla taşınamıyor; “ilk iki faza denk gelen dönemde, önceki eğilimin ve bilgi stokunun açıklayamadığı bir yükseliş vardır ve üçüncü fazda sürmemiştir” betimleyici bulgusu ise güçlü."),
        h("p", { class: "small", style: "margin:0" }, "Birinci jüri raporundaki “önemli düzeltme gerekli” yargısıyla örtüşüyor; ikinci jüri raporunun “düzeltmelerle yayına hazır” yargısı fazla iyimser. Düzeltmelerin çoğu yeni veri değil, yeniden yazım ve birkaç ek tablo gerektiriyor.")),
      h("div", { class: "grid g2" },
        h("div", { class: "tile" }, h("div", { class: "lab" }, "Birebir yeniden üretilen değer"), h("div", { class: "val" }, u[0] + " / " + u[1]), h("div", { class: "note" }, "katsayı, istatistik, VIF, korelasyon")),
        h("div", { class: "tile" }, h("div", { class: "lab" }, "Bulgu"), h("div", { class: "val" }, IC.bulgular.length), h("div", { class: "chips", style: "margin-top:4px" }, badge(say("kritik") + " kritik", "b-kritik"), badge(say("önemli") + " önemli", "b-onemli"), badge(say("orta") + " orta", "b-orta"), badge(say("küçük") + " küçük", "b-kucuk"))),
        h("div", { class: "tile" }, h("div", { class: "lab" }, "Etki sıfırken tezin yönteminin “anlamlı” bulma oranı"), h("div", { class: "val" }, simr("rej_boot", "A")), h("div", { class: "note" }, "nominal %5; etkin küme sayısı " + tr(C("m1", P, "F1").Gstar, 1) + " (14 ülke)")),
        h("div", { class: "tile" }, h("div", { class: "lab" }, "Faz 2'nin pozitif ve anlamlı çıktığı tanım"), h("div", { class: "val" }, "%" + tr(100 * R.ek.spec_ozet.F2.poz_anlamli5, 1)), h("div", { class: "note" }, R.ek.spec_ozet.n + " alternatif tanım içinde")))));

    const yrs = Object.keys(R.veri.yillik_toplam).map(Number);
    el.append(h("div", { class: "grid g2", style: "margin-top:18px" },
      chartCard("14 ülkenin toplam yeşil patent başvurusu", "EPO, iklim değişikliği azaltım teknolojileri, öncelik yılına göre; gölgeli alanlar AB ETS fazları", null,
        (host) => Viz.line(host, { series: [{ name: "Toplam başvuru", cls: "c1", points: yrs.map((y) => [y, R.veri.yillik_toplam[y]]) }], bands: Viz.PHASES, yMin: 0, dec: 0, height: 290, yLabel: "adet" }),
        () => table(["Yıl", "Toplam başvuru"], yrs.map((y) => [y, tr(R.veri.yillik_toplam[y], 0)]), { num: [1], tall: true }),
        "Yükseliş <b>ETS'den önce başlıyor</b> (1997–2004'te %60 artış), 2011'de zirve yapıyor, 2013–2016'da geriliyor. Tezin temel sorusu, 2005 sonrasındaki hızlanmanın ne kadarının ETS'ye atfedilebileceği."),
      chartCard("Faz katsayıları (Model 1)", "ETS öncesine (1997–2004) göre log fark; çubuklar %95 yüzdelik bootstrap aralığı", [["c1", FAM[P]], ["c2", FAM[N]]],
        (host) => Viz.dotci(host, { cats: ["F1", "F2", "F3"], catLabels: ["Faz 1\n2005–2007", "Faz 2\n2008–2012", "Faz 3\n2013–2020"], pct: true, height: 290, yLabel: "katsayı (log puan)", ciLabel: "%95 yüzdelik bootstrap",
          series: [P, N].map((f, j) => ({ name: FAM[f], cls: "c" + (j + 1), pts: ["F1", "F2", "F3"].map((k) => ({ b: B("m1", f, k).b, lo: B("m1", f, k).pct[0], hi: B("m1", f, k).pct[1] })) })) }),
        () => table(["", "Tahminci", "Katsayı", "≈ %", "%95 yüzdelik"], ["F1", "F2", "F3"].flatMap((k) => [P, N].map((f) => [AD[k], FAM[f], tr(B("m1", f, k).b, 4), pctEff(B("m1", f, k).b), `[${tr(B("m1", f, k).pct[0], 3)}; ${tr(B("m1", f, k).pct[1], 3)}]`])), { num: [2, 3, 4] }),
        "Faz 1 ve Faz 2 pozitif, Faz 3 sıfırdan ayırt edilemiyor. Bu katsayılar yeniden üretildi; tartışma, bunların <b>neyin etkisi</b> olduğunda.")));

    el.append(h("h2", null, "Sağlam olan ve olmayan"));
    el.append(h("div", { class: "grid g2" },
      h("div", { class: "card" }, h("h3", null, badge("Sağlam", "b-ok"), " Yeniden üretilen ve dayanıklı bulgular"),
        h("ul", null,
          h("li", null, "Tezdeki bütün katsayılar, testler ve tablolar bağımsız yazılımla yeniden üretildi."),
          h("li", null, `Faz 2 farkı negatif binomda her çıkarsama yönteminde anlamlı (küme jackknife p = ${pv(C("m1", N, "F2").p_cv3)}) ve “gerçek etki sıfır” benzetimlerinde nadir (Monte Carlo p = ${mcr(N, 1)}).`),
          h("li", null, `Model 2'de Faz 1 eğim (${tr(C("m2", N, "S1").b, 3)}) ve Faz 2 düzey (${tr(C("m2", N, "F2").b, 3)}) katsayıları stoklu ve stoksuz tanımlarda anlamlı; benzetimlerde yanlılık yok denecek kadar küçük (Monte Carlo p = ${mcr(N, 4)} ve ${mcr(N, 5)}).`),
          h("li", null, "Eskime oranı, son yılların çıkarılması, ülke dışlamaları ve kesirli sayım kullanımı sonucu değiştirmiyor."),
          h("li", null, "Faz 3'te stok kontrol edildiğinde ek fark yok (tezin H4 sonucu doğru)."))),
      h("div", { class: "card" }, h("h3", null, badge("Sorunlu", "b-kritik"), " Tezin iddia ettiği ama kanıtın taşımadığı"),
        h("ul", null,
          h("li", null, h("b", null, "Nedensellik: "), "kontrol grubu yok; faz kuklaları o yılların bütün ortak şoklarını ölçüyor (Kyoto 2008–2012 = Faz 2)."),
          h("li", null, h("b", null, "H5: "), `“ETS öncesi eğilim yok” stok kontrolünün yan ürünü; stoksuz tanımda eğilim yılda ${tr(R.ek.m2_stoksuz.nb.tstar.b, 3)} ve anlamlı.`),
          h("li", null, h("b", null, "H1: "), "“toplam etki %44 / %101 / %89” eğilimi de içeriyor; Faz 3 değeri eğilimin öngördüğünün altında."),
          h("li", null, h("b", null, "Çıkarsama: "), `tezin yöntemi gerçek etki sıfırken %5 yerine ${simr("rej_boot", "A")} oranında “anlamlı” buluyor; Faz 1 kırılgan (Monte Carlo p: Poisson ${mcr(P, 0)}, negatif binom ${mcr(N, 0)}).`),
          h("li", null, h("b", null, "Yanlılık: "), `gerçek etki sıfırken bile Model 1 ortalama Faz 1 ≈ +${tr(SIMP.A.nb.ort[0], 2)}, Faz 2 ≈ +${tr(SIMP.A.nb.ort[1], 2)}, Faz 3 ≈ +${tr(SIMP.A.nb.ort[2], 2)} tahmin ediyor (stok katsayısı aşağı yanlı).`),
          h("li", null, h("b", null, "Tanıma duyarlılık: "), `sabit etkiler yerine ön-örneklem ortalaması kullanılınca Faz 1 ve Faz 2 katsayıları ${tr(R.ek.presample.nb.F1.b, 2)} ve ${tr(R.ek.presample.nb.F2.b, 2)}'ye iniyor.`)),
        h("a", { href: "#bulgular" }, "Tüm bulgular →"))));

    el.append(h("h2", null, "Hipotezlerin yeniden değerlendirilmesi"));
    const hc = h("div", { class: "card" }); el.append(hc);
    const vcls = { "Destekleniyor": "b-ok", "Kısmen": "b-orta", "Koşullu": "b-orta", "Desteklenmiyor": "b-info", "Bu hâliyle desteklenmiyor": "b-kritik" };
    hc.append(h("div", { class: "hyp small", style: "font-weight:600" }, h("div"), h("div", null, "Hipotez"), h("div", null, "Tezin sonucu"), h("div", null, "Yeniden değerlendirme")));
    IC.hipotez.forEach((x) => hc.append(h("div", { class: "hyp" }, h("div", { class: "hid" }, x[0]), h("div", null, h("div", { style: "font-weight:600" }, x[1]), h("div", { class: "small", style: "margin-top:4px" }, x[5])), h("div", null, badge(x[2], x[2].includes("mem") ? "b-info" : "b-ok")), h("div", null, badge(x[3], vcls[x[3]] || "")))));
    el.append(h("h2", null, "İncelemenin sınırları"), h("div", { class: "card" }, h("ul", null,
      h("li", null, h("b", null, "Ham veri kaynağından doğrulanamadı: "), "çalışma ortamından OECD, Eurostat ve Dünya Bankası sunucularına erişim kapalıydı. Veri setinin iç tutarlılığı tam; kaynaklarla karşılaştırma yapılmadı."),
      h("li", null, "Birleşik Krallık'ın eklenmesi, Ar-Ge harcaması kontrolü ve maruziyet tasarımı yeni veri gerektirdiği için sınanamadı."),
      h("li", null, "Pedroni testi ve Kao'nun düzeltilmiş istatistikleri yeniden üretilmedi; Stata do-dosyası görülmedi."),
      h("li", null, "Yalnızca 5. Bölüm incelendi. Nihai akademik hüküm danışman ve jüriye aittir."))));
  }

  // ================================================================ VERİ
  function veri(el) {
    el.append(h("h1", null, "Veri seti"), h("p", { class: "lede" }, `14 AB ülkesi, 1990–2020 (tahmin dönemi 1997–2020, ${R.meta.N} gözlem). Değişkeni seçin; en çok üç ülkeyi vurgulayın, diğerleri bağlam olarak gri kalır.`));
    const VARS = { inten: ["Yeşil patent yoğunluğu (milyar € reel GSYİH başına)", 3], ccm: ["Yeşil patent başvurusu (adet)", 0], K: ["Yeşil patent stoku", 0], gdp_real: ["Reel GSYİH (milyon €, 2015 zincirlenmiş)", 0], gdp_growth: ["GSYİH büyüme oranı (%)", 1], renew_wdi: ["Yenilenebilir enerji payı (%)", 1], impdep: ["Enerji ithalat bağımlılığı (%)", 1], manuf: ["İmalat sanayi payı (%)", 1], trade: ["Ticaret açıklığı (%)", 1] };
    const ctry = [...new Set(PANEL.map((r) => r.country))].sort((a, b) => a.localeCompare(b, "tr"));
    let v = "inten", hi = ["Almanya", "Danimarka", "Portekiz"];
    const chips = h("div", { class: "row" });
    const host = h("div"), lg = h("div"), tw = h("div", { style: "display:none" });
    const slot = () => { const m = {}; hi.forEach((c, i) => (m[c] = "c" + (i + 1))); return m; };
    const draw = () => {
      const sl = slot();
      const series = ctry.filter((c) => !sl[c]).map((c) => ({ name: c, cls: "cg thin", points: PANEL.filter((r) => r.country === c).map((r) => [r.year, r[v]]) }))
        .concat(hi.map((c) => ({ name: c, cls: sl[c], points: PANEL.filter((r) => r.country === c).map((r) => [r.year, r[v]]) })));
      lg.replaceChildren(legend(hi.map((c) => [sl[c], c]).concat([["cg", "diğer ülkeler"]])));
      Viz.line(host, { series, bands: Viz.PHASES, dec: VARS[v][1], height: 360, yLabel: VARS[v][0].split(" (")[0] });
      tw.replaceChildren(table(["Yıl", ...hi], [...new Set(PANEL.map((r) => r.year))].map((y) => [y, ...hi.map((c) => { const r = PANEL.find((q) => q.country === c && q.year === y); return r && r[v] != null ? tr(r[v], VARS[v][1]) : "–"; })]), { num: [1, 2, 3], tall: true }));
    };
    const mkChips = () => { chips.replaceChildren(...ctry.map((c) => h("label", { class: "chk" }, h("input", Object.assign({ type: "checkbox", onchange: (e) => { if (e.target.checked) { if (hi.length >= 3) hi.shift(); hi.push(c); } else hi = hi.filter((x) => x !== c); mkChips(); draw(); } }, hi.includes(c) ? { checked: "" } : {})), c))); };
    mkChips();
    el.append(h("div", { class: "filters" }, h("label", null, "Değişken", sel(Object.entries(VARS).map(([k, x]) => [k, x[0]]), v, (x) => { v = x; draw(); })), h("label", null, "Vurgulanan ülkeler (en çok 3)", chips)));
    const tb = h("button", { type: "button", onclick: () => { const on = tw.style.display === "none"; tw.style.display = on ? "" : "none"; tb.textContent = on ? "Tabloyu gizle" : "Tablo olarak göster"; } }, "Tablo olarak göster");
    el.append(h("div", { class: "card" }, lg, host, h("div", { class: "chart-tools" }, tb), tw));
    redraws.push(() => { if (host.offsetParent !== null) draw(); }); requestAnimationFrame(draw);

    const yo = Object.entries(R.veri.yogunluk_ulke).map(([k, x]) => ({ label: k, a: x[0], b: x[1] })).sort((p, q) => q.b - p.b);
    el.append(h("div", { class: "grid g2" },
      chartCard("Ülkelere göre ortalama yoğunluk: ETS öncesi ve ETS dönemi", "milyar € reel GSYİH başına yeşil patent başvurusu", [["cg", "1997–2004"], ["c1", "2005–2020"]],
        (hst) => Viz.dumbbell(hst, { rows: yo, clsA: "cg", clsB: "c1", nameA: "1997–2004", nameB: "2005–2020", xLabel: "yoğunluk" }),
        () => table(["Ülke", "1997–2004", "2005–2020", "Kat"], yo.map((r) => [r.label, tr(r.a, 3), tr(r.b, 3), "×" + tr(r.b / r.a, 1)]), { num: [1, 2, 3] }),
        "Yoğunluk 14 ülkenin hepsinde arttı. ETS <b>öncesinde</b> en yüksek değer Lüksemburg'da; tezdeki “en yüksek Danimarka, Almanya, Finlandiya, İsveç” sıralaması yalnız ETS dönemi için geçerli."),
      h("div", { class: "card" }, h("h3", null, "Veri denetimi"), h("div", { class: "sub" }, "Ham dosyadan yeniden hesaplanan kontroller"),
        table(["Kontrol", "Sonuç"], [
          ["Yapı", `${R.veri.satir} satır = ${R.veri.ulke} ülke × 31 yıl; tam dengeli`], ["Mükerrer ülke-yıl", R.veri.mukerrer === 0 ? h("span", { class: "ok" }, "yok ✓") : R.veri.mukerrer],
          ["Tahmin örnekleminde eksik değer", R.veri.eksik_tahmin_orneklemi === 0 ? h("span", { class: "ok" }, "yok ✓") : R.veri.eksik_tahmin_orneklemi],
          ["Büyüme oranı ↔ GSYİH düzeyi", `en büyük fark ${tr(R.veri.buyume_tutarlilik_max_fark, 2)} puan (yuvarlama) ✓`], ["Stok (Excel ↔ yeniden hesap)", "aynı (fark < 10⁻⁹) ✓"],
          ["Toplam başvuru (1997–2020)", tr(R.veri.toplam_ccm, 0) + " ✓"], ["Almanya / Fransa payı", `%${tr(R.veri.pay["Almanya"], 1)} / %${tr(R.veri.pay["Fransa"], 1)} ✓`],
          ["Medyan / çarpıklık", `${tr(R.veri.medyan, 1)} / ${tr(R.veri.carpiklik, 1)} ✓`], ["Yarım değerli (yukarı yuvarlanan) gözlem", R.veri.yuvarlama_yarim + " (sonuçları etkilemiyor)"],
          ["Kaynaklarla (OECD, Eurostat, WDI) karşılaştırma", h("span", { class: "warn" }, "yapılamadı (erişim yok)")]]))));
  }

  // ================================================================ YENİDEN ÜRETİM
  function replikasyon(el) {
    el.append(h("h1", null, "Yeniden üretim: tezdeki sayılar doğru mu?"), h("p", { class: "lede" }, `Evet. Karşılaştırılan ${IC.ozet.uyum[1]} değerin tamamı ham veriden, bağımsız yazılımla (kendi yazdığım Poisson ve negatif binom tahmincileri) birebir yeniden üretildi. Bootstrap standart hataları farklı rassal sayı üretecine rağmen tezdekilerden medyan %${tr(100 * IC.ozet.se_med, 0)}, en çok %${tr(100 * IC.ozet.se_fark, 0)} farklı.`));
    const box = h("div"); let tab = "m1";
    const dd = (a, b, tol) => (Math.abs(a - b) <= tol ? h("span", { class: "ok" }, "✓") : h("span", { class: "bad" }, "≠"));
    const T = {
      m1: () => { const t = R.tez.t511; return h("div", null, table(["Değişken", "Tahminci", "Katsayı (tez)", "Katsayı (hesap)", "", "SH (tez)", "SH (hesap)", "BC aralığı (tez)", "BC aralığı (hesap)"],
        Object.keys(t.nb).flatMap((k) => [N, P].map((f) => [AD[k], FAM[f], tr(t[f][k][0], 4), tr(C("m1", f, k).b, 4), dd(t[f][k][0], C("m1", f, k).b, 6e-5), tr(t[f][k][1], 4), tr(B("m1", f, k).se, 4), `[${tr(t[f][k][2], 4)}; ${tr(t[f][k][3], 4)}]`, `[${tr(B("m1", f, k).bc[0], 4)}; ${tr(B("m1", f, k).bc[1], 4)}]`])), { num: [2, 3, 5, 6, 7, 8] }),
        h("p", { class: "small", style: "margin-top:8px" }, `α = ${tr(R.m1.nb.alpha, 4)} [${tr(R.m1.nb.alpha_ci[0], 4)}; ${tr(R.m1.nb.alpha_ci[1], 4)}] (tez 0,0178 [0,0137; 0,0230]) · LR = ${tr(R.m1.LR, 2)} (tez 669,77) · Wald δ₁=δ₂: ${tr(R.m1.nb.boot.wald["d1=d2"].chi2, 2)} / ${tr(R.m1.poisson.boot.wald["d1=d2"].chi2, 2)} (tez 4,33 / 6,23) · δ₂=δ₃: ${tr(R.m1.nb.boot.wald["d2=d3"].chi2, 2)} / ${tr(R.m1.poisson.boot.wald["d2=d3"].chi2, 2)} (tez 15,34 / 32,21)`)); },
      m2: () => { const t = R.tez.t513; return h("div", null, table(["Değişken", "Tahminci", "Katsayı (tez)", "Katsayı (hesap)", "", "SH (tez)", "SH (hesap)", "BC aralığı (tez)", "BC aralığı (hesap)"],
        Object.keys(t.nb).flatMap((k) => [N, P].map((f) => [AD2[k], FAM[f], tr(t[f][k][0], 4), tr(C("m2", f, k).b, 4), dd(t[f][k][0], C("m2", f, k).b, 6e-5), tr(t[f][k][1], 4), tr(B("m2", f, k).se, 4), t[f][k][2] == null ? "(tezde boş)" : `[${tr(t[f][k][2], 4)}; ${tr(t[f][k][3], 4)}]`, `[${tr(B("m2", f, k).bc[0], 4)}; ${tr(B("m2", f, k).bc[1], 4)}]`])), { num: [2, 3, 5, 6, 7, 8] }),
        h("p", { class: "small", style: "margin-top:8px" }, `α = ${tr(R.m2.nb.alpha, 4)} · LR = ${tr(R.m2.LR, 2)} (tez 0,0161; 564,59) · Ortak testler NB: ${R.m2.nb.boot.joint.map((x) => tr(x.chi2, 2)).join(" / ")} (tez 12,27 / 21,02 / 0,73) · Poisson: ${R.m2.poisson.boot.joint.map((x) => tr(x.chi2, 2)).join(" / ")} (tez 15,39 / 28,23 / 2,22)`)); },
      sag: () => { const nm = { a: "(a) Stok hariç", b: "(b) GSYİH esnekliği serbest", c: "(c) Almanya hariç" }; return h("div", null, table(["Tanım", "Tahminci", "Faz", "Katsayı (tez)", "Katsayı (hesap)", "", "SH (tez)", "SH (hesap)", "p (bootstrap)"],
        Object.keys(nm).flatMap((s) => [N, P].flatMap((f) => ["F1", "F2", "F3"].map((k, j) => { const o = R.saglamlik[s][f]; return [nm[s], FAM[f], AD[k], tr(o.tez[j][0], 4), tr(o[k].b, 4), dd(o.tez[j][0], o[k].b, 6e-5), tr(o.tez[j][1], 4), tr(o[k].se_boot, 4), pcell(o[k].p_boot)]; }))), { num: [3, 4, 6, 7], tall: true }),
        h("p", { class: "small", style: "margin-top:8px" }, `GSYİH esnekliği: ${tr(R.saglamlik.b.nb.lngdp.b, 3)} (NB), ${tr(R.saglamlik.b.poisson.lngdp.b, 3)} (Poisson); H₀: esneklik = 1 testi χ² = ${tr(R.saglamlik.b.nb.elast_test_boot.chi2, 2)} / ${tr(R.saglamlik.b.poisson.elast_test_boot.chi2, 2)} (tez 10,78 / 15,92). AIC: NB ${tr(R.saglamlik.b.nb.aic.sabit, 1)} → ${tr(R.saglamlik.b.nb.aic.serbest, 1)}; Poisson ${tr(R.saglamlik.b.poisson.aic.sabit, 1)} → ${tr(R.saglamlik.b.poisson.aic.serbest, 1)} (serbest esneklik daha iyi uyuyor).`)); },
      loo: () => table(["Dışlanan ülke", "Faz 1 (tez)", "Faz 1 (hesap)", "p (tez)", "p (hesap)", "Faz 2 (tez)", "Faz 2 (hesap)", "p (hesap)", "Faz 3 (tez)", "Faz 3 (hesap)", "p (hesap)"],
        Object.entries(R.loo).map(([c, o]) => [c, tr(o.tez[0], 4), tr(o.hesap[0][0], 4), tr(o.tez[1], 3), pcell(o.hesap[0][1]), tr(o.tez[2], 4), tr(o.hesap[1][0], 4), pcell(o.hesap[1][1]), tr(o.tez[4], 4), tr(o.hesap[2][0], 4), pcell(o.hesap[2][1])]), { num: [1, 2, 3, 5, 6, 8, 9], tall: true }),
      tan: () => { const lab = { ccm: "Yeşil patent başvurusu", gdp_bn: "Reel GSYİH (milyar €)", inten: "Yeşil patent yoğunluğu", lnK1: "ln(1+K₍t−1₎)", gdp_growth_l1: "GSYİH büyümesi (t−1)", renew_wdi_l1: "Yenilenebilir payı (t−1)", impdep_l1: "Enerji ithalat bağ. (t−1)", manuf_l1: "İmalat payı (t−1)", trade_l1: "Ticaret açıklığı (t−1)" };
        return h("div", null, h("h4", null, "Tablo 5.2"), table(["Değişken", "Ortalama (tez)", "Ortalama (hesap)", "Std. sapma (tez)", "Std. sapma (hesap)", "En küçük", "En büyük", ""], Object.entries(R.tanim.t52).map(([k, o]) => [lab[k], tr(o.tez[0], 3), tr(o.hesap[0], 3), tr(o.tez[1], 3), tr(o.hesap[1], 3), tr(o.hesap[2], 3), tr(o.hesap[3], 3), o.uyum ? h("span", { class: "ok" }, "✓") : h("span", { class: "bad" }, "≠")]), { num: [1, 2, 3, 4, 5, 6] }),
          h("h4", { style: "margin-top:16px" }, "Tablo 5.4: korelasyonlar — tezdeki ham değerler ve model için ilgili olan ülke-içi değerler"),
          table(["Çift", "Tez", "Ham (hesap)", "Ülke-içi (hesap)"], R.tanim.t54.map((x) => [AD[x.a] + " – " + AD[x.b], tr(x.tez, 2), tr(x.ham, 2), Math.abs(x.ici) > 0.5 ? h("b", { class: "warn" }, tr(x.ici, 2)) : tr(x.ici, 2)]), { num: [1, 2, 3] }),
          h("h4", { style: "margin-top:16px" }, "Tablo 5.6: VIF (ülke-içi) ve tezde raporlanmayan Model 2 VIF değerleri"),
          table(["Değişken", "Model 1 (tez)", "Model 1 (hesap)", "Model 2 (hesap)"], Object.keys(EKD.vif_m2).map((k) => [AD2[k], R.tanim.vif[k] ? tr(R.tanim.vif[k].tez, 2) : "–", R.tanim.vif[k] ? tr(R.tanim.vif[k].hesap, 2) : "–", EKD.vif_m2[k] > 10 ? h("b", { class: "warn" }, tr(EKD.vif_m2[k], 1)) : tr(EKD.vif_m2[k], 1)]), { num: [1, 2, 3] })); },
      kok: () => h("div", null, table(["Değişken", "Fisher-ADF (tez)", "Fisher-ADF (hesap)", "IPS (tez)", "IPS (hesap)", "CD (tez)", "CD (hesap)", "CIPS (tez)", "CIPS (hesap)", "CIPS p (benzetim)"],
        Object.values(UR).map((o) => [o.etiket, o.tez57 ? tr(o.tez57[0][0], 2) : "–", tr(o.fisher_c[0], 2), o.tez57 ? tr(o.tez57[2][0], 2) : "–", tr(o.ips_c[0], 2), o.tez59 ? tr(o.tez59[0], 3) : "–", tr(o.cd[0], 3), o.tez59 ? tr(o.tez59[1], 3) : "–", tr(o.cips_c.stat, 3), pcell(o.cips_c.p_sim)]), { num: [1, 2, 3, 4, 5, 6, 7, 8] }),
        h("div", { class: "takeaway", html: "Tezdeki “Yeşil Patent Yoğunluğu” satırı aslında <b>yoğunluğun logaritmasıyla</b> hesaplanmış: logaritmayla bütün istatistikler birebir çıkıyor; düzeyle (ikinci satır) farklı ve CIPS birim kökü reddedemiyor. Düzey (sabitli) tanım gösterilmiştir. Kao'nun düzeltilmemiş iki istatistiği de logaritma ve 1997–2020 dönemiyle birebir: " + tr(EKD.kao.hesap["1997-2020 | lninten"].DF_rho, 3) + " ve " + tr(EKD.kao.hesap["1997-2020 | lninten"].DF_t, 3) + " (tez −18,260 ve −11,434)." })),
      pls: () => h("div", null, table(["Sahte kırılma yılı", "Tezde", "Poisson χ²(2) (hesap)", "p (küme)", "p (bootstrap)", "NB χ²(2) (hesap)", "p (küme)", "p (bootstrap)"],
        Object.entries(EKD.plasebo).map(([t, o]) => [t, R.plasebo[t].poisson.tez ? `${tr(R.plasebo[t].poisson.tez[0], 2)} / ${tr(R.plasebo[t].nb.tez[0], 2)}` : h("span", { class: "warn" }, "raporlanmamış"), tr(o.poisson.chi2_kume, 2), pcell(o.poisson.p_kume), pcell(o.poisson.p_boot), tr(o.nb.chi2_kume, 2), pcell(o.nb.p_kume), pcell(o.nb.p_boot)]), { num: [2, 5] }),
        h("div", { class: "takeaway", html: "Tezdeki üç yılın dört χ² değeri birebir. Raporlanmayan <b>2003</b> kırılması tezin kendi yöntemiyle (ülke-kümeli SH) reddediyor; bootstrap kovaryansıyla hiçbir yıl reddetmiyor." })),
    };
    const tabs = [["m1", "Model 1 (Tablo 5.11)"], ["m2", "Model 2 (Tablo 5.13)"], ["sag", "Sağlamlık (5.14)"], ["loo", "Ülke dışlama (5.15)"], ["tan", "Tanımlayıcı, VIF (5.2–5.6)"], ["kok", "Birim kök (5.7–5.10)"], ["pls", "Plasebo (5.16)"]];
    el.append(h("div", { class: "filters" }, seg(tabs, tab, (x) => { tab = x; box.replaceChildren(T[x]()); })));
    el.append(h("div", { class: "card" }, box)); box.append(T.m1());
  }

  // ================================================================ MODELLER
  function modeller(el) {
    el.append(h("h1", null, "Modeller"), h("p", { class: "lede" }, "Tezin iki modeli ve yıl etkileri. Güven aralığı yöntemini değiştirerek sonuçların çıkarsama tercihine ne kadar bağlı olduğunu görebilirsiniz."));
    let ci = "pct";
    const CI = { pct: "%95 yüzdelik bootstrap", bc: "%95 BC bootstrap (tezin yöntemi)", cl: "ülke-küme SH × t(13)", cv3: "küme jackknife SH × t(13)", w2: "iki yönlü küme SH × 1,96" };
    const iv = (m, f, k) => { const c = C(m, f, k), b = B(m, f, k); if (ci === "pct") return b.pct; if (ci === "bc") return b.bc; if (ci === "cl") return [c.b - T13 * c.se_cl, c.b + T13 * c.se_cl]; if (ci === "cv3") return [c.b - T13 * c.se_cv3, c.b + T13 * c.se_cv3]; return [c.b - 1.96 * c.se_2w, c.b + 1.96 * c.se_2w]; };
    const cards = [];
    const mk = (m, keys, labs, ad, title, sub, note) => chartCard(title, sub, [["c1", FAM[P]], ["c2", FAM[N]]],
      (host) => Viz.dotci(host, { cats: keys, catLabels: labs, pct: true, height: 330, yLabel: "katsayı (log puan)", ciLabel: CI[ci], series: [P, N].map((f, j) => ({ name: FAM[f], cls: "c" + (j + 1), pts: keys.map((k) => ({ b: C(m, f, k).b, lo: iv(m, f, k)[0], hi: iv(m, f, k)[1] })) })) }),
      () => table(["Katsayı", "Tahminci", "b", "≈ %", CI[ci]], keys.flatMap((k) => [P, N].map((f) => [ad[k], FAM[f], tr(C(m, f, k).b, 4), pctEff(C(m, f, k).b), `[${tr(iv(m, f, k)[0], 3)}; ${tr(iv(m, f, k)[1], 3)}]`])), { num: [2, 3, 4] }), note);
    el.append(h("div", { class: "filters" }, h("label", null, "Güven aralığı yöntemi", sel(Object.entries(CI), ci, (x) => { ci = x; cards.forEach((c) => c.redraw()); }))));
    cards.push(mk("m1", ["F1", "F2", "F3", "lnK1"], ["Faz 1", "Faz 2", "Faz 3", "Stok"], AD, "Model 1: faz kuklaları", "ETS öncesine göre ortalama log fark; stok katsayısı esnekliktir",
      `Poisson gözlemleri patent sayısıyla ağırlıklandırır: Almanya'nın payı <b>%${tr(R.agirlik["Almanya"][0], 0)}</b>; negatif binomda <b>%${tr(R.agirlik["Almanya"][1], 0)}</b>. İki tahminci arasındaki fark bundan kaynaklanıyor: Almanya çıkarılınca Poisson Faz 1 katsayısı ${tr(R.saglamlik.c.poisson.F1.b, 3)}'e çıkıp negatif binomun değerine (${tr(C("m1", N, "F1").b, 3)}) eşitleniyor.`));
    cards.push(mk("m2", ["tstar", "F1", "S1", "F2", "S2", "F3", "S3"], ["ETS öncesi\neğilim", "Faz 1\ndüzey", "Faz 1\neğim", "Faz 2\ndüzey", "Faz 2\neğim", "Faz 3\ndüzey", "Faz 3\neğim"], AD2, "Model 2: segmentli kesintili zaman serisi", "Her fazın düzey ve eğim sapması, ETS öncesi doğrusal eğilime göre",
      `İki bulgu her çıkarsama yönteminde ayakta: <b>Faz 1 eğimi</b> ve <b>Faz 2 düzeyi</b>. Ancak “ETS öncesi eğilim ≈ 0” sonucu stokun eğilimi emmesinden kaynaklanıyor: Model 2'de eğilimin ülke-içi VIF değeri <b>${tr(EKD.vif_m2.tstar, 1)}</b>, stok–zaman korelasyonu <b>${tr(EKD.ici_kor["lnK1~zaman"], 2)}</b>.`));
    cards.forEach((c) => el.append(c));

    // stoklu / stoksuz model 2
    const ks = ["tstar", "F1", "S1", "F2", "S2", "F3", "S3"];
    el.append(chartCard("Model 2: stoklu ve stoksuz (negatif binom)", "Tezde yalnız stoklu tanım var; stok çıkarıldığında ETS öncesi eğilim ortaya çıkıyor. Çubuklar ülke-küme SH × t(13)", [["c1", "Stoklu (tezdeki)"], ["c3", "Stoksuz"]],
      (host) => Viz.dotci(host, { cats: ks, catLabels: ["ETS öncesi\neğilim", "Faz 1\ndüzey", "Faz 1\neğim", "Faz 2\ndüzey", "Faz 2\neğim", "Faz 3\ndüzey", "Faz 3\neğim"], height: 330, yLabel: "katsayı (log puan)", ciLabel: "ülke-küme × t(13)",
        series: [{ name: "Stoklu", cls: "c1", pts: ks.map((k) => ({ b: C("m2", N, k).b, lo: C("m2", N, k).b - T13 * C("m2", N, k).se_cl, hi: C("m2", N, k).b + T13 * C("m2", N, k).se_cl })) },
          { name: "Stoksuz", cls: "c3", pts: ks.map((k) => { const o = R.ek.m2_stoksuz.nb[k]; return { b: o.b, lo: o.b - T13 * o.se, hi: o.b + T13 * o.se }; }) }] }),
      () => table(["Katsayı", "Stoklu b", "p", "Stoksuz b", "p", "Stoksuz Poisson b", "p (bootstrap)"], ks.map((k) => [AD2[k], tr(C("m2", N, k).b, 4), pcell(C("m2", N, k).p_cl_t), tr(R.ek.m2_stoksuz.nb[k].b, 4), pcell(R.ek.m2_stoksuz.nb[k].p_t), tr(R.ek.m2_stoksuz.poisson[k].b, 4), pcell(R.ek.m2_stoksuz_boot.poisson[k].p)]), { num: [1, 3, 5] }),
      `Stoksuz tanımda ETS öncesi eğilim yılda <b>${tr(R.ek.m2_stoksuz.nb.tstar.b, 3)}</b> (≈ %${pctEff(R.ek.m2_stoksuz.nb.tstar.b)}) ve anlamlı. İyi haber: Faz 1 eğimi ve Faz 2 düzeyi stoksuz tanımda da anlamlı kalıyor. Stoksuz Poisson'da Faz 3 eğimi negatif (${tr(R.ek.m2_stoksuz.poisson.S3.b, 3)}).`));

    // yıl etkileri
    let ym = "cl";
    const yrs = Object.keys(EKD.yil_boot).map(Number);
    const yc = chartCard("Yıl etkileri (Poisson, referans 2004)", "Stok ve kontroller sabitken her yılın 2004'e göre log farkı", [["c1", "Stoklu (tezdeki Şekil 5.5)"], ["c3", "Stoksuz"]],
      (host) => Viz.dotci(host, { cats: yrs.concat([2004]).sort(), numericX: true, bands: Viz.PHASES, height: 360, yLabel: "katsayı (log puan)", ciLabel: ym === "boot" ? "%95 yüzdelik bootstrap" : "ülke-küme SH × 1,96 (tezin yöntemi)", xLabel: "yıl",
        series: [{ name: "Stoklu", cls: "c1", pts: yrs.concat([2004]).sort().map((y) => { if (y === 2004) return { b: 0, hollow: true, note: "referans yıl" }; const o = EKD.yil_boot[y]; return { b: o.b, lo: ym === "boot" ? o.pct[0] : o.b - 1.96 * o.se_cl, hi: ym === "boot" ? o.pct[1] : o.b + 1.96 * o.se_cl, note: "p (küme) " + pv(o.p_cl) + " · p (bootstrap SH) " + pv(o.p_boot) }; }) },
          { name: "Stoksuz", cls: "c3", pts: yrs.concat([2004]).sort().map((y) => { if (y === 2004) return null; const o = R.yil.poisson_stoksuz.yil[y]; return ym === "boot" ? { b: o[0], note: "stoksuz seri için bootstrap aralığı hesaplanmadı" } : { b: o[0], lo: o[0] - 1.96 * o[1], hi: o[0] + 1.96 * o[1] }; }) }] }),
      () => table(["Yıl", "Stoklu b", "p (küme)", "p (bootstrap SH)", "%95 yüzdelik", "Stoksuz b"], yrs.map((y) => { const o = EKD.yil_boot[y]; return [y, tr(o.b, 3), pcell(o.p_cl), pcell(o.p_boot), `[${tr(o.pct[0], 3)}; ${tr(o.pct[1], 3)}]`, tr(R.yil.poisson_stoksuz.yil[y][0], 3)]; }), { num: [1, 4, 5], tall: true }),
      `Etki <b>2009'da zirve</b> yapıp 2012'de sıfıra iniyor; tezdeki “Faz 2 boyunca korunuyor” yorumuyla çelişiyor. Bootstrap standart hatasıyla %5 düzeyini yalnız 2009 geçiyor. Stoksuz seride ETS öncesi yıllar belirgin biçimde yükseliyor (1997: ${tr(R.yil.poisson_stoksuz.yil["1997"][0], 2)}): eğilim ETS'den önce de vardı.`);
    el.append(h("div", { class: "filters" }, h("label", null, "Yıl etkileri grafiğinde güven aralığı", seg([["cl", "Ülke-küme SH (tezin yöntemi)"], ["boot", "Yüzdelik bootstrap (yalnız stoklu seri)"]], ym, (x) => { ym = x; yc.redraw(); }))));
    el.append(yc);
  }

  // ================================================================ ÇIKARSAMA
  function cikarsama(el) {
    el.append(h("h1", null, "Çıkarsama duyarlılığı"), h("p", { class: "lede" }, "Tez tek bir yöntem raporluyor: ülke bazlı eşli bootstrap standart hatası ve normal dağılım kritik değeri. 14 küme, bir ülkenin %45 ağırlığı ve ülkeler arası bağımlılık varken sonuçların yönteme ne kadar bağlı olduğu ve hangi yöntemin bu veride güvenilir olduğu aşağıda."));
    let m = "m1";
    const box = h("div");
    const mat = () => { const keys = m === "m1" ? ["F1", "F2", "F3", "lnK1", "trade_l1"] : ["tstar", "F1", "S1", "F2", "S2", "F3", "S3"], ad = m === "m1" ? AD : AD2;
      const pt13 = (b, se) => { const t = Math.abs(b / se); return tdist2(t, 13); };
      return table(["Katsayı", "Tahminci", "b", "Ülke-küme t(13)", "İki yönlü küme", "Küme jackknife (CV3)", "Bootstrap z (tez)", "Bootstrap t(13)", "Bootstrap-t (yüzdelik-t)"],
        keys.flatMap((k) => [N, P].map((f) => { const c = C(m, f, k), b = B(m, f, k); return [ad[k], FAM[f], tr(c.b, 4), pcell(c.p_cl_t), pcell(c.p_2w), pcell(c.p_cv3), pcell(b.p), pcell(pt13(c.b, b.se)), f === P ? pcell(b.p_pt) : h("td", { class: "pcell" }, "–")]; })), { num: [2] }); };
    function tdist2(t, df) { // iki kuyruklu t olasılığı (sayısal integral)
      const f = (x) => Math.pow(1 + (x * x) / df, -(df + 1) / 2); let s = 0; const n = 4000, hi = 60, st = (hi - t) / n; if (t >= hi) return 0;
      for (let i = 0; i <= n; i++) s += f(t + i * st) * (i === 0 || i === n ? 1 : i % 2 ? 4 : 2);
      const g = (z) => { let x = z, r = 1; while (x < 8) { r *= x; x += 1; } return Math.exp((x - 0.5) * Math.log(x) - x + 0.5 * Math.log(2 * Math.PI) + 1 / (12 * x)) / r; };
      const cst = g((df + 1) / 2) / (Math.sqrt(df * Math.PI) * g(df / 2)); return Math.min(1, 2 * cst * (s * st) / 3);
    }
    el.append(h("div", { class: "filters" }, seg([["m1", "Model 1"], ["m2", "Model 2"]], m, (x) => { m = x; box.replaceChildren(mat()); }), h("span", { class: "small" }, "Hücreler p değeridir: ", h("span", { class: "pp p5", style: "padding:1px 7px;border-radius:6px" }, "< 0,05"), " ", h("span", { class: "pp p10", style: "padding:1px 7px;border-radius:6px" }, "< 0,10"), " ", h("span", { class: "pp pn", style: "padding:1px 7px;border-radius:6px" }, "≥ 0,10"))));
    el.append(h("div", { class: "card" }, h("h3", null, "Aynı katsayı, altı farklı çıkarsama"), h("div", { class: "sub" }, "Ülke-küme ve iki yönlü kovaryanslar Stata'nın en çok olabilirlik kuralıyla; jackknife bir ülke dışarıda bırakılarak"), box,
      h("div", { class: "takeaway", html: `<b>Faz 2</b> ve Model 2'nin iki ana katsayısı (Faz 1 eğimi, Faz 2 düzeyi) negatif binomda her yöntemde anlamlı. <b>Faz 1</b> Poisson'da jackknife ile ${pv(C("m1", P, "F1").p_cv3)}. Aşağıdaki benzetim, bu sütunlardan hangisine güvenilebileceğini gösteriyor: nominal düzeye en yakın yöntem <b>küme jackknife</b>; <b>iki yönlü kümeleme en kötüsü</b> (o sütun yalnız şeffaflık için duruyor).` })));
    box.append(mat());

    // bootstrap histogram
    let hk = "F1", hf = P;
    const hcard = chartCard("Bootstrap dağılımı ve güven aralıkları", "", null,
      (host) => { const d = BOOT[hf][hk], b = B("m1", hf, hk); const s = [...d].sort((a, c) => a - c), lo = s[Math.floor(0.005 * s.length)], hi = s[Math.ceil(0.995 * s.length) - 1];
        Viz.hist(host, { groups: [{ name: "bootstrap tekrarı", cls: "c1", values: d.filter((x) => x >= lo && x <= hi) }], min: lo, max: hi, bins: 46, height: 300, xLabel: AD[hk] + " katsayısı — " + FAM[hf] + " (uçlardaki %1 gösterilmiyor)", yLabel: "tekrar",
          markers: [{ x: b.b, label: "nokta tahmin " + tr(b.b, 3) }, { x: b.mean, label: "bootstrap ort. " + tr(b.mean, 3), left: b.mean < b.b }] }); },
      () => { const b = B("m1", hf, hk); return table(["", "Değer"], [["Nokta tahmin", tr(b.b, 4)], ["Bootstrap ortalaması", tr(b.mean, 4)], ["Bootstrap medyanı", tr(b.median, 4)], ["Standart hata", tr(b.se, 4)], ["Çarpıklık", tr(b.skew, 2)], ["Medyan sapması z₀", tr(b.z0, 2)], ["%95 yüzdelik", `[${tr(b.pct[0], 4)}; ${tr(b.pct[1], 4)}]`], ["%95 BC (tez)", `[${tr(b.bc[0], 4)}; ${tr(b.bc[1], 4)}]`], ...(b.pt ? [["%95 bootstrap-t", `[${tr(b.pt[0], 4)}; ${tr(b.pt[1], 4)}]`]] : []), ["Almanya'sız tekrarların ortalaması", tr(b.mean_noDE, 4)], ["Almanya'lı tekrarların ortalaması", tr(b.mean_DE, 4)]], { num: [1] }); });
    const info = h("div", { class: "takeaway" });
    const upd = () => { const b = B("m1", hf, hk); info.innerHTML = `Nokta tahmin <b>${tr(b.b, 4)}</b>, bootstrap ortalaması <b>${tr(b.mean, 4)}</b>, z₀ = <b>${tr(b.z0, 2)}</b>. Üç aralık — yüzdelik [${tr(b.pct[0], 3)}; ${tr(b.pct[1], 3)}], BC [${tr(b.bc[0], 3)}; ${tr(b.bc[1], 3)}]${b.pt ? `, bootstrap-t [${tr(b.pt[0], 3)}; ${tr(b.pt[1], 3)}]` : ""}. Tekrarların %${tr(100 * R.m1[hf].boot.share_noDE, 0)}'inde Almanya örneklemde yok; o tekrarların ortalaması ${tr(b.mean_noDE, 3)}, Almanya'lı olanların ${tr(b.mean_DE, 3)}. z₀ sıfırdan uzaklaştıkça BC aralığı yüzdelik aralıktan kopuyor.`; hcard.redraw(); };
    hcard.append(info);
    el.append(h("h2", null, "Bootstrap dağılımları neden sorunlu?"), h("div", { class: "filters" }, h("label", null, "Katsayı", sel(Object.keys(BOOT[P]).map((k) => [k, AD[k]]), hk, (x) => { hk = x; upd(); })), h("label", null, "Tahminci", seg([[P, FAM[P]], [N, FAM[N]]], hf, (x) => { hf = x; upd(); }))), hcard); upd();

    // Monte Carlo
    el.append(h("h2", null, "Monte Carlo: gerçek etki sıfır olsaydı ne bulunurdu?"));
    const SA = { A: "A — tezin kendi modeli doğru", B: "B — A + küçük ortak yıl şoku", C: "C — sabit etkisiz stok modeli doğru" };
    const ML = [["rej_cl", "Ülke-küme t(13)"], ["rej_2w", "İki yönlü küme"], ["rej_cv3", "Küme jackknife (CV3)"], ["rej_boot", "Eşli bootstrap SH, z (tezin yöntemi)"], ["rej_boot_t", "Eşli bootstrap SH, t(13)"]];
    const meter = (x) => h("td", { class: "num" }, h("span", { style: `display:inline-block;vertical-align:middle;margin-right:6px;height:8px;border-radius:4px;width:${Math.min(70, 70 * x / 0.6)}px;background:var(${x > 0.1 ? "--s2" : "--s1"})` }), "%" + tr(100 * x, 0));
    el.append(h("div", { class: "card" }, h("h3", null, "Tezin katsayıları “sıfır etki” dünyasında ne kadar nadir?"), h("div", { class: "sub" }, `Parametrik bootstrap: her senaryoda ${SIMP.A.n} yapay veri seti, gerçek faz etkisi sıfır. Hücre: boş hipotez altındaki ortalama tahmin (yanlılık) ve gözlenen değerin aşılma olasılığı (tek yönlü p).`),
      table(["Katsayı", "Tahminci", "Tezdeki değer", "A: tezin modeli", "A2: ülkeye özgü yayılım", "B: + ortak şok", "C: sabit etkisiz model"],
        SIMP.katsayilar.flatMap((nm, j) => [N, P].map((f) => [nm, FAM[f], tr(SIMP.gozlenen[f][j], 3), ...SEN.map((g) => h("td", { class: "pcell" }, tr(SIMP[g][f].ort[j], 3) + " ", h("span", { class: "pp " + pcls(SIMP[g][f].p_tek[j]) }, pv(SIMP[g][f].p_tek[j]))))])), { num: [2], tall: true }),
      h("div", { class: "takeaway", html: `Negatif binomda <b>Faz 2</b> (p = ${mcr(N, 1)}), Model 2 <b>Faz 2 düzeyi</b> (p = ${mcr(N, 5)}) ve <b>Faz 1 eğimi</b> (p = ${mcr(N, 4)}) dört senaryonun hepsinde nadir: tahminci yanlılığı ve örnekleme gürültüsüyle açıklanamıyor. <b>Faz 1</b> (Model 1) negatif binomda sınırda (${mcr(N, 0)}), Poisson'da sıfır etkiyle tamamen uyumlu (${mcr(P, 0)}). Model 1'in faz katsayıları boş hipotez altında pozitif ortalamaya sahip (yukarı yanlı); Model 2'ninkiler sıfıra çok yakın.` })));
    el.append(h("div", { class: "card" }, h("h3", null, "Yanlılık: gerçek etki 0 iken ortalama tahmin"), h("div", { class: "sub" }, `Çıkarsama boyutu deneyi: her senaryoda ${SIM.A.n} yapay veri seti, her birinde ${SIM.ayar.B} bootstrap tekrarı; stok, üretilen patentlerden yeniden kuruldu. Gerçek stok katsayısı ${tr(SIM.ayar.gamma_A, 2)} (A, B) ve ${tr(SIM.ayar.gamma_C, 2)} (C). Ortak şok std = ${tr(SIM.ayar.sigma_ortak_sok, 3)} log puan (ETS öncesi yıl etkilerinden kalibre).`),
      table(["Senaryo", "Tahminci", "Faz 1", "Faz 2", "Faz 3", "Stok katsayısı"], ["A", "B", "C"].flatMap((g) => [P, N].map((f) => [SA[g], FAM[f], ...SIM[g][f].ort_b.map((x) => tr(x, 3)), tr(SIM[g][f].ort_gamma, 2)])), { num: [2, 3, 4, 5] }),
      h("h3", { style: "margin-top:18px" }, "Boyut: gerçek etki 0 iken %5 düzeyinde “anlamlı” bulma oranı"), h("div", { class: "sub" }, "İdeal değer %5. Turuncu çubuk: %10'un üzerinde."),
      table(["Senaryo", "Tahminci", "Yöntem", "Faz 1", "Faz 2", "Faz 3"], ["A", "B", "C"].flatMap((g) => [P, N].flatMap((f) => ML.map(([k, lab]) => [SA[g].slice(0, 1), FAM[f], lab, ...SIM[g][f][k].map(meter)]))), { tall: true }),
      IC.ozet.sim_yorum ? h("div", { class: "takeaway md", html: marked.parse(IC.ozet.sim_yorum) }) : null));
  }

  // ================================================================ SAĞLAMLIK
  function saglamlik(el) {
    el.append(h("h1", null, "Sağlamlık"), h("p", { class: "lede" }, `${SPEC.length} alternatif tanım: tahminci × stok × eskime oranı × maruziyet × kontroller × örneklem × gecikme × eğilim. Süzgeçlerle hangi tercihin sonucu ne kadar değiştirdiğini görebilirsiniz.`));
    const F = { faz: 1, fam: "", stok: "", trend: "", expo: "", ctrl: "", smp: "", lag: "" };
    const host = h("div"), sum = h("div", { class: "takeaway" });
    const draw = () => { const j = F.faz;
      let pts = SPEC.filter((s) => (!F.fam || s.fam === F.fam) && (F.stok === "" || String(s.stok) === F.stok) && (F.trend === "" || String(s.trend) === F.trend) && (!F.expo || s.expo === F.expo) && (!F.ctrl || s.ctrl === F.ctrl) && (!F.smp || s.smp === F.smp) && (!F.lag || String(s.lag) === F.lag));
      pts = pts.map((s) => ({ b: s.b[j], lo: s.b[j] - T13 * s.se[j], hi: s.b[j] + T13 * s.se[j], cls: s.fam === P ? "c1" : "c2", sig: s.p[j] < 0.05, tipTitle: `${FAM[s.fam]} · ${s.smp}`, tipRows: [{ value: tr(s.b[j], 4), label: "katsayı (p = " + pv(s.p[j]) + ")" }, { value: s.stok ? "var (δ = " + tr(s.delta, 2) + ")" : "yok", label: "stok" }, { value: s.expo === "fixed" ? "sabit (1)" : "serbest", label: "GSYİH esnekliği" }, { value: s.ctrl, label: "kontroller" }, { value: String(s.lag), label: "gecikme" }, { value: s.trend ? "var" : "yok", label: "doğrusal eğilim" }] })).sort((a, b) => a.b - b.b);
      if (!pts.length) { host.replaceChildren(h("p", null, "Bu süzgeçle tanım yok.")); sum.textContent = ""; return; }
      const main_ = R.m1.nb.coef["F" + (j + 1)].b;
      Viz.spec(host, { pts, height: 380, yLabel: "Faz " + (j + 1) + " katsayısı (log puan)", xLabel: pts.length + " tanım, katsayıya göre sıralı; soluk nokta: %5 düzeyinde anlamsız", ref: main_, refLabel: "tezin ana modeli (NB) " + tr(main_, 3) });
      const pos = pts.filter((p) => p.b > 0 && p.sig).length, neg = pts.filter((p) => p.b < 0 && p.sig).length, med = pts[Math.floor(pts.length / 2)].b;
      sum.innerHTML = `Seçili <b>${pts.length}</b> tanımda Faz ${j + 1} katsayısının medyanı <b>${tr(med, 3)}</b>; aralık ${tr(pts[0].b, 3)} – ${tr(pts[pts.length - 1].b, 3)}. Pozitif ve %5'te anlamlı: <b>%${tr(100 * pos / pts.length, 1)}</b>; negatif ve anlamlı: %${tr(100 * neg / pts.length, 1)}. Anlamlılık ülke-kümeli SH ve t(küme−1) ile.`; };
    const S = (key, lab, opts) => h("label", null, lab, sel([["", "hepsi"]].concat(opts), "", (x) => { F[key] = x; draw(); }));
    el.append(h("div", { class: "filters" }, h("label", null, "Katsayı", seg([[0, "Faz 1"], [1, "Faz 2"], [2, "Faz 3"]], 1, (x) => { F.faz = x; draw(); })),
      S("fam", "Tahminci", [[P, FAM[P]], [N, FAM[N]]]), S("stok", "Stok", [["true", "var"], ["false", "yok"]]), S("trend", "Eğilim", [["true", "var"], ["false", "yok"]]), S("expo", "GSYİH esnekliği", [["fixed", "sabit"], ["free", "serbest"]]),
      S("ctrl", "Kontroller", [["tam", "tam"], ["yok", "yok"]]), S("smp", "Örneklem", [...new Set(SPEC.map((s) => s.smp))].map((x) => [x, x])), S("lag", "Gecikme", [["1", "1"], ["2", "2"]])));
    el.append(h("div", { class: "card" }, h("h3", null, "Spesifikasyon eğrisi"), h("div", { class: "sub" }, "Her nokta bir tanım; dikey çizgi ülke-küme SH × t aralığı"), legend([["c1", FAM[P]], ["c2", FAM[N]]]), host, sum,
      h("p", { class: "small", style: "margin:10px 0 0" }, "Uyarı: bu tanımların hepsi aynı önce–sonra tasarımını ve ülke sabit etkilerini paylaşıyor. Eğri, bulguların tanım seçimine dayanıklılığını gösterir; ortak şoklara ya da sabit etki/stok yapısına dayanıklılığını göstermez.")));
    F.faz = 1; redraws.push(() => { if (host.offsetParent !== null) draw(); }); requestAnimationFrame(draw);

    const cs = Object.keys(R.loo);
    el.append(chartCard("Ülkelerin tek tek dışlanması (Poisson)", "Her sütunda bir ülke dışarıda; çubuklar BC bootstrap aralığı (tezin yöntemi)", [["c1", "Faz 1"], ["c2", "Faz 2"], ["c3", "Faz 3"]],
      (hst) => Viz.dotci(hst, { cats: cs, catLabels: cs.map((c) => c.length > 7 ? c.slice(0, 6) + "." : c), height: 340, yLabel: "katsayı (log puan)", ciLabel: "%95 BC bootstrap", series: [0, 1, 2].map((j) => ({ name: "Faz " + (j + 1), cls: "c" + (j + 1), pts: cs.map((c) => ({ b: R.loo[c].hesap[j][0], lo: R.loo[c].hesap[j][2][0], hi: R.loo[c].hesap[j][2][1], note: "p = " + pv(R.loo[c].hesap[j][1]) })) })) }),
      () => table(["Dışlanan", "Faz 1", "p", "Faz 2", "p", "Faz 3", "p", "NB Faz 1", "NB Faz 2", "NB Faz 3"], cs.map((c) => { const o = R.loo[c]; return [c, tr(o.hesap[0][0], 3), pcell(o.hesap[0][1]), tr(o.hesap[1][0], 3), pcell(o.hesap[1][1]), tr(o.hesap[2][0], 3), pcell(o.hesap[2][1]), ...o.nb.map((x) => tr(x, 3))]; }), { num: [1, 3, 5, 7, 8, 9], tall: true }),
      `Faz 2 her dışlamada anlamlı. Faz 1, 14 tahminin yalnız <b>${cs.filter((c) => R.loo[c].hesap[0][1] < 0.05).length}</b>'sinde %5 düzeyinde anlamlı. <b>Danimarka</b> ya da <b>Almanya</b> çıkarılınca Faz 2 katsayısı ≈0,07 büyüyor ve Faz 3'ün işareti pozitife dönüyor; “bulgular hiçbir ülkeye bağlı değil” ifadesi Faz 2 için doğru, Faz 1 ve 3 için değil.`));

    const ET = [["m1_trend", "Ana model + doğrusal eğilim"], ["m1_trend2", "Ana model + karesel eğilim"], ["m1_trend_stoksuz", "Stoksuz + doğrusal eğilim"], ["kontrolsuz", "Yalnız stok (kontrolsüz)"], ["yalniz_faz", "Yalnız faz kuklaları (stok ve kontrol yok)"], ["beklenti", "2003–2004 beklenti kuklası eklenmiş"], ["2020_haric", "2020 hariç"], ["2018_2020_haric", "2018–2020 hariç"], ["irlanda_haric", "İrlanda hariç"], ["luksemburg_haric", "Lüksemburg hariç"], ["DE_FR_haric", "Almanya ve Fransa hariç"], ["delta_0.05", "Eskime oranı 0,05"], ["delta_0.1", "Eskime oranı 0,10"], ["delta_0.2", "Eskime oranı 0,20"], ["delta_0.25", "Eskime oranı 0,25"], ["presample", "Sabit etki yerine ön-örneklem ortalaması"]];
    const cell = (o) => h("td", { class: "pcell" }, tr(o.b, 3) + " ", h("span", { class: "pp " + pcls(o.p_t) }, pv(o.p_t)));
    el.append(h("div", { class: "card" }, h("h3", null, "Seçilmiş ek tahminler"), h("div", { class: "sub" }, "Faz katsayısı ve ülke-kümeli t(13) p değeri"),
      table(["Tanım", "Tahminci", "Faz 1", "Faz 2", "Faz 3"], [["Tezin ana modeli", N], ["Tezin ana modeli", P]].map(([t, f]) => [h("b", null, t), FAM[f], ...["F1", "F2", "F3"].map((k) => cell({ b: C("m1", f, k).b, p_t: C("m1", f, k).p_cl_t }))]).concat(ET.flatMap(([k, t]) => [N, P].map((f) => [t, FAM[f], ...["F1", "F2", "F3"].map((x) => cell(R.ek[k][f][x]))]))), { tall: true }),
      h("div", { class: "takeaway", html: `İki tanım sonucu belirgin biçimde değiştiriyor: <b>beklenti kuklası</b> (Poisson Faz 1 → ${tr(R.ek.beklenti.poisson.F1.b, 3)}, anlamsız) ve <b>ön-örneklem ortalaması</b> (Faz 1 ve 2 ≈ 0; stok katsayısı ${tr(R.ek.presample.nb.lnK1.b, 2)}). Diğerleri bulguları koruyor ya da güçlendiriyor. Ön-örneklem tanımı ile sabit etkili tanım arasındaki fark, benzetimlerde görülen yanlılıkla (stok katsayısının aşağı, faz katsayılarının yukarı kayması) aynı yöne işaret ediyor.` })));

    const hs = Object.entries(R.ek.heterojen);
    el.append(h("div", { class: "grid g2" },
      h("div", { class: "card" }, h("h3", null, "Faz 2'nin içi: 2008–2009 ve 2010–2012"), h("div", { class: "sub" }, "Faz 2 kuklası ikiye bölündüğünde"),
        table(["Dönem", "Poisson", "NB"], [["Faz 1 (2005–2007)", "F1"], ["2008–2009", "F2a"], ["2010–2012", "F2b"], ["Faz 3 (2013–2020)", "F3"]].map(([t, k]) => [t, cell(R.ek.faz2_bolunmus.poisson[k]), cell(R.ek.faz2_bolunmus.nb[k])])),
        h("div", { class: "takeaway", html: "Fark 2008–2009'da yoğunlaşıyor; 2010–2012'de küçülüp anlamsızlaşıyor. 2009/29/AT Direktifi Nisan 2009'da kabul edildi: “kurumsal kesinlik” açıklaması zamanlamayla uyuşmuyor." })),
      h("div", { class: "card" }, h("h3", null, "Ülke heterojenliği (Poisson, ülke × faz)"), h("div", { class: "sub" }, "Ortak stok ve kontrol katsayılarıyla; tek ülkelik katsayılar gürültülüdür, yalnız nokta tahmin"),
        table(["Ülke", "Faz 1", "Faz 2", "Faz 3", "Poisson ağırlığı"], hs.map(([c, v]) => [c, ...v.map((x) => tr(x, 2)), "%" + tr(R.agirlik[c][0], 1)]), { num: [1, 2, 3, 4], tall: true }))));
  }

  // ================================================================ BULGULAR
  function bulgular(el) {
    el.append(h("h1", null, "Bulgular"), h("p", { class: "lede" }, "Beş kaynaktan gelen bütün tespitler tek listede: ilk inceleme, iki jüri raporu, bağımsız hakem okuması ve bu yeniden inceleme. Her biri veriyle yeniden sınandı; sayılar hesap çıktılarından otomatik çekiliyor. Her bulgunun altında tezde neyin, nasıl değişeceğini söyleyen adım adım düzeltme listesi ve uygun yerlerde teze yazılabilecek örnek metin var. Tamamı tek belge olarak: ", h("a", { href: "#belgeler" }, "Belgeler"), " sayfasında “Sade anlatım ve adım adım düzeltme rehberi”."));
    const st = { onem: new Set(), kat: "", kay: "", q: "" };
    const list = h("div"), cnt = h("span", { class: "small" });
    el.append(anlatimBar(), h("details", { class: "sozluk" }, h("summary", null, "Terimler sözlüğü (" + IC.sozluk.length + " terim)"), h("dl", null, IC.sozluk.flatMap(([a, t]) => [h("dt", null, a), h("dd", null, t)]))));
    const kats = [...new Set(IC.bulgular.map((b) => b.kat))], kays = [...new Set(IC.bulgular.flatMap((b) => b.kaynak))];
    const draw = () => { const q = st.q.toLocaleLowerCase("tr");
      const fs = IC.bulgular.filter((b) => (!st.onem.size || st.onem.has(b.onem)) && (!st.kat || b.kat === st.kat) && (!st.kay || b.kaynak.includes(st.kay)) && (!q || (b.baslik + b.tespit + b.kanit + b.oneri + b.id + b.sade.baslik + b.sade.sorun + b.sade.neden + b.sade.adimlar.join(" ") + (b.sade.ornek || "")).toLocaleLowerCase("tr").includes(q)));
      cnt.textContent = fs.length + " / " + IC.bulgular.length + " bulgu";
      list.replaceChildren(...fs.map((b) => findingEl(b)));
      if (!fs.length) list.append(h("p", null, "Bu süzgeçle bulgu yok.")); };
    el.append(h("div", { class: "filters" }, h("label", null, "Önem", h("div", { class: "row" }, ["kritik", "önemli", "orta", "küçük"].map((o) => h("label", { class: "chk" }, h("input", { type: "checkbox", onchange: (e) => { e.target.checked ? st.onem.add(o) : st.onem.delete(o); draw(); } }), o + " (" + say(o) + ")")))),
      h("label", null, "Kategori", sel([["", "hepsi"]].concat(kats.map((k) => [k, k])), "", (x) => { st.kat = x; draw(); })), h("label", null, "Kaynak", sel([["", "hepsi"]].concat(kays.map((k) => [k, k])), "", (x) => { st.kay = x; draw(); })),
      h("label", null, "Ara", h("input", { type: "search", placeholder: "ör. bootstrap, stok, Faz 2", oninput: (e) => { st.q = e.target.value; draw(); } })), cnt,
      h("button", { type: "button", onclick: () => list.querySelectorAll("details").forEach((d) => (d.open = true)) }, "Hepsini aç"), h("button", { type: "button", onclick: () => list.querySelectorAll("details").forEach((d) => (d.open = false)) }, "Hepsini kapat")));
    el.append(list); draw();
    el.append(h("h2", null, "Doğrulanan (sorun bulunmayan) noktalar"), h("div", { class: "card" }, h("ul", null, IC.dogrulanan.map(([a, b]) => h("li", null, h("b", null, a + ". "), b)))));
  }

  // ================================================================ JÜRİ
  function juri(el) {
    el.append(h("h1", null, "Jüri raporları ve bağımsız hakem okuması"), h("p", { class: "lede" }, "İki jüri ekibinin raporlarındaki her madde veriyle sınandı. Ayrıca, önceki sonuçlara demirlenmemek için hiçbir ön bilgi verilmeden bağımsız bir hakem okuması yaptırıldı; oradaki iddialar da tek tek yeniden hesaplandı."));
    const box = h("div"); let tab = "j2";
    const stance = (t) => badge(t, t.startsWith("Katılmıyorum") || t.startsWith("Kavramsal") ? "b-kritik" : t.includes("Kısmen") || t.includes("çare") || t.includes("kısmen") ? "b-orta" : "b-ok");
    const cellJ = (d, k) => (d[k] ? h("td", { class: "pcell" }, tr(d[k].b, 3) + " ", h("span", { class: "pp " + pcls(d[k].p_t) }, pv(d[k].p_t))) : h("td", { class: "pcell" }, "–"));
    const T = {
      j2: () => { const d = h("div");
        d.append(h("div", { class: "card" }, h("h3", null, "İkinci jüri raporu: genel değerlendirme"),
          h("p", null, "Rapor kısa, isabetli ve yapıcı; beş eleştirisinin dördü birinci jüri raporu ve bu incelemeyle örtüşüyor, üç yeni öneri getiriyor (ön-örneklem ortalaması tahmincisi, karbon fiyatı, yeşil olmayan patentlerle plasebo). Üç noktada veriyle çelişiyor ya da fazla iyimser:"),
          h("ul", null,
            h("li", null, h("b", null, "Çıkarsama övgüsü (G3): "), `eşli bootstrap + BC'nin birinci tip hatayı “başarıyla kontrol ettiği” söyleniyor; benzetimlerde yöntem %5 yerine ${simr("rej_boot", "A")} oranında reddediyor.`),
            h("li", null, h("b", null, "Önerilen çare (E1): "), `ön-örneklem ortalaması tahmincisi Model 1'i kurtarmıyor (negatif binom Faz 2: ${tr(J2D.psm[Object.keys(J2D.psm)[0]].nb.F2.b, 3)}); Model 2'nin Faz 1 eğimi (${tr(J2D.psm_m2.nb.S1.b, 3)}) ve Faz 2 düzeyi (${tr(J2D.psm_m2.nb.F2.b, 3)}) ise bu tahmincide de anlamlı.`),
            h("li", null, h("b", null, "Kapanış yargısı (S): "), "listelenen düzeltmeler gerekli ama yeterli değil; raporun değinmediği kritik noktalar var.")),
          h("p", { class: "small", style: "margin:0" }, h("a", { href: "#rapor" , onclick: () => { try { sessionStorage.setItem("rapor", "Juri2_Raporu_Degerlendirmesi.md"); } catch (e) {} } }, "Ayrı değerlendirme raporunun tam metni →"))));
        ["Güçlü yön", "Eleştiri", "Tutarlılık", "Kapanış"].forEach((g) => { d.append(h("h2", null, { "Güçlü yön": "Güçlü yönler", "Eleştiri": "Yöntemsel eleştiriler", "Tutarlılık": "Tutarlılık denetimi", "Kapanış": "Kapanış yargısı" }[g]));
          IC.juri2.filter((j) => j[1] === g).forEach((j) => d.append(h("div", { class: "card" }, h("div", { class: "qa" }, h("div", { class: "q" }, j[0] + " · " + j[2]), h("div", { class: "chips", style: "margin-bottom:8px" }, stance(j[3])),
            h("p", { class: "small" }, h("b", null, "Jürinin ifadesi: "), j[5]), h("p", null, j[6]), j[7].length ? h("div", null, h("span", { class: "small" }, "İlgili bulgular: "), j[7].map(bulguLink)) : null)))); });
        d.append(h("h2", null, "Önerilen sınama: ön-örneklem ortalaması tahmincisi"), h("div", { class: "card" }, h("div", { class: "sub" }, "Ülke kuklaları yerine ön-örneklem dönemi bilgisi; hücreler katsayı ve ülke-kümeli t(13) p değeri"),
          table(["Tanım", "Tahminci", "Faz 1", "Faz 2", "Faz 3", "Stok"], Object.entries(J2D.psm).flatMap(([nm, v]) => [N, P].map((f) => [nm, FAM[f], cellJ(v[f], "F1"), cellJ(v[f], "F2"), cellJ(v[f], "F3"), cellJ(v[f], "lnK1")])), { tall: true }),
          h("h4", { style: "margin-top:14px" }, "Model 2, ön-örneklem ortalamalı"),
          table(["Katsayı", "Negatif binom", "Poisson QML", "Tezin sabit etkili tahmini (NB)"], ["tstar", "F1", "S1", "F2", "S2", "F3", "S3", "lnK1"].map((k) => [AD2[k], cellJ(J2D.psm_m2.nb, k), cellJ(J2D.psm_m2.poisson, k), tr(C("m2", N, k).b, 3)]), { num: [3] }),
          h("div", { class: "takeaway", html: "Model 1'de sonuç ön-örneklem bilgisinin biçimine çok duyarlı (A ve B'de faz farkı yok, C'de var). <b>Model 2</b>'nin Faz 1 eğimi ve Faz 2 düzeyi ise sabit etkili tahminlere çok yakın ve anlamlı: tezin en dayanıklı bulgusu burada." })));
        d.append(h("h2", null, "Savunma için cevap taslakları")); IC.juri2_cevap.forEach(([q, a]) => d.append(h("div", { class: "card" }, h("div", { class: "qa" }, h("div", { class: "q" }, q), h("div", null, a)))));
        return d; },
      j1: () => { const d = h("div"); d.append(h("h2", null, "Birinci jürinin soruları ve veriyle desteklenen cevaplar"));
        IC.juri.forEach((j) => d.append(h("div", { class: "card" }, h("div", { class: "qa" }, h("div", { class: "q" }, j[0]), h("div", { class: "chips", style: "margin-bottom:8px" }, badge(j[1], j[1].startsWith("Katıl") || j[1].startsWith("Tamamen") ? "b-ok" : "b-info"), j[2] !== "bilgi" ? badge(j[2], ONEM[j[2]]) : null), h("div", null, j[3]))))); return d; },
      kars: () => h("div", { class: "card" }, h("h3", null, "İki jüri raporunun karşılaştırması"), table(["Konu", "1. jüri raporu", "2. jüri raporu", "Bu incelemedeki karşılığı"], IC.juri_karsilastirma),
        h("div", { class: "takeaway", html: "İki rapor dört temel eleştiride birleşiyor (ortak şoklar, stok, maruziyet, birim kök). Ayrıştıkları tek esaslı nokta <b>bootstrap</b>: birinci jüri yöntemi sorguluyor, ikinci jüri övüyor; benzetim sonuçları birinci jüriyi destekliyor. Genel hükümde bu inceleme birinci jüriye daha yakın." })),
      hakem: () => h("div", { class: "card" }, h("h3", null, "Bağımsız hakemin iddiaları: yeniden hesap"), table(["İddia", "Benim hesabım", ""], [
        ["Model 2 ülke-içi VIF: eğilim 42,8; Faz 3 25,4; stok 12,0", `${tr(EKD.vif_m2.tstar, 1)}; ${tr(EKD.vif_m2.F3, 1)}; ${tr(EKD.vif_m2.lnK1, 1)}`, h("span", { class: "ok" }, "✓")],
        ["Stok–zaman ülke-içi korelasyonu 0,95", tr(EKD.ici_kor["lnK1~zaman"], 3), h("span", { class: "ok" }, "✓")],
        ["Eğilim tek başına 0,27 / 0,46 / 0,78 log puan üretir", ["F1", "F2", "F3"].map((f) => tr(EKD.egilim_katkisi.nb[f].egilimden, 2)).join(" / "), h("span", { class: "ok" }, "✓")],
        ["2003 plasebosu reddediyor (Poisson χ² = 9,51)", `${tr(EKD.plasebo["2003"].poisson.chi2_kume, 2)} (p = ${pv(EKD.plasebo["2003"].poisson.p_kume)}); bootstrap p = ${pv(EKD.plasebo["2003"].poisson.p_boot)}`, h("span", { class: "ok" }, "✓")],
        ["Bootstrap SH ile yalnız 2009 anlamlı", "p: " + ["2006", "2007", "2008", "2009", "2010"].map((y) => pv(EKD.yil_boot[y].p_boot)).join(" / "), h("span", { class: "ok" }, "✓")],
        ["Yalnız kontroller 2 gecikmeli: AIC 2966,65", tr(R.gecikme.nb.lag2_yalniz_kontrol, 2), h("span", { class: "ok" }, "✓")],
        ["Yoğunluk birim kök testleri logaritmayla", `Fisher ${tr(UR.lninten.fisher_c[0], 2)} ↔ ${tr(UR.inten.fisher_c[0], 2)}`, h("span", { class: "ok" }, "✓")],
        ["Birleşik Krallık 31.12.2020'ye kadar AB ETS'de", "web kaynaklarından teyit", h("span", { class: "ok" }, "✓")],
        ["Pedroni +2,255'in “ret” sayılması şüpheli", "yeniden üretilmedi", h("span", { class: "warn" }, "orta güven")]]),
        h("p", { class: "small", style: "margin:10px 0 0" }, "İki bağımsız okumanın birbirinden habersiz aynı kritik noktalara ulaşması (kontrol grubu, H5'in stoka bağlılığı, bootstrap gerekçesi, Tablo 5.4, BC aralıkları) bu bulguların güvenilirliğini artırıyor.")),
      duz: () => h("div", { class: "card" }, h("h3", null, "Önceki incelememdeki düzeltmeler"), h("div", { class: "sub" }, "İlk incelemede yazdığım ve sonraki aşamalarda yanlış ya da eksik çıkan değerlendirmeler"), table(["Önceki ifadem", "Şimdiki durum"], IC.duzeltmeler)),
    };
    el.append(h("div", { class: "filters" }, seg([["j2", "2. jüri raporu"], ["j1", "1. jüri raporu"], ["kars", "Karşılaştırma"], ["hakem", "Bağımsız hakem"], ["duz", "Düzeltmelerim"]], tab, (x) => { box.replaceChildren(T[x]()); })));
    el.append(box); box.append(T.j2());
  }

  // ================================================================ RAPOR (tam metin)
  function rapor(el) {
    el.append(h("h1", null, "Rapor (tam metin)"), h("p", { class: "lede" }, "Kapsamlı yeniden inceleme raporunun ve ikinci jüri değerlendirmesinin tam metni. Rapordaki bütün sayılar hesap çıktılarından otomatik üretilir."));
    const RD = [["Kapsamli_Yeniden_Inceleme.md", "Kapsamlı yeniden inceleme raporu"], ["Juri2_Raporu_Degerlendirmesi.md", "İkinci jüri raporunun değerlendirmesi"]];
    let cur = RD[0][0]; try { const x = sessionStorage.getItem("rapor"); if (x) { cur = x; sessionStorage.removeItem("rapor"); } } catch (e) {}
    const view = h("div", { class: "md" }), toc = h("div", { class: "chips" });
    const show = async (f) => { await mdView(view, f); toc.replaceChildren(...[...view.querySelectorAll("h2")].map((x, i) => { x.id = "r-" + i; return h("button", { type: "button", onclick: () => x.scrollIntoView({ behavior: "smooth", block: "start" }) }, x.textContent); })); };
    el.append(h("div", { class: "filters" }, h("label", null, "Belge", sel(RD, cur, show)), h("a", { class: "btn", href: REPO + "analiz/Kapsamli_Yeniden_Inceleme.md" }, "GitHub'da aç")),
      h("div", { class: "card" }, h("div", { class: "sub" }, "Bölümler"), toc), h("div", { class: "card" }, view));
    show(cur);
  }

  // ================================================================ TEZ BÖLÜMLERİ
  function bolumler(el) {
    el.append(h("h1", null, "Tez bölümlerine göre değerlendirme"), h("p", { class: "lede" }, "Beşinci bölümün her alt bölümü için: tezde ne yapılıyor, neler doğrulandı, hangi bulgular o bölümle ilgili ve ne düzeltilmeli. Bir bulgu birden çok bölümle ilgiliyse her birinde görünür."));
    const GIT = { "5.1": [["cikarsama", "Çıkarsama"]], "5.2": [["ozet", "Hipotez tablosu"]], "5.4": [["veri", "Veri gezgini"], ["replikasyon", "Tanımlayıcı tablolar"]], "5.6": [["cikarsama", "Çıkarsama ve benzetim"], ["replikasyon", "Birim kök tabloları"]], "5.7": [["modeller", "Modeller ve yıl etkileri"]], "5.8": [["saglamlik", "Sağlamlık"]], "5.9": [["ozet", "Hipotezler"], ["juri", "Jüri raporları"]] };
    const box = h("div");
    const show = (key) => { const b = IC.bolumler.find((x) => x[0] === key), fs = IC.bulgular.filter((x) => x.bolum.includes(key));
      const cnt = (o) => fs.filter((x) => x.onem === o).length;
      box.replaceChildren(h("div", { class: "card" }, h("h3", null, b[1]), h("h4", { style: "margin-top:10px;color:var(--ink-2)" }, "Tezde ne var"), h("p", null, b[2]), h("h4", { style: "color:var(--ink-2)" }, "Genel durum"), h("p", null, b[3]),
        h("div", { class: "chips" }, badge(cnt("kritik") + " kritik", "b-kritik"), badge(cnt("önemli") + " önemli", "b-onemli"), badge(cnt("orta") + " orta", "b-orta"), badge(cnt("küçük") + " küçük", "b-kucuk"), (GIT[key] || []).map(([p_, t]) => h("a", { class: "btn", href: "#" + p_ }, t + " →")))),
        h("h2", null, "Bu bölümle ilgili bulgular (" + fs.length + ")"), anlatimBar(), ...fs.map((x) => findingEl(x, "s-")),
        h("h2", null, "Bu bölüm için yapılacaklar"), h("div", { class: "card" }, h("ul", null, IC.yapilacak.filter((y) => y[2].split(", ").some((r) => fs.some((x) => x.id === r))).map((y) => h("li", null, badge(y[0], y[0] === "A" ? "b-kritik" : y[0] === "B" ? "b-onemli" : y[0] === "C" ? "b-orta" : "b-kucuk"), " " + y[1])))));
    };
    el.append(h("div", { class: "filters" }, seg(IC.bolumler.map((b) => [b[0], b[1].split(" ")[0] + " " + b[1].split(" ").slice(1).join(" ")]), "5.1", show)), box); show("5.1");
  }

  // ================================================================ KAYNAKÇA
  function kaynakca(el) {
    const K = IC.kaynakca;
    el.append(h("h1", null, "Kaynakça ve atıf denetimi"), h("p", { class: "lede" }, K.ozet));
    el.append(h("div", { class: "grid g4" },
      h("div", { class: "tile" }, h("div", { class: "lab" }, "Bölümdeki farklı atıf"), h("div", { class: "val" }, IC.atiflar.length), h("div", { class: "note" }, "yazar–yıl çifti")),
      h("div", { class: "tile" }, h("div", { class: "lab" }, "Kaynakçada karşılığı olmayan"), h("div", { class: "val" }, IC.atiflar.filter((a) => !a.kaynakcada).length), h("div", { class: "note" }, "programla eşleştirildi")),
      h("div", { class: "tile" }, h("div", { class: "lab" }, "Kaynakça kaydı"), h("div", { class: "val" }, IC.n_kayit), h("div", { class: "note" }, "liste tezin tamamı için")),
      h("div", { class: "tile" }, h("div", { class: "lab" }, "Yazım hatalı atıf"), h("div", { class: "val" }, K.bicim.length), h("div", { class: "note" }, "boşluk, “&”, “and”"))));
    const q = h("input", { type: "search", placeholder: "yazar ara" }), tb = h("div");
    const draw = () => { const x = q.value.toLocaleLowerCase("tr"); tb.replaceChildren(table(["Atıf", "Yıl", "Bölümde geçiş sayısı", "Kaynakçada"], IC.atiflar.filter((a) => !x || a.atif.toLocaleLowerCase("tr").includes(x)).map((a) => [a.atif, a.yil, a.adet, a.kaynakcada ? h("span", { class: "ok" }, "✓") : h("span", { class: "bad" }, "yok")]), { num: [2], tall: true })); };
    q.addEventListener("input", draw);
    el.append(h("div", { class: "grid g2", style: "margin-top:18px" },
      h("div", { class: "card" }, h("h3", null, "Metin içi atıflar"), h("div", { class: "sub" }, "Bölüm metninden otomatik çıkarıldı; yazım biçimi birleştirilmiştir"), q, h("div", { style: "height:8px" }), tb),
      h("div", null,
        h("div", { class: "card" }, h("h3", null, "Atıf yazım hataları"), table(["Satır", "Metindeki yazım", "Sorun"], K.bicim)),
        h("div", { class: "card" }, h("h3", null, "Kaynakça kayıtları"), table(["Kayıt", "Sorun"], K.kayit)))));
    draw();
    el.append(h("div", { class: "grid g2" },
      h("div", { class: "card" }, h("h3", null, "Eksik metin içi atıflar"), table(["Yer", "Konu", "Not"], K.eksik_atif)),
      h("div", { class: "card" }, h("h3", null, "Birincil kaynaktan doğrulanması gereken aktarımlar"), table(["Yer", "İfade", "Durum"], K.dogrulanamayan))));
    el.append(h("div", { class: "card" }, h("h3", null, "Eklenmesi önerilen kaynaklar"), h("div", { class: "sub" }, "Bulgularda önerilen yöntem ve tartışmalar için"), table(["Kaynak", "Neden"], K.onerilen)));
    el.append(h("h2", null, "İlgili bulgular"), anlatimBar(), ...IC.bulgular.filter((x) => x.bolum.includes("kaynakca")).map((x) => findingEl(x, "k-")));
  }

  // ================================================================ YAPILACAKLAR
  function yapilacak(el) {
    el.append(h("h1", null, "Yapılacaklar"), h("p", { class: "lede" }, "Öncelik sırasına göre düzeltme listesi. İşaretlediğiniz maddeler bu tarayıcıda saklanır."));
    let done = {}; try { done = JSON.parse(localStorage.getItem("yapilacak") || "{}"); } catch (e) {}
    const bar = h("div", null), pl = h("div", { class: "small" });
    const upd = () => { const n = IC.yapilacak.filter((_, i) => done[i]).length; bar.style.width = (100 * n / IC.yapilacak.length) + "%"; pl.textContent = n + " / " + IC.yapilacak.length + " tamamlandı"; try { localStorage.setItem("yapilacak", JSON.stringify(done)); } catch (e) {} };
    el.append(h("div", { class: "card" }, pl, h("div", { class: "progress" }, bar), h("button", { type: "button", onclick: () => { done = {}; el.querySelectorAll(".todo input").forEach((i) => { i.checked = false; i.closest(".todo").classList.remove("done"); }); upd(); } }, "Sıfırla")));
    ["A", "B", "C", "D"].forEach((oc) => { const c = h("div", { class: "card" }, h("h3", null, badge(oc, oc === "A" ? "b-kritik" : oc === "B" ? "b-onemli" : oc === "C" ? "b-orta" : "b-kucuk"), " " + IC.oncelik[oc]));
      IC.yapilacak.forEach((y, i) => { if (y[0] !== oc) return; const row = h("label", { class: "todo" + (done[i] ? " done" : "") }, h("input", Object.assign({ type: "checkbox", onchange: (e) => { done[i] = e.target.checked; row.classList.toggle("done", e.target.checked); upd(); } }, done[i] ? { checked: "" } : {})),
        h("span", null, h("span", { class: "tt" }, y[1]), " ", y[2].split(", ").map((r) => h("a", { href: "#bulgular", class: "small", style: "margin-left:6px", onclick: () => setTimeout(() => { const d = document.getElementById("b-" + r); if (d) { d.open = true; d.scrollIntoView({ block: "center" }); } }, 60) }, r)))); c.append(row); });
      el.append(c); }); upd();
  }

  // ================================================================ BELGELER
  function belgeler(el) {
    el.append(h("h1", null, "Belgeler"), h("p", { class: "lede" }, "Raporların tam metinleri, tez bölümü, veri seti ve bütün hesapları yeniden üreten kod."));
    const DOCS = [["Kapsamli_Yeniden_Inceleme.md", "Kapsamlı yeniden inceleme raporu (ana rapor)"], ["Sade_Anlatim_ve_Duzeltme_Rehberi.md", "Sade anlatım ve adım adım düzeltme rehberi"], ["Juri2_Raporu_Degerlendirmesi.md", "İkinci jüri raporunun değerlendirmesi"], ["Juri2_Degerlendirme_Raporu.md", "İkinci jüri ekibinin raporu (dış değerlendirme)"], ["Juri1_Degerlendirme_Raporu.md", "Birinci jüri değerlendirme raporu (dış değerlendirme)"], ["Bagimsiz_Hakem_Raporu.md", "Bağımsız hakem raporu (kör ikinci okuma, İngilizce)"], ["01_Ilk_Inceleme_ve_Juri_Analizi.md", "İlk inceleme ve birinci jüri analizi (arşiv; bazı değerlendirmeleri güncellendi)"], ["Tez_Bolum5_metin.md", "Tez 5. bölüm, düz metin (satır numaraları buna göre)"]];
    const view = h("div", { class: "md" });
    const show = (f) => mdView(view, f);
    el.append(h("div", { class: "grid g2" },
      h("div", { class: "card" }, h("h3", null, "Depodaki dosyalar"), h("ul", null,
        h("li", null, h("a", { href: REPO + "dokumanlar/Nihai_Model_19112026.docx" }, "Tez 5. bölüm (docx)"), " · ", h("a", { href: REPO + "dokumanlar/Nihai_Model_19112026_metin.md" }, "düz metin (satır numaraları buna göre)")),
        h("li", null, h("a", { href: REPO + "veri/AB14_nihai_veri.xlsx" }, "Veri seti (xlsx)")),
        h("li", null, h("a", { href: REPO + "dokumanlar/Juri2_Degerlendirme_Raporu.docx" }, "İkinci jüri raporu (özgün docx)"), " · ", h("a", { href: REPO + "analiz/Juri2_Raporu_Degerlendirmesi.md" }, "değerlendirmesi"), " · ", h("a", { href: REPO + "analiz/py/juri2.py" }, "sınama kodu")),
        h("li", null, h("a", { href: REPO + "analiz/py/yeniden_inceleme.py" }, "Ana analiz betiği"), " · ", h("a", { href: REPO + "analiz/py/tezlib.py" }, "tahminciler"), " · ", h("a", { href: REPO + "analiz/py/simulasyon.py" }, "Monte Carlo"), " · ", h("a", { href: REPO + "analiz/py/birim_kok.py" }, "birim kök")),
        h("li", null, h("a", { href: "data/sonuclar.json" }, "Tüm sonuçlar (JSON)"), " · ", h("a", { href: "data/spec_egrisi.json" }, "spesifikasyon eğrisi"), " · ", h("a", { href: "data/panel.json" }, "panel verisi")))),
      h("div", { class: "card" }, h("h3", null, "Yeniden üretmek için"), h("pre", { style: "background:var(--surface-2);padding:12px;border-radius:8px;overflow-x:auto;font-size:.82rem" }, "pip install pandas numpy scipy statsmodels openpyxl\npython analiz/py/yeniden_inceleme.py 1999\npython analiz/py/birim_kok.py\npython analiz/py/ek_dogrulama.py\npython analiz/py/simulasyon.py 300 199\npython analiz/py/simulasyon_p.py 1000\npython analiz/py/juri2.py\npython analiz/py/rapor_uret.py"))));
    el.append(h("div", { class: "filters" }, h("label", null, "Belge", sel(DOCS, DOCS[0][0], show))), h("div", { class: "card" }, view)); show(DOCS[0][0]);
  }

  const BUILD = { ozet, rapor, bolumler, veri, replikasyon, modeller, cikarsama, saglamlik, bulgular, kaynakca, juri, yapilacak, belgeler };
  function go() {
    let id = (location.hash || "#ozet").slice(1); if (!BUILD[id]) id = "ozet";
    for (const k in pages) pages[k].classList.toggle("on", k === id);
    nav.querySelectorAll("a").forEach((a) => a.classList.toggle("on", a.dataset.p === id));
    if (!built[id]) { built[id] = true; BUILD[id](pages[id]); }
    Viz.hideTip(); window.scrollTo(0, 0);
    requestAnimationFrame(() => redraws.forEach((f) => f()));
  }
  addEventListener("hashchange", go);
  let rt; addEventListener("resize", () => { clearTimeout(rt); rt = setTimeout(() => redraws.forEach((f) => f()), 150); });
  go();
})();
