/* ==========================================================================
   Rychlý Zámečník Praha — interakce a animace

   Plynulý scroll obstarává Lenis (assets/js/vendor/lenis.min.js, MIT).
   Všechno ostatní je vanilla JS bez dalších závislostí a jede v jediné
   rAF smyčce, kterou řídí Lenis — žádné soupeřící scroll listenery.

   Při `prefers-reduced-motion: reduce` se Lenis vůbec nespustí a všechny
   efekty se vypnou; obsah zůstane rovnou viditelný.
   ========================================================================== */
(function () {
  "use strict";

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var clamp = function (v, a, b) { return Math.max(a, Math.min(b, v)); };

  var motionQuery = window.matchMedia("(prefers-reduced-motion: reduce)");
  var reduced = motionQuery.matches;

  // Žádné efekty se nevypínají podle typu zařízení — naklopení karet,
  // magnetická tlačítka i světelná stopa běží stejně pod myší, prstem
  // i perem. Pointer Events pokrývají všechny tři vstupy najednou.

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
    var marquees = $$(".marquee__track, .rev-track");
    var parallax = collectParallax();

    var navLinks = $$(".nav a[href*='#']");
    var sections = navLinks
      .map(function (a) {
        var id = a.getAttribute("href").split("#")[1];
        return id ? document.getElementById(id) : null;
      })
      .filter(Boolean);

    var lastY = 0;

    function onScroll(y, velocity) {
      var max = document.documentElement.scrollHeight - window.innerHeight;

      if (header) {
        header.classList.toggle("is-stuck", y > 12);
        // Při scrollu dolů se hlavička schová, při scrollu nahoru vyjede.
        if (y > 320 && y > lastY + 4) header.classList.add("is-hidden");
        else if (y < lastY - 4 || y < 320) header.classList.remove("is-hidden");
      }
      if (progress) progress.style.transform = "scaleX(" + (max > 0 ? clamp(y / max, 0, 1) : 0) + ")";
      if (callBar) callBar.classList.toggle("is-on", y > 420);

      // Běžící pásy reagují na rychlost scrollu — zrychlí a lehce se zkosí.
      if (!reduced && marquees.length) {
        var v = clamp((velocity || 0) / 45, -1.6, 1.6);
        marquees.forEach(function (m) {
          m.style.setProperty("--skew", (v * 4).toFixed(2) + "deg");
          m.style.setProperty("--boost", (1 + Math.abs(v) * 0.9).toFixed(2));
        });
      }

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
      lenis.on("scroll", function (e) { onScroll(e.scroll, e.velocity); });
    } else {
      var ticking = false;
      window.addEventListener("scroll", function () {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(function () { onScroll(window.scrollY, 0); ticking = false; });
      }, { passive: true });
    }
    onScroll(window.scrollY, 0);

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
   * 11. Cookie lišta
   * ====================================================================== */
  function initCookies() {
    var bar = $(".cookiebar");
    if (!bar) return;

    var KEY = "rz-cookies";
    var stored = null;
    try { stored = localStorage.getItem(KEY); } catch (err) { /* private mode */ }
    if (stored) return;

    // Zobrazit až po chvilce, ať nepřekryje první dojem
    setTimeout(function () { bar.classList.add("is-on"); }, 1200);

    $$("[data-cookie]", bar).forEach(function (btn) {
      btn.addEventListener("click", function () {
        try { localStorage.setItem(KEY, btn.dataset.cookie); } catch (err) { /* ignore */ }
        bar.classList.remove("is-on");
      });
    });
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
    initReveal();
    initCounters();
    initScrollUI();
    initAnchors();
    initMobileNav();
    initMagnetic();
    initTilt();
    initSpotlight();
    initCookies();

    // Duplikace skupin v běžících pásech kvůli nekonečné smyčce
    $$("[data-marquee]").forEach(function (track) {
      var group = track.firstElementChild;
      if (group) track.appendChild(group.cloneNode(true));
    });

    var yr = $("[data-year]");
    if (yr) yr.textContent = new Date().getFullYear();

    // Pokud uživatel přepne preferenci pohybu, načteme stránku znovu —
    // je to čistší než rozebírat všechny efekty za běhu.
    motionQuery.addEventListener("change", function () { location.reload(); });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
