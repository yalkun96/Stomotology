import sys
import os

# Add the app's directory to the PYTHONPATH
sys.path.insert(0, 'public_html/Stomotology')

from django.core.wsgi import get_wsgi_application

# Set environment variable for the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'Stomotology.settings'

application = get_wsgi_application()