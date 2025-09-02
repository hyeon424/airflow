import pendulum

from airflow.sdk import DAG
from airflow import Dataset
# from airflow.sdk import task, task_group

# from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.bash import BashOperator
# from airflow.providers.standard.operators.python import PythonOperator
# from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator

# from airflow.utils.task_group import TaskGroup
# from airflow.utils.edgemodifier import Label


dataset_dags_dataset_producer_2 = Dataset("dags_dataset_producer_2")

with DAG(
    dag_id="dags_dataset_producer_2",
    schedule="0 8 * * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    bash_task = BashOperator(
        task_id="bash_task",
        outlets=[dataset_dags_dataset_producer_2],
        bash_command='echo "producer_2 수행 완료'
    )