from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago
from airflow import DAG

from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator


# Example to run your job in every 2 mins you can use this in the schedule_interval argument
CRON_INTERVAL = '*/2 * * * *'


with DAG(
    dag_id='hamlet_gcp_operator_no_edit',
    start_date=days_ago(2),
    schedule_interval=CRON_INTERVAL,
    tags=['hamlet'],
    catchup=False
) as dag:

    start_task = DummyOperator(
        task_id='start_task',
    )

    local_file_system_to_bucket = LocalFilesystemToGCSOperator(
        task_id='local_file_system_to_bucket',
        google_cloud_storage_conn_id='gcp_connection_id',
        src='/opt/airflow/dags/data/hamlet_wordcounts.csv',
        dst='hamlet_nazli.csv',
        bucket='hamlet_exercises',
    )

    from_bucket_to_bigquery = GCSToBigQueryOperator(
        task_id='from_bucket_to_bigquery',
        google_cloud_storage_conn_id='gcp_connection_id',
        bigquery_conn_id='gcp_connection_id',
        bucket='hamlet_exercises',
        source_objects='hamlet_nazli.csv',
        destination_project_dataset_table='tutorial_hamlet.hamlet_nazli',
        field_delimiter='|',
        write_disposition='WRITE_TRUNCATE',
        skip_leading_rows=1,
        schema_fields=[
            {'name': 'word', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'counts', 'type': 'INT64', 'mode': 'NULLABLE'},
        ],
        # You will be filling here
    )

    end_task = DummyOperator(
        task_id='end_task',
    )

    start_task >> local_file_system_to_bucket >> from_bucket_to_bigquery >> end_task
