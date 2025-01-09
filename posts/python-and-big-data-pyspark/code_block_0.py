from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PySparkExample").getOrCreate()

data = [1, 2, 3, 4, 5]
rdd = spark.sparkContext.parallelize(data)

squared_rdd = rdd.map(lambda x: x * x)
sum_of_squares = squared_rdd.sum()

print(f"Sum of squares: {sum_of_squares}")

spark.stop()