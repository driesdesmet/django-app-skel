{% if False %}
# Django 1.4 App Template

## About

This is a starting template for Django 1.4 apps based on the work that was done here [django-app-skeleton](https://github.com/callowayproject/django-app-skeleton). Apart from some minor personal tastes it's basically the same but uses the new django-admin --template functionality instead of running a python program to generate an app skeleton.

## Features ##

* An app skeleton
* A simple model with list and detail view
* Setuptools
* An example project that has the app installed
* Todo lines for IDE's to pick up on.

## How to use this template to create your app ##

* Install Django 1.4
* Run the following one of the following commands, specifying your project name:
        
    * To use plain app skeleton:

            django-admin.py startapp --template https://github.com/triotorus/django-app-skel/zipball/master --extension py,md,gitignore,dist yourappname

{% endif %}
# {{ app_name|title }} Django App #

## About ##

Describe {{ app_name }} here.

## How to install the app ##

* Simply run 'python setup.py install'

## How to run the example project ##

* cd into the 'example' folder
* run 'python manage.py syncdb' and fill in the superuser details
* run 'python manage.py runserver'