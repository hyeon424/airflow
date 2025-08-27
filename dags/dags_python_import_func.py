from airflow.sdk import DAG

import pendulum
import datetime

from airflow.operators.python import PythonOperator

from common.common_func import get_sftp # airflow 기준으로 path를 설정해주어야 함 -> .env



with DAG(
    dag_id="dags_python_import_func",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2025, 8, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    task_get_sftp = PythonOperator(
        task_id="task_get_sftp",
        python_callable=get_sftp
    )