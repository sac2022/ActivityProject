# ActivityProject
INTRODUCTION
------------

Designed an WebApp
Django application with User and ActivityPeriod models.
Members are the user who has there details and tracking one particular members activity period by there activity start time and end time with there remember id.

Requirments:

pip install -r requirements.txt

Steps:

#if your executing in local machine or using localhost
1) The first thing to do is to create a virtual environment for the app:

virtualenv Project
or
python3 -m venv Project
cd Project
source bin\activate


2) Lets create the project and the apps:
django-admin startproject djangoProject
cd ticketapi
python manage.py startapp webapp

3) The first thing is the INSTALLED APPS :
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'webapp',#appname
]

4) Migrations and Admin

python manage.py createsuperuser 

python manage.py migrate

python manage.py makemigrations
 


5) Python manage.py runserver 'PORT NUMBER'#optional



Heruko:
 
Deployed in heruko: https://acttestapp.herokuapp.com/

1) heroku run python manage.py migrate

2) heroku run python manage.py makemigrations

3) heroku run python manage.py createsuperuser

Steps:

1) once super user is created, open the admin mode https://acttestapp.herokuapp.com/admin

2) add Member Details followed by Period

3)Save both

4)Open Activity Mode, https://acttestapp.herokuapp.com/Activity

5)APi links:
  a) https://acttestapp.herokuapp.com/Activity/Members/
  
  
  b) https://acttestapp.herokuapp.com/Activity/Period/

You can easily test the endpoints we have created with many tools. You can use Postman to do that if you are the gui type. Or simply use httpie , a command line for HTTP client. It is a CLI, cURL-like tool for humans.

