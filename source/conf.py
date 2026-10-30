# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import urllib
from pathlib import Path

from docutils import nodes
from sphinx_collections.api import register_driver

sys.path.append(str((Path(__file__).parent / "_ext").resolve()))

from git_pull_driver import GitPullDriver

register_driver("git_pull", GitPullDriver)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "edh-docs"
copyright = "2026, European Union"
author = "B-Open"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

BASE_URL = os.getenv("BASE_URL", "https://earthdatahub.destine.eu").rstrip("/")
DOCUMENTATION_PORTAL_URL = os.getenv(
    "DOCUMENTATION_PORTAL_URL", "https://earthdatahub.destine.eu/docs"
).rstrip("/")

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_sitemap",
    "sphinx_copybutton",
    "sphinx_togglebutton",
    "sphinx_collections",
    "nbsphinx",
    "notfound.extension",
    "sphinxcontrib.youtube",
    "sphinx_iconify",
    "sphinx_substitution_extensions",
    "sphinx_llm.txt",
    "edh_badges",
    "edh_icons",
    "edh_llms_markdown",
]

copybutton_prompt_text = r">>> |\.\.\. "
copybutton_prompt_is_regexp = True

templates_path = ["_templates"]
exclude_patterns = ["_collections"]

myst_enable_extensions = ["attrs_block", "substitution"]

myst_substitutions = {
    "stac_api_url": f"{BASE_URL}/api/stac/v1",
    "datastore_host": os.getenv("DATASTORE_HOST", "api.earthdatahub.destine.eu"),
    "datastore_internal_host": os.getenv(
        "DATASTORE_INTERNAL_HOST", "data.earthdatahub.destine.eu"
    ),
    "private_test_dataset_path": "/"
    + os.getenv("PRIVATE_TEST_DATASET_PATH", "/private/test-dataset-v1.zarr").lstrip(
        "/"
    ),
    "info_icon": "info" if "sphinx_llm_markdown" in tags else "{octicon}`info`",  # noqa: F821
}

collections = {
    "edh-learning": {
        "driver": "git_pull",
        "source": "https://github.com/bopen/edh-learning.git",
        "clean": False,
        "final_clean": False,
    },
    "DESP-UserWorkflowService-Templates": {
        "driver": "git_pull",
        "source": "https://github.com/SercoSPA/DESP-UserWorkflowService-Templates",
        "clean": False,
        "final_clean": False,
    },
    "edh-learning-notebooks": {
        "driver": "copy_folder",
        "source": "./_collections/edh-learning/notebooks/",
        "target": "../notebooks/edh-learning/",
        "clean": True,
        "final_clean": False,
    },
    "insula-notebooks": {
        "driver": "copy_folder",
        "source": "./_collections/DESP-UserWorkflowService-Templates/EarthDataHub/",
        "target": "../notebooks/insula-code-lab/",
        "ignore": ["demo-*"],
        "clean": True,
        "final_clean": False,
    },
}
# The parallel sphinx-llm build must reuse these files: re-fetching would wipe them
# mid-build and crash it (alternative: llms_txt_build_parallel = False, but slower)
if "sphinx_llm_markdown" in tags:  # noqa: F821
    collections = {}
nbsphinx_execute = "never"
nbsphinx_codecell_lexer = "ipython3"
nbsphinx_prolog = r"""
{% set doc = env.docname %}

{% if doc.startswith('notebooks/edh-learning/') %}

.. note::
   To run this notebook locally, follow the setup instructions in the `GitHub repository <https://github.com/bopen/edh-learning>`_.

{% endif %}

.. |download-link-opening| raw:: html

   <span><a href="{{ doc.split('/')[-1] | e }}.ipynb" download>

.. |download-link-closing| raw:: html

   </a></span>

.. |insula-link-opening| raw:: html

   <span><a href="https://code.insula.destine.eu/hub/user-redirect/lab/tree/platform-lab/EarthDataHub/{{ doc.split('/')[-1] | e }}.ipynb" target="_insula">

.. |insula-link-closing| raw:: html

   </a></span>

{% if doc.startswith('notebooks/insula-code-lab/') %}

.. container:: buttons edh-notebook-actions

   |download-link-opening| :octicon:`download` Download notebook |download-link-closing| |insula-link-opening| :octicon:`terminal` Run this notebook |insula-link-closing|

{% else %}

.. container:: buttons edh-notebook-actions

   |download-link-opening| :octicon:`download` Download notebook |download-link-closing|

{% endif %}

----
"""

