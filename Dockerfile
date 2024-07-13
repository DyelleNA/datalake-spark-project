# Usando uma imagem oficial do Spark com Python
FROM bitnami/spark:latest

# Instalando Python e dependências
USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-pip \
    python3-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho
WORKDIR /app

# Copie seus scripts Python para o contêiner
COPY . .

# Instale pacotes Python necessários
RUN pip3 install pandas

# Comando padrão para iniciar o Spark
CMD ["spark-submit", "seu_script.py"]
