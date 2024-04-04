from django.core.management.base import BaseCommand
from ...models import Order
from dateutil.relativedelta import relativedelta



class Command(BaseCommand):
    help = "Edit order"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="Order ID")
        parser.add_argument("-d", "--days", nargs="?", type=int, help="Date days")
        parser.add_argument("-w", "--weeks", nargs="?", type=int, help="Date weeks")
        parser.add_argument("-m", "--months", nargs="?", type=int, help="Date months")
        parser.add_argument("-y", "--years", nargs="?", type=int, help="Date years")

    def handle(self, *args, **options):
        pk = options.get("pk")
        days = options.get("days")
        weeks = options.get("weeks")
        months = options.get("months")
        years = options.get("years")
        order = Order.objects.filter(pk=pk).first()
        time_delta = relativedelta()
        if days is not None:
            time_delta += relativedelta(days=days)
        if weeks is not None:
            time_delta += relativedelta(weeks=weeks)
        if months is not None:
            time_delta += relativedelta(months=months)
        if years is not None:
            time_delta += relativedelta(years=years)
        order.date = order.date-time_delta
        order.save()
        self.stdout.write(f"{order}")