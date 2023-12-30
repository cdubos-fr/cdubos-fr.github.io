# Python

## Liens

- [Le Blue book](https://lyz-code.github.io/blue-book/)
- [aide-mémoire Python](https://www.pythoncheatsheet.org/)
- [Python Array API standard](https://data-apis.org/array-api/2022.12/)

## Installation de python

### Windows

- [Python.org](https://www.python.org/downloads/)

### Unix
- [deadsnakes](https://github.com/deadsnakes), un repo linux pour les versions de python
  - mise en place du repo:
    > ```bash
    > $ sudo add-apt-repository ppa:deadsnakes/ppa
    > ```
  - configuration des alias:
    > ```bash
    > $ sudo apt install python3-pip python-is-python3
    > ```
  - Installation d'une version de python:
    > ```bash
    > $ sudo apt install python3.X python3.X-distutils python3.X-dev
    > ```
  - pour changer la version de python par défaut:
    > ```bash
    > $ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.X 1
    > $ sudo update-alternatives --config python
    > ```
- [pyenv](https://github.com/pyenv/pyenv), un outils de management des versions de pythons:
  - [Pre-requis](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)
  - [Téléchargement](https://github.com/pyenv/pyenv#basic-github-checkout)
  - [Configuration](https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv)
  - [Usage](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)
  - Installation d'une version de python:
    -  `$ pyenv install 3.X`
    - configuration global `$ pyenv global 3.X`
    - configuration local `$ pyenv local 3.X`

### Dependencies et Venv manager

- [Pip](https://pypi.org/project/pip/)
- [Pipx](https://pipx.pypa.io/stable/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)
- [Poetry](https://python-poetry.org/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Pip-tools](https://github.com/jazzband/pip-tools)
- [PDM](https://pdm-project.org/latest/)
- [Hatchling](https://hatch.pypa.io/latest/)

### Packaging

- [Flit](https://flit.pypa.io/en/stable/)
- [SetupTools](https://setuptools.pypa.io/en/latest/)
  - [SetupTools-SCM](https://setuptools-scm.readthedocs.io/en/latest/)

### Test

- [Pytest](https://docs.pytest.org/en/7.2.x/): Test unitaire
- [Hypothesis](https://hypothesis.readthedocs.io/en/latest/): Génération de donnée
- [Behave](https://behave.readthedocs.io/en/stable/): Behavior Driven Development

### Qualité de code

- [Xenon](https://readthedocs.org/projects/xenon/): Complexité cyclomatique
- [Flake8](https://flake8.pycqa.org/en/latest/): Linter
- [Doc Cov](https://pypi.org/project/doc-cov/): Couverture de la documentation
- [bandit](https://bandit.readthedocs.io/en/latest/): Analyse static de code
- [autopep8](https://pypi.org/project/autopep8/): Formatter
- [Mypy](https://mypy.readthedocs.io/en/stable/): Validation des annotations de type
- [Ruff](https://beta.ruff.rs/docs/): Linter with autofix
- [Black](https://pypi.org/project/black/): Formatter
- [YAPF](https://github.com/google/yapf): Formatter
- [reorder-python-import](https://github.com/asottile/reorder-python-imports)
- [pyupgrade](https://github.com/asottile/pyupgrade)

### Outils

- [tox](https://tox.wiki/en/latest/): Automotisation
- [Nox](https://nox.thea.codes/en/stable/): Automatisation
- [Pre-Commit](https://pre-commit.com/)
- [Commitizen](https://commitizen-tools.github.io/commitizen/): gestion des commits et des tags selon le [Convential Commit](https://www.conventionalcommits.org/en/v1.0.0/)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/): Génération de projet
- [jupyter](https://docs.jupyter.org/en/latest/): Environnement intéractif et reproductible

### Documentation

- [Sphinx](https://www.sphinx-doc.org/en/master/): générateur de Documentation
- [Furo](https://pradyunsg.me/furo/): Theme Sphinx
- [Mkdocs](https://www.mkdocs.org/) & [Mkdocstring](https://mkdocstrings.github.io/): generateur de documentation
- [Mkdocs-material](https://squidfunk.github.io/mkdocs-material/getting-started/): theme Mkdocs

### Développement Web

- [FastApi](https://fastapi.tiangolo.com/): Framework WEB Asynchrone pour la réalisation d'API REST
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Falcon](https://falcon.readthedocs.io/en/stable/)
- [Sanic](https://sanic.dev/en/)
- [Django](https://www.djangoproject.com/): Framework dévelopment WEB
  - [Django-Ninja](https://django-ninja.dev/): Extension django pour le rendre plus moderne

#### Web Server

- [Gunicorn](https://gunicorn.org/)
- [Uvicorn](https://www.uvicorn.org/)
- [HyperCorn](https://pgjones.gitlab.io/hypercorn/)

#### GraphQL

- [Graphene](https://graphene-python.org/)
- [Strawberry](https://strawberry.rocks/)

### Command line interface

- [Click](https://click.palletsprojects.com/en/8.1.x/): Pour la création de CLI
- [Typer](https://typer.tiangolo.com/): Pour la création de CLI, build autour de click
- [Click-completion](https://github.com/click-contrib/click-completion): pour l'autocompletion avec click

### Base de donnée

- [SqlAlchemy](https://www.sqlalchemy.org/): ORM
- [SqlModel](https://sqlmodel.tiangolo.com/): Wrapper autour de sqlalchemy et pydantic

### Data

- [Numpy](https://numpy.org/): LA librairie de calcule scientifique
- [Scipy](https://scipy.org/): extension numpy
- [Pandas](https://pandas.pydata.org/): Traitement de donnée en lot
- [Dask](https://www.dask.org/): Orchestration et calcule distribué

### Machine learning

- [Scikit-learn](https://scikit-learn.org/stable/): librairie de machine learning
- [Pytorch](https://pytorch.org/): framework deeplearning
- [Keras](https://keras.io/): framework deeplearning
- [Tensorflow](https://www.tensorflow.org/): framework deeplearning

### Validation de donnée

- [Pydantic](https://docs.pydantic.dev/): Validation de donnée et Settings management

### Templating

- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)
