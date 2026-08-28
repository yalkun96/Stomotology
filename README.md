# Stomotology — Dental Clinic Web Application

A Django-based web application for a dental clinic, built as a full-stack project with multilingual content and an administrative interface.

## Features

- Dental clinic website and service pages
- Multilingual content managed through Django
- Django Admin for content management
- PostgreSQL / SQLite support
- Google Maps integration
- Production deployment with Gunicorn

## Tech Stack

- Python
- Django
- PostgreSQL / SQLite
- HTML / CSS
- JavaScript
- Bootstrap
- Google Maps API
- Gunicorn

## Project Structure

```text
Stomotology/
├── dent/              # Django application
├── locale/            # Translation files
├── media/             # Uploaded media
├── manage.py
└── app.py             # Application/deployment entry point
```

## Running Locally

Clone the repository, create a virtual environment, install the project dependencies, configure the database and run Django migrations.

```bash
python manage.py migrate
python manage.py runserver
```

The application can then be accessed locally through the Django development server.

## Notes

This project demonstrates practical Django application development, database integration, multilingual content management and deployment-oriented configuration.

## Author

**Yalkun Mametov**
