# Enterprise Data Cleaning & ETL Orchestration Framework using Python

A **modular ETL (Extract–Transform–Load) framework** built using Python to design, execute, and monitor reliable data pipelines.  
This project focuses on clean separation of concerns, configuration-driven execution, centralized logging, and scalable data processing workflows.

---

## 📌 Key Features

- Modular **Extract, Transform, Load (ETL)** architecture  
- Configuration-driven pipeline execution  
- Centralized logging and error handling  
- Scalable design suitable for enterprise-style data workflows  
- Easily extensible for orchestration and API integration  

---

## 🧱 Tech Stack & Requirements

### Core Language
- Python 3.8+

### Data Processing
- Python (custom ETL modules)
- Pandas
- CSV / SQL-based data sources

### Logging & Configuration
- Python `logging` module  
- Config files for pipeline parameters  

*(Airflow, Docker, and API layers can be integrated as future enhancements.)*

---

## 📁 Project Structure

```text
├── etl/              # Core ETL logic (extract, transform, load)
├── config/           # Configuration files
├── data/             # Input and processed datasets
├── run_test.py       # Entry point to execute the ETL pipeline
├── etl.log           # Application logs
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
└── LICENSE           # MIT License


```

## ▶️ How to Run

### Run ETL Pipeline Locally

```bash
python run_test.py
```
### Ensure all dependencies are installed before execution:
```bash
pip install -r requirements.txt
```
### Run with Docker & Airflow
```bash
cd docker
docker-compose up
```
## Development & Agile Approach

- The project was developed using a modular and iterative approach.
- Each ETL stage (Extract, Transform, Load) is independently designed and tested.
- Logging and configuration were added incrementally to improve reliability.
- The framework is structured to support future extensions such as workflow orchestration and API triggers.

## Use Cases

- Academic ETL and data engineering projects.
- Backend data preprocessing pipelines.
- Demonstration of clean ETL framework design.
- Foundation for workflow orchestration systems.

## Author
NITHYA SRI P R  ,  Infosys SpringBoard Internship
