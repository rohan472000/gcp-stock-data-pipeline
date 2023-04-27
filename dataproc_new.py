
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg
from pyspark.sql.types import DoubleType

# Set the GCS bucket and file paths

bucket_name = 'rohan_bkk'
file_path = 'gs://rohan_bkk/data.csv'
output_path = 'gs://rohan_bkk/new_data.csv'
# Create a SparkSession
spark = SparkSession.builder.appName('ETL').getOrCreate()

# Load the CSV file from GCS into a PySpark DataFrame
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Add a new column to the DataFrame with the average of close, high, low, and open
df = df.withColumn('average', (col('close') + col('high') + col('low') + col('open')) / 4.0)

# Convert the 'average' column to DoubleType to avoid precision loss when writing to CSV
df = df.withColumn('average', col('average').cast(DoubleType()))

try:
    # Write the transformed data back to GCS as a CSV file
    df.write.format('csv').option('header', 'true').mode('overwrite').save(output_path)
    print('Data saved successfully to {}'.format(output_path))
except Exception as e:
    print('Error writing data to GCS: {}'.format(str(e)))

spark.stop()