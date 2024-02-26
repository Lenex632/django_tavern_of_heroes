#!/bin/bash

python manage.py makemigrations --no-input tavern_of_heroes
python manage.py migrate --no-input
python manage.py createsuperuser
python manage.py loaddata db.json
python manage.py runserver 0.0.0.0:8000