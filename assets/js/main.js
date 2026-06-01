const SkyUnited = {
  page: document.body.dataset.page || "unknown",
};

document.documentElement.classList.add("js-enabled");

// Hamburger menu toggle
document.addEventListener("DOMContentLoaded", () => {
  const hamburger = document.querySelector(".hamburger");
  const body = document.body;

  if (hamburger) {
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
