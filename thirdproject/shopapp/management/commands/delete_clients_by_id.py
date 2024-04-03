from django.core.management.base import BaseCommand
from ...models import Client


class Command(BaseCommand):
    help = "Delete client by id"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=str, nargs="+", help="Client ID")

    def handle(self, *args, **options):
        pks = options.get("pk")
        pk_list = []
        for pk in pks:
            if pk.isdigit():
                pk_list.append(int(pk))
            elif not pk.isdigit():
                pk_range = pk.split("-")
                if (
                    len(pk_range) == 2
                    and pk_range[0].isdigit()
                    and pk_range[1].isdigit()
                ):
                    for i in range(int(pk_range[0]), int(pk_range[1]) + 1):
                        pk_list.append(i)
        for pk in pk_list:
            client = Client.objects.filter(pk=pk).first()
            if client is not None:
                client.delete()
        self.stdout.write(f"Clients delete")
