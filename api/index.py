import os
from django.core.wsgi import get_wsgi_application

# Set the settings module for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

# Expose the WSGI application as `app`
app = get_wsgi_application()