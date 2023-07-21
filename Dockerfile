FROM python:3.8-slim

EXPOSE 8080

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering
ENV PYTHONUNBUFFERED=1
ENV PORT 8080
ENV SENTRY_DSN https://26676060bb3c46d4bb92026571455074@o4504589836222464.ingest.sentry.io/4504589836222464
ENV SECRET_KEY fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
RUN apt-get -y update; apt-get -y install curl

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

CMD gunicorn lettings_site.wsgi --bind 0.0.0.0:$PORT
