# 💼 Expériences
```{tags} Python, C#, Java, Jenkins, Scala, Spark, ElasticStack, GitlabCI, GithubAction, Pulumi, Django, FastAPI, PostGres, Dask, Terraform, Azure, AWS, Pydantic
```

## Extia
🗓️ Fev. 2020 -> Aujourd'hui
::::{tab-set}
:::{tab-item} Lead. Tech
```{tags} Python, GithubAction, Pulumi, PostGres, Azure, AWS, Pydantic, Pulumi
```
```{dropdown} Réfentiel de donnée

**Contexte**

L'entreprise Bimpli est un aggrégateur de service pour les salariés.
Dans un but de centralisation, qualification et uniformisation de la donnée, celle-ci a souhaité mettre en place un système de management de la donnée (MdM) dans un ecosystème AWS.

**Réalisation**

Garantir la qualité du code
- Mise en place de bonne pratique de code
- Architecture logiciel
- Mise en place Test unitaire, linter, analyse statique de sécurité ...
- Utilisation de localstack pour les tests
Réalisation des briques devops pour le déroulement du projet
- Règle de protection des branches
- CI (Test unitaire + coverage, linter, sécurité ...)
- CD: déploiement selon environement et branche
- github action, reusable workflow, ...
Mise en place de l'infrastructure sous la supervision de l'équipe infra
- Pulumi
- mise en place d'un framework d'organisation pour l'IaC
- Ecriture et test de l'ensemble des stacks
```
:::

:::{tab-item} Expert/Lead. Python
```{tags} Python, GitlabCI, GithubAction, Dask
```
```{dropdown} Framework data

**Contexte**

Dans un soucie d'harmonisation de l'existant, l'ESA (European Spatial Agency) souhaite la réalisation d'un framework double usage en python:
- pour la création d'algorithme de traitement de donnée satellitaire pour l'usage de l'ESA
- pour la manipulation de donnée satellitaire par une personne quelconque.

L'outil doit fournir:
- une interface standardisé pour accéder a différent type de donnée (zarr, netcdf, cog, ...), sur différent système de fichier (s3, local, ...) de manière lazy.
- un système de calcule distribué par graphe.
- différentes méthodes de déclenchement des algorithmes (cli, rest, ...)
- un mecanisme de trace et de log.

**Réalisation**

Développeur python
- Mise en oeuvre du module d'accès aux données
- Mise en oeuvre du module de traitement de la donnée
- Encadrement partiel et support des autres développeurs
- Python 3.9
- Test unitaire et test d'intégration => utilisation de Pytest et de Hypothesis.
- Dask pour l'accès lazy des données.
- Respect du "Python array API standard" pour l'interface des données.
DevOps
- Intégration CI/CD dans différent environment (github/gitlab)
- mise en place de l'environement de développement : pre-commit, outil d'analyse de securité, linter, formatter...
- mise en place du système d'auto génération de la documentation
- Intégration gitlab / sonarqube
```
:::

:::{tab-item} Développeur Web
```{tags} Python, Django, FastAPI, PostGres, Terraform, Azure
```
```{dropdown} Visualisation donnée client

**Contexte**

Dans le but d'apporter a ses client la meilleur expérience possible, BVA propose, en plus de ces outils de collecte, un outils d'analyse de la satisfaction client continue afin de proposer des axes d'améliorations.

**Réalisation**

Amélioration de l'existant et ajout de feature
- Factorisation du code par création de package python
- Amélioration du code existant par polymorphisme d'héritage et paramétré.
- Apport d'une expertise de développement python
- Amélioration des performances pour Azure function et base de donnée (pool de connection)
- Stratégie de mise a disposition de l'information (API)
Amelioration de la CI/CD
- Ajout de vérification d'impact de securité : bandit
- Accélération de la pipeline
- Test Behave
- Maintien des dépendances
Maintien de l'infrastructure
- Infrastructure sur Azure
- Maintien de l'infrastructure Kubernetes
- Azure function
- Azure web app
- Amélioration de l'infrastructure - factorisation
Integration SSO
- Management OKTA
- Aide a l'intégration client
```
```{tags} Python, Django, PostGres, Azure
```
```{dropdown} Recensement Agricole

**Contexte**

Dans le cadre du recensement des exploitations agricoles par le ministère, la réalisation d'un portails pour les exploitants et le support est réalisé.
Projet Majeur en durée limité.

Equipe de 3 developpeurs, 1 Scrum Master, 1 PO, 1 UX/UI.

**Réalisation**

Architecure Infrastructure et réseau
- Cloud Azure
Développement d'un portail web
- Python/Django
- Azure functions
- Threading
- Modélisation
CI/CD
- Azure devops
- Analyse de vulnérabilité - python bandit
- Compléxité/Maintenabilité - python xenon/Flake8
- Test Unitaire / code coverage
- Formatage du code - python Black
- validation avant commit : pre-commit
```
:::
::::

## YesWeHack
🗓️ Avril 2019 -> Déc. 2019
```{tags} Python, GitlabCI, Django
```
:::{dropdown} Ingénieur R&D

**Contexte**

YesWeHack est une société proposant un service de mise en place de programme de bug bounty pour des sociétés.
Celle ci dispose de près de dix milles hunters inscrits sur sa plateforme pour l'aide à la découverte de bug.
Dans ce contexte, YesWeHack propose également des outils tierce pour aider aussi bien les managers de programmes que les hunters dans leur travaux respectifs.

**Réalisation**

