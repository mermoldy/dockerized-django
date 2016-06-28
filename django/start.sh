#!/usr/bin/env bash

python manage.py collectstatic --no-input
python manage.py migrate
gunicorn src.wsgi:application -w 2 -b :8000