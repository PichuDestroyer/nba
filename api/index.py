import os
from django.core.wsgi import get_wsgi_application

# Set the settings module for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

# Create the WSGI application
application = get_wsgi_application()

def handler(environ, start_response):
    response = application(environ, start_response)
    return response