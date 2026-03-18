<div align="center">

# 🚛 Transport Data Engineering Pipeline

**Master BigData & Cloud Computing — 2025/2026**

[![Python](https://img.shields.io/badge/Python-3.9-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PySpark](https://img.shields.io/badge/PySpark-3.5.0-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)](https://spark.apache.org)
[![Kafka](https://img.shields.io/badge/Apache_Kafka-3.7.0-231F20?style=for-the-badge&logo=apachekafka&logoColor=white)](https://kafka.apache.org)
[![Airflow](https://img.shields.io/badge/Apache_Airflow-2.8.0-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)](https://airflow.apache.org)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)

*Pipeline complet de Data Engineering appliqué au domaine Transport & Logistique au Maroc*

</div>

---

## 📋 Table des matières

- [Contexte et objectifs](#-contexte-et-objectifs)
- [Architecture du pipeline](#-architecture-du-pipeline)
- [Stack technique](#-stack-technique)
- [Structure du projet](#-structure-du-projet)
- [Les 7 étapes du pipeline](#-les-7-étapes-du-pipeline)
- [Résultats ML](#-résultats-ml)
- [Installation et démarrage](#-installation-et-démarrage)
- [Auteur](#-auteur)

---

## 🎯 Contexte et objectifs

Ce projet implémente un pipeline de **Data Engineering de bout en bout** pour une entreprise de transport et logistique au **Maroc**. Il couvre l'intégralité du cycle de vie des données, de la collecte en temps réel jusqu'à la modélisation Machine Learning.

### Problématique
> *Comment prédire efficacement les retards de livraison en exploitant des données multi-sources (GPS, météo, trafic, historique chauffeurs et véhicules) ?*

### Objectifs
- Collecter des événements GPS de véhicules en **temps réel** via Apache Kafka
- Construire un **pipeline de traitement** complet avec PySpark
- Intégrer **5 sources de données** hétérogènes
- Créer **15+ features métier** pertinentes
- Prédire les retards de livraison avec un modèle ML (Random Forest / GBT)
- Orchestrer le tout avec **Apache Airflow**

---

## 🏗️ Architecture du pipeline
```
┌─────────────────────────────────────────────────────────────┐
│                    SOURCES DE DONNÉES                       │
│  GPS Véhicules │ API Météo │ Trafic │ Chauffeurs │ Parc Vh  │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                   INGESTION (Kafka)                         │
│         Producer ──► Topic transport_events ──► Consumer    │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                  TRAITEMENT (PySpark)                       │
│                                                             │
│  [Cleaning] ──► [Transformation] ──► [Reduction PCA]       │
│                                                             │
│  [Integration 5 sources] ──► [Feature Engineering]         │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│               MODÉLISATION ML (PySpark MLlib)               │
│                                                             │
│   Train/Val/Test ──► Random Forest / GBT ──► Évaluation    │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│              ORCHESTRATION (Apache Airflow)                 │
│              DAGs ──► Scheduling ──► Monitoring             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Stack technique

| Catégorie | Technologie | Version | Rôle |
|---|---|---|---|
| Langage | Python | 3.9 | Développement |
| Big Data | Apache Spark / PySpark | 3.5.0 | Traitement distribué |
| Streaming | Apache Kafka | 3.7.0 | Ingestion temps réel |
| Orchestration | Apache Airflow | 2.8.0 | Scheduling des DAGs |
| Containerisation | Docker Compose | latest | Infrastructure |
| ML | PySpark MLlib | 3.5.0 | Modèles ML |
| ML | Scikit-learn | 1.3.2 | Évaluation |
| Visualisation | Matplotlib + Seaborn | 3.8.2 | Graphiques |
| Stockage | Parquet + CSV | — | Data Lake |
| IDE | PyCharm Professional | 2025.x | Développement |

---

## 📁 Structure du projet
```
transport-data-engineering/
│
├── 📓 notebooks/
│   └── transport_pipeline.ipynb    ← Pipeline complet (7 sections)
│
├── 📁 src/
│   ├── ingestion/                  ← Kafka Producer / Consumer
│   ├── cleaning/                   ← Nettoyage PySpark
│   ├── transformation/             ← Normalisation, encodage
│   ├── reduction/                  ← PCA et sélection features
│   ├── integration/                ← Jointures multi-sources
│   ├── feature_engineering/        ← Features métier
│   ├── preparation/                ← Split Train/Val/Test
│   └── modeling/                   ← Modèles ML
│
├── 📁 dags/
│   └── transport_pipeline_dag.py   ← DAG Airflow
│
├── 📁 config/
│   └── config.py                   ← Configuration globale
│
├── 📁 data/                        ← (gitignored — généré localement)
│   ├── raw/                        ← Données brutes Parquet
│   ├── cleaned/                    ← Données nettoyées
│   ├── processed/                  ← Données transformées
│   └── final/                      ← Features finales
│
├── 📁 outputs/
│   ├── models/                     ← Modèles sauvegardés
│   └── reports/                    ← Graphiques et visualisations
│
├── 🐳 docker-compose.yml           ← Kafka + Zookeeper + Airflow
├── 📋 requirements.txt             ← Dépendances Python
├── 🔒 .gitignore
└── 📖 README.md
```

---

## 🔄 Les 7 étapes du pipeline

### 1️⃣ Data Collection
- Simulation d'événements GPS transport en temps réel
- **Kafka Producer** → 500 événements → topic `transport_events`
- Données collectées : véhicule, chauffeur, GPS, vitesse, statut, colis
- Villes couvertes : Casablanca, Rabat, Marrakech, Fès, Tanger, Agadir, Meknès, Oujda

### 2️⃣ Data Cleaning
- Chargement depuis le Data Lake **Parquet**
- Suppression des doublons sur `event_id`
- Traitement des **valeurs nulles** (fillna par stratégie métier)
- Filtrage des **outliers** vitesse (0–130 km/h)
- Validation des coordonnées **GPS** (bbox Maroc : 27°–36° N, 14° O–0°)
- Correction et standardisation des types

### 3️⃣ Data Transformation
- Extraction de **variables temporelles** : heure, jour, période, heure de pointe
- **Encodage** des catégorielles : StringIndexer (PySpark MLlib)
- **Normalisation MinMax** des 7 variables numériques
- Calcul des distances réelles avec la formule **Haversine**

### 4️⃣ Data Reduction
- **Matrice de corrélation** Pearson complète
- **PCA** (Principal Component Analysis) — PySpark MLlib
- Sélection automatique du nombre de composantes (90% variance)
- Réduction dimensionnelle et sélection des features par importance

### 5️⃣ Data Integration
Jointures PySpark avec **5 sources** :

| Source | Colonnes ajoutées |
|---|---|
| Météo départ | condition, précipitations, vent, visibilité, risque |
| Météo arrivée | même colonnes pour la destination |
| Trafic route | incidents, temps attente, route fermée, score trafic |
| Historique chauffeurs | expérience, note, taux retard, score fiabilité |
| Parc véhicules | âge, capacité, pannes, score maintenance |

### 6️⃣ Feature Engineering
Création de **15+ features métier** :

| Feature | Description |
|---|---|
| `score_risque_chauffeur` | Score composite basé sur l'historique |
| `score_risque_vehicule` | État du véhicule (âge + pannes + maintenance) |
| `score_risque_externe` | Météo + trafic + route fermée |
| `score_retard_global` | Score composite final pondéré |
| `conditions_difficiles` | Flag binaire conditions dégradées |
| `charge_utile_pct` | Taux de chargement du véhicule |
| `categorie_risque` | FAIBLE / MOYEN / ÉLEVÉ |
| `chauffeur_experimente` | Expérience ≥ 5 ans |
| `pluie_forte` | Précipitations ≥ 20mm |
| `trafic_bloquant` | Incidents ≥ 5 ou route fermée |

### 7️⃣ Data Preparation + Modélisation ML

**Split des données :**
```
Total : 500 événements
  ├── Train      : 70% (350 lignes)
  ├── Validation : 15%  (75 lignes)
  └── Test       : 15%  (75 lignes)
```

**Modèles entraînés :**
- `RandomForestClassifier` — 100 arbres, profondeur 8
- `GBTClassifier` — 50 itérations, learning rate 0.1

---

## 📊 Résultats ML

### Comparaison des modèles

| Métrique | Random Forest | GBT |
|---|---|---|
| AUC-ROC | — | — |
| F1-Score | — | — |
| Accuracy | — | — |
| Precision | — | — |
| Recall | — | — |

### Visualisations générées

| Fichier | Description |
|---|---|
| `correlation_matrix.png` | Matrice de corrélation Pearson |
| `pca_variance.png` | Variance expliquée par composante PCA |
| `feature_importance_pca.png` | Importance des features (loadings) |
| `feature_engineering.png` | Distribution des nouvelles features |
| `confusion_matrix.png` | Matrice de confusion du meilleur modèle |
| `feature_importance_model.png` | Importance des features du modèle ML |

---

## 🚀 Installation et démarrage

### Prérequis

- Python 3.9+
- Java 11 ou 17
- Docker Desktop
- Git

### Étapes
```bash
# 1. Cloner le repository
git clone https://github.com/ghassouine19/transport-data-engineering.git
cd transport-data-engineering

# 2. Créer l'environnement virtuel
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Linux/Mac

# 3. Installer les dépendances
pip install --upgrade pip
pip install -r requirements.txt

# 4. Démarrer l'infrastructure Docker
docker-compose up -d

# 5. Créer le topic Kafka
docker exec -it transport-data-engineering-kafka-1 \
  kafka-topics --create \
  --topic transport_events \
  --bootstrap-server localhost:9092 \
  --partitions 3 --replication-factor 1

# 6. Lancer Jupyter
jupyter notebook
```

### Accès aux interfaces

| Service | URL | Credentials |
|---|---|---|
| Jupyter Notebook | http://localhost:8888 | — |
| Apache Airflow | http://localhost:8080 | admin / admin |
| Kafka Broker | localhost:9092 | — |

### Note Windows — winutils.exe

PySpark nécessite `winutils.exe` sur Windows :
```
1. Télécharger : https://github.com/cdarlint/winutils/raw/master/hadoop-3.3.5/bin/winutils.exe
2. Placer dans  : C:\hadoop\bin\winutils.exe
3. Variable env : HADOOP_HOME = C:\hadoop
```

---

## 👨‍💻 Auteur

<div align="center">

**Abdou Ghassouine**

Master BigData & Cloud Computing

[![GitHub](https://img.shields.io/badge/GitHub-ghassouine19-181717?style=for-the-badge&logo=github)](https://github.com/ghassouine19)
[![Email](https://img.shields.io/badge/Email-ghassouine19abdou@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ghassouine19abdou@gmail.com)

</div>

---

<div align="center">

*Projet réalisé dans le cadre du Master BigData & Cloud Computing — 2025/2026*

⭐ N'hésitez pas à star le repo si ce projet vous a été utile !

</div>
