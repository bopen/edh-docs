# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

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
    "sphinx_copybutton",
    "sphinx_togglebutton",
    "sphinx_collections",
    "nbsphinx",
]

copybutton_exclude = ".linenos, .gp, .go"

templates_path = ["_templates"]
exclude_patterns = [
    "_collections/edh-learning/README.md",
    "_collections/DESP-UserWorkflowService-Templates",
]

myst_enable_extensions = [
    "attrs_block",
]

collections = {
    "edh-learning": {
        "driver": "git",
        "source": "https://github.com/bopen/edh-learning.git",
    },
    "DESP-UserWorkflowService-Templates": {
        "driver": "git",
        "source": "https://github.com/SercoSPA/DESP-UserWorkflowService-Templates",
    },
    "insula-notebooks": {
        "driver": "copy_folder",
        "source": "./_collections/DESP-UserWorkflowService-Templates/EarthDataHub",
        "target": "insula-notebooks/",
    },
}
nbsphinx_execute = "never"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "shibuya"
html_title = "Earth Data Hub documentation"
html_favicon = "_static/favicon.ico"
html_static_path = ["_static"]
html_css_files = ["portal-frame.css"]
html_js_files = ["portal-frame.js"]
html_context = {
    "portal_url": "https://earthdatahub.destine.eu",
    "desp_platform_url": "https://platform.destine.eu",
}
html_theme_options = {
    "globaltoc_expand_depth": 1,
    "toctree_collapse": True,
    "toctree_maxdepth": 2,
    "toctree_titles_only": False,
}
