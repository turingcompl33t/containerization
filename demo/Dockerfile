FROM python:3.8-alpine

RUN mkdir /app
WORKDIR /app

ADD src /app/src

RUN mkdir /mount
WORKDIR /mount

ENTRYPOINT ["python", "/app/src/main.py"]
