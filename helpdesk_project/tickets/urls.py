"""
URLs for the tickets API.

The DefaultRouter automatically creates all the standard endpoints for our
ViewSets, e.g.:
  GET    /api/tickets/          -> list tickets
  POST   /api/tickets/          -> create a ticket
  GET    /api/tickets/1/        -> retrieve ticket #1
  PUT    /api/tickets/1/        -> update ticket #1
  DELETE /api/tickets/1/        -> delete ticket #1
  POST   /api/tickets/1/add_comment/   -> add a comment
  GET    /api/tickets/stats/    -> status counts
  GET    /api/categories/       -> list/create categories
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r"tickets", TicketViewSet, basename="ticket")
router.register(r"categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]
