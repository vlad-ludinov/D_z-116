from django.core.management.base import BaseCommand
from ...models import Client, Product, Order


class Command(BaseCommand):
    help = "Fill db"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="Count")

    def handle(self, *args, **options):
        count = options.get("count")
        client_list = []
        product_list = []
        count_price = 0
        for i in range(1, count + 1):
            product = Product(
                name=f"ProductName{i}",
                description=f"Best description{i}",
                price=i * 1000,
                quantity=i,
            )
            count_price += i*1000
            product.save()
            product_list.append(product)
        for i in range(1, count + 1):
            if i % 10 == 0:
                number = "000000000"
            else:
                number = f"{(i % 10) * 111111111}"
            client = Client(
                name=f"Name{i}",
                email=f"email{i}@mail.ru",
                phone=f"+79{number}",
                address=f"Country{i}",
            )
            client.save()
            client_list.append(client)
            order = Order(
                client=client,
                # product=product_list[0],
                price=count_price
            )
            order.save()
            order.product.set(product_list)
            self.stdout.write(f"db fill fake data")
