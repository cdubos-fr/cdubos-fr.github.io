# Copilot Instructions

Ce fichier fournit des directives pour générer du code ou du contenu cohérent avec ce dépôt.

## Contexte du projet
- Projet: Site vitrine personnel `cdubos.fr`
- Générateur: Zola (static site) – migration achevée depuis Sphinx
- Racine Zola: `source/` (contient `config.toml`, `content/`, `templates/`, `static/`)
- Templates: Tera (`base.html`, pages, sections) + composants CSS custom (hero, timeline, slices, cartes solutions, FAQ)
- Déploiement: GitHub Pages via `shalzz/zola-deploy-action`

## Structure essentielle
```
source/
  config.toml            # Configuration Zola
  content/               # Pages & sections (Markdown)
  templates/             # Templates Tera
  static/                # Assets copiés (favicon, pdf, og-image, CNAME...)
  static/style.css       # Styles custom (design système léger)
Justfile                 # Raccourcis build/serve
.github/workflows/ci.yaml
.pre-commit-config.yaml
README.md
```

## Commandes clés
- Build: `zola build` (alias `just build`)
- Serveur local auto-reload: `zola serve` (alias `just serve`)
- Hooks pre-commit (optionnel): `pre-commit install`

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

### Code / Style
Le dépôt est essentiellement du contenu Markdown + Tera + CSS.
- Éviter le JavaScript si une variante pure CSS suffit.
- Limiter les dépendances externes (autonomie du bundle).
- Préserver la cohérence des classes utilitaires existantes.

### Contenu Markdown
- Toujours commencer par un H1 unique
- Ton concis, orienté valeur / concret
- Préférer listes courtes, blocs de code minimalistes
- Pas de wrapping manuel des lignes
- Pour les liens internes: utiliser chemins relatifs cohérents

## Ajout de contenu
1. Créer le fichier sous `source/content/` (ex: `content/memo/nom.md`)
2. Mettre un `title` dans le front matter si nécessaire (sinon H1 utilisé)
3. Ajouter un H1 (`# Titre de la page`)
4. Sections: utiliser H2/H3 progressifs
5. Fournir exemples concrets (commandes shell, fragments config) plutôt que discours abstrait
6. Option discrète (noindex) pour pages internes: front matter `extra.noindex = true` + lien uniquement depuis pied de page si besoin

## CI / Déploiement
- Action unique: build + (sur `main`) déploiement vers `gh-pages` avec `shalzz/zola-deploy-action`
- Pull Requests: build only + link check (`CHECK_LINKS=true`)
- Variables d'env principales : `BUILD_DIR=source`, `PAGES_BRANCH=gh-pages`
- Possibilité future: ajouter un job distinct `zola check --drafts` ou Lighthouse (manuel)

## Dépendances
Runtime: Aucune (binaire Zola uniquement).
Dev tools:
```
pre-commit
commitizen
```
Tout ajout doit être justifié (éviter empilement d'outils).

## Bonnes pratiques de suggestions
- Ne pas introduire de frameworks web ou bundlers lourds
- Privilégier variantes CSS (utiliser :focus-visible, @media, prefers-color-scheme)
- Garder les classes semantiques (`slice`, `solution-card`, `timeline`, etc.)
- Pas de libs JS tiers pour accordéons (utiliser `<details>`)
- Ne pas toucher aux fichiers générés (`public/`)

## Tâches fréquentes automatisables
- Nouvelle page: créer fichier + vérifier navigation (si besoin d'un lien explicite)
- Ajouter un asset: placer dans `static/` (sera copié tel quel)
- Page confidentielle: `extra.noindex = true` et lien discret
- Ajustement SEO: modifier `<head>` dans `templates/base.html`

## Limitations connues
- Pas de tests automatiques de rendu HTML (possible d'ajouter `zola check` + grep liens cassés)
- Pas (encore) de génération automatisée d'images Open Graph
- Link checker simple dépend de Zola (peut manquer certains cas dynamiques)

## Idées futures (guidage pour suggestions Copilot)
- Job dédié `zola check` séparé pour liens
- Génération d'OG images dyn (ex: script headless)
- Ajout d'un mini audit accessibilité (liste focus, contrastes)
- Mode imprimable CSS minimal

---
Copilot: suivez ces directives pour rester cohérent avec l’intention du projet.
