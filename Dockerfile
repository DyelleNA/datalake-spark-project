FROM openjdk:8-jdk-alpine 
RUN apk add --no-cache bash 
RUN mkdir /app 
WORKDIR /app 
ADD https://archive.apache.org/dist/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz /app 
RUN tar -xvzf spark-3.0.1-bin-hadoop2.7.tgz && mv spark-3.0.1-bin-hadoop2.7 spark && rm spark-3.0.1-bin-hadoop2.7.tgz 
ENV SPARK_HOME=/app/spark 
ENV PATH=$SPARK_HOME/bin:$PATH 
