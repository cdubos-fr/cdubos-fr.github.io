+++
title = "Plateforme MMS (Mission Management Service) | Loft Orbital"
date = "2023-12-01"
+++

_Période : Décembre 2023 – Avril 2025_

**Organisation :**
- **Équipe :** 1 Lead Tech, 6 Développeurs (Contexte international : France /
USA).
- **Rôle :** Software Engineer & Platform Specialist.
- **Méthode :** Agile (Scrum/Kanban) en environnement multi-fuseaux horaires

**Stack Technique :**
- **Langage & Core :** Python (3.9 à 3.13), Django, Pydantic.
- **Data & Format :** Pandas, GeoParquet (Données géospatiales).
- **Interfaces :** Graphene (GraphQL), Architecture micro-services.
- **Infra & Ops :** GCP, Kubernetes, GitLab CI, Docker.
- **Developer Experience :** MyPy, Pytest, Black/isort, Pylint, Pre-Commit, JupyterLab/Notebook, Sphinx.

**Contexte :** Loft Orbital propose des services d'exploitation de données satellitaires
"as-a-service". L'équipe MMS est responsable de la chaîne logicielle orchestrant la
réception, le traitement et la restitution automatisée des données provenant des satellites en
orbite.

**Mission :** Développer de nouvelles fonctionnalités au sein de l'équipe MMS (Mission Management Service), participé à l'orchestration de la chaîne logicielle gérant la réception, le traitement et la restitution automatisée des données satellitaires, garantir la stabilité et la scalabilité de la plateforme existante.

**Réalisations :**
- **Ingénierie d'Observabilité :** Conception et implémentation d'une librairie interne d'instrumentation basée sur OpenTelemetry. Ce socle a permis d'assurer un monitoring fin, le traçage distribué et la santé des services en production.
- **Standardisation (Framework Métier) :** Développement d'un framework interne pour simplifier et homogénéiser l'écriture des workflows de traitement de données satellitaires, permettant aux équipes métier de se concentrer sur la logique de traitement plutôt que sur l'infrastructure.
- **Industrialisation & Conteneurisation :** Optimisation de la "Software Supply Chain" via la création de conteneurs Docker haute performance et la maintenance de templates de projets (Scaffolding) pour garantir l'uniformité des développements applicatifs.
- **Évolutions CI/CD :** Modernisation des pipelines GitLab CI pour supporter les montées de versions Python (jusqu'à 3.13) et répondre aux exigences de déploiement continu sur GCP/Kubernetes.
- **Traitement de Données (EarthDaily) :** Mise en œuvre de pipelines de traitement spécifiques pour des clients stratégiques, intégrant des contraintes de volume et de précision géospatiale.
- **Coordination Internationale :** Garantie de la cohérence technique entre les équipes françaises et américaines, assurant la continuité du développement malgré les contraintes de décalage horaire.
