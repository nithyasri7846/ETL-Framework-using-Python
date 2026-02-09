import sys
sys.path.append("/opt/airflow")

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

from etl.ingestion.main import run as ingestion_run
from etl.cleaning.main import run as cleaning_run
from etl.validation.main import run as validation_run
from etl.transform.main import run as transform_run
from etl.load.main import run as load_run
from etl.metadata.metadata_logger import log_pipeline_run
from etl.metadata.metadata_logger import log_pipeline_run


default_args = {
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    dag_id="enterprise_etl_pipeline",
    start_date=datetime(2026, 1, 21),
    schedule_interval=None,
    catchup=False,
    default_args=default_args,
) as dag:

    test_task = BashOperator(
        task_id="test_task",
        bash_command="echo 'ETL pipeline working inside Docker'",
    )

    ingestion = PythonOperator(
        task_id="ingestion",
        python_callable=ingestion_run,
    )

    cleaning = PythonOperator(
        task_id="cleaning",
        python_callable=cleaning_run,
    )

    validation = PythonOperator(
        task_id="validation",
        python_callable=validation_run,
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=transform_run,
    )

    load = PythonOperator(
        task_id="load",
        python_callable=load_run,
    )

    log_metadata = PythonOperator(
        task_id="log_metadata",
        python_callable=log_pipeline_run,
        op_kwargs={"status": "SUCCESS"},
        provide_context=True,
    )

    ingestion >> cleaning >> validation >> transform >> load #>> log_metadata
