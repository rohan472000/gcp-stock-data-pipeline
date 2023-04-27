import subprocess
import time

# Set the project and region
PROJECT_ID = 'clean-phoenix-378215'
REGION = 'us-central1'

# Define the cluster name and configuration
CLUSTER_NAME = 'roh-435'
CLUSTER_CONFIG = '--num-workers=2 --master-machine-type=n1-standard-2 --worker-machine-type=n1-standard-2 --master-boot-disk-size=30GB --worker-boot-disk-size=100GB --image-version=2.0-debian10'.split()

# Define the PySpark job properties
JOB_FILE_URI = 'gs://rohan_bkk/dataproc_new.py'

# Upload the PySpark job file to the bucket
upload_file_cmd = ['gsutil', 'cp', 'dataproc_new.py', JOB_FILE_URI]
subprocess.run(upload_file_cmd, check=True)

# # Create the cluster
# create_cluster_cmd = ['gcloud', 'dataproc', 'clusters', 'create', CLUSTER_NAME,
#                       '--region', REGION, '--project', PROJECT_ID] + CLUSTER_CONFIG
# subprocess.run(create_cluster_cmd, check=True)
# Check if cluster already exists
describe_cluster_cmd = ['gcloud', 'dataproc', 'clusters', 'describe', CLUSTER_NAME,
                        '--region', REGION, '--project', PROJECT_ID]
result = subprocess.run(describe_cluster_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode == 0:
    print(f"Cluster '{CLUSTER_NAME}' already exists. Skipping creation.")
else:
    # Create the cluster
    create_cluster_cmd = ['gcloud', 'dataproc', 'clusters', 'create', CLUSTER_NAME,
                          '--region', REGION, '--project', PROJECT_ID] + CLUSTER_CONFIG
    subprocess.run(create_cluster_cmd, check=True)
    print(f"Cluster '{CLUSTER_NAME}' created successfully.")

# Wait for the cluster to be ready
time.sleep(60)

# Submit the PySpark job
submit_job_cmd = ['gcloud', 'dataproc', 'jobs', 'submit', 'pyspark', '--cluster', CLUSTER_NAME,
                  '--region', REGION, '--project', PROJECT_ID, '--properties', 'spark.submit.deployMode=cluster',
                  JOB_FILE_URI]
subprocess.run(submit_job_cmd, check=True)
