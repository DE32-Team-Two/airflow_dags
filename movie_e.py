import sys
from datetime import datetime, timedelta
from textwrap import dedent
from pprint import pprint

from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

from airflow.operators.python import (
    PythonOperator,
    BranchPythonOperator,
    PythonVirtualenvOperator,

)

with DAG(
        'movie_e',
        default_args={
            'depends_on_past': False,
            'retries': 1,
            'retry_delay': timedelta(seconds=3)
        },
        max_active_runs=1,
        max_active_tasks=3,
        description='movie',
        schedule="0 0 1 * *",
        start_date=datetime(2024, 7, 24),
        catchup=True,
        tags=['api', 'movie', 'amt'],
) as dag:


    start = BashOperator(
        task_id="start",
        bash_command="echo 'start'"
    )

    one_to_four = BashOperator(
        task_id="one_to_four",
        bash_command='echo "oneTofour"'
    )
    
    five_to_eight = BashOperator(
        task_id="five_to_eight",
        bash_command='echo "oneTofour"'
    )

    nine_to_twelve = BashOperator(
        task_id="nine_to_twelve",
        bash_command='echo "oneTofour"'
    )


    end = BashOperator(
        task_id="end",
        bash_command="echo 'end'"
    )

    start >> [one_to_four, five_to_eight, nine_to_twelve] >> end
