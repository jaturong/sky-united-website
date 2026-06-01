const SkyAnimations = {
  enabled: !window.matchMedia("(prefers-reduced-motion: reduce)").matches,
};

window.addEventListener("load", () => {
  const animatedItems = document.querySelectorAll("[data-animate]");

  if (!SkyAnimations.enabled) {
    animatedItems.forEach((item) => {
      item.style.opacity = "1";
      item.style.transform = "none";
    });
    return;
  }

  if (window.gsap && window.ScrollTrigger) {
    gsap.registerPlugin(ScrollTrigger);

    animatedItems.forEach((item) => {
      gsap.to(item, {
        opacity: 1,
        y: 0,
        duration: 0.9,
        ease: "power3.out",
        scrollTrigger: {
          trigger: item,
          start: "top 84%",
        },
      });
    });

    if (document.querySelector(".chip-scene")) {
      gsap.to(".chip-scene", {
        yPercent: 5,
        rotate: 1.5,
        ease: "none",
        scrollTrigger: {
          trigger: ".hero-section",
          start: "top top",
          end: "bottom top",
          scrub: true,
        },
      });
    }

    if (document.querySelector(".layer-stack span")) {
      gsap.to(".layer-stack span", {
        y: -18,
        stagger: 0.08,
        ease: "none",
        scrollTrigger: {
          trigger: ".protection-section",
          start: "top bottom",
          end: "bottom top",
          scrub: true,
        },
      });
    }

    if (document.querySelector(".building-image-wrap img")) {
      gsap.to(".building-image-wrap img", {
        scale: 1.04,
        y: -24,
        ease: "none",
        scrollTrigger: {
          trigger: ".building-reveal",
          start: "top bottom",
          end: "bottom top",
          scrub: true,
        },
      });
    }

    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.style.opacity = "1";
        entry.target.style.transform = "none";
        entry.target.style.transition = "opacity 700ms ease, transform 700ms ease";
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.18 }
  );

  animatedItems.forEach((item) => observer.observe(item));
});
