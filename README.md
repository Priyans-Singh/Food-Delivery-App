
# Treats - Food Ordering App

This a food-ordering-app made using React as a frontend and Django as backend and PostgreSQL as database. 

For anyone who is willing to test this on their machine can download and will have to install the dependicies mentonied in the requirements.txt file .

For frontend we have used Redux , Redux toolkit, reactstrap, tailwindCSS, React-dom, react-slick, 





## Backend Installation

Install django-admin, django_restframework and psycopg2 for the Django and postgreSQL. 

As Django by default uses SQL lite we'll have to connect it to our postgreSQL database by going into main folder's setting.py file and changing the DATABASE to the below format
  
     DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':  'databaseName',
        'USER': 'userName',
        'PASSWORD': 'userPassword',
    }
    }  

Once done with that you can start by creating a project folder that will hold all the models and url calls, use *django-admin startproject nameofAPI *

connect it to the urls in main folder urls.py and add the app in 
INSTALLED_APPS in settings.py.

## Cors error

I have designed the website such that both the frontend and backend run on the same server that's why Cors error shouldn't be a problem .

But still I have added the setting require for handling cors errors. Just look in the settings.py for CORS.

