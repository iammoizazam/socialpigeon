FROM ubuntu:latest


LABEL Name="Social Pigeon" Version=1.4.2
LABEL org.opencontainers.image.source = "https://github.com/iammoizazam/socialpigeon"

ARG srcDir=src
WORKDIR /app
COPY $srcDir/requirements.txt .
RUN apt-get update
RUN apt-get install mysql-client -y
RUN apt-get install libmysqlclient-dev  -y
RUN pip install --no-cache-dir -r requirements.txt

COPY $srcDir/run.py .
COPY $srcDir/app ./app

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
