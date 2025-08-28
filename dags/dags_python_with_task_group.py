import pendulum

from airflow.sdk import DAG, task, task_group
from airflow.utils.task_group import TaskGroup

from airflow.providers.standard.operators.python import PythonOperator


with DAG(
    dag_id="dags_python_with_task_group",
    schedule=None,
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    def inner_func(**kwargs):
        message = kwargs.get("msg") or ''
        print(message)
        
    @task_group(group_id='first_group')
    def group_1():
        # task_group 데커레이터를 이용한 첫 번째 그룹
        @task(task_id='inner_fucntion_1')
        def inner_func1(**kwargs):
            print('첫 번째 TaskGroup 내 첫 번째 task입니다.')
        
        inner_func2 = PythonOperator(
            task_id='inner_func2',
            python_callable=inner_func,
            op_kwargs={'msg': '첫 번째 TaskGroup 내 두 번째 task입니다.'}
        )
        
        inner_func1() >> inner_func2
        
    with TaskGroup(group_id='second_group', tooltip='두 번째 TaskGroup입니다.') as group_2:
        # 이곳에 작성한 docstring은 표시되지 않습니다.
        @task(task_id='inner_function_1')
        def inner_func1(**kwargs):
            print('두 번째 TaskGroup 내 첫 번째 task입니다.')
            
        inner_func2 = PythonOperator(
            task_id='inner_func2',
            python_callable=inner_func,
            op_kwargs={'msg': '두 번째 TaskGroup 내 두 번째 task입니다.'}
        )
        
        inner_func1() >> inner_func2
        
    group_1() >> group_2