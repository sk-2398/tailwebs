# Teacher Portal

A Django-based web application for managing student and teacher interactions.

## Features

- User Authentication (Login/Signup)
- CRUD operations for students and teachers
- Dashboard with analytics and visualizations

## Prerequisites

- Python 3.x
- Django
- Virtualenv

## Installation

### Clone the Repository

```bash
git clone https://github.com/sk-2398/tailwebs.git
cd teacher_portal
```
### Create and Activate a Virtual Environment
```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
### Set Up Database
```bash
python manage.py makemigrations
python manage.py migrate
```
### Run the Server
```bash
python manage.py runserver
```
It will run this project on localhost.
Visit http://127.0.0.1:8000/ to access the application.
