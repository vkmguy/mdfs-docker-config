from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_hello():
    return 'Hello world!'

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 8, 29),
}

with DAG('hello_world',
         default_args=default_args,
         schedule_interval='@daily',
         ) as dag:

    start = DummyOperator(task_id='start')

    hello = PythonOperator(task_id='hello',
                           python_callable=print_hello)

    end = DummyOperator(task_id='end')

    start >> hello >> end