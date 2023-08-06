from csv import DictReader

from django.core.management.base import BaseCommand

from foodgram.settings import BASE_DIR
from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загрузка ингредиентов в базу данных'

    def importingredient(self):
        if Ingredient.objects.exists():
            print('Данные для Ingredient уже загружены')
        else:
            for row in DictReader(open(
                    BASE_DIR / './data/ingredients.csv',
                    encoding='utf8')):
                Ingredient.objects.create(
                    name=row['name'],
                    measurement_unit=row['measurement_unit'],)
            print('Данные для Ingredient загружены')

    def handle(self, *args, **kwargs):
        self.importingredient()
