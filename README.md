# cdubos.fr

Site vitrine personnel construit avec [Zola](https://www.getzola.org/).

## Structure

```
source/            # Racine du site Zola (config + contenu + templates + static)
	config.toml      # Configuration Zola
	content/         # Pages et sections markdown
	templates/       # Templates Tera
	static/          # Assets copiés tels quels (favicon, pdf...)
	sass|css         # Styles additionnels si besoin
Justfile           # Raccourcis de commandes (build / serve)
.pre-commit-config.yaml
```

## Prérequis

- Avoir Zola installé localement (binaire) : https://www.getzola.org/documentation/getting-started/installation/
- (Optionnel) `just` pour les commandes simplifiées : https://github.com/casey/just

## Installation (dev minimal)

Il n'y a plus de dépendances Python. Clone simplement le dépôt puis (optionnel) installe les hooks :

```bash
pre-commit install  # si pre-commit est déjà disponible globalement
```

## Construire le site

Avec `just` :
```bash
just build
```

Sans `just` :
```bash
zola build --root source
```

La sortie se trouve dans `public/`.

## Serveur de développement

Avec `just` :
```bash
just serve
```

Sans `just` :
```bash
zola serve --root source --open
```

## Déploiement

Le déploiement GitHub Pages est géré par l'action `shalzz/zola-deploy-action`. Sur `main`, elle :
1. Construit le site
2. Publie le contenu sur la branche `gh-pages`

Assure-toi que dans Settings > Pages, la source est bien `gh-pages` (root).

### Variables / personnalisation

- Custom domain : placer un fichier `static/CNAME` contenant le domaine (ex: `cdubos.fr`).
- Brouillons: ajouter `--drafts` via la variable d'env `BUILD_FLAGS` si nécessaire (non activé par défaut en prod).

## Qualité / hooks

Le dépôt conserve des hooks basiques (trailing whitespace, fin de fichier, YAML, etc.) + commitizen pour formater les messages de commit.

## Migration (historique)

Le site était auparavant généré avec Sphinx (thème furo). Tout l'écosystème Python a été supprimé pour simplifier la maintenance.

## Commandes utiles

```bash
just build     # build production
just serve     # serveur de dev auto-reload
just clean     # (si défini) nettoyer la sortie
```

## Licence

Voir le fichier `LICENSE` (MIT ou autre selon le dépôt).

---
Suggestions / améliorations futures :
- Ajout d'un job de vérification de liens (`zola check`)
- Audit de performance Lighthouse (manuel)
- Génération d'images Open Graph automatiques
