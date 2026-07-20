"""
Serializers convert between Django models (Python objects) and JSON.

JSON is the language web APIs speak. When you GET a ticket from the API, the
serializer turns the database row into JSON. When you POST JSON to create a
ticket, the serializer turns it back into a model object.
"""

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Ticket, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    # Show the full author object when reading, but accept just an id when writing.
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "ticket", "author", "body", "created_at"]
        # ticket and author are set by the view (via save()), not the request body.
        read_only_fields = ["author", "ticket"]


class TicketSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    # write_only lets the API accept a category "id" without sending the whole object back.
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category",
        write_only=True, required=False, allow_null=True
    )
    created_by = UserSerializer(read_only=True)
    assigned_to = UserSerializer(read_only=True)
    assigned_to_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="assigned_to",
        write_only=True, required=False, allow_null=True
    )
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = [
            "id", "title", "description", "status", "priority",
            "category", "category_id", "created_by", "assigned_to",
            "assigned_to_id", "comments", "created_at", "updated_at",
        ]
        read_only_fields = ["created_by"]
