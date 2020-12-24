from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

from airflow.operators import MyFirstOperator

dag = DAG('my_test_dag', description='DAG sample with custom operator',
          schedule_interval='0 12 * * *',
          start_date=datetime(2020, 3, 20), catchup=False)

start_task = DummyOperator(task_id='dummy_task', dag=dag)

operator_task = MyFirstOperator(my_operator_param='This is a test operator',
                                task_id='my_first_operator_task', dag=dag)
start_task >> operator_task