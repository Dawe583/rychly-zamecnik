/* ==========================================================================
   Rychlý Zámečník Praha — interakce
   Vanilla JS, bez závislostí. Vše respektuje prefers-reduced-motion.
   ========================================================================== */
(function () {
  "use strict";

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- Sticky header + scroll progress + mobilní call bar ---------- */
  var header = $(".header");
  var progress = $(".progress");
  var callBar = $(".call-bar");
  var ticking = false;

  function onScroll() {
    var y = window.scrollY;
    var max = document.documentElement.scrollHeight - window.innerHeight;

    header.classList.toggle("is-stuck", y > 12);
    if (progress) progress.style.transform = "scaleX(" + (max > 0 ? y / max : 0) + ")";
    if (callBar) callBar.classList.toggle("is-on", y > 420);

    ticking = false;
  }
  window.addEventListener("scroll", function () {
    if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
  }, { passive: true });
  onScroll();

  /* ---------- Mobilní menu ---------- */
  var burger = $(".burger");
  var mobileNav = $(".mobile-nav");
  if (burger && mobileNav) {
    burger.addEventListener("click", function () {
      var open = burger.getAttribute("aria-expanded") === "true";
      burger.setAttribute("aria-expanded", String(!open));
      mobileNav.classList.toggle("is-open", !open);
      document.body.style.overflow = !open ? "hidden" : "";
    });
    $$("a", mobileNav).forEach(function (a) {
      a.addEventListener("click", function () {
        burger.setAttribute("aria-expanded", "false");
        mobileNav.classList.remove("is-open");
        document.body.style.overflow = "";
      });
    });
  }

  /* ---------- Reveal on scroll ---------- */
  var revealables = $$("[data-reveal]");
  if (reduced || !("IntersectionObserver" in window)) {
    revealables.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    var revealIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("is-in");
          revealIO.unobserve(e.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.06 });

    revealables.forEach(function (el, i) {
      // Postupné zpoždění uvnitř jedné skupiny (mřížky)
      var sibs = el.parentElement ? $$("[data-reveal]", el.parentElement) : [];
      var idx = sibs.indexOf(el);
      el.style.setProperty("--d", (idx > 0 ? Math.min(idx, 6) * 80 : 0) + "ms");
      revealIO.observe(el);
    });
  }

  /* ---------- Počítadla ---------- */
  function animateCount(el) {
    var target = parseFloat(el.dataset.count);
    var dec = (el.dataset.count.split(".")[1] || "").length;
    var dur = 1500;
    var t0 = null;

    function frame(t) {
      if (t0 === null) t0 = t;
      var p = Math.min((t - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      var val = target * eased;
      el.textContent = dec
        ? val.toFixed(dec).replace(".", ",")
        : Math.round(val).toLocaleString("cs-CZ");
      if (p < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  var counters = $$("[data-count]");
  if (reduced || !("IntersectionObserver" in window)) {
    counters.forEach(function (el) {
      var d = (el.dataset.count.split(".")[1] || "").length;
      el.textContent = d
        ? parseFloat(el.dataset.count).toFixed(d).replace(".", ",")
        : parseFloat(el.dataset.count).toLocaleString("cs-CZ");
    });
  } else {
    var countIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { animateCount(e.target); countIO.unobserve(e.target); }
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { countIO.observe(el); });
  }

  /* ---------- Ceníkové záložky ---------- */
  var tablist = $(".tabs");
  if (tablist) {
    var tabs = $$(".tab", tablist);

    function select(tab) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute("aria-selected", String(on));
        t.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(t.getAttribute("aria-controls"));
        if (panel) panel.hidden = !on;
      });
    }

    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () { select(tab); });
    });

    tablist.addEventListener("keydown", function (e) {
      var i = tabs.indexOf(document.activeElement);
      if (i < 0) return;
      var next = null;
      if (e.key === "ArrowRight") next = tabs[(i + 1) % tabs.length];
      if (e.key === "ArrowLeft") next = tabs[(i - 1 + tabs.length) % tabs.length];
      if (e.key === "Home") next = tabs[0];
      if (e.key === "End") next = tabs[tabs.length - 1];
      if (next) { e.preventDefault(); next.focus(); select(next); }
    });
  }

  /* ---------- Aktivní položka navigace podle scrollu ---------- */
  var navLinks = $$(".nav a[href^='#']");
  var sections = navLinks
    .map(function (a) { return document.getElementById(a.getAttribute("href").slice(1)); })
    .filter(Boolean);

  if (sections.length && "IntersectionObserver" in window) {
    var spyIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        navLinks.forEach(function (a) {
          a.classList.toggle("is-active", a.getAttribute("href") === "#" + e.target.id);
        });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    sections.forEach(function (s) { spyIO.observe(s); });
  }

  /* ---------- Jemný parallax hero obrázku ---------- */
  var heroImg = $(".hero__media img");
  if (heroImg && !reduced) {
    var raf = false;
    window.addEventListener("scroll", function () {
      if (raf) return;
      raf = true;
      requestAnimationFrame(function () {
        var y = window.scrollY;
        if (y < window.innerHeight * 1.2) {
          heroImg.style.translate = "0 " + y * 0.16 + "px";
        }
        raf = false;
      });
    }, { passive: true });
  }

  /* ---------- Duplikace marquee skupin pro plynulou smyčku ---------- */
  $$("[data-marquee]").forEach(function (track) {
    var group = track.firstElementChild;
    if (group) track.appendChild(group.cloneNode(true));
  });

  /* ---------- Rok v patičce ---------- */
  var yr = $("[data-year]");
  if (yr) yr.textContent = new Date().getFullYear();
})();
