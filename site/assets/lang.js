// Runs in <head> before paint: pick the language from ?lang=, the saved choice, or the browser.
(function () {
  var q = new URLSearchParams(location.search).get("lang"), saved = null;
  try { saved = localStorage.getItem("lang"); } catch (e) {}
  var lang = q || saved || ((navigator.language || "en").toLowerCase().indexOf("fr") === 0 ? "fr" : "en");
  if (lang === "fr") document.documentElement.classList.add("fr");
  document.documentElement.lang = lang === "fr" ? "fr" : "en";
  window.setLang = function (l) {
    document.documentElement.classList.toggle("fr", l === "fr");
    document.documentElement.lang = l;
    try { localStorage.setItem("lang", l); } catch (e) {}
    document.querySelectorAll(".lang button").forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.set === l)); });
    var t = document.querySelector('meta[name="title-' + l + '"]'); if (t) document.title = t.content;
  };
  document.addEventListener("DOMContentLoaded", function () { window.setLang(document.documentElement.lang); });
})();
