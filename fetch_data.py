import pandas_datareader as pdr
from google.cloud import storage
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()

creds = os.getenv("CREDS")
# Set your GCS credentials
storage_client = storage.Client.from_service_account_json(creds)

# from google.oauth2 import service_account
# Set your GCS credentials
# auth = os.environ.get('CREDS')
# creds = os.getenv("CREDS")
# auth = service_account.Credentials.from_service_account_info(creds)
# print(type(auth))
# storage_client = storage.Client(credentials=creds)

bucket_name = 'rohan_bkk'
# Create a new GCS bucket
bucket = storage_client.create_bucket(bucket_name)

print(f'Bucket {bucket_name} created.')

# Fetch data with pandas_datareader
api_key = os.getenv("KEY")
df = pdr.get_data_tiingo('NDAQ', api_key)

# Convert DataFrame to CSV file
csv_file = 'data.csv'
df.to_csv(csv_file, index=False)

# Upload file to GCS bucket
bucket = storage_client.get_bucket(bucket_name)
blob = bucket.blob(csv_file)
blob.upload_from_filename(csv_file)
