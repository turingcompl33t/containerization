## Web

Containerizing a simple web service.

### Setup

Create a virtual environment and activate it:

```bash
python -m venv env
source ./env/bin/activate
```

Ensure that your editor resolves your virtual environment. This is typically done in the editor GUI.

Install dependencies:

```bash
pip install flask
```

### Development

Write the following simple program:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"
```

Start the server:

```bash
python -m flask --app src/app run
```

Visit `localhost:5000` in a web browser to verify that the application works as expected. Alternatively, we can hit the server endpoint from the command prompt:

```bash
curl http://localhost:5000
```

We now have a functioning web server. It is time to containerize it.

### Containerization

Create a file that defines the requirements for our application:

```bash
pip freeze > requirements.txt
```

Define the image in `Dockerfile`:

```Dockerfile
FROM python:3.8-alpine

RUN mkdir /app
WORKDIR /app

ADD requirements.txt .
RUN python -m pip install -r requirements.txt

ADD src/ .

CMD ["python", "-m", "flask", "--app", "src/app.py:app", "run", "--host=0.0.0.0"]
```

Build the image with Docker:

```bash
docker build -t web .
```

Run a local copy of the image:

```bash
docker run --rm -p 5000:5000 web
```

Again, visit `localhost:5000` in your web browser to verify that the application is working correctly, or hit the server with:

```bash
curl http://localhost:5000
```