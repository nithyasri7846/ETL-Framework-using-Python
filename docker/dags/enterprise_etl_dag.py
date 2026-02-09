from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="enterprise_etl_pipeline",
    start_date=datetime(2026, 1, 21),
    schedule_interval=None,
    catchup=False,
) as dag:

    run_etl = BashOperator(
        task_id="run_etl_pipeline",
        bash_command="python /opt/airflow/enterprise_etl/run_test.py"
    )
