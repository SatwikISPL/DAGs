from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG(
    'a_first',
    description='The simplest DAG',
    schedule_interval=None,
    start_date=datetime(2023, 10, 27),
    catchup=False
)

task = BashOperator(
    task_id='simplest_task',
    bash_command='echo "Hello, World!"',
    dag=dag
)

task

