from django.core.management.base import BaseCommand
from ...models import Product


class Command(BaseCommand):
    help = "Create fake products"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="User ID")

    def handle(self, *args, **options):
        count = options.get("count")
        for i in range(1, count + 1):
            product = Product(
                name=f"ProductName{i}",
                description=f"Best description{i}",
                price=i * 1000,
                quantity=i,
            )
            product.save()
        self.stdout.write(f"{count} fake clients was created")