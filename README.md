# Transport Data Engineering Pipeline

> Projet Master BigData & Cloud Computing

Pipeline complet de Data Engineering appliqué au domaine Transport & Logistique.

## Stack technique
- **Ingestion** : Apache Kafka
- **Processing** : Apache Spark / PySpark
- **Orchestration** : Apache Airflow
- **Notebook** : Jupyter
- **ML** : Scikit-learn

## Structure
```
transport-data-engineering/
├── data/           # raw → cleaned → processed → final
├── notebooks/      # Jupyter notebooks
├── src/            # Modules Python par étape
├── dags/           # DAGs Airflow
├── config/         # Configuration
└── outputs/        # Modèles et rapports
```

## Étapes du pipeline
1. Data Collection (Kafka Producer)
2. Data Ingestion (Kafka Consumer + PySpark)
3. Raw Storage (Parquet)
4. Data Cleaning
5. Data Transformation
6. Data Reduction (PCA)
7. Data Integration (Joins multi-sources)
8. Feature Engineering
9. Data Preparation (Train/Val/Test)
10. Modélisation ML
