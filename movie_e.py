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
        schedule="25 * * * *",
        start_date=datetime(2024, 7, 24),
        catchup=True,
        tags=['api', 'movie', 'amt'],
) as dag:


    start = BashOperator(
        task_id="start",
        bash_command="echo 'start'"
    )

    def get_one_echo():
        from extract.api.one_to_four import ice_b
        print(ice_b())

    def get_five_echo():
        from extract.api.five_to_eight import ice_breaking
        print(ice_breaking())

    def get_eight_echo():
        from extract.api.nine_to_twelve import ice_breaking
        print(ice_breaking())

    one_to_four = PythonVirtualenvOperator(
        task_id="one_to_four",
        python_callable=get_one_echo,
        requirements=["git+https://github.com/DE32-Team-Two/Extract.git@d1.0.0/20240802hotfix"],
        system_site_packages=False,
    )
    
    five_to_eight = PythonVirtualenvOperator(
        task_id="five_to_eight",
        python_callable=get_five_echo,
        requirements=["git+https://github.com/DE32-Team-Two/Extract.git@d1.0.0/20240802hotfix"],
        system_site_packages=False,
    )

    nine_to_twelve = PythonVirtualenvOperator(
        task_id="nine_to_twelve",
        python_callable=get_eight_echo,
        requirements=["git+https://github.com/DE32-Team-Two/Extract.git@d1.0.0/20240802hotfix"],
        system_site_packages=False,
    )


    end = BashOperator(
        task_id="end",
        bash_command="echo 'end'"
    )

    start >> [one_to_four, five_to_eight, nine_to_twelve] >> end
