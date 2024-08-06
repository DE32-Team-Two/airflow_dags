import sys
from datetime import datetime, timedelta
from textwrap import dedent

from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

from airflow.operators.python import (
    PythonOperator,
    BranchPythonOperator,
    PythonVirtualenvOperator,

)

with DAG(
        'movie_l',
        default_args={
            'depends_on_past': False,
            'retries': 0,
            'retry_delay': timedelta(seconds=3)
        },
        max_active_runs=1,
        max_active_tasks=3,
        description='movie',
        schedule="2 0 1 * *",
        start_date=datetime(2022, 1, 1),
        end_date=datetime(2022, 12, 31),
        catchup=True,
        tags=['api', 'movie', 'amt'],
) as dag:


    start = BashOperator(
        task_id="start",
        bash_command="echo 'start'"
    )

    def get_tabulate(ds_nodash):
        from load.api.util import tabulate_df

        before, after = tabulate_df(ds_nodash)
        print("*"*20)
        print(before)
        print("*"*20)
        print(after)
        print("*"*20)
        

    tabulate_L = PythonVirtualenvOperator(
        task_id="one_to_four",
        python_callable=get_tabulate,
        requirements=["git+https://github.com/DE32-Team-Two/Load.git@d3.0.0/tabulate"],
        system_site_packages=False,
        
    )
    
    end = BashOperator(
        task_id="end",
        bash_command="echo 'end'",
		trigger_rule='one_success'
    )

    start >> tabulate_L >> end
