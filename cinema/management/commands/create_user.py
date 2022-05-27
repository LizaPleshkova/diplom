from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create_user(
            username='Elizaveta',
            password='password_for_liza',
            birth_date=datetime(2000, 9, 24),
            is_superuser=True,
            is_staff=True
        )
        user.save()
