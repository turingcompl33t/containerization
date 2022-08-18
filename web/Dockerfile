# Dockerfile
# Image definition for web service.

FROM python:3.8-alpine

# Create and switch context to a working directory
RUN mkdir /app
WORKDIR /app

# Add requirements
ADD requirements.txt .
# Install requirements
RUN python -m pip install -r requirements.txt

# Add source
ADD src/ .

# Run the web server
CMD ["python", "-m", "flask", "--app", "src/app.py:app", "run", "--host=0.0.0.0"]
