/Users/zzzzzz/PycharmProjects/Stomotology/venv/bin/python

import sys
import os

# Add your project directory to the sys.path
sys.path.insert(0, "public_html/Stomotology")

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = "Stomotology.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from flup.server.fcgi import WSGIServer
if __name__ == '__main__':
    WSGIServer(application).run()