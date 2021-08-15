from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago
from airflow import DAG

from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator


# Example to run your job in every 2 mins you can use this in the schedule_interval argument
CRON_INTERVAL = '*/2 * * * *'


with DAG(
    dag_id='hamlet_gcp_operator',
    start_date=days_ago(2),
    schedule_interval=None,
    tags=['hamlet'],
    catchup=False
) as dag:

    start_task = DummyOperator(
        task_id='start_task',
    )

    local_file_system_to_bucket = LocalFilesystemToGCSOperator(
        task_id='local_file_system_to_bucket',
        google_cloud_storage_conn_id='gcp_connection_id',
        src='fill_this',
        dst='and_this',
        bucket='and_this',
        # You will be filling here
    )

    from_bucket_to_bigquery = GCSToBigQueryOperator(
        task_id='from_bucket_to_bigquery',
        google_cloud_storage_conn_id='gcp_connection_id',
        bigquery_conn_id='gcp_connection_id',
        bucket='fill_this',
        source_objects='and_this',
        destination_project_dataset_table='dataset.table_name',
        # You will be filling here
    )

    end_task = DummyOperator(
        task_id='end_task',
    )

    start_task >> end_task
