# CRM_Project

## Introduction

 This project is part of the training program. We are creating a course-resource management app that allows users to browse and enquire about courses. Administrators review the user enquiries and allot corresponding resources to the user based on their qualifications and eligibilty.

## Setup Guide

This project requires the following tools:
 - Flask - A microframework for Python web applications
 - SQLAlchemy - A Flask extension that adds ORM support for your data models.
 - Virtualenv - A tool for creating an isolated Python environment
 - Jinja - A templating language for Python, used by Flask

To get started, do the following :

1. Create virtual environment:
    ```console
    $ pip install virtualenv
    ```

    ```console
    $ virtualenv venv
    ```

2. Activate the environment

3. Install dependencies:
    ```console
    $ pip install -r requirements.txt
    ```
4. Deploy database
    ```console
    $ python manage.py
    ```

5. Run the app
    ```console
    $ python app.py
    ```

## Modules

This project has 3 core modules:

- User

  > This module contains user side enquiry and profile management. 

- Admin

  > This module contains all admin side operations. The admin has higher privileges than the user and has power to control users, enquiries, courses, etc.

- Authentication
 
  >  This module deals with the authentication of the user. It maps user and admin to their pages respectively