FROM python:3.8-alpine

RUN mkdir /app
WORKDIR /app

ADD src /app/src

ENTRYPOINT ["python", "src/main.py"]
