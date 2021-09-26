#!/bin/bash
bash ./app/utils/update.sh
gunicorn wsgi:app -c gunicorn.py