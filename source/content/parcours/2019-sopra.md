+++
title = "Analyse de flux STANAG (POC) | Sopra Steria (BU Défense & Sécurité)"
date = 2019-01-01
+++

_Période : Janvier 2019 – Avril 2019_

**Organisation :**
- **Rôle :** Développeur & Architecte IA (binôme).
- **Équipe :** 1 Chef de projet, 1 Data Engineer, 1 Architecte logiciel, 1 Data Scientist.
- **Méthode :** Cycle en V (Environnement défense).

**Stack Technique :**
- **Langage & Core** : Python 3.7, Keras (Deep Learning).
- **Data & Observabilité :** ElasticStack (ELK : Elasticsearch, Logstash, Kibana).
- **Infra & DevOps :** Jenkins (CI/CD).
- **Developer Experience :** Pytest, Conda.

**Contexte :** Les opérateurs de la DGA-MI réalisent manuellement la qualification des appareils de communication répondant aux normes OTAN (STANAG). Ce projet visait à mettre en place un Proof of Concept (POC) pour automatiser cette qualification. Le défi consistait à traiter des flux de données techniques massifs pour vérifier la conformité et la sécurité des transmissions militaires.

**Mission :** Compréhension et étude approfondie de la norme STANAG afin de concevoir une architecture neuronale et une infrastructure d'analyse de données capables de valider les flux, tout en offrant une interface de retour efficace pour les opérateurs.

**Réalisations :**
- **Analyse de Norme :** Étude détaillée des spécifications techniques de la norme STANAG pour traduire les contraintes protocolaires en caractéristiques exploitables (features) et structurer les différentes couches (layers) du réseau de neurones.
- **Ingénierie IA :** Co-conception d'une architecture de réseau de neurones semi-supervisé (Keras) pour la qualification automatique des flux. Implémentation d'un système de détection à seuil avec projection de données pour faciliter l'interprétation humaine.
- **Plateforme Big Data :** Déploiement et configuration de la stack ELK. Développement d'un plugin Kibana sur-mesure permettant aux opérateurs de déclencher des analyses approfondies à la demande.
- **Industrialisation :** Intégration de pipelines Jenkins pour l'automatisation des tests et la création de builds. Mise en œuvre d'un mirroring Conda pour sécuriser les environnements de développement.

**Difficultés Rencontrées :** La faible diversité des données d'entrée a constitué un défi majeur, limitant la validation statistique du système. Ce projet a mis en évidence l'importance critique de la représentativité des datasets pour la généralisation des règles de la norme STANAG.
