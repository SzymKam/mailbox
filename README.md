# MAILBOX

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies](#technologies)
- [Usage](#usage)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the Development Server](#running-the-development-server)
  - [Run in Docker](#run-in-docker)
- [Database](#database)
- [Testing](#testing)
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

[//]: # (### Running the Development Server)

[//]: # ()
[//]: # (1. Run database migrations:)

[//]: # ()
[//]: # (   ```bash)

[//]: # (   poetry run python manage.py migrate)

[//]: # (   ```)

[//]: # ()
[//]: # (2. Create a superuser &#40;admin&#41;:)

[//]: # ()
[//]: # (   ```bash)

[//]: # (   poetry run python manage.py createsuperuser)

[//]: # (   ```)

[//]: # ()
[//]: # (3. Start the development server:)

[//]: # ()
[//]: # (   ```bash)

[//]: # (   poetry run python manage.py runserver)

[//]: # (   ```)

[//]: # ()
[//]: # (Your Django project should now be accessible at [http://localhost:8000/].)

[//]: # ()
[//]: # (### Run in Docker)

[//]: # ()
[//]: # (Make sure you have installed and running Docker engine. Docker, docker-compose files and nginx files are configured for)

[//]: # (three containers: web, db and nginx server for staticfiles. To run project:)

[//]: # ()
[//]: # (```bash)

[//]: # (docker compose up --build)

[//]: # (```)

[//]: # ()
[//]: # (Your Django project should now be accessible at [http://localhost/].)

[//]: # (Don't forget to make migrations, collect staticfiles and createsuperuser.)

[//]: # ()
[//]: # (```bash)

[//]: # (docker-compose  exec web python manage.py migrate)

[//]: # (docker-compose  exec web python manage.py collectstatic)

[//]: # (docker-compose  exec web python manage.py createsuperuser)

[//]: # (```)

[//]: # ()
## Database

[//]: # ()
[//]: # (Overview of the database structure and models:)

[//]: # ()
[//]: # (- [Model 1]: Event - user can add nane, event localization, short description, start date and status - some of them are)

[//]: # (  set by default - able to change by user. When user close event - end date is set automatically.)

[//]: # (- [Model 2]: Patient - includes personal information about birthdate, name, contact information etc. When patient has no)

[//]: # (  name &#40;ex. unconscious&#41; can be set by default. This model includes a few FK models: AuthorizedPerson, Event, Treatment.)

[//]: # (  This model includes information necessary to hospital workflow - priority, bed number, status.)

[//]: # (- [Model 3]: AuthorizedPerson - FK of Patient. Person to contact about patient treatment &#40;ex. parent&#41;.)

[//]: # (- [Model 4]: Drug - FK of Patient. Can add dose, form and unit of drug. Drug is selected from list.)

[//]: # (- [Model 5]: MedicalStaff - FK of Treatment. The most important thing apart from the name field is medical qualifications.)

[//]: # (- [Model 6]: VitalSign - FK of Patient. Can add blood pressure, heart rate, saturation, Glasgow Coma Scale, temperature)

[//]: # (  and sugar level. For BP, HR and SpO2 graph of the values is drawn.)

[//]: # (- [Model 7]: Treatment - FK of Patient. Have fields: interview, description, medical staff and diagnosis. For diagnose)

[//]: # (  user can choose ICD10 list &#40;International Classification of Diseases&#41;.)

[//]: # ()

## Author

SzymKam
https://github.com/SzymKam
