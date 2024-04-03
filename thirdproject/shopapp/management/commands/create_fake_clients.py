from django.core.management.base import BaseCommand
from ...models import Client


class Command(BaseCommand):
    help = "Create fake clients"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="User ID")

    def handle(self, *args, **options):
        count = options.get("count")
        for i in range(1, count + 1):
            if i % 10 == 0:
                number = "000000000"
            else:
                number = f"{(i%10)*111111111}"
            client = Client(
                name=f"Name{i}",
                email=f"email{i}@mail.ru",
                phone=f"+79{number}",
                address=f"Country{i}",
            )
            client.save()
        self.stdout.write(f"{count} fake clients was created")
