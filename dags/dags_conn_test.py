from airflow import DAG

import pendulum
import datetime

from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(
    dag_id='dags_conn_test',
    schedule=None,
    start_date=pendulum.datetime(2025, 8, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    task1 = EmptyOperator(
        task_id = 'task1'
    )
    
    task2 = EmptyOperator(
        task_id = 'task2'
    )
    
    task3 = EmptyOperator(
        task_id = 'task3'
    )
    
    task4 = EmptyOperator(
        task_id = 'task4'
    )
    
    task5 = EmptyOperator(
        task_id = 'task5'
    )
    
    task6 = EmptyOperator(
        task_id = 'task6'
    )
    
    task7 = EmptyOperator(
        task_id = 'task7'
    )
    
    task8 = EmptyOperator(
        task_id = 'task8'
    )
    
    task1 >> [task2, task3] >> task4
    task5 >> task4
    [task4, task7] >> task6 >> task8