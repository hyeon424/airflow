import pendulum

from airflow.sdk import DAG
# from airflow.sdk import task, task_group
# from airflow.utils.task_group import TaskGroup

# from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.utils.edgemodifier import Label


with DAG(
    dag_id="dags_empty_with_edge_label",
    schedule=None,
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    empty_1 = EmptyOperator(
        task_id='empty_1'
    )
    
    empty_2 = EmptyOperator(
        task_id='empty_2'
    )
    
    empty_1 >> Label('1 & 2 사이') >> empty_2
    
    empty_3 = EmptyOperator(
        task_id='empty_3'
    )
    
    empty_4 = EmptyOperator(
        task_id='empty_4'
    )
    
    empty_5 = EmptyOperator(
        task_id='empty_5'
    )
    
    empty_6 = EmptyOperator(
        task_id='empty_6'
    )
    
    empty_2 >> Label('Start Branch') >> [empty_3, empty_4, empty_5] >> Label('End Branch') >> empty_6