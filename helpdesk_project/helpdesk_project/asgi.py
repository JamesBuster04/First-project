"""ASGI config for the helpdesk_project project.

ASGI is the newer async interface. You don't need to edit this file.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helpdesk_project.settings")

application = get_asgi_application()
