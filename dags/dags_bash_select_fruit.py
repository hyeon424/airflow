from airflow import DAG

import pendulum
import datetime

from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_select_fruit",
    schedule="10 0 * * 6#1",
    start_date=pendulum.datetime(2025, 8, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    task1_apple = BashOperator(
        task_id="task1_apple",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh APPLE",
    )
    
    task2_avocado = BashOperator(
        task_id="task2_avocado",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh AVOCADO",
    )
    
    task1_apple >> task2_avocado