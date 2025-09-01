import pendulum

from airflow.sdk import DAG
# from airflow.sdk import task, task_group

# from airflow.providers.standard.operators.empty import EmptyOperator
# from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
# from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator

# from airflow.utils.task_group import TaskGroup
# from airflow.utils.edgemodifier import Label


with DAG(
    dag_id="dags_python_with_postgres",
    schedule=None,
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    def insrt_postgres(ip, port, dbname, user, passwd, **kwargs):
        import psycopg2

        from contextlib import closing

        with closing(psycopg2.connect(host=ip, port=int(port), dbname=dbname, user=user, password=passwd)) as conn:
            with closing(conn.cursor()) as cursor:
                dag_id = kwargs.get('ti').dag_id
                task_id = kwargs.get('ti').task_id
                run_id = kwargs.get('ti').run_id
                msg = 'insrt 수행'
                sql = 'insert into py_opr_drct_insrt values (%s,%s,%s,%s);'

                cursor.execute(sql, (dag_id, task_id, run_id, msg))

                conn.commit()

    insrt_postgres = PythonOperator(
        task_id='insrt_postgres',
        python_callable=insrt_postgres,
        op_args=['172.28.0.3', '5432', 'hspark', 'hspark', 'hspark']
    )

    insrt_postgres
