# Python Client Library Example for InfluxDB 2

## Setup

Currently this example can be setup with the following commands:

```console
# This puts you inside a container
make dshell

# From inside the container, run:
make setup
make load-data
```

## Dependencies

```console
pipenv install
```

## Read

```console
pipenv run python src/read.py
```

## Write

I will add Python write examples in time.
