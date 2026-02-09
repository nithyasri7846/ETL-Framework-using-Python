from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="master_etl_pipeline",
    start_date=datetime(2026, 1, 21),
    schedule_interval="0 2 * * *",  # Daily at 2 AM
    catchup=False,
    default_args=default_args,
) as dag:

    trigger_ingestion = TriggerDagRunOperator(
        task_id="trigger_ingestion",
        trigger_dag_id="ingestion_pipeline",
        wait_for_completion=True,
    )

    trigger_cleaning = TriggerDagRunOperator(
        task_id="trigger_cleaning",
        trigger_dag_id="cleaning_pipeline",
        wait_for_completion=True,
    )

    trigger_transform = TriggerDagRunOperator(
        task_id="trigger_transform",
        trigger_dag_id="transform_pipeline",
        wait_for_completion=True,
    )

    trigger_load = TriggerDagRunOperator(
        task_id="trigger_load",
        trigger_dag_id="load_pipeline",
        wait_for_completion=True,
    )

    log_metadata_task = BashOperator(
        task_id="log_metadata",
        bash_command="echo 'Logging metadata for ETL run'",
    )

    (
        trigger_ingestion
        >> trigger_cleaning
        >> trigger_transform
        >> trigger_load
        >> log_metadata_task
    )
