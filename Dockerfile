FROM python:3.9-slim-buster
FROM mysql



# ROOT PASSWORD
ENV MYSQL_ROOT_PASSWORD=system@123

#ENV MYSQL_DATABASE=sampledb
ENV MYSQL_USER=moizazam
ENV MYSQL_PASSWORD=system@123


ENV MYSQL_DATA_DIR=/var/lib/mysql \
    MYSQL_RUN_DIR=/run/mysqld \
    MYSQL_LOG_DIR=/var/log/mysql

#ADD ["db_dump.sql", "/tmp/dump.sql"]

#RUN systemctl start mysql && \
#         mysql -u root -p$MYSQL_ROOT_PASSWORD  -e "create database socialpigeon;" 
#" && \
 #       mysql -u root -p${MYSQL_ROOT_PASSWORD}  < /tmp/dump.sql

#PORT
EXPOSE 3306


LABEL Name="Social Pigeon" Version=1.4.2
LABEL org.opencontainers.image.source = "https://github.com/iammoizazam/socialpigeon"

ARG srcDir=src
WORKDIR /app
COPY $srcDir/requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt

COPY $srcDir/run.py .
COPY $srcDir/app ./app

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
