from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
import json
import random

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 7),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

def get_character_info(character_id, **kwargs):
    url = f"https://api.disneyapi.dev/character/{character_id}"
    response = requests.get(url)
    character_info = response.json()
    
    # 
    key_name = ''
    if character_id % 2 == 0:
        key_name = 'even'
    else:
        key_name = 'odd'

    # Store character info in XCom for later use
    kwargs['ti'].xcom_push(key=f'character_info_{key_name}', value=character_info)



def process_character_info(**kwargs):
    # Retrieve character info from XCom
    even_character_info = kwargs['ti'].xcom_pull(key='character_info_even')
    odd_character_info = kwargs['ti'].xcom_pull(key='character_info_odd')

    id_even = even_character_info['data']['_id']
    id_odd = odd_character_info['data']['_id']

    local_path = f'/opt/airflow/dags/character_{id_even}_plus_{id_odd}_info.txt'

    combined_info = {
        "even_character_info": even_character_info,
        "odd_character_info": odd_character_info
    }
    with open(local_path, "w") as file:
        json.dump(combined_info, file)


with DAG('fetch_disney_character_info', 
         default_args=default_args,
         description='Fetch two characters info from Disney API, merge the information and save to local file', 
         schedule_interval=timedelta(minutes=5)) as dag:

    get_even_character_info = PythonOperator(
        task_id='get_even_character_info',
        python_callable=get_character_info,
        op_kwargs={'character_id': random.randint(1, 500) * 2 }
    )

    get_odd_character_info = PythonOperator(
        task_id='get_odd_character_info',
        python_callable=get_character_info,
        op_kwargs={'character_id': random.randint(1, 500) * 2 + 1}
    )

    process_character_info = PythonOperator(
        task_id='process_character_info',
        python_callable=process_character_info
    )

    get_even_character_info >> process_character_info
    get_odd_character_info >> process_character_info
