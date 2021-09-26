#!/bin/bash
bash ./app/utils/update.sh
flask db upgrade
gunicorn wsgi:app -c gunicorn.py