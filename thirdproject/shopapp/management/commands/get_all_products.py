from django.core.management.base import BaseCommand
from ...models import Product


class Command(BaseCommand):
    help = "Get all products"

    def handle(self, *args, **options):
        products = Product.objects.all()
        products_list = []
        for product in products:
            products_list.append(f"id: {product.id} {product}")
        products_str = "\n".join(products_list)
        self.stdout.write(f"{products_str}")