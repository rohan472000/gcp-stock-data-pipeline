import os

from google.cloud import bigquery
from google.oauth2 import service_account

# Replace these with your own values
PROJECT_ID = 'clean-phoenix-378215'
DATASET_ID = 'livestock'
TABLE_ID = 'first_table'

creds = os.getenv("CREDS")
credentials = service_account.Credentials.from_service_account_file(creds)

# Set up the BigQuery client
client = bigquery.Client(credentials=credentials, project=PROJECT_ID)

# Check if the table already exists
table_ref = client.dataset(DATASET_ID).table(TABLE_ID)
try:
    table = client.get_table(table_ref)
    print(f'Table {table.project}.{table.dataset_id}.{table.table_id} already exists')
except:
    # Construct a schema for the table
    schema = [
        bigquery.SchemaField("close", "FLOAT"),
        bigquery.SchemaField("high", "FLOAT"),
        bigquery.SchemaField("low", "FLOAT"),
        bigquery.SchemaField("open", "FLOAT"),
        bigquery.SchemaField("volume", "INTEGER"),
        bigquery.SchemaField("adjClose", "FLOAT"),
        bigquery.SchemaField("adjHigh", "FLOAT"),
        bigquery.SchemaField("adjLow", "FLOAT"),
        bigquery.SchemaField("adjOpen", "FLOAT"),
        bigquery.SchemaField("adjVolume", "INTEGER"),
        bigquery.SchemaField("divCash", "FLOAT"),
        bigquery.SchemaField("splitFactor", "FLOAT"),
        bigquery.SchemaField("average", "FLOAT"),
    ]

    # # Create the BigQuery table
    # table = bigquery.Table(table_ref, schema=schema)
    # table = client.create_table(table)
    # print(f'Table {table.project}.{table.dataset_id}.{table.table_id} created')
    # Check if table already exists
    if not client.exists(table_ref):
        # Create the BigQuery table
        table = bigquery.Table(table_ref, schema=schema)
        table = client.create_table(table)
        print(f'Table {table.project}.{table.dataset_id}.{table.table_id} created')
    else:
        print(f"Table '{table_ref.table_id}' already exists in dataset '{DATASET_ID}'. Skipping creation.")


import pandas as pd
import pandas_gbq

# Load the CSV file into a Pandas DataFrame
#df = pd.read_csv('gs://tinngobucket/new_data.csv/part-00000-d6e357ee-af2d-4ec2-90bf-0a18932d1c9b-c000.csv')
df = pd.read_csv('gs://rohan_bkk/new_data.csv/part-00000-74a1b7c6-034a-49fa-baad-9491064637f3-c000.csv')

# Upload the DataFrame to BigQuery
pandas_gbq.to_gbq(df, destination_table='{}.{}'.format(DATASET_ID, TABLE_ID), project_id=PROJECT_ID, if_exists='append')
