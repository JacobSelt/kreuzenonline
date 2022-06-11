## Installation of Postgres and Django

### Instllation Of Postgresql For Linux: 

```sh
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
```

Log in to the postgres db (an operating system user named postgres was created to correspond to the postgres PostgreSQL administrative user)
```sh
sudo -u postgres psql
```

```sh
CREATE DATABASE kreuzenonline;
CREATE USER djangouser WITH PASSWORD '???????';
```

In order to speed up Django and Postgres
```sh
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
```

At the end log out: \q
```sh
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
\q
```

Change database settings according to your password and username

tutorial: https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-20-04

### Windows and Mac

Please look up tutorials.

## Virtual Env and Requirements

```sh
python -m venv env
source env/bin/activate
pip install requirements.txt
```

## Starting with Django

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
