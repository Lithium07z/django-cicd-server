#!/bin/bash

echo "a"
python3 manage.py makemigrations testapp
echo "b"
python3 manage.py migrate
echo "c"
python3 manage.py makemigrations
echo "d"
gunicorn -b 0.0.0.0:8000 config.wsgi:application
