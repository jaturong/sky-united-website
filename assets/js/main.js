const SkyUnited = {
  page: document.body.dataset.page || "unknown",
};

document.documentElement.classList.add("js-enabled");

// Hamburger menu toggle
document.addEventListener("DOMContentLoaded", () => {
  const hamburger = document.querySelector(".hamburger");
  const body = document.body;
  const header = document.querySelector(".site-header");
  const mobileNav = document.querySelector(".mobile-nav");

  if (hamburger) {
    // Set mobile-nav top position based on header height
    const updateMobileNavPosition = () => {
      if (header && mobileNav) {
        const headerHeight = header.offsetHeight;
        mobileNav.style.top = `${headerHeight}px`;
      }
    };

    // Update on load and resize
    updateMobileNavPosition();
    window.addEventListener("resize", updateMobileNavPosition);

    hamburger.addEventListener("click", () => {
      body.classList.toggle("nav-open");
    });

    // Close on nav link click
    document.querySelectorAll(".mobile-nav a").forEach((link) => {
      link.addEventListener("click", () => {
        body.classList.remove("nav-open");
      });
    });
  }
});
