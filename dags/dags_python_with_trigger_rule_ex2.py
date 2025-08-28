import pendulum

from airflow.sdk import DAG, task

from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator

from airflow.exceptions import AirflowException


with DAG(
    dag_id="dags_python_with_trigger_rule_ex1",
    schedule=None,
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    @task.branch(task_id='branching')
    def random_branch():
        import random

        item_list = ['A', 'B', 'C']
        selected_item = random.choice(item_list)

        if selected_item == 'A':
            return 'return task A'
        elif selected_item == 'B':
            return 'return task B'
        else:
            return 'return task C'

    task_a = BashOperator(
        task_id='task_a',
        bash_command='echo upstream 1'
    )

    @task(task_id='task_b')
    def task_b():
        print('정상 처리')

    @task(task_id='task_c')
    def task_c():
        print('정상 처리')

    @task(task_id='task_d', trigger_rule="none_skipped")
    def task_d():
        print('정상 처리')

    random_branch() >> [task_a, task_b(), task_c()] >> task_d()
