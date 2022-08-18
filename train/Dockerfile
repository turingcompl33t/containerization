# Dockerfile
# Image definition for classifier training.

FROM python:3.8-alpine

# Create a workspace
RUN mkdir /mount
WORKDIR /mount

# Install dependencies
RUN apk --no-cache add musl-dev linux-headers g++

# Install requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

ENTRYPOINT ["python", "src/train.py"]