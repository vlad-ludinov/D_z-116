from django.core.management.base import BaseCommand
from ...models import Product


class Command(BaseCommand):
    help = "Get all products"

    def handle(self, *args, **options):
        products = Product.objects.all()
        for product in products:
            product.delete()
        self.stdout.write(f"Products delete")