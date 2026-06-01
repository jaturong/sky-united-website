/**
 * Product Carousel — CSS Transform Slide + Pagination Dots
 * Smooth GPU-accelerated animation using translateX
 * Slides by 1 item at a time
 */

const ProductCarousel = (() => {
  const ITEMS_VISIBLE = 4;
  const REDUCED_MOTION = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function createState(element) {
    const track    = element.querySelector('.esd-product-list');
    const controls = element.querySelector('.product-carousel-controls');
    const cards    = [...element.querySelectorAll('[data-product-card]')];
    const totalPositions = Math.max(1, cards.length - ITEMS_VISIBLE + 1);
    return { element, track, controls, cards, totalPositions, current: 0, dots: [] };
  }

  function buildDots(state) {
    state.controls.innerHTML = '';
    const nav = document.createElement('nav');
    nav.className = 'carousel-pagination';
    nav.setAttribute('aria-label', 'Product slide navigation');

    for (let i = 0; i < state.totalPositions; i++) {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'pagination-dot' + (i === 0 ? ' active' : '');
      btn.setAttribute('aria-label', `สไลด์ ${i + 1} จาก ${state.totalPositions}`);
      btn.addEventListener('click', () => goToPosition(state, i));
      nav.appendChild(btn);
      state.dots.push(btn);
    }

    state.controls.appendChild(nav);
  }

  function slide(state) {
    const { track, cards, current } = state;
    const offset = REDUCED_MOTION ? 0 : (cards[current]?.offsetLeft ?? 0);
    track.style.transform = `translateX(-${offset}px)`;
  }

  function goToPosition(state, posIndex) {
    if (posIndex === state.current) return;
    state.current = posIndex % state.totalPositions;
    slide(state);
    state.dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === state.current);
      dot.setAttribute('aria-pressed', i === state.current ? 'true' : 'false');
    });
  }

  function attachInitialAnimation(state) {
    if (!window.gsap || !window.ScrollTrigger || REDUCED_MOTION) return;
    gsap.fromTo(
      state.cards.slice(0, ITEMS_VISIBLE),
      { opacity: 0, y: 32, scale: 0.96 },
      {
        opacity: 1, y: 0, scale: 1,
        duration: 0.72,
        ease: 'power3.out',
        stagger: 0.09,
        scrollTrigger: { trigger: state.element, start: 'top 80%', once: true }
      }
    );
  }

  function attachInteraction(state) {
    // Keyboard arrows
    state.element.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight') goToPosition(state, (state.current + 1) % state.totalPositions);
      if (e.key === 'ArrowLeft')  goToPosition(state, (state.current - 1 + state.totalPositions) % state.totalPositions);
    });

    // Touch swipe
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

    // Resize: recalculate offset
    window.addEventListener('resize', () => slide(state));
  }

  function attachAutoAdvance(state) {
    if (state.totalPositions <= 1) return; // Only auto-advance if there are multiple positions

    let autoTimer;

    const startAutoAdvance = () => {
      autoTimer = setInterval(() => {
        const nextPos = (state.current + 1) % state.totalPositions;
        goToPosition(state, nextPos);
      }, 5000);
    };

    const stopAutoAdvance = () => {
      clearInterval(autoTimer);
    };

    // Stop on hover/focus, resume on leave
    state.element.addEventListener('mouseenter', stopAutoAdvance);
    state.element.addEventListener('mouseleave', startAutoAdvance);
    state.element.addEventListener('focusin', stopAutoAdvance);
    state.element.addEventListener('focusout', startAutoAdvance);

    // Manual position changes reset timer
    const originalGoToPosition = goToPosition;
    goToPosition = (st, posIndex) => {
      originalGoToPosition(st, posIndex);
      stopAutoAdvance();
      startAutoAdvance();
    };

    startAutoAdvance();
  }

  function init() {
    document.querySelectorAll('[data-product-carousel]').forEach((el) => {
      const state = createState(el);
      if (!state.track || state.cards.length === 0) return;

      buildDots(state);
      requestAnimationFrame(() => slide(state)); // wait for layout
      attachInitialAnimation(state);
      attachInteraction(state);
      attachAutoAdvance(state);
    });
  }

  return { init };
})();

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', ProductCarousel.init);
} else {
  ProductCarousel.init();
}
