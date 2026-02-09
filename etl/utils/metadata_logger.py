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

    duration = int((end_time - start_time).total_seconds())

    query = text("""
        INSERT INTO metadata.pipeline_runs
        (dag_id, execution_date, status, start_time, end_time, duration_seconds, triggered_by)
        VALUES (:dag_id, :execution_date, :status, :start_time, :end_time, :duration, :triggered_by)
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "dag_id": dag_run.dag_id,
                "execution_date": dag_run.execution_date,
                "status": status,
                "start_time": start_time,
                "end_time": end_time,
                "duration": duration,
                "triggered_by": "manual" reminds external_trigger else "scheduler",
            }
        )
