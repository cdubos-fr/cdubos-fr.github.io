+++
title = "Parcours & Impact"
description = "Parcours professionnel, missions clés, formations et engagements annexes."
template = "page.html"
+++

<div class="slice">
	<div class="container">
		<h2>Timeline sélective</h2>
		<p style="max-width:65ch; color:var(--color-muted); font-size:.95rem;">Sélection de missions structurantes (innovation, industrialisation, data, infrastructure) avec rôle, contexte et réalisations clés. Chaque entrée se replie pour favoriser la lecture rapide.</p>
		<div class="timeline">

<!-- Loft Orbital -->
<details open>
	<summary><span class="period">Déc. 2023 → Avr. 2025</span><span class="role">Dév. Python · Loft Orbital (MMS)</span></summary>
	<div class="body">
		<div class="meta">Équipe: 5 dev + 1 manager · Rôle: Développeur Python</div>
		<div class="badges"><span>Python</span><span>Django</span><span>GraphQL</span><span>Docker</span><span>GCP</span></div>
		<strong>Contexte:</strong> Infrastructure spatiale as a service : élaboration plan d'exécution (orchestration) & système de requête satellite.<br/>
		<strong>Réalisations:</strong>
		<ul class="compact">
			<li>Composants Ground Software (API GraphQL, orchestration, architecture).</li>
			<li>Renforcement pratiques génie logiciel (revues, qualité, standards).</li>
			<li>Framework interne de définition & exécution de workflows.</li>
			<li>Corrections ciblées & consolidation architecture applicative.</li>
		</ul>
	</div>
</details>

<!-- Freelance Platform Engineer -->
<details>
	<summary><span class="period">Juil. 2023</span><span class="role">Platform Engineer · Freelance (Bimpli)</span></summary>
	<div class="body">
		<div class="meta">Équipe: 5 membres + 1 manager · Rôle: Platform Engineer</div>
		<div class="badges"><span>Python</span><span>GitHubActions</span><span>Pulumi</span><span>AWS</span><span>Pydantic</span></div>
		<strong>Contexte:</strong> Mise en place accélératrice d'un socle outillage & infra pour équipes produit.<br/>
		<strong>Réalisations:</strong>
		<ul class="compact">
			<li>Règles de protection branches & flux de revue.</li>
			<li>CI unifiée (tests, couverture, lint, sécurité).</li>
			<li>CD multi-environnements piloté par branche.</li>
			<li>Cadre Pulumi (organisation, stacks partagées).</li>
		</ul>
	</div>
</details>

<!-- Extia Platform Engineer -->
<details>
	<summary><span class="period">Avr. 2023 → Juil. 2023</span><span class="role">Platform Engineer · Extia</span></summary>
	<div class="body">
		<div class="meta">Équipe: 5 membres + 1 manager · Rôle: Platform Engineer</div>
		<div class="badges"><span>Python</span><span>GitHubActions</span><span>Pulumi</span><span>AWS</span><span>Pydantic</span></div>
		<strong>Contexte:</strong> Support transverse aux équipes (infrastructure, automatisation déploiements, gouvernance qualité).<br/>
		<strong>Réalisations:</strong>
		<ul class="compact">
			<li>CI/CD complète (tests, quality gates, security, coverage).</li>
			<li>Reusable workflows & standardisation pipelines.</li>
			<li>Cadre IaC Pulumi & implémentation des stacks.</li>
			<li>Structuration bonnes pratiques de code & revue.</li>
		</ul>
	</div>
</details>

<!-- Référentiel de donnée -->
<details>
	<summary><span class="period">Sept. 2022 → Avr. 2023</span><span class="role">Lead Tech · Référentiel de donnée (Bimpli)</span></summary>
	<div class="body">
		<div class="meta">Équipe: 2 dev + 1 lead + 1 PO · Rôle: Lead Tech</div>
		<div class="badges"><span>Python</span><span>AWS</span><span>Pulumi</span><span>Pydantic</span><span>Postgres</span></div>
		<strong>Contexte:</strong> Mise en place d'un Master Data Management AWS (train SAFe) pour centraliser & qualifier la donnée.<br/>
		<strong>Réalisations:</strong>
		<ul class="compact">
			<li>Architecture logicielle & standards (qualité, sécurité, test).</li>
			<li>Tests + linter + analyse sécurité + Localstack.</li>
			<li>CI/CD multi-stages (qualité + déploiement contrôlé).</li>
			<li>Cadre Pulumi & implémentation complète des stacks.</li>
		</ul>
	</div>
