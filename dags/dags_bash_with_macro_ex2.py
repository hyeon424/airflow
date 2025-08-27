import pendulum

from datetime import datetime
from dateutil import relativedelta

from airflow.sdk import DAG, task
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="dags_bash_with_macro_ex2",
    # schedule="10 0 * * 6#2",
    schedule="10 0 1 * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=True,
) as dag:
    # START_DATE: 2주전 월요일, END_DATE: 2주전 토요일
    bash_task_2 = BashOperator(
        task_id="bash_task_2",
        env={
            "START_DATE": "{{ ( (dag_run.logical_date.in_timezone('Asia/Seoul')
                                 - macros.dateutil.relativedelta.relativedelta(weeks=2))
                                 - macros.timedelta(days=(dag_run.logical_date.in_timezone('Asia/Seoul')
                                                          - macros.dateutil.relativedelta.relativedelta(weeks=2)).weekday())
                               ) | ds }}",
            "END_DATE": "{{ ( ( (dag_run.logical_date.in_timezone('Asia/Seoul')
                                  - macros.dateutil.relativedelta.relativedelta(weeks=2))
                                  - macros.timedelta(days=(dag_run.logical_date.in_timezone('Asia/Seoul')
                                                           - macros.dateutil.relativedelta.relativedelta(weeks=2)).weekday())
                               ) + macros.timedelta(days=5) ) | ds }}",
        },
        bash_command="echo \"START_DATE: $START_DATE\" && echo \"END_DATE: $END_DATE\""
    )