# Enterprise Data Cleaning & ETL Orchestration Framework using Python

A **modular ETL (Extract–Transform–Load) framework** built with Python to design, execute, and monitor reliable data pipelines.  
The framework supports clean separation of concerns, logging, configuration-driven execution, and workflow orchestration.

---

## 📌 Key Features

- Modular **Extract, Transform, Load** architecture  
- Configuration-driven pipelines  
- Centralized logging & error handling  
- REST API support for triggering ETL jobs  
- Workflow orchestration using **Apache Airflow**  
- Dockerized setup for consistent environments  

---

## 🧱 Tech Stack & Requirements

### Core Language
- Python 3.8+

### ETL & Data Processing
- Python (custom ETL modules)
- Pandas
- SQL / File-based sources (CSV)

### Orchestration
- Apache Airflow  
- DAG-based scheduling and monitoring  

### API Layer
- Flask (REST API for triggering ETL jobs)

### Containerization
- Docker  
- Docker Compose  

### Logging & Configuration
- Python `logging` module  
- `.env` / config files for environment variables  

---
## 📁 Project Structure

```text
├── airflow/          # Airflow DAGs for ETL orchestration
├── api/              # Flask API for ETL triggers
├── config/           # Configuration & environment files
├── data/             # Input and processed data
├── docker/           # Docker & docker-compose setup
├── etl/              # Core ETL logic (extract, transform, load)
├── run_test.py       # Entry point to run ETL pipeline
├── etl.log           # Application logs
└── requirements.txt  # Python dependencies

```

## ▶️ How to Run

### Run ETL Pipeline Locally

```bash
python run_test.py
```

### Run with Docker & Airflow
```bash
cd docker
docker-compose up
```


## Use Cases

- Batch data processing pipelines
- Academic ETL / Data Engineering projects
- Backend data preprocessing systems
- Airflow-based workflow orchestration demos
