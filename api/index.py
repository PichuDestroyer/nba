import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nba.settings')  # Replace 'nba' with your project name
app = get_wsgi_application()