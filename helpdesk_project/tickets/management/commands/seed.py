"""Custom management command: `python manage.py seed`

Fills the database with realistic sample data so you have something to play
with immediately. Run it once after migrating.
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tickets.models import Category, Ticket, Comment


class Command(BaseCommand):
    help = "Seed the database with sample help desk data"

    def handle(self, *args, **options):
        # Create a staff user you can log into the admin with.
        user, _ = User.objects.get_or_create(
            username="admin", defaults={"is_staff": True, "is_superuser": True}
        )
        user.set_password("admin123")
        user.save()

        cat_hw, _ = Category.objects.get_or_create(
            name="Hardware", defaults={"description": "Physical equipment issues"}
        )
        cat_sw, _ = Category.objects.get_or_create(
            name="Software", defaults={"description": "Application problems"}
        )
        cat_net, _ = Category.objects.get_or_create(
            name="Network", defaults={"description": "Connectivity issues"}
        )

        t1, _ = Ticket.objects.get_or_create(
            title="Laptop will not power on",
            defaults={
                "description": "User reports a black screen on boot.",
                "priority": "HIGH",
                "category": cat_hw,
                "created_by": user,
            },
        )
        t2, _ = Ticket.objects.get_or_create(
            title="Outlook keeps crashing",
            defaults={
                "description": "App closes when opening the calendar.",
                "priority": "MEDIUM",
                "status": "IN_PROGRESS",
                "category": cat_sw,
                "created_by": user,
                "assigned_to": user,
            },
        )

        Comment.objects.get_or_create(
            ticket=t1, author=user,
            defaults={"body": "Requested to remote into the machine."},
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Seed data created. Admin login -> username: admin / password: admin123"
            )
        )
