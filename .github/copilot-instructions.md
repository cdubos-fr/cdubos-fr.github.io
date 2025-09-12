# Copilot Instructions

Ce fichier fournit des directives pour générer du code ou du contenu cohérent avec ce dépôt.

## Contexte du projet
- Projet: Site vitrine personnel `cdubos.fr`
- Générateur: Sphinx (build HTML statique)
- Sources: Dossiers Markdown/ReST dans `source/`
- Thème principal: `furo`
- Extensions Sphinx activées: myst-parser, sphinx-design, sphinx-copybutton, sphinx-inline-tabs, sphinx-sitemap, sphinxext-opengraph, sphinx-favicon (vérifier disponibilité), + extensions core (autodoc, todo, mathjax, viewcode, intersphinx, extlinks)

## Structure essentielle
```
source/
  index.md
  articles.md
  contact.md
  projets.md
  cv/ ...
  memo/ ...
  _static/ (assets, favicon, css)
  _templates/ (layout custom)
pyproject.toml (dépendances et outils de dev)
.github/workflows/ci.yaml (CI)
Justfile (commandes build / serveur)
```

## Commandes clés
- Construire: `sphinx-build source build -b html` (alias `just build`)
- Servir (local): `python -m http.server -d build`
- Préparer env: `pip install -e .[dev] && pre-commit install`

## Conventions
### Commits (Conventional Commits)
Format: `<type>(<scope>): <message>`
Types permis (prioritaires):
- feat, fix, docs, build, chore, refactor, perf, ci, style
Scopes suggérés: build, docs, ci, deps, content
Exemples:
- `feat(content): ajouter section expériences récentes`
- `docs(readme): préciser installation avec uv`
- `ci(build-docs): ajouter artefact zipped`

### Style Python
- Black (line-length 100)
- Flake8 (max-line-length 100, ignore E203)
- Mypy en mode modéré (pas strict = strict=false mais warnings activés)
- Imports: laisser pre-commit réordonner (reorder-python-imports)

### Sphinx / Contenu
- Préférer Markdown via myst-parser
- Utiliser `:::`, `:::` fences colon_fence pour blocs
- Ajouter ancres titres: myst_heading_anchors=3
- Badges design: `{bdg-primary}` etc. (voir exemples dans `conf.py`)

## Ajout de contenu
Lorsque Copilot propose une nouvelle page:
1. Créer le fichier `.md` dans le dossier approprié (ex: `source/memo/` pour notes techniques)
2. Ajouter un titre H1 unique (`# Titre`)
3. Éviter les phrases vides d’information; privilégier exemples concrets (code Python minimal ou commandes shell)
4. Pas de wrapping manuel des lignes (la longueur 100 est gérée côté outils)

## CI
Deux jobs:
- `lint-and-typecheck`: exécute pre-commit sur l’ensemble du repo
- `build-docs`: construit la doc et publie un artefact

Toute modification de build doit maintenir la compatibilité Python 3.12+ (voir `requires-python`).

## Dépendances
Runtime doc:
```
sphinx
furo
myst-parser
sphinx-copybutton
sphinx-design
sphinx-inline-tabs
sphinx-sitemap
sphinxext-opengraph
sphinx-favicon (si disponible)
```
Dev:
```
pre-commit
black
flake8
mypy
tox
bandit
commitizen
```

## Bonnes pratiques de suggestions
- Ne pas introduire de frameworks web (Django, FastAPI, etc.) sans justification -> le site est statique
- Ne pas proposer d’ajout de JavaScript lourd; privilégier le CSS existant
- Vérifier que toute extension Sphinx proposée est compatible avec Sphinx >=7.3
- Pour un snippet Python inséré dans la doc, utiliser des blocs markdown triple backticks avec `python`
- Ne pas toucher aux fichiers générés dans `build/`

## Tâches fréquentes automatisables
- Ajout d’une nouvelle page: créer fichier + lister dans `index.md` si navigation manuelle
- Mise à jour dépendance: ajuster version dans `pyproject.toml` puis relancer `pip install -e .[dev]`
- Ajout CI: cloner structure de job dans `.github/workflows/ci.yaml`

## Limitations connues
- Pas de test unitaire pour l’instant (site statique). Tests légers possibles: grep dans HTML produit.
- `sphinx-favicon` était auparavant géré via Nix; fallback possible: suppression si non installable.

## Idées futures (guidage pour suggestions Copilot)
- Ajouter un job de déploiement GitHub Pages
- Ajouter un script de validation HTML (link checker) via `sphinx-build -b linkcheck`
- Intégrer Ruff pour unifier flake8 + import ordre
- Ajouter un petit script de purge d’artefacts

---
Copilot: suivez ces directives pour rester cohérent avec l’intention du projet.
