# MAILBOX

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies](#technologies)
- [Usage](#usage)
- [Configuration](#configuration)
- [Running app](#running-app)
- [Database](#database)
- [Author](#author)

## Project Overview

This project is created to manage api for mailbox. Mailbox is created for managing asynchronous
tasks by using Celery and Redis. It is build using Django 4.2.7. Project has no own GUI, is available by API. 

## Technologies

The most important technologies used in the project:

- Python 3.12
- Django 4.2.7
- DjangoRestFramework 3.14.0
- Celery 5.3.4
- Redis 5.0.1
- PostgreSQL 16
- Docker 24.0.5
- Pre-commit 3.5.0

## Usage

User can create his own mailbox and email template. Using them it's possible to email to any address with the structure
of a created template.


### Configuration

Configure your project by setting up environment variables:

- SECRET_KEY - default is randomly generated

Create local server of PostgreSQL, and set variables to connect:

- DB_USER - database user
- DB_PASSWORD - database user password
- DB_HOST - database host
- DB_NAME - database name
- PORT - database port

For sending mail, connect to email service:

- EMAIL_HOST_USER - user of email host
- EMAIL_HOST_PASSWORD - password to email host
- DEFAULT_FROM_EMAIL - default email address to send mails
- EMAIL_HOST=smtp.sendgrid.net
- EMAIL_USE_TLS=True
- EMAIL_PORT=587

### Running app
You have follow a few steps:

1. Run database migrations:

   ```bash
    cd src
    python manage.py migrate
   ```

2. Run redis on Docker:

   ```bash
   docker-compose up --build 
   ```
   
3. Run app server:

   ```bash
   python manage.py runserver
   ```

4. Run Celery worker

   ```bash
   celery -A core worker -l info
   ```
   

## Database
Overview of the database structure and models:

- [Model 1]: Mailbox - model for mailbox. Include all settings and login

- [Model 2]: Template - for message. Include subject, text and attachments.

- [Model 3]: Email - model for every message. Include Template and Mailbox as FK's. 

## Author

SzymKam
https://github.com/SzymKam