set shell := ["zsh", "-uc"]

devenv:
    tox devenv -e devenv .venv
    pre-commit install

build:
    sphinx-build source build -b html