</details>

<!-- Framework data ESA -->
<details>
	<summary><span class="period">Déc. 2021 → Août 2022</span><span class="role">Lead Python · Framework data (ESA)</span></summary>
	<div class="body">
		<div class="meta">Équipe: 7 dev + 1 lead tech + 1 lead python · Rôle: Lead Python</div>
		<div class="badges"><span>Python</span><span>Dask</span><span>GitLabCI</span><span>GitHubActions</span><span>Data</span></div>
		<strong>Contexte:</strong> Framework double usage (interne ESA & externe) pour accès unifié & traitement distribué de données satellitaires.<br/>
		<strong>Réalisations:</strong>
		<ul class="compact">
			<li>Accès lazy multi-formats (zarr, netcdf, COG...).</li>
			<li>Moteur de traitement distribué (graphe Dask).</li>
			<li>Encadrement & respect Python Array API standard.</li>
			<li>CI multi-plateformes & génération documentation.</li>
			<li>Tests unitaires & propriétés (Pytest + Hypothesis).</li>
		</ul>
	</div>
</details>

<!-- Data Visualisation BVA -->
<details>
	<summary><span class="period">Janv. 2021 → Déc. 2021</span><span class="role">Dév. Web · Data Visualisation (BVA)</span></summary>
	<div class="body">
		<div class="meta">Équipe: 3 dev + 1 lead + 1 SM + 1 PO · Rôle: Développeur</div>
		<div class="badges"><span>Python</span><span>Django</span><span>FastAPI</span><span>Azure</span><span>Terraform</span></div>
		<strong>Contexte:</strong> Outil d'analyse continue de satisfaction client (stack Azure) pour valoriser la donnée collectée.<br/>
		<strong>Réalisations:</strong>
		<ul class="compact">
			<li>Factorisation (packages internes, polymorphisme).</li>
			<li>Optimisation perf (Azure Functions, pool connexions DB).</li>
			<li>Stratégie exposition données via API.</li>
			<li>Pipeline CI accélérée (sécurité, tests Behave).</li>
			<li>Intégration SSO (OKTA) & support clients.</li>
		</ul>
	</div>
</details>

<!-- Recensement Agricole BVA -->
<details>
	<summary><span class="period">Mars 2020 → Janv. 2021</span><span class="role">Dév. Web · Recensement Agricole (BVA)</span></summary>
	<div class="body">
		<div class="meta">Équipe: 3 dev + 1 SM + 1 PO + 1 UX/UI · Rôle: Développeur</div>
		<div class="badges"><span>Python</span><span>Django</span><span>Azure</span><span>Postgres</span><span>CI/CD</span></div>
		<strong>Contexte:</strong> Portail national pour la mise à jour & orchestration des données des exploitations agricoles.<br/>
		<strong>Réalisations:</strong>
		<ul class="compact">
			<li>Architecture & portail Django (threads, modélisation).</li>
			<li>CI/CD Azure DevOps (tests, couverture, sécurité, complexité).</li>
			<li>Qualimétrie & outillage (Flake8, Black, Bandit, Xenon).</li>
		</ul>
	</div>
</details>

<!-- YesWeHack -->
<details>
	<summary><span class="period">Avr. 2019 → Déc. 2019</span><span class="role">Ing. R&D · YesWeHack</span></summary>
	<div class="body">
		<div class="meta">Équipe: 1 dev + 1 chef de projet · Rôle: Développeur</div>
		<div class="badges"><span>Python</span><span>Django</span><span>Flask</span><span>GitLabCI</span><span>Sécurité</span></div>
		<strong>Contexte:</strong> Plateforme bug bounty & outils pour gestion programmes & hunters (sécurité offensive / reporting).<br/>
		<strong>Réalisations:</strong>
		<ul class="compact">
			<li>Outils d'intégration de bugs & automatisations.</li>
			<li>Détection programmes bug bounty (JS) & scraping.</li>
			<li>API REST + maintenance Firebounty (Django / Flask).</li>
			<li>Pipeline qualité (Bandit, tests, couverture, Black).</li>
		</ul>
	</div>
</details>

