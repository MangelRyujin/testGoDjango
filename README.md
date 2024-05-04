# Test GoDjango

## Previous knowledge
<!-- UL -->
1. [Git](https://github.com/)
2. [Python](https://www.python.org/)
3. [Django](https://www.djangoproject.com/)
4. [Django Rest Framework](https://www.django-rest-framework.org/)


## Getting started

Follow the steps below to install the app in your corresponding environment

## Download the repository via git

```
# Clone git repo in your path
git clone https://github.com/MangelRyujin/testGoDjango.git

# Change to dev branch 
git checkout dev          
```

## Development environment 

Create your virtual env 

```
Example:
python -m venv env    
```
Linux Run env
```
source env/bin/activate
```

Windows Run env
```
env\Scripts\activate
```


## Install the project requirements

>Run next comand 
```
pip install -r requirements.txt
```

## Configure .env file with environment variables


Create your .env and configure it if you use production environment. 

#### First run the command in the cmd 

By default it is in: task.settings.development
```python
set DJANGO_SETTINGS_MODULE=task.settings.production
```


```
ENGINE = <your db engine>                   # default django.db.backends.postgresql
DB_NAME = <your db name>                    # default postgres
DB_USER = <your db user>                    # default postgres
DB_PASSWORD = <your db password>            # default postgres
DB_HOST = <your db host>                    # default 127.0.0.1
DB_PORT = <your db port>                    # default 5432
SECRET_KEY= <your secret key>
EMAIL_BACKEND = <your email backend>        # default django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST = <your email host>              # default smtp.gmail.com
EMAIL_USER = <your email user>              # default zona0django@gmail.com
EMAIL_PASSWORD = <your email password>      # default vuyt nhje qnrb npqb

```

## Run migrations

```python
python manage.py migrate
```

## If you want to create a super user
##### Remember to enter real emails so that the task editing messages can reach multiple users.

```python
python manage.py createsuperuser
```

## Run test

The tests have been created to create and update tasks
```python
python manage.py test
```
If everything is correct the answer should look like:

```
Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
Destroying test database for alias 'default'...
```

## Run server

```python
python manage.py runserver
```

## To dockerize the project visit the following link and apply it to your current project


https://dev.to/adgaray/dockerizar-un-proyecto-django-2np3