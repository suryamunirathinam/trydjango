# trydjango

creating virtual environment:
python3 -m venv./venv
pip3 freeze
source ./venv/bin/activate
deactivate
pip install django

#to create a django app : cli command
 
  start project django-admin startproject btre .
  python manange.py runserver  
  
  when server is run dbsqllite file will be created  its not suitable for production environment
  pycache - will be created every time youy run the program 
  init - to start not needed after the new version 
  settings -- 
  urls.py -- collection of all apps url links
  wsgi -- webserver gateway interface 
  
# creating an app 

  python manage.py startapp pages
   in settings.py --add your appname.apps.appmethod
                                              
