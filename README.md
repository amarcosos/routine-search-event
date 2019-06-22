
# Routine Search Event

## Sympla events page crawler Python + MongoDB + Docker

This file contains all the instructions for running the project in your machine.

## Table of Contents

1. [Dependencies](#dependencies)
1. [Getting Started](#getting-started)
1. [Commands](#commands)
1. [Database](#database)
1. [Application Structure](#application-structure)
1. [Development](#development)
1. [Testing](#testing)
1. [Lint](#lint)

## Dependencies

You will need [docker](https://docs.docker.com/engine/installation/) and [docker-compose](https://docs.docker.com/compose/install/).

## Getting Started

First, clone the project:

```bash
$ git clone https://github.com/amarcosos/routine-search-event.git <my-project-name>
$ cd <my-project-name>
```

Then install dependencies and check that it works

```bash
$ make install      # Install the pip dependencies on the docker container
$ make start        # Run the local server routine in its own docker container
```

The aplication runs locally on docker containers. You can easily change the python version you are willing to use [here](https://github.com/amarcosos/routine-search-event/blob/master/docker-compose.yml#L4), by fetching a docker image of the python version you want.

## Commands

While evaluating the application, you are likely to rely primarily on `make start`; however, there are additional scripts at your disposal:

| `make <script>` | Description                                                                  |
| --------------- | ---------------------------------------------------------------------------- |
| `install`       | Install the pip dependencies on the server's container.                      |
| `start`         | Run the local server routine in its own docker container.                    |
| `daemon`        | Run your local server in its own docker container as a daemon.               |
| `test`          | Run unit tests with pytest in its own container.                             |
| `coverage`      | Run test coverage using pytest-cov.                                          |
| `lint`          | Run flake8 on the `src` and `test` directories.                              |
| `safety`        | Run safety to check if your vendors have security issues.                    |

## Database

The database is in [mongoDB](https://www.mongodb.com).

Locally, you can connect to your database using :

```bash
$ make connect
```

## Application Structure

The application structure presented in this boilerplate is grouped primarily by file type. Please note, however, that this structure is only meant to serve as a guide, it is by no means prescriptive.

```
.
├── devops                            # Project devops configuration settings
│   └── deploy                        # Environment-specific configuration files for shipit
├── src                               # Application source code
│   ├── connection                    # Python classes that connects to the database
│   │   └── mongo_connection.py       # Definition of the user model
│   ├── repositories                  # Python classes allowing you to interact with your models
│   │   └── destination_repository.py # Methods to easily handle event templates
│   │   └── source_repository.py      # Crawler methods for easily manipulating event page templates
│   ├── services                      # Python classes allowing you to interact with your source and destination models
│   │   └── processor_service.py      # Methods to easily perform the ETL process on the source and target event models
│   ├── util                          # Some helpfull, non-business Python functions for your project
│   │   └── multi_thread_manager.py   # Methods to apply mult-thread in ETL processes
│   ├── config.py                     # Project configuration settings
│   ├── main.py                       # Project commands
│   └── server.py                     # Server configuration
└── test                              # Unit tests source code
```

## Development

To develop locally, here are your two options:

```bash
$ make start           # Create the containers containing your python server in your terminal
$ make daemon          # Create the containers containing your python server as a daemon
```

The containers will reload by themselves as your source code is changed.
You can check the logs in the `./server.log` file.

## Testing

To add a unit test, simply create a `test_*.py` file anywhere in `./test/`, prefix your test classes with `Test` and your testing methods with `test_`. Unittest will run them automaticaly.
You can add objects in your database that will only be used in your tests, see example.
You can run your tests in their own container with the command:

```bash
$ make test
```

## Lint

To lint your code using flake8, just run in your terminal:

```bash
$ make lint
```

It will run the flake8 commands on your project in your server container, and display any lint error you may have in your code.

#### Author
#### Antônio Marcos de Oliveira Souza
