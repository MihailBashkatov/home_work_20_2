import json
import os

from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Clean table Category
        Category.objects.all().delete()

        # Clearing autoincrement for pk filed table Category
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")

        # Read file data json
        with open('data.json', 'r', encoding='UTF8') as file:

            json_file = json.load(file)
            category_for_create = []

            for element in json_file:
                category_for_create.append(Category(name=element['fields']['name'], description=element['fields']['description']))

            Category.objects.bulk_create(category_for_create)
