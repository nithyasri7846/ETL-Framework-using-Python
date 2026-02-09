from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os

DB_CONN = os.getenv(
    "AIRFLOW__DATABASE__SQL_ALCHEMY_CONN",
    "postgresql+psycopg2://airflow:airflow@localhost:5432/airflow"
)

engine = create_engine(DB_CONN)
app = FastAPI(title="ETL Monitoring API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/pipelines/status")
def pipeline_status(limit: int = 10):
    query = text("""
        SELECT dag_id, status, start_time, end_time
        FROM metadata.pipeline_runs
        ORDER BY start_time DESC
        LIMIT :limit
    """)

    with engine.begin() as conn:
        rows = conn.execute(query, {"limit": limit}).fetchall()

    return [
        {
            "dag_id": r[0],
            "status": r[1],
            "start_time": r[2],
            "end_time": r[3],
        }
        for r in rows
    ]
