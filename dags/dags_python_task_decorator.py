import pendulum

from airflow.sdk import DAG, task


with DAG(
    dag_id="dags_python_task_decorator",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    # [START howto_operator_python]
    @task(task_id="python_task_1")
    def print_context(some_input):
        print(some_input)

    # task decorator 사용으로 task간 실행 관계 표현을 명시해주지 않아도 됨
    python_task_1 = print_context('task_decorator 실행합니다.')
