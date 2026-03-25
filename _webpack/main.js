import "bootstrap";

// Auto-wrap Markdown tables in a responsive container
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("main table").forEach(function (t) {
    var wrapper = document.createElement("div");
    wrapper.className = "table-responsive";
    t.parentNode.insertBefore(wrapper, t);
    wrapper.appendChild(t);
  });

  // Open external links in a new tab
  document.querySelectorAll("a[href^='http']").forEach(function (a) {
    if (a.hostname && a.hostname !== location.hostname) {
      a.setAttribute("target", "_blank");
      a.setAttribute("rel", "noopener noreferrer");
    }
  });
});
