(function () {
  function initPortalFrame() {
    var openMenu = null;

    function setOpen(menu, open) {
      menu.panel.hidden = !open;
      menu.button.setAttribute('aria-expanded', open ? 'true' : 'false');
      openMenu = open ? menu : null;
    }

    function closeOpenMenu() {
      if (openMenu) {
        setOpen(openMenu, false);
      }
    }

    document.querySelectorAll('[data-portal-menu]').forEach(function (root) {
      var menu = {
        root: root,
        button: root.querySelector('[data-portal-menu-button]'),
        panel: root.querySelector('[data-portal-menu-panel]'),
      };

      if (!menu.button || !menu.panel) {
        return;
      }

      menu.button.addEventListener('click', function () {
        var wasOpen = openMenu === menu;

        closeOpenMenu();

        if (!wasOpen) {
          setOpen(menu, true);
        }
      });
    });

    document.addEventListener('click', function (event) {
      if (openMenu && !openMenu.root.contains(event.target)) {
        closeOpenMenu();
      }
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') {
        closeOpenMenu();
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPortalFrame);
  } else {
    initPortalFrame();
  }
}());
