import yaml
from etl.ingestion.csv_ingest import ingest
from etl.cleaning.cleaner import clean
from etl.validation.dq_checks import validate
from etl.transform.transformer import transform
from etl.load.db_loader import save_to_db

with open("config/pipeline.yaml") as f:
    config = yaml.safe_load(f)

# Ingestion
df = ingest(config["source"]["path"])

# Cleaning
df = clean(df, config["cleaning"])

# Validation
dq_report = validate(df, config["validation"])

# Transformation
df = transform(df)

# Load to database
save_to_db(df)

print("SPRINT 3 PIPELINE COMPLETED")
print("DQ REPORT:", dq_report)
print("Enterprise ETL pipeline executed successfully")

