# syntax=docker/dockerfile:1
FROM python:3.8

# Define work directory
WORKDIR /

# Update pip & install pipenv
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade pipenv --no-cache-dir

# Copy files
COPY . .

# Install dependencies
RUN pipenv install --deploy --system --ignore-pipfile

# Expose server port
EXPOSE 5000

# Install crontab updater dependencies
RUN apt-get update
RUN apt-get install cron -y
RUN apt-get install curl -y

# Run updater
RUN chmod +x ./app/utils/update.sh
RUN ./app/utils/update.sh

# Run WSGI
CMD ["gunicorn", "wsgi:app", "-c", "gunicorn.py"]