<!-- Aide à la décision SopraStéria -->
<details>
	<summary><span class="period">Déc. 2018 → Avr. 2019</span><span class="role">Data Eng. · Aide à la décision (SopraStéria)</span></summary>
	<div class="body">
		<div class="meta">Équipe: Dev/DataEng + Chef proj + Archi + DataScientist · Rôle: Data Engineer</div>
		<div class="badges"><span>Python</span><span>Elastic</span><span>GitLabCI</span><span>Flask</span><span>Keras</span></div>
		<strong>Contexte:</strong> Validation normes STANAG via outils modulaires exploitant ML & étiquetage automatique.<br/>
		<strong>Réalisations:</strong>
		<ul class="compact">
			<li>Architecture & modélisation (Keras/Scikit, ingestion Logstash, ElasticSearch).</li>
			<li>API REST pilotage système (Flask) & restitution (Kibana/React).</li>
			<li>Pipelines CI (tests, SonarQube, indicateurs maintenabilité).</li>
		</ul>
	</div>
</details>

<!-- Détection intrusion -->
<details>
	<summary><span class="period">Juin 2018 → Déc. 2018</span><span class="role">Data Eng. · Détection intrusion réseau (SopraStéria)</span></summary>
	<div class="body">
		<div class="meta">Équipe: Dev/DataEng + stagiaire + Archi + Chef proj + 2 DataSci · Rôle: Data Engineer</div>
		<div class="badges"><span>Scala</span><span>Spark</span><span>Elastic</span><span>ML</span><span>VueJS</span></div>
		<strong>Contexte:</strong> Système big data de détection d'anomalies réseau (projet national, forte volumétrie).<br/>
		<strong>Réalisations:</strong>
		<ul class="compact">
			<li>Pipeline extraction & features (Scala/Spark).</li>
			<li>Moteur ML (DL4S) & stockage ElasticSearch.</li>
			<li>API restitution + interface VueJS.</li>
		</ul>
	</div>
</details>

<!-- Outils de supervision -->
<details>
	<summary><span class="period">Fév. 2018 → Juin 2018</span><span class="role">Dév. Logiciel · Outils supervision (SopraStéria)</span></summary>
	<div class="body">
		<div class="meta">Équipe: 5 dev + Intégrateur + Analyste Sécu + Chef proj · Rôle: Développeur</div>
		<div class="badges"><span>Python</span><span>Java</span><span>Jenkins</span><span>Bash</span><span>Nagios</span></div>
		<strong>Contexte:</strong> Système d'analyse d'intégrité & maintien réseau pour environnements embarqués maritimes.<br/>
		<strong>Réalisations:</strong>
		<ul class="compact">
			<li>Logiciel configuration centralisée (Java 7) & scripts supervision.</li>
			<li>Intégrations Shinken/Nagios & scripts Bash.</li>
			<li>Maintien pipeline Jenkins & automatisations.</li>
		</ul>
	</div>
</details>

