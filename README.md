# Airflow GCP - Basic Exercises

1. We need to setup a connection to Google Cloud Platform using Airflow to interact with it. 

2. You will be given a csv file stating the word counts for the Shakespeare’s Hamlet. Insert this in the /dags/data folder. We will be uploading this into the GCP Storage buckets using your name ‘hamlet_<your_name>.csv’ needs to be in the bucket ‘hamlet_exercises’.
    * We need LocalFilesystemToGCSOperator for this task. 
    * Look at the documentation: https://airflow.apache.org/docs/apache-airflow-providers-google/1.0.0/operators/transfer/local_to_gcs.html 

3. From the GCP Storage we will be dumping our brand-new csv files to the ‘hamlet_exercises’ dataset in ‘your-bigquery-project’ with the table names ‘hamlet_<your_name>’. 
    * We need GCSToBigQueryOperator for this task. 
    * Look at the documentation: https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/transfers/gcs_to_bigquery/index.html 