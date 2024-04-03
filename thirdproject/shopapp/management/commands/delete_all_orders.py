from django.core.management.base import BaseCommand
from ...models import Order


class Command(BaseCommand):
    help = "Get all orders"

    def handle(self, *args, **options):
        orders = Order.objects.all()
        for order in orders:
            order.delete()
        self.stdout.write(f"Orders delete")