<!-- ISAGRI -->
<details>
	<summary><span class="period">Oct. 2017 → Nov. 2017</span><span class="role">Dév. Logiciel · ISAGRI</span></summary>
	<div class="body">
		<div class="meta">Équipe: Collaboration locale · Rôle: Développeur</div>
		<div class="badges"><span>C#</span><span>WPF</span><span>Desktop</span></div>
		<strong>Contexte:</strong> Développement de feuilles de saisie pour progiciel agricole/comptable.<br/>
		<strong>Réalisations:</strong>
		<ul class="compact">
			<li>Interfaces WPF & logique métier (C#).</li>
		</ul>
	</div>
</details>

<!-- Doctorat -->
<details>
	<summary><span class="period">Oct. 2016 → Août 2017</span><span class="role">Doctorant · HEUDIASYC (UTC)</span></summary>
	<div class="body">
		<div class="meta">Équipe: Recherche académique · Rôle: Doctorant</div>
		<div class="badges"><span>Python</span><span>Keras</span><span>TensorFlow</span><span>Scipy</span><span>ML</span></div>
		<strong>Contexte:</strong> Recherche sur apprentissage de signaux sur graphes par réseaux de neurones.<br/>
		<strong>Réalisations:</strong>
		<ul class="compact">
			<li>Étude état de l'art & modélisation.</li>
			<li>Transformation données → graphes (Pandas/Scipy).</li>
			<li>Architectures CNN graphes (Keras/TensorFlow).</li>
			<li>Expérimentations, présentations & publication (ICPR).</li>
		</ul>
	</div>
</details>
</div>

<div class="slice alt" id="axes">
	<div class="container">
		<h2>Axes de spécialisation</h2>
		<div class="pack-layout" style="grid-template-columns:repeat(auto-fit,minmax(300px,1fr));">
			<div class="info-box">
				<h4>Plateformes & Infrastructure</h4>
				<ul>
					<li>CI/CD multi-env</li>
					<li>Socles projet & templates</li>
					<li>Gouvernance qualité</li>
				</ul>
			</div>
			<div class="info-box">
				<h4>Python & Écosystème</h4>
				<ul>
					<li>API backend (Django/FastAPI)</li>
					<li>Workflows data & calcul distribué (Dask)</li>
					<li>Packaging & reproductibilité</li>
				</ul>
			</div>
			<div class="info-box">
				<h4>Données & Traitement</h4>
				<ul>
					<li>Accès unifié multi-formats</li>
					<li>Modélisation & optimisation</li>
					<li>Standards & validation</li>
				</ul>
			</div>
			<div class="info-box">
				<h4>Culture Ingénierie</h4>
				<ul>
					<li>Revue structurée & mentoring</li>
					<li>Sécurité applicative</li>
					<li>Dette & priorisation</li>
				</ul>
			</div>
		</div>
	</div>
</div>

<div class="slice" id="formations">
	<div class="container">
		<h2>Formations clés</h2>
		<ul style="line-height:1.5; font-size:.9rem; color:var(--color-muted);">
			<li><strong>Master IGIS STIM (2014–2016)</strong> – Data, optimisation, apprentissage. Publication ICPR 2016.</li>
			<li><strong>Licence EEA GEII (2011–2014)</strong> – Informatique industrielle, électronique, systèmes embarqués.</li>
		</ul>
	</div>
</div>

<div class="slice alt" id="engagements">
	<div class="container">
		<h2>Engagements annexes</h2>
		<div class="pack-layout" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
			<div class="info-box">
				<h4>Communautés</h4>
				<ul>
					<li>Rés'Aude – Dynamique territoriale</li>
					<li>Comet' (Extia) – Talks & partage</li>
					<li>AREIGE – Événements & pédagogie</li>
				</ul>
			</div>
			<div class="info-box">
				<h4>Publication</h4>
				<ul>
					<li><a href="/icpr_2016.pdf" target="_blank" rel="noopener">ICPR 2016 – SVM cost-sensitive</a></li>
					<li>Projet long: optimisation apprentissage supervisé</li>
				</ul>
			</div>
		</div>
	</div>
</div>

<div class="slice" id="valeur">
	<div class="container">
		<h2>Valeur en mission</h2>
		<div class="pack-layout" style="grid-template-columns:repeat(auto-fit,minmax(300px,1fr));">
			<div class="info-box">
				<h4>Accélération</h4>
				<ul>
					<li>Socles & pipelines industrialisés</li>
					<li>Standards qualité actionnables</li>
					<li>Points de contrôle lisibles</li>
				</ul>
			</div>
			<div class="info-box">
				<h4>Architecture & Clarté</h4>
				<ul>
					<li>Alignement métier / technique</li>
					<li>Découpage incrementable</li>
					<li>Endettement maîtrisé</li>
				</ul>
			</div>
			<div class="info-box">
				<h4>Transmission</h4>
				<ul>
					<li>Documentation courte ciblée</li>
					<li>Mentorat & revue structurée</li>
					<li>Autonomie progressive</li>
				</ul>
			</div>
		</div>
	</div>
</div>

<div class="slice accent" id="cta-parcours">
	<div class="container" style="text-align:center;">
		<h2>Aller plus loin</h2>
		<p style="color:var(--color-muted); max-width:60ch; margin:0 auto 1.2rem;">Détails supplémentaires, références anonymisées ou focus sur une problématique spécifique disponibles sur simple demande professionnelle.</p>
		<p>
			<a href="/cv_clement_dubos.pdf" class="btn" target="_blank" rel="noopener">CV (PDF)</a>
			<a href="/contact/" class="btn btn-outline">Me contacter</a>
		</p>
	</div>
</div>
