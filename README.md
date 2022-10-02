
 # Twitter-backend setup 
 
It's a simple social media application

Functionality

 1.User registration using unique username and a password
 
 2.User login (Including session maintenance using any means you’re comfortable with)
 
 3.Unit tests for these basic methods
 
 4.Create, read, update, delete tweet


#API Tools:
1. Django
2. Django Rest Framework
3. Database Postgresql


git clone https://github.com/silpathomas/twitter.git

1.Create a virtual environment using following command

    python -m venv twitter-env

2.Activate  virtual environment

    source twitter-env/bin/activate

3.iInstall the requirements

   Enter into stockemarket folder
   
       cd twitter
       pip install -r requirements.txt
4.Change the database details in settings.py file


      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql_psycopg2',
              'NAME':stock_market, 
              'USER': 'postgres', 
              'PASSWORD': 'postgres',
              'HOST': '127.0.0.1', 
              'PORT': '5432',
          }
      }
5.Apply Migrations

       python manage.py migrate
       
6.Run the project using below command

	Python manage.py runserver
