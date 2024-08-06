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
        'movie_t',
        default_args={
            'depends_on_past': False,
            'retries': 0,
            'retry_delay': timedelta(seconds=3)
        },
        max_active_runs=1,
        max_active_tasks=3,
        description='movie',
        schedule="0 0 1 * *",
        start_date=datetime(2022, 1, 1),
        end_date=datetime(2022, 12, 31),
        catchup=True,
        tags=['api', 'movie', 'amt'],
) as dag:


    start = BashOperator(
        task_id="start",
        bash_command="echo 'start'"
    )

    def get_one_echo(ds_nodash):
        import sys
        from transform.api.util import merge

        if ds_nodash[4:6] != '01':
            merge(ds_nodash)
        

    merge_T = PythonVirtualenvOperator(
        task_id="one_to_four",
        python_callable=get_one_echo,
        requirements=["git+https://github.com/DE32-Team-Two/Transform.git@d3.0.0/merge"],
        system_site_packages=False,
        
    )
    
    end = BashOperator(
        task_id="end",
        bash_command="echo 'end'",
		trigger_rule='one_success'
    )

    start >> merge_T >> end
