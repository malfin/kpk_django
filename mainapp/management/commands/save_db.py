from abc import ABC
from django.core.management import BaseCommand
import json

from mainapp.models import Hosting, Category


class Command(BaseCommand, ABC):
    help = 'copy of db in file'

    def handle(self, *args, **options):
        categories = Category.objects.all()
        categories_json = []
        for item in categories:
            categories_json.append(
                {
                    'name': str(item.name),
                    'image': str(item.image),
                }
            )

        hosting = Hosting.objects.all()
        hosting_json = []
        for items in hosting:
            hosting_json.append(
                {
                    'category_name': items.category,
                    'name_tariff': items.name,
                    'desc': items.desc,
                    'price': items.prise,
                    'disk': items.disk,
                    'site': items.site,
                    'db': items.db,
                    'cpu': items.cpu,
                    'ram': items.ram,
                    'traffic': items.traffic,
                    'location': items.location,
                    'ddos': items.ddos,
                    'image': str(items.image),
                }
            )

        with open('backup/categories.json', 'w', encoding='utf-8') as f:
            json.dump(categories_json, f)
        with open('backup/hosting.json', 'w', encoding='utf-8') as f:
            json.dump(hosting_json, f)
