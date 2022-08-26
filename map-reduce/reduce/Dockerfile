FROM python:3.8-slim-buster

# Create a workspace
RUN mkdir -p /app
WORKDIR /app

# Copy source to container
COPY src/ /app/src/

# Run the application
ENTRYPOINT ["python", "src/reduce.py"]