Développement d'outils d'intégrations de bug
- Programme réalisé en python 3.7
Outils de détection de program de bug bounty en navigation web
- Réalisé en javascript
Maintenance et ajout de feature sur Firebounty.com
- Utilisation de Django
- Ajout d'une api REST avec Django
- Utilisation de Scrapy
Maintenance du Dashboard sur l'evenement le HACK 2019
- Dashboard réalisé en Flask
Gestion et maintien de la CI/CD
- Gitlab CI
- Analyse de vulnérabilité - python bandit
- Compléxité/Maintenabilité - python xenon/Flake8
- Test Unitaire / code coverage
- Formatage du code - python Black
:::

## SopraStéria
🗓️ Fev. 2018 -> Avril 2019
::::{tab-set}

:::{tab-item} Data Engineer
```{tags} Python, ElasticStack, GitlabCI
```
```{dropdown} Aide à la décision

**Contexte**

Afin de facilité la validation de norme STANAG par des experts métiers, la création d'un outils à partir d'une architecture modulaire, et facilement réutilisable en utilisant des concepts de méthodes de deeplearning et d'étiquettage automatique fut proposé.

Equipe composé d'un Développeur/DataEngineer, d'un Architecte infrastructure réseau et d'un Datascientiste.

Ce Projet ma permis d'être au coeur d'un projet majeur et d'être force de proposition sur mes domaines d'expertises.

**Réalisation**

Ce Projet ma permis d'être au coeur d'un projet majeur et d'être force de proposition sur mes domaines d'expertises.
- Modélisation et création de l'architecture logiciel et d'analyse de données.
- Prototype d'un système simple - Keras / Scikit-learn
- Etat de l'art sur le décodage de donnée binaire par machine learning.
Outil de décodage de donnée binaire et d'analyse d'anomalie
- Outil de décodage de l'information - Keras/Scikit-Learn
- API REST d'intéraction (marche / arret / configuration du système) - Flask.
- Ingestion des données - Logstash
- Stockage des données - ElasticSearch
Resitution des données
- Plugin Kibana - ReactJS.
- Graphique d'analyse de donnée préconfiguré - Kibana.
Gestion et maintien de la CI/CD
- Mise en place d'un pipeline Gitlab CI
- Test Unitaire
- Analyse de code/vulnérabilité - SonarQube
- Remonté d'indicateur minimaux : maintenabilité/complexité du code
```
```{tags} Scala, ElasticStack, Spark
```
```{dropdown} Détection d'intrusion réseau

**Contexte**

Dans le contexte d'un projet national majeur de la protection des données et des systèmes informatiques, la nécessité de développer un outils dans l'air du big data à amener à la création de ce projet compétitif.

Equipe composé de 1 développeurs, 1 stagiaire, 1 Architecte, 1 chef de projet et 2 Data-scientist.

**Réalisation**

Réalisation d'un système d'aide à la détection d'anomalie réseau par machine learning
- Test Unitaire
- Récupération des données : Scala/Spark
- Extraction des features : Scala/Spark
- Système de machine learning : DL4S-Scala
- Stockage des données - ElasticSearch
- Prototypage -  Jupyter.
- Tech Lead / Data Engineer
Réstitution des données
- Scripts de configuration réseau et d'installation - Bash.
- API de récupération des informations collecté - Ruby On Rails.
- Développement d'une application Web de restitution par graphique - VueJS.
```
:::

:::{tab-item} Développeur Logiciel
```{tags} Python, Java, Jenkins
```
```{dropdown} Outils de supervision

**Contexte**

Dans le cadre du développement des systèmes informatiques embarqués lors de mission maritimes, le besoin de développer un système capable d'assurer l'analyse de l'intégrité et le maintien du réseau hors réseaux présentait un enjeu majeur au sein de ce projet.

Equipe composé de 5 développeurs, 1 Intégrateur, 1 Analyste de Sécurité et 1 chef de projets.

**Réalisation**

Développement d'un logiciel de configuration centralisé. Java 7
- Test Unitaire
- Ecriture des fichiers de configuration des systèmes de supervision managées.
- Architecture logiciel
- Lead Tech
Management des Logiciels de supervisions
- Scripts de configuration réseau et d'installation
- Bash.
- Scripts python d'intégrations Shinken/Nagios.
Maintien de la CI
- Jenkins

```
:::
::::


## ISAGRI
🗓️ Oct. 2017 -> Nov. 2017
```{tags} C#
```
:::{dropdown} Développeur Logiciel - ISAGRI

**Contexte**

Développement de progiciel à destination des comptables et des aggriculteurs.

**Réalisation**

- Développement de feuille de saisie à l'aide de C# et WPF
:::

## HEUDIASYC
🗓️ Oct. 2016 -> Août 2017
```{tags} Python
```

:::{dropdown} Doctorant

**Contexte**

Recherche théorique et applicative dans le domaine de l'intelligence artificielle.

Le Laboratoire HEUDIASYC est un laboratoire de recherche rattaché à l'Université Technonologique de Compiègne (UTC) et proposant des sujets de recherches liées à l'automatisation de tâches (véhicule autonome, essain de drône, etc ...).

L'objectif de cette thèse était d'étudier l'apprentissage de signaux sur graphes par réseau de neuronnes artificiels

**Réalisation**

- Etude de l'existant
- Transformation de données numérique en représentation par graphe : Pandas/Scipy
- Réalisation de systèmes de réseau de neurones convolutif : Keras/Tensorflow


:::
