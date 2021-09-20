# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY ./oc_lettings/ /app/
RUN python manage.py collectstatic --noinput

RUN useradd stduser
USER stduser
CMD gunicorn --pythonpath oc_lettings oc_lettings_site.wsgi --bind 0.0.0.0:$PORT
