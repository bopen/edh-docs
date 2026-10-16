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

(function () {
  var containerUrl = document.currentScript.getAttribute('data-matomo-container-url');

  function enableTracking() {
    var queue = window._paq = window._paq || [];
    queue.push(['setConsentGiven']);
  }

  function markCopyButtons() {
    document.querySelectorAll('button.copybtn:not([data-matomo-copy])').forEach(function (button) {
      button.setAttribute('data-matomo-copy', 'docs-code-snippet');
    });
    document.querySelectorAll('.copy-page-wrapper button.js-copy:not([data-matomo-copy])').forEach(function (button) {
      button.setAttribute('data-matomo-copy', 'docs-page-content');
    });
  }

  document.addEventListener('DOMContentLoaded', markCopyButtons);

  enableTracking();
  var dataLayer = window._mtm = window._mtm || [];
  dataLayer.push({'mtm.startTime': new Date().getTime(), event: 'mtm.Start'});

  var script = document.createElement('script');
  script.async = true;
  script.src = containerUrl;
  script.onload = enableTracking;
  document.head.appendChild(script);
}());
