from csv import reader

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загрузка ингредиентов в базу данных'

    def importingredient(self):
        if Ingredient.objects.exists():
            print('Данные для Ingredient уже загружены')
        else:
            with open('./data/ingredients.csv',
                      'r', encoding='UTF-8') as ingredients:
                for row in reader(ingredients):
                    ingre = [Ingredient(name=row[0], measurement_unit=row[1])]
                    Ingredient.objects.bulk_create(ingre)
                print('Данные для Ingredient загружены')

    def handle(self, *args, **kwargs):
        self.importingredient()
