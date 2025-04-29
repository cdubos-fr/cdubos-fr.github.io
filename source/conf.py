import os
import time

# Fix for incorrect SOURCE_DATE_EPOCH Nix env'
os.environ["SOURCE_DATE_EPOCH"] = str(int(time.time()))

# -- Project information -----------------------------------------------------
project = "cdubos-vitrine"
copyright = "2024, Clément Dubos"
author = "Clément Dubos"

# -- Configuration -----------------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx_design",
    "furo.sphinxext",
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "sphinx_favicon",
    "sphinx_sitemap",
    "sphinxext.opengraph",
]
myst_enable_extensions = ["colon_fence", "deflist"]
myst_heading_anchors = 3

templates_path = ["_templates"]
exclude_patterns: list[str] = []
language = "fr"

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

# -- Theme -------------------------------------------------------------------
DARK_COLOR = "#3BD16F"
LIGHT_COLOR = "#0E7322"

html_theme = "furo"
html_static_path = ["_static"]
html_show_sphinx = True
html_show_sourcelink = False

html_logo = "_static/icon.svg"
html_title = "Clément Dubos | Développeur logiciel"
html_short_title = "Clément Dubos"
html_description = (
    "Développeur logiciel, expert Python, "
    "j'accompagne les entreprises dans leur besoin du quotidien."
)
sitemap_url_scheme = "{link}"
ogp_site_url = html_baseurl = "https://cdubos.fr/"
ogp_description_length = 300
ogp_site_name = "Clément Dubos - Développeur logiciel"
ogp_image = "_static/icon.svg"

html_theme_options = {
    "dark_css_variables": {
        "color-brand-primary": DARK_COLOR,
        "color-brand-content": DARK_COLOR,
    },
    "light_css_variables": {
        "color-background-primary": "#eeebee",
        "color-background-secondary": "#D0D0D0",
        "color-brand-primary": LIGHT_COLOR,
        "color-brand-content": LIGHT_COLOR,
    },
}

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css",
    "css/custom.css",
]

FAVICON_DIR = "favicon"

favicons = [{"href": f"{FAVICON_DIR}/{file}"} for file in os.listdir(f"_static/{FAVICON_DIR}")]


# {bdg}`plain badge`
# {bdg-primary}`primary`, {bdg-primary-line}`primary-line`
# {bdg-secondary}`secondary`, {bdg-secondary-line}`secondary-line`
# {bdg-success}`success`, {bdg-success-line}`success-line`
# {bdg-info}`info`, {bdg-info-line}`info-line`
# {bdg-warning}`warning`, {bdg-warning-line}`warning-line`
# {bdg-danger}`danger`, {bdg-danger-line}`danger-line`
# {bdg-light}`light`, {bdg-light-line}`light-line`
# {bdg-dark}`dark`, {bdg-dark-line}`dark-line`
