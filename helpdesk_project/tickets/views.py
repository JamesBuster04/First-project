"""
Views handle requests. A "ViewSet" bundles the common CRUD operations
(Create, Read, Update, Delete) for a model into one neat class.

You mostly just set `queryset` and `serializer_class`; Django REST Framework
does the rest. The custom @action methods add extra endpoints.
"""

from django.db.models import Count, Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Ticket, Comment
from .serializers import CategorySerializer, TicketSerializer, CommentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by("-created_at")
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        # If the caller is logged in, record them as the creator.
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(created_by=user)

    @action(detail=True, methods=["post"])
    def add_comment(self, request, pk=None):
        """POST /api/tickets/<id>/add_comment/  -> add a comment to a ticket."""
        ticket = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            user = self.request.user if self.request.user.is_authenticated else None
            serializer.save(ticket=ticket, author=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"])
    def stats(self, request):
        """GET /api/tickets/stats/  -> counts of tickets by status."""
        data = Ticket.objects.aggregate(
            open=Count("id", filter=Q(status="OPEN")),
            in_progress=Count("id", filter=Q(status="IN_PROGRESS")),
            resolved=Count("id", filter=Q(status="RESOLVED")),
            closed=Count("id", filter=Q(status="CLOSED")),
        )
        return Response(data)
