import pendulum

from datetime import datetime
from dateutil import relativedelta

from airflow.sdk import DAG, task
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="dags_bash_with_macro_ex2",
    schedule="10 0 * * 6#2",
    start_date=pendulum.datetime(2025, 7, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    # START_DATE: 2주전 월요일, END_DATE: 2주전 토요일
    bash_task_2 = BashOperator(
        task_id="bash_task_2",
        env={
            "START_DATE": "{{ (data_interval_start.in_timezone('Asia/Seoul') - macros.dateutil.relativedelta.relativedelta(weeks=2)) | ds }}",
            "END_DATE": "{{ (data_interval_end.in_timezone('Asia/Seoul') - macros.dateutil.relativedelta.relativedelta(weeks=2) + macros.timedelta(days=5)) | ds }}"
        },
        bash_command="echo \"START_DATE: $START_DATE\" && echo \"END_DATE: $END_DATE\""
    )
