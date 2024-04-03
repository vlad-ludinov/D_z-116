from django.core.management.base import BaseCommand
from ...models import Client


class Command(BaseCommand):
    help = "Get client by id"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="Client ID")

    def handle(self, *args, **options):
        pk = options.get("pk")
        client = Client.objects.filter(pk=pk).first()
        self.stdout.write(f"{client}")
