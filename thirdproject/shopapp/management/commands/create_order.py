from django.core.management.base import BaseCommand
from ...models import Client, Product, Order


class Command(BaseCommand):
    help = "Create order"

    def add_arguments(self, parser):
        parser.add_argument("-c", "--client", nargs="?", type=int, help="Client ID")
        parser.add_argument("-p", "--products", nargs="+", type=int, help="Products ID")

    def handle(self, *args, **options):
        client_id = options.get("client")
        products_id = options.get("products")
        client = Client.objects.filter(pk=client_id).first()
        products_list = []
        price = 0
        for pk in products_id:
            product = Product.objects.filter(pk=pk).first()
            products_list.append(product)
            price += product.price
        order = Order(
            client=client,
            price=price
        )
        order.save()
        order.product.set(products_list)
        self.stdout.write(f"{order}")