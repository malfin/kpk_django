import json
from abc import ABC

from django.core.management import BaseCommand

from mainapp.models import Category, Hosting


class Command(BaseCommand, ABC):
    help = 'copy of db in file'

    def handle(self, *args, **options):
        categories = Category.objects.all()
        categories_json = []
        for item in categories:
            categories_json.append(
                {
                    'name': item.name,
                    'image': str(item.image),
                }
            )

        web = Hosting.objects.all()
        web_json = []
        for items in web:
            web_json.append(
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

        with open('categories.json', 'w', encoding='utf-8') as f:
            json.dump(categories_json, f)
        with open('web.json', 'w', encoding='utf-8') as f:
            json.dump(web_json, f)
