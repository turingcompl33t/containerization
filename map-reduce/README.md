## MapReduce

This repository demonstrates a simple data pipeline over the local filesystem. The demonstrated application is a "MapReduce" style pipeline that implements the word count program.

### Contents

- `map/`: Implementation for the `map` container.
- `reduce/`: Implementation for the `reduce` container.

### Deploy

These steps assume that sample data is present at `./data/input/data.txt`.

Run the `map` operation:

```bash
docker run -v $(pwd)/data:/mnt/data map /mnt/data/input/data.txt /mnt/data/mapped/out.txt
```

Run the `reduce` operation:

```bash
docker run -v $(pwd)/data:/mnt/data reduce /mnt/data/mapped/out.txt /mnt/data/output/out.txt
```