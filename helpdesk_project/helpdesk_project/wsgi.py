"""WSGI config for the helpdesk_project project.

WSGI is the standard way Python web servers talk to Django. You don't need
to edit this file for learning purposes.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helpdesk_project.settings")

application = get_wsgi_application()
