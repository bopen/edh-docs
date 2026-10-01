# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
from pathlib import Path

sys.path.append(str((Path(__file__).parent / "_ext").resolve()))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "edh-docs"
copyright = "2026, bopen"
author = "bopen"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

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
    "sphinx_llm.txt",
    "edh_badges",
    "edh_icons",
    "edh_llms_markdown",
]

copybutton_prompt_text = r">>> |\.\.\. "
copybutton_prompt_is_regexp = True

templates_path = ["_templates"]
exclude_patterns = [
    "_collections/edh-learning/README.md",
    "_collections/DESP-UserWorkflowService-Templates",
    "_collections/insula-notebooks/demo-*",
]

myst_enable_extensions = [
    "attrs_block",
]

collections = {
    "edh-learning": {
        "driver": "git",
        "source": "https://github.com/bopen/edh-learning.git",
        "clean": False,
        "final_clean": False,
    },
    "DESP-UserWorkflowService-Templates": {
        "driver": "git",
        "source": "https://github.com/SercoSPA/DESP-UserWorkflowService-Templates",
        "clean": False,
        "final_clean": False,
    },
    "insula-notebooks": {
        "driver": "copy_folder",
        "source": "./_collections/DESP-UserWorkflowService-Templates/EarthDataHub/",
        "target": "insula-notebooks/",
        "clean": True,
        "final_clean": False,
    },
}
nbsphinx_execute = "never"
nbsphinx_codecell_lexer = "ipython3"
nbsphinx_prolog = r"""
{% set doc = env.docname %}

{% if doc.startswith('_collections/edh-learning') %}

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

{% if doc.startswith('_collections/insula-notebooks') %}

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

html_baseurl = "https://earthdatahub.destine.eu/docs/"
html_theme = "shibuya"
html_title = "Earth Data Hub documentation"
html_copy_source = False
html_favicon = "_static/favicon.ico"
html_static_path = ["_static"]
sitemap_excludes = ["genindex.html", "search.html"]
sitemap_url_scheme = "{link}"
html_css_files = [
    "headings.css",
    "portal-frame.css",
    "cards.css",
    "notebook-gallery.css",
    "badges.css",
    "search-icons.css",
]
html_js_files = ["portal-frame.js", "search-icons.js"]
html_context = {
    "portal_url": "https://earthdatahub.destine.eu",
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
}

# -- Options for LLMs (sphinx-llm) -------------------------------------------
# https://github.com/NVIDIA/sphinx-llm#configuration

llms_txt_full_build = True
llms_txt_suffix_mode = "replace"
llms_txt_exclude = ["404"]
