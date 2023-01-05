# -- Project information -----------------------------------------------------
project = 'cdubos-vitrine'
copyright = '2023, Clément Dubos'
author = 'Clément Dubos'

# -- Configuration -----------------------------------------------------------
extensions = ['myst_parser', 'sphinx_design']
myst_enable_extensions = ['colon_fence']
templates_path = ['_templates']
exclude_patterns = []
language = 'fr'

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Theme -------------------------------------------------------------------
DARK_COLOR = '#3BD16F'
LIGHT_COLOR = '#0E7322'

html_theme = 'furo'
html_static_path = ['_static']
html_show_sphinx = True

html_logo = '_static/me.jpg'
html_title = 'Clément Dubos'

html_theme_options = {
    'dark_css_variables': {
        'color-brand-primary': DARK_COLOR,
        'color-brand-content': DARK_COLOR,
    },
    'light_css_variables': {
        'color-brand-primary': LIGHT_COLOR,
        'color-brand-content': LIGHT_COLOR,
    },
}

html_css_files = [
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css',
]
