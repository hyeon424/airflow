import datetime

import pendulum

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id='dags_bash_operator',  # DAG 파일명과 ID는 일치시키는 것이 권장됨
    schedule='0 0 * * *',

    # start_date와 catchup은 같이 보아야 함
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False,  # 일반적으로는 False가 default

    # dagrun_timeout=datetime.timedelta(minutes=60), # timeout되면 stop시킴
    # tags=['example', 'example2'],
    # params={"example_key": "example_value"},
) as dag:
    # [START howto_operator_bash]
    bash_task1 = BashOperator(
        task_id='bash_task1', # DAG와 마찬가지로 일치시키는 것이 권장됨
        bash_command='echo whoami',
    )

    bash_task2 = BashOperator(
        task_id='bash_task2',
        bash_command='echo $HOSTNAME', # 해당 task 실행의 출력 결과를 통해 worker container가 수행했음을 알 수 있음
    )
    
    bash_task1 >> bash_task2
