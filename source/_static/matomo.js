// Copyright 2026 European Union
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Mirrors the webportal's useTrackingConsent and useMatomo hooks.
(function () {
  var TRACKING_CONSENT_STORAGE_KEY = 'edh.trackingConsent';

  var containerUrl = document.currentScript.getAttribute('data-matomo-container-url');

  function getStoredTrackingConsent() {
    try {
      var storedConsent = window.localStorage.getItem(TRACKING_CONSENT_STORAGE_KEY);
      return storedConsent === 'accepted' || storedConsent === 'denied' ? storedConsent : null;
    } catch (error) {
      return null;
    }
  }

  function storeTrackingConsent(consent) {
    try {
      window.localStorage.setItem(TRACKING_CONSENT_STORAGE_KEY, consent);
    } catch (error) {
      // Consent still applies for the current page when storage is unavailable.
    }
  }

  function applyMatomoTrackingConsent(consent) {
    var queue = window._paq = window._paq || [];

    if (consent === 'accepted') {
      queue.push(['setConsentGiven']);
      return;
    }

    queue.push(['forgetConsentGiven']);
    queue.push(['deleteCookies']);
  }

  // Matomo Tag Manager creates the pageview tracker while the container loads,
  // so reapply stored consent after load to reach the live tracker.
  function reapplyStoredConsent() {
    if (getStoredTrackingConsent() === 'accepted') {
      applyMatomoTrackingConsent('accepted');
    }
  }

  function loadMatomoContainer() {
    var dataLayer = window._mtm = window._mtm || [];
    dataLayer.push({'mtm.startTime': new Date().getTime(), event: 'mtm.Start'});

    var script = document.createElement('script');
    script.async = true;
    script.src = containerUrl;
    script.onload = reapplyStoredConsent;
    document.head.appendChild(script);
  }

  function openCookieSettings() {
    var dialog = document.querySelector('[data-cookie-settings]');
    var trackingSwitch = dialog.querySelector('[data-cookie-settings-tracking]');
    var trackingLabel = dialog.querySelector('[data-cookie-settings-tracking-label]');

    function saveTrackingConsent(isTrackingCookiesEnabled) {
      var consent = isTrackingCookiesEnabled ? 'accepted' : 'denied';

      dialog.close();
      applyMatomoTrackingConsent(consent);
      storeTrackingConsent(consent);
    }

    trackingSwitch.addEventListener('change', function () {
      trackingLabel.textContent = trackingSwitch.checked ? 'Enabled' : 'Disabled';
    });
    dialog.querySelector('[data-cookie-settings-deny]').addEventListener('click', function () {
      saveTrackingConsent(false);
    });
    dialog.querySelector('[data-cookie-settings-accept]').addEventListener('click', function () {
      saveTrackingConsent(true);
    });
    dialog.querySelector('[data-cookie-settings-save]').addEventListener('click', function () {
      saveTrackingConsent(trackingSwitch.checked);
    });
    document.addEventListener('keydown', function (event) {
      if (dialog.open && event.key === 'Escape' && !event.isComposing) {
        event.preventDefault();
        saveTrackingConsent(trackingSwitch.checked);
      }
    });
    dialog.addEventListener('cancel', function (event) {
      event.preventDefault();
    });

    dialog.showModal();
    dialog.focus();
  }

  function markCopyButtons() {
    document.querySelectorAll('button.copybtn:not([data-matomo-copy])').forEach(function (button) {
      button.setAttribute('data-matomo-copy', 'docs-code-snippet');
    });
    document.querySelectorAll('.copy-page-wrapper button.js-copy:not([data-matomo-copy])').forEach(function (button) {
      button.setAttribute('data-matomo-copy', 'docs-page-content');
    });
  }

  window.addEventListener('DOMContentLoaded', markCopyButtons);

  var storedConsent = getStoredTrackingConsent();

  if (storedConsent) {
    applyMatomoTrackingConsent(storedConsent);
  }

  if (containerUrl) {
    loadMatomoContainer();
  }

  if (!storedConsent) {
    openCookieSettings();
  }
}());
