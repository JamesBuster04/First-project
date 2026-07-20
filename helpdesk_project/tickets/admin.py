"""Register models so you can view/edit them in the Django admin at /admin/."""

from django.contrib import admin
from .models import Category, Ticket, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "priority", "category", "assigned_to", "created_at")
    list_filter = ("status", "priority", "category")
    search_fields = ("title", "description")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("ticket", "author", "created_at")
