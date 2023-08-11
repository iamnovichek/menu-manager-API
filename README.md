# Installation


### Creating and Activating a Virtual Environment


```bash    
  python3 -m venv django
  source django/bin/activate
  pip3 install -r requirements.txt
```


# Installation postgresql-server and creating a database


```bash
  sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
  wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
  sudo apt-get update
  sudo apt-get install postgresql
```

### Creating a new user

```bash
  sudo -u postgres psql
  CREATE ROLE admin WITH LOGIN PASSWORD 'password';
```

### Creating a new database

```bash
  sudo -i -u postgres
  psql
  CREATE DATABASE menu;
```

### Creating migrations 


```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
```

### Creating a superuser 

```bash
  python3 manage.py createsuperuser
```

Finally:

```bash
  python3 manage.py runserver
```