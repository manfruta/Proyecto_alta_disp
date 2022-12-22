FROM python:3.8.5-alpine
RUN apk add postgresql-dev
COPY . /cronjob
WORKDIR /cronjob

RUN pip install --upgrade pip
RUN pip install psycopg2-binary
RUN pip install requests 
RUN pip install beautifulsoup4
RUN crontab cronjob
CMD crond && tail -f /cronjob/out.log