linkcheck_ignore = [
    r"https://data\.earthdatahub\.destine\.eu/private/.*\.zarr",
]
linkcheck_anchors_ignore_for_url = [
    r"https://earthdatahub\.destine\.eu/quota-api-keys",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_baseurl = f"{DOCUMENTATION_PORTAL_URL}/"
html_theme = "shibuya"
html_title = "Earth Data Hub documentation"
html_copy_source = False
html_favicon = "_static/favicon.ico"
html_static_path = ["_static"]
sitemap_excludes = ["genindex.html", "search.html"]
sitemap_url_scheme = "{link}"
html_css_files = [
    "fonts.css",
    "headings.css",
    "portal-frame.css",
    "cards.css",
    "notebook-gallery.css",
    "badges.css",
    "search-icons.css",
    "cookie-settings.css",
]
matomo_container_url = os.getenv("MATOMO_TAG_MANAGER_CONTAINER_URL", "").strip()
html_js_files = [
    "portal-frame.js",
    "search-icons.js",
    (
        "matomo.js",
        {"data-matomo-container-url": matomo_container_url, "priority": 400},
    ),
]

html_context = {
    "portal_url": BASE_URL,
    "desp_platform_url": "https://platform.destine.eu",
    "source_type": "github",
    "source_user": "bopen",
    "source_repo": "edh-docs",
    "source_docs_path": "/source/",
}
html_sidebars = {
    "**": [
        "sidebars/localtoc.html",
        "sidebars/carbon-ads.html",
        "sidebars/ethical-ads.html",
    ],
}
html_theme_options = {
    "globaltoc_expand_depth": 1,
    "toctree_collapse": True,
    "toctree_maxdepth": 2,
    "toctree_titles_only": False,
    "open_in_perplexity": True,
}

# -- Options for LLMs (sphinx-llm) -------------------------------------------
# https://github.com/NVIDIA/sphinx-llm#configuration

llms_txt_description = "The Earth Data Hub documentation provides an overview of the platform and guides on accessing data, core concepts, notebooks, FAQs, and troubleshooting."
llms_txt_full_build = True
llms_txt_suffix_mode = "replace"
llms_txt_exclude = ["404", "index"]
# Meta nodes (notebook descriptions, see edh_llms_markdown) have no Markdown equivalent
llms_txt_suppress_unknown_node_warnings = ["meta"]
markdown_http_base = html_baseurl


def edh_url_with_camefrom_role(name, rawtext, text, lineno, inliner, options=None):
    """Generates configurable URL to EDH with a came_from parameter back to documentation portal.

    Syntax:
    {edh_url_with_camefrom}`Link Text </aaa/bb/ccc>`
    Or just:    {edh_url_with_camefrom}`/aaa/bb/ccc`
    """

    options = options or {}

    # Extract the current document name (e.g., 'folder/page')
    env = inliner.document.settings.env
    docname = env.docname
    current_page = f"{docname}.html"

    # Read the base URL from the environment variable.
    base_url = BASE_URL

    # Parse the text (Link Text <path>)
    if "<" in text and ">" in text:
        link_text, path = text.split("<")
        link_text = link_text.strip()
        path = path.strip(">")
    else:
        # Fallback if the user just types {edh_url}`/aaa/bb/ccc`
        link_text = text
        path = text

    # Ensure the path starts with a slash
    path = path.strip()
    if not path.startswith("/"):
        path = "/" + path

    # Safely URL-encode the current page name
    encoded_page = urllib.parse.quote(f"{DOCUMENTATION_PORTAL_URL}/{current_page}")

    # Construct the final URL
    separator = "&" if "?" in base_url else "?"
    full_url = f"{base_url}{path}{separator}came_from={encoded_page}"

    # Create the docutils reference node
    node = nodes.reference(rawtext, link_text, refuri=full_url, **options)
    return [node], []


def edh_url_role(name, rawtext, text, lineno, inliner, options=None):
    """Generates configurable URL to EDH.

    Syntax:
    {edh_url}`Link Text </aaa/bb/ccc>`
    Or just:    {edh_url}`/aaa/bb/ccc`
    """

    options = options or {}

    # Read the base URL from the environment variable.
    base_url = os.getenv("BASE_URL", "https://earthdatahub.destine.eu").rstrip("/")

    # Parse the text (Link Text <path>)
    if "<" in text and ">" in text:
        link_text, path = text.split("<")
        link_text = link_text.strip()
        path = path.strip(">")
    else:
        # Fallback if the user just types {edh_url}`/aaa/bb/ccc`
        link_text = text
        path = text

    # Ensure the path starts with a slash
    path = path.strip()
    if not path.startswith("/"):
        path = "/" + path

    # Construct the final URL
    full_url = f"{base_url}{path}"

    # Create the HTML anchor node
    node = nodes.reference(rawtext, link_text, refuri=full_url, **options)
    return [node], []


def setup(app):
    app.add_role("edh_url", edh_url_role)
    app.add_role("edh_url_with_camefrom", edh_url_with_camefrom_role)
