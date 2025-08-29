import pendulum

from airflow.sdk import DAG
# from airflow.sdk import task, task_group

# from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.bash import BashOperator
# from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator

# from airflow.utils.task_group import TaskGroup
# from airflow.utils.edgemodifier import Label


with DAG(
    dag_id="dags_trigger_dag_run_operator",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    start_task = BashOperator(
        task_id='start_task',
        bash_command='echo "Start!"'
    )

    trigger_dag_task = TriggerDagRunOperator(
        task_id='trigger_dag_task', # 필수 값
        trigger_dag_id='dags_python_operator', # 필수 값
        trigger_run_id=None, # run_id 값 직접 지정
        logical_date='{{ data_interval_start }}', # manual__{{execution_date}}로 수행
        reset_dag_run=True, # 이미 run_id에 값이 있는 경우에도 재수행 할 것인지에 대한 유무
        wait_for_completion=False,
        poke_interval=60,
        allowed_states=['success'],
        failed_states=None
    )

    start_task >> trigger_dag_task
