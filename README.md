# cdubos.fr

Site vitrine personnel construit avec Sphinx.

## Installation (environnement local hors Nix)

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev]
pre-commit install
```

## Construction du site

```bash
just build
```
(équivalent) :
```bash
sphinx-build source build -b html
```

## Lancer un serveur local

```bash
just run-server
# ou
python -m http.server -d build
```

## CI

La CI GitHub Actions installe désormais les dépendances via `pyproject.toml` (sans Nix) et construit la documentation.

## Notes

- Les hooks pre-commit définissent les versions exactes de certains outils.
- `sphinx-favicon` est référencé ; si non disponible sur PyPI, envisager un vendor local ou le retirer.
