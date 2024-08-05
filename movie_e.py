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
        schedule="0 0 * * *",
        start_date=datetime(2022, 1, 1),
        catchup=True,
        tags=['api', 'movie', 'amt'],
) as dag:


    start = BashOperator(
        task_id="start",
        bash_command="echo 'start'"
    )

    def get_one_echo(ds_nodash):
        import sys
        from extract.api.one_to_four import ice_b, save2df
        if int(ds_nodash[4:6]) < 5:
            save2df(ds_nodash)
        else:
            sys.exit(1)

    def get_five_echo(ds_nodash):
        from extract.api.five_to_eight import ice_breaking, save2df
        if 4 < int(ds_nodash[4:6]) < 9:
            save2df(ds_nodash)
        else:
            sys.exit(1)

    def get_eight_echo(ds_nodash):
        from extract.api.nine_to_twelve import ice_breaking, save2df
        if 8 < int(ds_nodash[6:]):
            save2df(ds_nodash)
        else:
            sys.exit(1)

    one_to_four = PythonVirtualenvOperator(
        task_id="one_to_four",
        python_callable=get_one_echo,
        requirements=["git+https://github.com/DE32-Team-Two/Extract.git@d2.0.0/parquet"],
        system_site_packages=False,
        
    )
    
    five_to_eight = PythonVirtualenvOperator(
        task_id="five_to_eight",
        python_callable=get_five_echo,
        requirements=["git+https://github.com/DE32-Team-Two/Extract.git@d2.0.0/parquet"],
        system_site_packages=False,
    )

    nine_to_twelve = PythonVirtualenvOperator(
        task_id="nine_to_twelve",
        python_callable=get_eight_echo,
        requirements=["git+https://github.com/DE32-Team-Two/Extract.git@d2.0.0/parquet"],
        system_site_packages=False,
    )


    end = BashOperator(
        task_id="end",
        bash_command="echo 'end'",
		trigger_rule=one_success
    )

    start >> [one_to_four, five_to_eight, nine_to_twelve] >> end
