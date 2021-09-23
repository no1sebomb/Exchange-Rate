# syntax=docker/dockerfile:1
FROM python:3.8

# Define work directory
WORKDIR /

# Update pip & install pipenv
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade pipenv --no-cache-dir

# Copy lists
COPY . .

# Install dependencies
RUN pipenv install --deploy --system --ignore-pipfile

# Expose server port
EXPOSE 5000

# Run WSGI
CMD ["gunicorn", "wsgi:app", "-c", "gunicorn.py"]
