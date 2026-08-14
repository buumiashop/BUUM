/* BUUMIA · animaciones de marca */
(function () {
  function initReveal() {
    var els = document.querySelectorAll('.buum-reveal');
    if (!('IntersectionObserver' in window) || !els.length) {
      els.forEach(function (el) { el.classList.add('buum-in'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('buum-in');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  function initHeader() {
    var header = document.querySelector('.shopify-section-group-header-group, .section-header, sticky-header');
    if (!header) return;
    var onScroll = function () {
      if (window.scrollY > 24) header.classList.add('buum-header-scrolled');
      else header.classList.remove('buum-header-scrolled');
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { initReveal(); initHeader(); });
  } else {
    initReveal();
    initHeader();
  }

  document.addEventListener('shopify:section:load', initReveal);
})();
