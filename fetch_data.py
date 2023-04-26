import pandas_datareader as pdr
from google.cloud import storage
from dotenv import load_dotenv
import os
from pathlib import Path


def configure():
    load_dotenv()

# Create a storage_client using your GCS credentials
creds_path = Path(__file__).resolve().parent / 'creds.json'
creds_path.write_text(os.getenv("CREDS"))
storage_client = storage.Client.from_service_account_json(str(creds_path))
creds_path.unlink()  # immediately delete the creds

# Create a new GCS bucket
bucket_name = 'rohan_bkk'
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
