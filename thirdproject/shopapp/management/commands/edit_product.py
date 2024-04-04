from django.core.management.base import BaseCommand
from ...models import Product


class Command(BaseCommand):
    help = "Edit product"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="Product ID")
        parser.add_argument("-n", "--name", nargs="?", type=str, help="Product name")
        parser.add_argument("-d", "--description", nargs="?", type=str, help="Product description")
        parser.add_argument("-p", "--price", nargs="?", type=int, help="Product price")
        parser.add_argument("-q", "--quantity", nargs="?", type=int, help="Product quantity")

    def handle(self, *args, **options):
        pk = options.get("pk")
        name = options.get("name")
        description = options.get("description")
        price = options.get("price")
        quantity = options.get("quantity")
        product = Product.objects.filter(pk=pk).first()
        if name is not None:
            product.name = name
        if description is not None:
            product.description = description
        if price is not None:
            product.price = price
        if quantity is not None:
            product.quantity = quantity
        product.save()
        self.stdout.write(f"{product}")