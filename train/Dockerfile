# Dockerfile
# Image definition for classifier training.

FROM python:3.8-slim-buster

# Create a workspace
RUN mkdir /mount
WORKDIR /mount

# Install requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

# Add source
ADD src ./src

ENTRYPOINT ["python", "/mount/src/train.py"]