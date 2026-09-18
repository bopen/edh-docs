(function () {
  function getDocname(link) {
    var href = link.getAttribute('href');

    if (!href) {
      return null;
    }

    var path = href.split('#')[0].split('?')[0];
    path = decodeURIComponent(path)
      .replace(/^\.\//, '')
      .replace(/\/$/, '')
      .replace(/\.html$/, '');

    return path || 'index';
  }

  function createIcon(svg) {
    var template = document.createElement('template');
    template.innerHTML = svg.trim();

    var icon = template.content.firstElementChild;
    if (!icon || icon.nodeName.toLowerCase() !== 'svg') {
      return null;
    }

    icon.classList.add('edh-search-result-icon');
    icon.setAttribute('aria-hidden', 'true');
    icon.setAttribute('focusable', 'false');
    return icon;
  }

  function decorateLink(link, icons) {
    if (link.dataset.edhSearchIcon) {
      return;
    }

    var svg = icons[getDocname(link)];
    if (!svg) {
      return;
    }

    var icon = createIcon(svg);
    if (!icon) {
      return;
    }

    if (link.firstChild && link.firstChild.nodeType === Node.TEXT_NODE) {
      link.firstChild.textContent = link.firstChild.textContent.trimStart();
    }

    link.prepend(icon);
    link.dataset.edhSearchIcon = 'true';
  }

  function decorateResults(root, icons) {
    root.querySelectorAll('li > a').forEach(function (link) {
      decorateLink(link, icons);
    });
  }

  function initSearchIcons() {
    var root = document.getElementById('search-results');
    if (!root) {
      return;
    }

    var contentRoot = document.documentElement.dataset.content_root || './';
    fetch(contentRoot + '_static/edh-search-icons.json')
      .then(function (response) {
        if (!response.ok) {
          throw new Error('Unable to load search icons');
        }
        return response.json();
      })
      .then(function (icons) {
        decorateResults(root, icons);
        new MutationObserver(function () {
          decorateResults(root, icons);
        }).observe(root, {childList: true, subtree: true});
      })
      .catch(function () {});
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSearchIcons);
  } else {
    initSearchIcons();
  }
}());
