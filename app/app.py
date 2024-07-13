from pyspark.sql import SparkSession

# Criar uma SparkSession
spark = SparkSession.builder.appName("DockerSparkExample").getOrCreate()

# Criar um DataFrame de exemplo
data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
columns = ["Name", "Value"]
df = spark.createDataFrame(data, columns)

# Mostrar o conteúdo do DataFrame
df.show()

# Parar a SparkSession
spark.stop()