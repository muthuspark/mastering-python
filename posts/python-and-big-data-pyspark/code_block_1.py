from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.appName("PySparkDataFrame").getOrCreate()

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True)
])

data = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]

df = spark.createDataFrame(data, schema)

df.show() # Display the DataFrame
df.printSchema() # Display the schema
filtered_df = df.filter(df["id"] > 1) # Filter rows where id > 1
filtered_df.show()

spark.stop()