from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg

# Criar uma SparkSession
spark = SparkSession.builder.appName("AnaliseVendas").getOrCreate()

# Criar um DataFrame
dados = [(f"Produto{i % 10}", i % 50, (i % 10) * 100 + 50) for i in range(1, 1001)]
colunas = ["Produto", "Quantidade", "Preco"]

df = spark.createDataFrame(dados, colunas)

# Mostrar as primeiras 20 linhas do DataFrame
df.show()

# Realizar algumas operações:

# 1) Calcular a receita total por produto
df = df.withColumn("Receita", col("Quantidade") * col("Preco"))
receita_df = df.groupBy("Produto").agg(sum("Receita").alias("Receita_Total"))

# 2) Calcular a média de vendas por produto
media_vendas_df = df.groupBy("Produto").agg(avg("Receita").alias("Media_Vendas"))

# Mostrar o resultado das agregações
print("Receita Total por Produto:")
receita_df.show()

print("Média de Vendas por Produto:")
media_vendas_df.show()

# Parar a SparkSession
spark.stop()