## Train

Training a simple machine learning classifier.

### Setup

Create a virtual environment and activate it:

```bash
python -m venv env
source ./env/bin/activate
```

Ensure that your editor resolves your virtual environment. This is typically done in the editor GUI.

Install dependencies:

```bash
pip install wheel
pip install sklearn pandas
```

### Development

Grab a local copy of the dataset:

```bash
wget https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv 
```

Define the classifier and run it locally to ensure that it is saved properly.

### Containerization

Define the dockerfile:

```Dockerfile
TODO
```

Build the image:

```bash
docker build -t train .
```

Run the container to perform training:

```bash
docker run --rm -v ~/dev/containerization/train/mount:/mount train data/iris.csv models/model.pkl
```