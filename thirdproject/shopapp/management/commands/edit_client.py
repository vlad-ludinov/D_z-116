from django.core.management.base import BaseCommand
from ...models import Client


class Command(BaseCommand):
    help = "Edit client"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="Client ID")
        parser.add_argument("-n", "--name", nargs="?", type=str, help="Client name")
        parser.add_argument("-e", "--email", nargs="?", type=str, help="Client email")
        parser.add_argument("-p", "--phone", nargs="?", type=str, help="Client phone number")
        parser.add_argument("-a", "--address", nargs="?", type=str, help="Client address")

    def handle(self, *args, **options):
        pk = options.get("pk")
        name = options.get("name")
        email = options.get("email")
        phone = options.get("phone")
        address = options.get("address")
        client = Client.objects.filter(pk=pk).first()
        if name is not None:
            client.name = name
        if email is not None:
            client.email = email
        if phone is not None:
            client.phone = phone
        if address is not None:
            client.address = address
        client.save()
        self.stdout.write(f"{client}")
