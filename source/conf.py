import os

# -- Project information -----------------------------------------------------
project = "cdubos-vitrine"
copyright = "2023, Clément Dubos"
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
    "sphinx_tags",
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

html_logo = "_static/icon.svg"
html_title = "Clément Dubos"

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
]

FAVICON_DIR = "favicon"

favicons = [{"href": f"{FAVICON_DIR}/{file}"} for file in os.listdir(f"_static/{FAVICON_DIR}")]


# -- Tags  -------------------------------------------------------------------
tags_create_tags = True
tags_create_badges = True
tags_extension = ["md", "rst"]
tags_badge_colors = {
    "Python": "primary",
    "GithubAction": "secondary",
    "GitlabCI": "secondary",
    "Pydantic": "info",
    "Pulumi": "warning",
    "Azure": "danger",
    "AWS": "danger",
    "*": "dark",
}
# Python, C#, Java, Jenkins, Scala, Spark, ElasticStack, GitlabCI,
# GithubAction, Pulumi, Django, FastAPI, PostGres, Dask, Terraform, Azure,
# AWS, Pydantic

# Badges values
# 'primary'
# 'secondary'
# 'success'
# 'info'
# 'warning'
# 'danger'
# 'light'
# 'dark'
