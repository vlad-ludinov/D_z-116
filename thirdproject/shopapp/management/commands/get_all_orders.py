from django.core.management.base import BaseCommand
from ...models import Order


class Command(BaseCommand):
    help = "Get all orders"

    def handle(self, *args, **options):
        orders = Order.objects.all()
        orders_list = []
        for order in orders:
            orders_list.append(f"id: {order.id} {order}")
        orders_str = "\n".join(orders_list)
        self.stdout.write(f"{orders_str}")