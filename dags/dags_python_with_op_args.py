import pendulum

from airflow.sdk import DAG, task

from airflow.operators.python import PythonOperator
from common.common_func import regist


with DAG(
    dag_id="dags_python_with_op_args",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    regist_task1 = PythonOperator(
        task_id="regist_task1",
        python_callable=regist,
        op_args=["John", "Male", "Engineer", "New York"]
    )

    regist_task1
