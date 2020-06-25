from django.core.management.base import BaseCommand, CommandError
from ftl_app.models import User, ActivityPeriod
from faker import Faker
import random
from datetime import timedelta

tz_list = ['GMT+0', 'GMT+0', 'Europe/Rome', 'Europe/Gibraltar', 'Egypt', 'Africa/Djibouti', 'Iran', 'Etc/GMT+4',
           'Asia/Karachi', 'Asia/Kolkata', 'Asia/Dhaka', 'Asia/Tokyo', 'Asia/Taipei', 'Japan', 'Australia/South',
           'Australia/Sydney', 'Pacific/Guadalcanal', 'NZ', 'Pacific/Midway', 'US/Hawaii', 'US/Alaska', 'US/Pacific',
           'America/Phoenix', 'US/Mountain', 'US/Central', 'US/Eastern', 'US/East-Indiana', 'Atlantic/Bermuda',
           'Canada/Newfoundland', 'America/Argentina/Buenos_Aires', 'Brazil/East', 'Africa/Bangui']


class Command(BaseCommand):
    help = 'Add dummy data for Users and their activity'

    def add_arguments(self, parser):
        parser.add_argument('records', nargs='+', type=int)

    def handle(self, *args, **options):
        fake = Faker()
        print(options['records'])
        for i in range(options['records'][0]):

            name_data = fake.name().split()
            first_name = name_data[0]
            last_name = name_data[1]
            tz = random.choice(tz_list)

            user = User.objects.create(first_name=first_name, last_name=last_name, tz=tz)

            for j in range(5):
                start_time = fake.date_time()
                end_time = start_time + timedelta(minutes=5)

                ActivityPeriod.objects.create(start_time=start_time, end_time=end_time, user=user)

            self.stdout.write(self.style.SUCCESS('Successfully closed user "%s"' % user.id))
