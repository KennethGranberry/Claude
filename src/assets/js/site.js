/* ============================================================
   Kenneth Granberry — shared behaviour
   Masthead shade on scroll + reveal-on-scroll.
   Page-specific behaviour (steppers, copy buttons, form
   captures) lives in each page's own script block.
   No localStorage / sessionStorage anywhere — in-memory only.
   ============================================================ */
(function () {
  // Masthead background on scroll.
  var mast = document.getElementById("masthead");
  if (mast) {
    var onScroll = function () {
      if (window.scrollY > 24) { mast.classList.add("scrolled"); }
      else { mast.classList.remove("scrolled"); }
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  // Reveal-on-scroll for any .reveal elements.
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var reveals = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) {
    reveals.forEach(function (el) { el.classList.add("in"); });
  } else {
    // Hero reveals fire immediately; the rest on scroll.
    document.querySelectorAll(".hero .reveal").forEach(function (el) {
      requestAnimationFrame(function () { el.classList.add("in"); });
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) {
      if (!el.closest(".hero")) { io.observe(el); }
    });
  }
})();

/* ------------------------------------------------------------
   Email capture — DEMO STUB.
   TODO: wire to the real provider (Kit / Beehiiv / Substack).
   For now this shows the page's thank-you state and captures
   nothing. Attach by giving a <form> the [data-capture]
   attribute and a sibling element with [data-capture-thanks].
   ------------------------------------------------------------ */
(function () {
  document.querySelectorAll("form[data-capture]").forEach(function (form) {
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var email = form.querySelector('input[type="email"]');
      if (!email || !email.value || email.value.indexOf("@") < 1) {
        if (email) { email.focus(); email.style.borderColor = "var(--star-bright)"; }
        return;
      }
      var mode = form.getAttribute("data-capture"); // "swap" hides form, "class" toggles a class
      if (mode === "class") {
        var holder = form.closest("[data-capture-holder]") || form.parentNode;
        holder.classList.add("done");
      } else {
        form.style.display = "none";
        var thanks = document.querySelector(form.getAttribute("data-capture-thanks"));
        if (thanks) { thanks.style.display = "block"; }
      }
    });
  });
})();
