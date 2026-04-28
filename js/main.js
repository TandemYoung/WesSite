// Site gate (preview password protection) ------------------------------
// To remove gate entirely: delete this IIFE AND remove class="locked" from each <body>.
(function () {
  'use strict';

  var STORAGE_KEY = 'wfsr_gate_v1';
  var PASSWORD = 'freeman2026'; // compared lowercase, so "Freeman2026" / "FREEMAN2026" all work

  if (!document.body.classList.contains('locked')) return;

  if (sessionStorage.getItem(STORAGE_KEY) === '1') {
    document.body.classList.remove('locked');
    return;
  }

  var gate = document.createElement('div');
  gate.id = 'site-gate';
  gate.innerHTML = [
    '<div class="gate-card" role="dialog" aria-labelledby="gate-title" aria-modal="true">',
      '<div class="gate-logo" aria-hidden="true">WF</div>',
      '<h1 id="gate-title">Wes Freeman for State Representative</h1>',
      '<p>Site preview &mdash; please enter the access password to continue.</p>',
      '<form class="gate-form" id="gate-form" novalidate>',
        '<label class="sr-only" for="gate-input">Access password</label>',
        '<input type="password" id="gate-input" autocomplete="off" autocapitalize="none" autocorrect="off" spellcheck="false" placeholder="Password" required>',
        '<p class="gate-error" id="gate-error" role="alert"></p>',
        '<button type="submit" class="btn btn-primary">Enter Site</button>',
      '</form>',
    '</div>'
  ].join('');
  document.body.appendChild(gate);

  var form = document.getElementById('gate-form');
  var input = document.getElementById('gate-input');
  var err = document.getElementById('gate-error');

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (input.value.trim().toLowerCase() === PASSWORD) {
      sessionStorage.setItem(STORAGE_KEY, '1');
      document.body.classList.remove('locked');
      gate.remove();
    } else {
      err.textContent = 'Incorrect password.';
      input.value = '';
      input.focus();
    }
  });

  setTimeout(function () { input.focus(); }, 30);
})();

// Site logic ------------------------------------------------------------
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
