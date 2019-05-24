from django.core.management.base import BaseCommand
from django.db import IntegrityError
from datetime import datetime, timedelta

from users.models import CustomUser, DateConversion


class Command(BaseCommand):
    help = 'This command will add dummy user & 100 PST date-times records'

    def handle(self, *args, **options):
            self.stdout.write(self.style.SUCCESS('Adding Dummy Users !!'))

            try:
                CustomUser.objects.create_user('dummy_user_3', 'dummyuser3@gmail.com', 'dummy_user_3')
            except IntegrityError:
                self.stdout.write(self.style.ERROR('User record already exist!!'))

            self.stdout.write(self.style.SUCCESS('Adding 100 PST Date-times !!'))
            new_datetime = datetime.now()

            for index in range(0, 100):
                new_datetime = new_datetime + timedelta(days=1)
                DateConversion.objects.create(date=new_datetime.strftime("%Y-%m-%d %H:%M:%S"))

            self.stdout.write(self.style.SUCCESS('Dummy users & 100 PST date-times added successfully!'))
