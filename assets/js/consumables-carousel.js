/**
 * Consumables Carousel — Fade Animation + Pagination Dots
 * Slides by 1 item with smooth opacity transitions
 */

const ConsumablesCarousel = (() => {
  const REDUCED_MOTION = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function getItemsVisible() {
    const width = window.innerWidth;
    if (width <= 640) return 1;
    if (width <= 980) return 2;
    return 3;
  }

  function createState(element) {
    const track    = element.querySelector('.consumables-product-list');
    const controls = element.querySelector('.consumables-carousel-controls');
    const cards    = [...element.querySelectorAll('[data-product-card]')];
    const itemsVisible = getItemsVisible();
    const totalPositions = Math.max(1, cards.length - itemsVisible + 1);
    return { element, track, controls, cards, totalPositions, current: 0, dots: [], autoTimer: null, itemsVisible };
  }

  function buildDots(state) {
    const nav = state.controls.querySelector('nav');
    nav.innerHTML = '';

    for (let i = 0; i < state.totalPositions; i++) {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'pagination-dot' + (i === 0 ? ' active' : '');
      btn.setAttribute('aria-label', `สไลด์ ${i + 1} จาก ${state.totalPositions}`);
      btn.addEventListener('click', () => goToPosition(state, i));
      nav.appendChild(btn);
      state.dots.push(btn);
    }
  }

  function slide(state) {
    const { track, cards, current } = state;
    const offset = REDUCED_MOTION ? 0 : (cards[current]?.offsetLeft ?? 0);
    track.style.transform = `translateX(-${offset}px)`;
  }

  function goToPosition(state, posIndex) {
    if (posIndex === state.current) return;
    state.current = posIndex % state.totalPositions;

    // Fade out current cards
    if (window.gsap && !REDUCED_MOTION) {
      gsap.to(state.cards, {
        opacity: 0,
        duration: 0.4,
        overwrite: 'auto',
        onComplete: () => {
          slide(state);
          // Fade in new cards
          gsap.to(state.cards, {
            opacity: 1,
            duration: 0.8,
            stagger: 0.08
          });
        }
      });
    } else {
      slide(state);
    }

    state.dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === state.current);
      dot.setAttribute('aria-pressed', i === state.current ? 'true' : 'false');
    });
  }

  function attachInitialAnimation(state) {
    if (!window.gsap || !window.ScrollTrigger || REDUCED_MOTION) return;
    gsap.fromTo(
      state.cards.slice(0, state.itemsVisible),
      { opacity: 0, scale: 0.96 },
      {
        opacity: 1, scale: 1,
        duration: 0.8,
        ease: 'power3.out',
        stagger: 0.1,
        scrollTrigger: { trigger: state.element, start: 'top 80%', once: true }
      }
    );
  }

  function attachInteraction(state) {
    state.element.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight') goToPosition(state, (state.current + 1) % state.totalPositions);
      if (e.key === 'ArrowLeft')  goToPosition(state, (state.current - 1 + state.totalPositions) % state.totalPositions);
    });

    let touchStartX = 0;
    state.element.addEventListener('touchstart', (e) => {
      touchStartX = e.touches[0].clientX;
    }, { passive: true });

    state.element.addEventListener('touchend', (e) => {
      const diff = touchStartX - e.changedTouches[0].clientX;
      if (Math.abs(diff) < 40) return;
      if (diff > 0) goToPosition(state, (state.current + 1) % state.totalPositions);
      else          goToPosition(state, (state.current - 1 + state.totalPositions) % state.totalPositions);
    }, { passive: true });

    window.addEventListener('resize', () => {
      const newItemsVisible = getItemsVisible();
      if (newItemsVisible !== state.itemsVisible) {
        state.itemsVisible = newItemsVisible;
        state.totalPositions = Math.max(1, state.cards.length - state.itemsVisible + 1);
        if (state.current >= state.totalPositions) {
          state.current = 0;
          buildDots(state);
        }
      }
      slide(state);
    });
  }

  function attachAutoAdvance(state) {
    if (state.totalPositions <= 1) return;

    const startAutoAdvance = () => {
      state.autoTimer = setInterval(() => {
        const nextPos = (state.current + 1) % state.totalPositions;
        goToPosition(state, nextPos);
      }, 5000); // 5 seconds
    };

    const stopAutoAdvance = () => {
      clearInterval(state.autoTimer);
    };

    state.element.addEventListener('mouseenter', stopAutoAdvance);
    state.element.addEventListener('mouseleave', startAutoAdvance);
    state.element.addEventListener('focusin', stopAutoAdvance);
    state.element.addEventListener('focusout', startAutoAdvance);

    startAutoAdvance();
  }

  function init() {
    document.querySelectorAll('[data-consumables-carousel]').forEach((el) => {
      const state = createState(el);
      if (!state.track || state.cards.length === 0) return;

      buildDots(state);
      requestAnimationFrame(() => slide(state));
      attachInitialAnimation(state);
      attachInteraction(state);
      attachAutoAdvance(state);
    });
  }

  return { init };
})();

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', ConsumablesCarousel.init);
} else {
  ConsumablesCarousel.init();
}
