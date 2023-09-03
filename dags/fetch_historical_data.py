from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import requests


def fetch_historical_data():
    # Replace with your API endpoint
    deployment_url = "localhost:5000"
    url = f"http://{deployment_url}/fetchHistoricalData/AAPL"
    response = requests.get(url)
    print(response.json())


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 8, 30),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('fetch_historical_data',
         default_args=default_args,
         description='A simple DAG to fetch historical data',
         schedule_interval=timedelta(days=1),
         ) as dag:
    fetch_historical_data_task = PythonOperator(
        task_id='fetch_historical_data',
        python_callable=fetch_historical_data,
    )

fetch_historical_data_task
