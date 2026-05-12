+++
title = "Framework Copernicus - Projet EOPF-CPM | Extia (Client : ESA x CSGroup)"
date = 2021-12-01
+++

_Période : Décembre 2021 – Juillet 2022_

**Repository :** [EOPF-CPM](https://gitlab.eopf.copernicus.eu/cpm/eopf-cpm)

**Organisation :**
- **Équipe :** 1 Scrum Master, 5 Développeurs, 1 Lead Tech.
- **Rôle :** Lead Tech & Expert Python.
- **Méthode :** SAFe

**Stack Technique :**
- **Langage & Core :** Python 3.9, Dask, Numpy, Xarray.
- **Data & Format :** Zarr, Datasets multi-dimensionnels (NetCDF-like).
- **Interfaces :** Click, FastAPI.
- **Infra & Ops :** GitLab CI, Docker, Kubernetes.
- **Developer Experience :** MyPy, Pytest / Hypothesis, Bandit, Safety, Pre-Commit, Black, Pylint / Flake8, Sphinx, JupyterLab / Notebook.

**Contexte :** Conception ex-nihilo du EOPF-CPM (Earth Observation Processing Framework - Core Python Modules) pour l'ESA. L'enjeu était de standardiser l'exploitation des données massives issues des satellites Sentinel (Copernicus) via un framework unique capable d'abstraire la complexité des formats de données et des infrastructures de calcul.

**Mission :** Direction technique du projet, définition de l'architecture du framework et garant
de la qualité logicielle. Livraison d'un socle technique robuste aujourd'hui utilisé pour la nouvelle génération de chaînes de traitement de données d'observation de la Terre (Earth Observation) au niveau européen.

**Réalisations :**
- **Architecture & Abstraction :** Conception et implémentation de la couche d'abstraction logicielle permettant de manipuler des données hétérogènes de manière homogène. Définition des standards de développement pour garantir l'interopérabilité des briques de traitement.
- **Performance & Big Data :** Architecture du moteur de calcul basé sur Dask pour la parallélisation des traitements de données géospatiales. Optimisation de la gestion mémoire et des graphes de tâches pour le traitement de fichiers volumineux.
- **Leadership Technique :** Direction de l'équipe de développement (5 personnes), arbitrages technologiques critiques et mentorat sur les problématiques de performance Python et d'architecture distribuée, mise en œuvre des meilleures pratiques Python.
- **Qualité & Robustesse :** Garant de la maintenabilité du code (couverture de tests, typage strict avec MyPy, documentation technique exhaustive). Mise en place de pipelines CI/CD complexes pour valider les performances à chaque release.
