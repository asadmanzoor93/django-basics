from django.core.management.base import BaseCommand
import pytz

from users.models import DateConversion

IN_PROGRESS = 'inprogress'
CONVERTED = 'converted'
PST_TIMEZONE = 'PST'
UTC_TIMEZONE = 'UTC'
KARACHI_TIMEZONE = 'Asia/Karachi'

class Command(BaseCommand):
    help = 'This command will convert date w.r.t time-zone'

    def handle(self, *args, **options):
            records = DateConversion.objects.filter(status=IN_PROGRESS)[:10]

            # Reset the conversion process on completion of conversion process
            if not records:
                DateConversion.objects.all().update(status=IN_PROGRESS)
                records = DateConversion.objects.filter(status=IN_PROGRESS)[:10]

            for record in records:
                if record.timezone == PST_TIMEZONE:
                    record.date = self.timezone_conversion(record.date, KARACHI_TIMEZONE, UTC_TIMEZONE)
                    record.timezone = 'UTC'

                elif record.timezone == "UTC":
                    record.date = self.timezone_conversion(record.date, UTC_TIMEZONE, KARACHI_TIMEZONE)
                    record.timezone = PST_TIMEZONE

                record.status = CONVERTED
                record.save()

            self.stdout.write(self.style.SUCCESS('Date-times updated successfully!'))

    def timezone_conversion(self, date, source_timezone, dest_timezone):
        datetime_obj = pytz.timezone(source_timezone).localize(date)
        datetime = datetime_obj.astimezone(pytz.timezone(dest_timezone))
        return datetime.replace(tzinfo=None)
