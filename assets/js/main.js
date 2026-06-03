const SkyUnited = {
  page: document.body.dataset.page || "unknown",
};

document.documentElement.classList.add("js-enabled");

document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector(".nav-toggle");
  const drawer = document.querySelector(".mobile-drawer");
  const body   = document.body;
  const header = document.querySelector(".site-header");

  // Header scroll-shrink animation
  if (header) {
    window.addEventListener("scroll", () => {
      header.classList.toggle("header--scrolled", window.scrollY > 60);
    }, { passive: true });
  }

  if (!toggle || !drawer) return;

  function closeMenu() {
    body.classList.remove("nav-open");
    toggle.setAttribute("aria-expanded", "false");
    drawer.setAttribute("aria-hidden", "true");
  }

  // Toggle open/close
  toggle.addEventListener("click", (e) => {
    e.stopPropagation();
    const isOpen = body.classList.toggle("nav-open");
    toggle.setAttribute("aria-expanded", String(isOpen));
    drawer.setAttribute("aria-hidden", String(!isOpen));
  });

  // Close on drawer link click
  drawer.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => closeMenu());
  });

  // Close on ESC
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeMenu();
  });

  // Close on click outside header
  document.addEventListener("click", (e) => {
    if (header && !header.contains(e.target)) closeMenu();
  });
});
