import pendulum

from airflow.sdk import DAG, task

from airflow.operators.python import PythonOperator
from common.common_func import regist2


with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    regist2_task1 = PythonOperator(
        task_id="regist2_task1",
        python_callable=regist2,
        op_args=["John", "Male", "Engineer", "New York"],
        op_kwargs={"email": "blah@example.com", "phone": "123-456-7890"}
    )

    regist2_task1
