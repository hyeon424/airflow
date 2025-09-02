import pendulum

from airflow.sdk import DAG
# from airflow import Dataset
# from airflow.sdk import task, task_group

# from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.bash import BashOperator
# from airflow.providers.standard.operators.python import PythonOperator
# from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator

# from airflow.utils.task_group import TaskGroup
# from airflow.utils.edgemodifier import Label


with DAG(
    dag_id="dags_bash_with_pool",
    schedule="10 0 * * 6",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    default_args={
        'pool': 'pool_small'
    }
) as dag:
    bash_task_1 = BashOperator(
        task_id="bash_task_1",
        bash_command='sleep 30',
        priority_weight=6
    )

    bash_task_2 = BashOperator(
        task_id="bash_task_2",
        bash_command='sleep 30',
        priority_weight=5
    )
    
    bash_task_3 = BashOperator(
        task_id="bash_task_3",
        bash_command='sleep 30',
        priority_weight=4
    )
    
    bash_task_4 = BashOperator(
        task_id="bash_task_4",
        bash_command='sleep 30'
    )
    
    bash_task_5 = BashOperator(
        task_id="bash_task_5",
        bash_command='sleep 30'
    )
    
    bash_task_6 = BashOperator(
        task_id="bash_task_6",
        bash_command='sleep 30',
    )
    
    bash_task_7 = BashOperator(
        task_id="bash_task_7",
        bash_command='sleep 30',
        priority_weight=7
    )
    
    bash_task_8 = BashOperator(
        task_id="bash_task_8",
        bash_command='sleep 30',
        priority_weight=8
    )
    
    bash_task_9 = BashOperator(
        task_id="bash_task_9",
        bash_command='sleep 30',
        priority_weight=9
    )