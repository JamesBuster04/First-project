"""Top-level URL configuration.

Think of URLs as the "addresses" of your website. Here we route:
  /admin/  -> the built-in Django admin panel
  /api/    -> our ticketing REST API (defined inside the tickets app)
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("tickets.urls")),
]
