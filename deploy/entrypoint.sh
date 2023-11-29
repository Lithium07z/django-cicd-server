#!/bin/bash

python3 manage.py migrate
python3 manage.py makemigrations
gunicorn -b 0.0.0.0:8000 config.wsgi:application
