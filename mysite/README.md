# django

## Create a project

`django-admin startproject mysite`

## Development server

`python manage.py runserver`

## Change the port

`py manage.py runserver 8080`

## Create the Poll app

`python manage.py startapp polls`

## Store changes to DB models

`py manage.py makemigrations polls`

### Create migrations

`py manage.py makemigrations`

## Run the migrations and manage DB schema automatically

`py manage.py sqlmigrate polls 0001`

## Checks for any problems in your project without making migrations or touching the database

`py manage.py check`

## Apply all migrations

`py manage.py migrate`
