(function () {
  'use strict';

  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');

  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });

    // Close the menu when a link is tapped (mobile UX)
    links.addEventListener('click', function (e) {
      if (e.target.tagName === 'A' && window.matchMedia('(max-width: 767px)').matches) {
        links.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });

    // Close on Escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && links.classList.contains('open')) {
        links.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  // Graceful image fallback — hide broken images so the CSS placeholder shows
  var photos = document.querySelectorAll('.hero-photo img, .meet-photo img');
  photos.forEach(function (img) {
    img.addEventListener('error', function () {
      img.classList.add('missing');
    });
    // If src is empty or the image never loaded, mark missing now
    if (!img.getAttribute('src') || img.complete && img.naturalWidth === 0) {
      img.classList.add('missing');
    }
  });

  // Highlight current nav item based on page
  var path = window.location.pathname.replace(/\/index\.html$/, '/');
  document.querySelectorAll('.nav-links a').forEach(function (a) {
    var href = a.getAttribute('href');
    if (href && (href === path || (href !== '/' && path.indexOf(href) !== -1))) {
      a.classList.add('active');
    }
  });
})();
