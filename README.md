# CRM_Project

## Introduction

 This is a training project

## Setup Guide

This project requires the following tools:
 - Flask - A microframework for Python web applications
 - SQLAlchemy - A Flask extension that adds ORM support for your data models.
 - Virtualenv - A tool for creating an isolated Python environment
 - Jinja - A templating language for Python, used by Flask

To get started, do the following :

- Create virtual environment:
    ```console
    $ pip install virtualenv
    ```

    ```console
    $ virtualenv venv
    ```

- Activate the environment

- Install dependencies:
    ```console
    $ pip install -r requirements.txt
    ```
- Deploy database
    ```console
    $ python manage.py
    ```

- Run the app
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