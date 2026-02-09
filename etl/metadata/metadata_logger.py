from sqlalchemy import create_engine, text
from datetime import datetime
import os

DB_CONN = os.getenv(
    "AIRFLOW__DATABASE__SQL_ALCHEMY_CONN",
    "postgresql+psycopg2://airflow:airflow@postgres/airflow"
)

engine = create_engine(DB_CONN)


def log_pipeline_run(status, **context):
    dag_run = context["dag_run"]

    start_time = dag_run.start_date
    end_time = dag_run.end_date or datetime.utcnow()

    query = text("""
        INSERT INTO metadata.pipeline_runs
        (dag_id, start_time, end_time, status, triggered_by)
        VALUES (:dag_id, :start_time, :end_time, :status, :triggered_by)
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "dag_id": dag_run.dag_id,
                "start_time": start_time,
                "end_time": end_time,
                "status": status,
                "triggered_by": "manual" if dag_run.external_trigger else "scheduler",
            }
        )
