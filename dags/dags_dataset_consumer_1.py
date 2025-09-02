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


dataset_dags_dataset_producer_1 = Dataset("dags_dataset_producer_1")

with DAG(
    dag_id="dags_dataset_consumer_1",
    schedule=[dataset_dags_dataset_producer_1],
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    bash_task = BashOperator(
        task_id="bash_task",
        bash_command='echo {{ ti.run_id }} && echo "producer_1이 완료되면 수행"'
    )