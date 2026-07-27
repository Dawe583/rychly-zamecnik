/* ==========================================================================
   Rychlý Zámečník Praha — interakce a animace

   Plynulý scroll obstarává Lenis (assets/js/vendor/lenis.min.js, MIT).
   Všechno ostatní je vanilla JS bez dalších závislostí a jede v jediné
   rAF smyčce, kterou řídí Lenis — žádné soupeřící scroll listenery.

   Efekty běží na všech zařízeních a ve všech režimech bez výjimky —
   viz poznámka u `reduced` níž.
   ========================================================================== */
(function () {
  "use strict";

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var clamp = function (v, a, b) { return Math.max(a, Math.min(b, v)); };

  // Efekty běží úplně všude, bez jediné výjimky — to je výslovné zadání.
  //
  // Nevypínají se podle typu zařízení: naklopení karet, magnetická tlačítka
  // i světelná stopa běží stejně pod myší, prstem i perem, protože stojí
  // na Pointer Events, které pokrývají všechny tři vstupy najednou.
  //
  // Nevypínají se ani podle `prefers-reduced-motion`. Tohle je jediné
  // místo, kde se to dá vrátit — přepnutím na `motionQuery.matches` se
  // systémová volba zase začne respektovat. Stojí za to vědět proč tam
  // byla: zapíná si ji člověk, kterému rychlý pohyb na obrazovce dělá
  // fyzicky zle (závrať, migréna, nevolnost). Na webu, kam lidi chodí
  // ve stresu se zabouchnutými dveřmi, to není úplně teoretická skupina.
  var motionQuery = window.matchMedia("(prefers-reduced-motion: reduce)");
  var reduced = false;

  /* ====================================================================== *
   * 1. Lenis — plynulý scroll
   * ====================================================================== */
  var lenis = null;

  function initLenis() {
    if (reduced || typeof window.Lenis !== "function") return null;

    var l = new window.Lenis({
      duration: 1.05,
      // Mírně "těžký" doběh — pohyb doklouže, ale nerozmazává orientaci.
      easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
      smoothWheel: true,
      wheelMultiplier: 1,
      touchMultiplier: 1.6,
      // Plynulý scroll i na dotyku, ne jen pod kolečkem myši.
      syncTouch: true,
      syncTouchLerp: 0.09,
      touchInertiaMultiplier: 24,
    });
    return l;
  }

  /* ====================================================================== *
   * 2. Rozdělení nadpisu na slova/řádky (pro nástupovou animaci)
   * ====================================================================== */
  function splitText(el) {
    if (el.dataset.splitDone) return;
    var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);

    nodes.forEach(function (node) {
      if (!node.nodeValue.trim()) return;
      var frag = document.createDocumentFragment();
      node.nodeValue.split(/(\s+)/).forEach(function (part) {
        if (!part) return;
        if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
        var outer = document.createElement("span");
        outer.className = "word";
        var inner = document.createElement("span");
        inner.className = "word__in";
        inner.textContent = part;
        outer.appendChild(inner);
        frag.appendChild(outer);
      });
      node.parentNode.replaceChild(frag, node);
    });

    // Zpoždění po slovech, ať text „naskáče“ zleva doprava.
    $$(".word__in", el).forEach(function (w, i) {
      w.style.transitionDelay = i * 42 + "ms";
    });
    el.dataset.splitDone = "1";
  }

  /* ====================================================================== *
   * 3. Odkrývání při scrollu
   * ====================================================================== */
  function initReveal() {
    var items = $$("[data-reveal]");

    if (reduced || !("IntersectionObserver" in window)) {
      items.forEach(function (el) { el.classList.add("is-in"); });
      $$("[data-split]").forEach(function (el) { el.classList.add("is-in"); });
      return;
    }

    // Kaskádové zpoždění mezi sourozenci ve stejné mřížce
    items.forEach(function (el) {
      if (el.dataset.revealDelay) {
        el.style.setProperty("--d", el.dataset.revealDelay + "ms");
        return;
      }
      var sibs = el.parentElement ? $$("[data-reveal]", el.parentElement) : [];
      var idx = sibs.indexOf(el);
      if (idx > 0) el.style.setProperty("--d", Math.min(idx, 6) * 85 + "ms");
    });

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add("is-in");
        io.unobserve(e.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.06 });

    items.forEach(function (el) { io.observe(el); });

    // Nadpisy se rozpadají na slova a naskakují zvlášť
    var splits = $$("[data-split]");
    splits.forEach(splitText);
    var splitIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add("is-in");
        splitIO.unobserve(e.target);
      });
    }, { rootMargin: "0px 0px -12% 0px", threshold: 0.15 });
    splits.forEach(function (el) { splitIO.observe(el); });
  }

  /* ====================================================================== *
   * 4. Počítadla
   * ====================================================================== */
  function initCounters() {
    var counters = $$("[data-count]");
    var fmt = function (val, dec) {
      return dec ? val.toFixed(dec).replace(".", ",") : Math.round(val).toLocaleString("cs-CZ");
    };

    if (reduced || !("IntersectionObserver" in window)) {
      counters.forEach(function (el) {
        var dec = (el.dataset.count.split(".")[1] || "").length;
        el.textContent = fmt(parseFloat(el.dataset.count), dec);
      });
      return;
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target;
        var target = parseFloat(el.dataset.count);
        var dec = (el.dataset.count.split(".")[1] || "").length;
        var t0 = null;
        (function frame(t) {
          if (t0 === null) t0 = t;
          var p = Math.min((t - t0) / 1600, 1);
          el.textContent = fmt(target * (1 - Math.pow(1 - p, 3)), dec);
          if (p < 1) requestAnimationFrame(frame);
        })(performance.now());
        io.unobserve(el);
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { io.observe(el); });
  }

  /* ====================================================================== *
   * 5. Parallax vrstvy — posun podle pozice prvku ve výřezu
   * ====================================================================== */
  function collectParallax() {
    return $$("[data-parallax]").map(function (el) {
      return { el: el, amt: parseFloat(el.dataset.parallax) || 0.15 };
    });
  }

  function applyParallax(list) {
    var vh = window.innerHeight;
    list.forEach(function (p) {
      var r = p.el.getBoundingClientRect();
      if (r.bottom < -200 || r.top > vh + 200) return;
      // -1 (prvek nad výřezem) … +1 (pod výřezem)
      var progress = (r.top + r.height / 2 - vh / 2) / (vh / 2 + r.height / 2);
      p.el.style.transform = "translate3d(0," + (progress * p.amt * 100).toFixed(2) + "px,0)";
    });
  }

  /* ====================================================================== *
   * 6. Magnetická tlačítka + 3D naklonění karet
   * ====================================================================== */
  function initMagnetic() {
    if (reduced) return;

    $$("[data-magnetic]").forEach(function (el) {
      var strength = parseFloat(el.dataset.magnetic) || 0.32;

      function move(e) {
        var r = el.getBoundingClientRect();
        var dx = e.clientX - (r.left + r.width / 2);
        var dy = e.clientY - (r.top + r.height / 2);
        el.style.transform = "translate3d(" + dx * strength + "px," + dy * strength + "px,0)";
      }
      function reset() { el.style.transform = ""; }

      el.addEventListener("pointermove", move);
      el.addEventListener("pointerdown", move);
      // Na dotyku po zvednutí prstu žádné pointerleave nepřijde
      el.addEventListener("pointerleave", reset);
      el.addEventListener("pointerup", reset);
      el.addEventListener("pointercancel", reset);
    });
  }

  function initTilt() {
    if (reduced) return;

    $$("[data-tilt]").forEach(function (el) {
      var max = parseFloat(el.dataset.tilt) || 6;

      function move(e) {
        var r = el.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width - 0.5;
        var py = (e.clientY - r.top) / r.height - 0.5;
        el.style.setProperty("--rx", (-py * max).toFixed(2) + "deg");
        el.style.setProperty("--ry", (px * max).toFixed(2) + "deg");
        // Lesk sleduje kurzor i prst
        el.style.setProperty("--mx", ((e.clientX - r.left) / r.width * 100).toFixed(1) + "%");
        el.style.setProperty("--my", ((e.clientY - r.top) / r.height * 100).toFixed(1) + "%");
        el.classList.add("is-touched");
      }
      function reset() {
        el.style.setProperty("--rx", "0deg");
        el.style.setProperty("--ry", "0deg");
        el.classList.remove("is-touched");
      }

      el.addEventListener("pointermove", move);
      el.addEventListener("pointerdown", move);
      el.addEventListener("pointerleave", reset);
      el.addEventListener("pointerup", reset);
      el.addEventListener("pointercancel", reset);
    });
  }

  /* ====================================================================== *
   * 7. Světelná stopa kurzoru
   * ====================================================================== */
  function initSpotlight() {
    if (reduced) return;

    var dot = document.createElement("div");
    dot.className = "spotlight";
    dot.setAttribute("aria-hidden", "true");
    document.body.appendChild(dot);

    var tx = window.innerWidth / 2, ty = window.innerHeight / 2, cx = tx, cy = ty;

    function track(e) {
      tx = e.clientX;
      ty = e.clientY;
      // Zobrazí se až s prvním pohybem — na dotyku není :hover, na který
      // by se dalo navázat.
      dot.classList.add("is-live");
    }
    window.addEventListener("pointermove", track, { passive: true });
    window.addEventListener("pointerdown", track, { passive: true });

    (function loop() {
      cx += (tx - cx) * 0.12;
      cy += (ty - cy) * 0.12;
      dot.style.transform = "translate3d(" + (cx - 220) + "px," + (cy - 220) + "px,0)";
      requestAnimationFrame(loop);
    })();

    // Nad interaktivními prvky se stopa zvýrazní
    $$("a, button, .svc, .why, .review, .post").forEach(function (el) {
      el.addEventListener("pointerenter", function () { dot.classList.add("is-hot"); });
      el.addEventListener("pointerdown", function () { dot.classList.add("is-hot"); });
      el.addEventListener("pointerleave", function () { dot.classList.remove("is-hot"); });
      el.addEventListener("pointerup", function () { dot.classList.remove("is-hot"); });
    });
  }

  /* ====================================================================== *
   * 8. Hlavička, ukazatel scrollu, mobilní lišta, scrollspy
   * ====================================================================== */
  function initScrollUI() {
    var header = $(".header");
    var progress = $(".progress");
    var callBar = $(".call-bar");
    var ring = $(".call-bar__ring");
    var parallax = collectParallax();

    var navLinks = $$(".nav a[href*='#']");
    var sections = navLinks
      .map(function (a) {
        var id = a.getAttribute("href").split("#")[1];
        return id ? document.getElementById(id) : null;
      })
      .filter(Boolean);

    var lastY = 0;

    function onScroll(y) {
      var max = document.documentElement.scrollHeight - window.innerHeight;

      if (header) {
        header.classList.toggle("is-stuck", y > 12);
        // Při scrollu dolů se hlavička schová, při scrollu nahoru vyjede.
        if (y > 320 && y > lastY + 4) header.classList.add("is-hidden");
        else if (y < lastY - 4 || y < 320) header.classList.remove("is-hidden");
      }
      var pct = max > 0 ? clamp(y / max, 0, 1) : 0;
      if (progress) progress.style.transform = "scaleX(" + pct + ")";
      if (callBar) callBar.classList.toggle("is-on", y > 420);
      if (ring) ring.style.setProperty("--p", pct.toFixed(3));
      // Ukazatel scrollování zmizí, jakmile se opustí hero
      document.documentElement.classList.toggle("is-scrolled", y > 120);

      // Běžící pásy ani recenze na scroll nijak nereagují — jedou pořád
      // stejnou rychlostí a bez zkosení. Dřív se jim tady podle rychlosti
      // scrollu přepisovalo --skew a --boost; při rychlém scrollu se text
      // v pásech naklonil a trhl, což u recenzí ruší při čtení.
      if (!reduced) applyParallax(parallax);
      lastY = y;
    }

    // Zvýraznění aktivní položky v menu
    if (sections.length && "IntersectionObserver" in window) {
      var spy = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          navLinks.forEach(function (a) {
            a.classList.toggle("is-active", a.getAttribute("href").split("#")[1] === e.target.id);
          });
        });
      }, { rootMargin: "-45% 0px -50% 0px" });
      sections.forEach(function (s) { spy.observe(s); });
    }

    if (lenis) {
      lenis.on("scroll", function (e) { onScroll(e.scroll); });
    } else {
      var ticking = false;
      window.addEventListener("scroll", function () {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(function () { onScroll(window.scrollY); ticking = false; });
      }, { passive: true });
    }
    onScroll(window.scrollY);

    window.addEventListener("resize", function () { parallax = collectParallax(); }, { passive: true });
  }

  /* ====================================================================== *
   * 9. Kotvy — přes Lenis, s ohledem na výšku hlavičky
   * ====================================================================== */
  function initAnchors() {
    document.addEventListener("click", function (e) {
      var a = e.target.closest('a[href*="#"]');
      if (!a) return;

      var href = a.getAttribute("href");
      var parts = href.split("#");
      var id = parts[1];
      if (!id) return;

      // Odkaz na kotvu na jiné stránce necháme projít normálně
      var path = parts[0];
      if (path && path !== "/" && path !== location.pathname) return;
      if (path === "/" && location.pathname !== "/") return;

      var target = document.getElementById(id);
      if (!target) return;

      e.preventDefault();
      var offset = -(parseFloat(getComputedStyle(document.documentElement)
        .getPropertyValue("--header-h")) || 76) - 12;

      if (lenis) lenis.scrollTo(target, { offset: offset });
      else window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY + offset,
                             behavior: reduced ? "auto" : "smooth" });

      history.replaceState(null, "", "#" + id);
    });
  }

  /* ====================================================================== *
   * 10. Mobilní menu
   * ====================================================================== */
  function initMobileNav() {
    var burger = $(".burger");
    var nav = $(".mobile-nav");
    if (!burger || !nav) return;

    function setOpen(open) {
      burger.setAttribute("aria-expanded", String(open));
      nav.classList.toggle("is-open", open);
      document.body.classList.toggle("is-locked", open);
      if (lenis) { open ? lenis.stop() : lenis.start(); }
    }

    burger.addEventListener("click", function () {
      setOpen(burger.getAttribute("aria-expanded") !== "true");
    });
    $$("a", nav).forEach(function (a) {
      a.addEventListener("click", function () { setOpen(false); });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) setOpen(false);
    });
  }

  /* ====================================================================== *
   * 10b. Hero video
   * ====================================================================== */
  function initHeroVideo() {
    var v = $(".hero__video");
    if (!v) return;

    // Při omezeném pohybu video vůbec nenačítáme — zůstane plakát.
    if (reduced) {
      v.removeAttribute("autoplay");
      $$("source", v).forEach(function (s) { s.remove(); });
      v.load();
      return;
    }
    // Režim úspory dat je výslovná volba uživatele, tu respektujeme taky.
    var c = navigator.connection;
    if (c && c.saveData) {
      $$("source", v).forEach(function (s) { s.remove(); });
      v.load();
      return;
    }

    // Mimo výřez se přehrávání zastaví, ať nežere baterii
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { var p = v.play(); if (p) p.catch(function () {}); }
          else v.pause();
        });
      }, { threshold: 0.05 }).observe(v);
    }
  }

  /* ====================================================================== *
   * 10c. Ambientní světla sekcí, ceníkové řádky, podtržení nadpisů
   * ====================================================================== */
  function initSectionFx() {
    if (!("IntersectionObserver" in window)) {
      $$(".section, .sec-head, .pricing").forEach(function (el) {
        el.classList.add("is-lit", "is-in");
      });
      return;
    }

    var lit = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { e.target.classList.toggle("is-lit", e.isIntersecting); });
    }, { rootMargin: "-10% 0px -10% 0px" });
    $$(".section").forEach(function (el) { lit.observe(el); });

    var heads = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add("is-in");
        heads.unobserve(e.target);
      });
    }, { threshold: 0.35 });
    $$(".sec-head").forEach(function (el) { heads.observe(el); });

    // Ceníkové řádky najíždějí po jednom. Prodleva se počítá zvlášť
    // v každé kategorii — kdyby se počítala přes celý ceník, druhá
    // a další záložka by měly všechny řádky za stropem a najely by naráz.
    function stagger(scope) {
      var groups = $$(".tab-panel", scope);
      if (!groups.length) groups = [scope];
      groups.forEach(function (g) {
        $$(".price-row", g).forEach(function (r, i) {
          r.style.setProperty("--rd", Math.min(i, 14) * 34 + "ms");
        });
      });
    }
    $$(".pricing").forEach(function (pr) {
      stagger(pr);
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          e.target.classList.add("is-in");
          io.unobserve(e.target);
        });
      }, { threshold: 0.12 });
      io.observe(pr);
    });
  }

  /* ====================================================================== *
   * 10e. Záložky ceníku
   *
   * Markup je hotový ARIA tablist, ale obsluha k němu chyběla — kliknutí
   * nedělalo nic a vidět byla jen první kategorie. Ovládání odpovídá
   * očekávání pro tablist: klik, šipky doleva/doprava dokola, Home a End.
   * ====================================================================== */
  function initTabs() {
    $$('[role="tablist"]').forEach(function (list) {
      var tabs = $$('[role="tab"]', list);
      if (!tabs.length) return;

      var panels = tabs.map(function (t) {
        return document.getElementById(t.getAttribute("aria-controls"));
      });

      function select(i, focus) {
        tabs.forEach(function (t, j) {
          var on = j === i;
          t.setAttribute("aria-selected", on ? "true" : "false");
          t.setAttribute("tabindex", on ? "0" : "-1");
          if (panels[j]) panels[j].hidden = !on;
        });
        if (focus) tabs[i].focus();

        // Řádky nové kategorie najedou znovu, ať přepnutí není jen skok.
        // `is-fresh` má v CSS připravenou animaci; sundat a hned nasadit
        // zpátky by prohlížeč sloučil do jednoho kroku a nic by se
        // nepřehrálo, proto je mezi tím vynucený reflow.
        var p = panels[i];
        if (p && !reduced) {
          p.classList.remove("is-fresh");
          void p.offsetWidth;
          p.classList.add("is-fresh");
        }
      }

      tabs.forEach(function (tab, i) {
        tab.addEventListener("click", function () { select(i, false); });
        tab.addEventListener("keydown", function (e) {
          var k = e.key, n = tabs.length, to = -1;
          if (k === "ArrowRight" || k === "ArrowDown") to = (i + 1) % n;
          else if (k === "ArrowLeft" || k === "ArrowUp") to = (i - 1 + n) % n;
          else if (k === "Home") to = 0;
          else if (k === "End") to = n - 1;
          if (to < 0) return;
          e.preventDefault();
          select(to, true);
        });
      });

      // Výchozí stav srovnat podle markupu, ať se HTML a JS nerozejdou.
      var start = tabs.findIndex(function (t) {
        return t.getAttribute("aria-selected") === "true";
      });
      select(start < 0 ? 0 : start, false);
    });
  }

  /* ====================================================================== *
   * 10d. Vlnka po kliknutí na tlačítko
   * ====================================================================== */
  function initRipple() {
    if (reduced) return;
    document.addEventListener("pointerdown", function (e) {
      var btn = e.target.closest(".btn");
      if (!btn) return;
      var r = btn.getBoundingClientRect();
      var d = Math.max(r.width, r.height);
      var s = document.createElement("span");
      s.className = "ripple";
      s.style.width = s.style.height = d + "px";
      s.style.left = e.clientX - r.left - d / 2 + "px";
      s.style.top = e.clientY - r.top - d / 2 + "px";
      btn.appendChild(s);
      setTimeout(function () { s.remove(); }, 700);
    });
  }

  /* ====================================================================== *
   * 11. Cookie lišta a souhlas
   *
   * Lišta sama nic nespouští — jen drží volbu a pouští k ní ostatní.
   * Analytika se navěsí přes rzConsent.onGrant() a spustí se teprve
   * tehdy, když návštěvník klikne na „Přijmout vše". Dokud to neudělá,
   * nesmí se načíst žádný skript, který sbírá statistiky.
   *
   *   rzConsent.onGrant(function () { … zavést měřicí kód … });
   *
   * Volba jde kdykoliv změnit — odkaz s data-cookie-settings lištu
   * otevře znovu, což GDPR vyžaduje (souhlas musí jít odvolat stejně
   * snadno, jako se dával).
   * ====================================================================== */
  function initCookies() {
    var KEY = "rz-cookies";
    var bar = $(".cookiebar");
    var waiting = [];

    function read() {
      try { return localStorage.getItem(KEY); } catch (err) { return null; }
    }

    function granted() { return read() === "all"; }

    function flush() {
      if (!granted()) return;
      while (waiting.length) {
        try { waiting.shift()(); } catch (err) { /* jeden padlý kód nesmí zbytek */ }
      }
    }

    function announce() {
      var v = read();
      document.dispatchEvent(new CustomEvent("rz:consent", {
        detail: { value: v, analytics: v === "all" }
      }));
      flush();
    }

    function show() { if (bar) bar.classList.add("is-on"); }

    function set(value) {
      try { localStorage.setItem(KEY, value); } catch (err) { /* private mode */ }
      if (bar) bar.classList.remove("is-on");
      announce();
    }

    window.rzConsent = {
      value: read,
      granted: granted,
      set: set,
      // Spustí se hned, pokud souhlas už je; jinak počká na kliknutí.
      onGrant: function (cb) {
        if (typeof cb !== "function") return;
        if (granted()) { cb(); return; }
        waiting.push(cb);
      },
      change: show
    };

    if (bar) {
      $$("[data-cookie]", bar).forEach(function (btn) {
        btn.addEventListener("click", function () { set(btn.dataset.cookie); });
      });
    }

    $$("[data-cookie-settings]").forEach(function (el) {
      el.addEventListener("click", function (e) { e.preventDefault(); show(); });
    });

    if (read()) {
      // Vracející se návštěvník — souhlas platí dál, lišta se neukazuje.
      announce();
    } else {
      // Zobrazit až po chvilce, ať nepřekryje první dojem
      setTimeout(show, 1200);
    }
  }

  /* ====================================================================== *
   * 12. Nástupová animace stránky
   * ====================================================================== */
  function initIntro() {
    document.documentElement.classList.add("is-ready");
    if (reduced) { document.documentElement.classList.add("intro-done"); return; }
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        document.documentElement.classList.add("intro-done");
      });
    });
  }

  /* ====================================================================== *
   * Start
   * ====================================================================== */
  function boot() {
    lenis = initLenis();

    if (lenis) {
      (function raf(time) {
        lenis.raf(time);
        requestAnimationFrame(raf);
      })(performance.now());
    }

    initIntro();
    initHeroVideo();
    initReveal();
    initCounters();
    initSectionFx();
    initScrollUI();
    initAnchors();
    initMobileNav();
    initMagnetic();
    initTilt();
    initSpotlight();
    initTabs();
    initRipple();
    initCookies();

    // Duplikace skupin v běžících pásech kvůli nekonečné smyčce
    $$("[data-marquee]").forEach(function (track) {
      var group = track.firstElementChild;
      if (group) track.appendChild(group.cloneNode(true));
    });

    var yr = $("[data-year]");
    if (yr) yr.textContent = new Date().getFullYear();

    // Přepnutí systémové preference pohybu se záměrně neřeší — efekty
    // běží pořád, takže není co překreslovat. Kdyby se `reduced` nahoře
    // vrátilo na `motionQuery.matches`, patří sem zpátky i reload:
    //   motionQuery.addEventListener("change", function () { location.reload(); });
    void motionQuery;
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
