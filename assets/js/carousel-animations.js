/**
 * Carousel Animations for Product Sections
 * Adds smooth transitions when sliding products
 */

const CarouselAnimations = (() => {
  const config = {
    fadeOutDuration: 0.3,
    fadeInDuration: 0.4,
    slideDistance: 20,
    easing: 'power2.inOut'
  };

  function init() {
    const carousels = document.querySelectorAll('[data-product-carousel]');
    carousels.forEach(carousel => {
      attachCarouselListeners(carousel);
    });
  }

  function attachCarouselListeners(carousel) {
    const prevBtn = carousel.querySelector('[data-carousel-prev]');
    const nextBtn = carousel.querySelector('[data-carousel-next]');
    const productList = carousel.querySelector('.esd-product-list');

    if (!prevBtn || !nextBtn || !productList) return;

    prevBtn.addEventListener('click', () => {
      animateCarouselChange(productList, 'prev');
    });

    nextBtn.addEventListener('click', () => {
      animateCarouselChange(productList, 'next');
    });
  }

  function animateCarouselChange(productList, direction) {
    const cards = Array.from(productList.querySelectorAll('[data-product-card]:not([hidden])'));

    if (cards.length === 0) return;

    // Determine which cards are moving out and which are coming in
    const firstCard = cards[0];
    const lastCard = cards[cards.length - 1];

    // Fade out and slide animation for exiting cards
    const exitCards = direction === 'next' ? [firstCard] : [lastCard];
    const enterCards = direction === 'next'
      ? [productList.querySelector('[data-product-card][hidden]')]
      : [productList.querySelector('[data-product-card][hidden]')];

    // Animate exiting cards
    exitCards.forEach(card => {
      if (!card) return;

      const direction_offset = direction === 'next' ? -config.slideDistance : config.slideDistance;

      gsap.to(card, {
        opacity: 0,
        x: direction_offset,
        duration: config.fadeOutDuration,
        ease: config.easing,
        onComplete: () => {
          card.style.opacity = '1';
          card.style.transform = 'translateX(0)';
        }
      });
    });

    // Small delay before animating entering cards
    setTimeout(() => {
      // Animate entering cards - fade in and slide
      const newVisibleCards = Array.from(productList.querySelectorAll('[data-product-card]:not([hidden])'));

      newVisibleCards.forEach((card, index) => {
        const direction_offset = direction === 'next' ? config.slideDistance : -config.slideDistance;
        const delay = index * 0.05; // Stagger effect

        gsap.fromTo(card,
          {
            opacity: 0,
            x: direction_offset
          },
          {
            opacity: 1,
            x: 0,
            duration: config.fadeInDuration,
            ease: config.easing,
            delay: delay
          }
        );
      });
    }, config.fadeOutDuration * 1000);
  }

  return {
    init
  };
})();

// Initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => CarouselAnimations.init());
} else {
  CarouselAnimations.init();
}
