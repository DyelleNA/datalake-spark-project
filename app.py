from pyspark.sql import SparkSession 
spark = SparkSession.builder.appName\(\"SimpleApp\"\).getOrCreate\(\) 
data = [\(\"Alice\", 1\), \(\"Bob\", 2\), \(\"Cathy\", 3\)] 
df = spark.createDataFrame\(data, \[\"Name\", \"Value\"\]\) 
df.show\(\) 
spark.stop\(\) 
