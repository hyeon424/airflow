import pendulum

from airflow.sdk import DAG, task

from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="dags_bash_with_template",
    schedule="10 0 * * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    bash_task_1 = BashOperator(
        task_id="bash_task_1",
        bash_command="echo \"data_interval_end: {{ data_interval_end }}\""
    )

    bash_task_2 = BashOperator(
        task_id="bash_task_2",
        env={
            "START_DATE": "{{data_interval_start | ds}}",
            "END_DATE": "{{data_interval_end | ds}}"
        },
        # &&는 START_DATE가 출력이 되면 END_DATE를 출력한다는 bash script 문법
        bash_command="echo $START_DATE && echo $END_DATE"
    )
