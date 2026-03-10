# Owner - Rahul Jadhav
# Name - rahul.generic.py
# Use - Read data from CSV, process and write in JSON
# Created on - 14-02-2026
# Modified - 19-02-2026
# Version - 1.2.1
# Run Cmd : spark-submit rahul.generic.py

# Libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import json

# Spark Session
spark = SparkSession.builder.appName("CSV to JSON").getOrCreate()

# Function to read config file
def read_config_from_json(json_file):
    with open(json_file, 'r') as file:
        config = json.load(file)
    return config

# Read config
config_data = read_config_from_json("D:/config.json")

src_path = config_data.get("src_path", "")
trg_path = config_data.get("trg_path", "")

print("Source Path:", src_path)
print("Target Path:", trg_path)

# Function to read CSV
def read_csv(spark, path, deli=",", header="true"):
    df_product = spark.read.format("csv") \
        .option("header", header) \
        .option("delimiter", deli) \
        .option("inferSchema", "true") \
        .load(path)
    return df_product

# Main Code
df_product = read_csv(spark, src_path)

df_product.show()

# Filter Panasonic category
df1_Panasonic = df_product.where(col("CAT") == "Panasonic")

df1_Panasonic.show()

# Write JSON
df1_Panasonic.write.mode("overwrite").json(trg_path)

spark.stop()
