from django.contrib.auth.models import User
from django.core.management import BaseCommand

from authapp.models import UserProfile


class Command(BaseCommand):
    help = 'Create Profile'

    def handle(self, *args, **options):
        # requset.user.userprofile.age
        for user in User.objects.filter(userprofile__isnull=True):
            UserProfile.objects.create(user=user)
            # print(user)
