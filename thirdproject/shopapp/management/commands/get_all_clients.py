from django.core.management.base import BaseCommand
from ...models import Client


class Command(BaseCommand):
    help = "Get all clients"

    def handle(self, *args, **options):
        clients = Client.objects.all()
        clients_list = []
        for client in clients:
            clients_list.append(f"id: {client.id} {client}")
        clients_str = "\n".join(clients_list)
        self.stdout.write(f"{clients_str}")
