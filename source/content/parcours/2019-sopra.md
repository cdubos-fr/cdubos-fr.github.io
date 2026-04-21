+++
title = "Analyse de flux STANAG (POC) | Sopra Steria (BU Défense & Sécurité)"
date = 2019-01-01
+++

_Période : Janvier 2019 – Avril 2019_

- **Technologies :** Python, Elasticstack (ElasticSearch, Kibana, Logstash), Keras,
Jenkins (CI/CD), Conda.
- **Équipe :** 1 Chef de projet, 1 Data Engineer, 1 Architecte logiciel, 1 Data scientist.
- **Rôle :** Développeur / Architecte IA (conjoint).

**Contexte :** Ce POC visait à automatiser la qualification des systèmes de communication
répondant aux normes OTAN (STANAG). Le défi consistait à traiter des flux de données
techniques pour aider les opérateurs à vérifier la conformité et la sécurité des transmissions.

**Mission :** Concevoir l'architecture neuronale et l'infrastructure d'analyse de données.

**Réalisations :**
- Co-conception de l'architecture de réseau de neurones semi-supervisé avec le Data
Scientist.
- Mise en place de l'infrastructure ELK et développement d'un plugin Kibana spécifique
pour le déclenchement d'analyses à la demande.
- Développement d'un système de détection à seuil avec module de projection des
données pour faciliter la lecture humaine.
- Intégration Jenkins pour l'exécution de tests automatisés et de création de build.
- Aide à l’intégration d’un mirroring Conda pour un ensemble de projets dédiés.

**Problème rencontré :** La faible diversité des données d'entrée a constitué un point de
blocage majeur, ne permettant pas de valider statistiquement la capacité du système à
généraliser l'ensemble des règles de la norme STANAG.
