"""
Models = the "tables" in your database, described in Python.

Each class below becomes a database table. Each field (e.g. title = ...) becomes
a column. Django automatically creates the SQL for you from these definitions.

This is the heart of the project and the best place to start reading.
"""

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Groups tickets by type, e.g. Hardware, Software, Network."""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    """A single support ticket — the main thing this app tracks."""

    # "choices" restrict a field to a fixed list of values (like a dropdown).
    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("IN_PROGRESS", "In Progress"),
        ("RESOLVED", "Resolved"),
        ("CLOSED", "Closed"),
    ]
    PRIORITY_CHOICES = [
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High"),
        ("URGENT", "Urgent"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="OPEN")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="MEDIUM")

    # ForeignKey = a link to another table (many tickets belong to one category).
    # on_delete=models.SET_NULL keeps the ticket if the category is deleted.
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="tickets"
    )
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="created_tickets"
    )
    assigned_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_tickets"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"#{self.id} {self.title}"


class Comment(models.Model):
    """A note added to a ticket during investigation."""

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.ticket}"
