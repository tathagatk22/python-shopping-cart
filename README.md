## Problem Statement

[Problem Statement](documentations/problem_statement.md)

## Compile into a single file

Perform the below steps to create a single executable file.

```shell script
$ cd /src 
$ pip install -r requirements.txt
$ pyinstaller --onefile main.py
```

The last command will create a single executable file.

## Database

Postgres has been used as a database for this application

## How to run

#### Environment Variables Accepted:
- **DB_User** 
- **DB_Host**
- **DB_Name** 
- **DB_Password**
- **DB_Port**

## To host the database locally, we can use PostgreSQL Docker image

To run the database locally, please find the below steps,

```shell script
$ docker pull postgres
$ mkdir -p $HOME/volumes/postgres-backup
$ docker run --rm \
 --name pg-docker -e POSTGRES_PASSWORD=postgres \
 -d -p 5432:5432 -v $HOME/docker/postgres-backup:/var/lib/postgresql/data \
 postgres
# to check if container is running
$ docker ps -a
```