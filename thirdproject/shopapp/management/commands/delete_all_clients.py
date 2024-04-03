from django.core.management.base import BaseCommand
from ...models import Client


class Command(BaseCommand):
    help = "Get all clients"

    def handle(self, *args, **options):
        clients = Client.objects.all()
        for client in clients:
            client.delete()
        self.stdout.write(f"Clients delete")
