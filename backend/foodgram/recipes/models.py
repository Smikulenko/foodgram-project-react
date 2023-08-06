from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название',
        help_text='Необходимо названия тега'
    )
    color = models.CharField(
        max_length=16,
        null=True,
        verbose_name='Цвет',
        help_text='Необходим Цвет'
    )

    slug = models.SlugField(
        max_length=200,
        unique=True,
        null=True,
        verbose_name='Адрес',
        help_text='Необходимо адрес тега'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тег'
        verbose_name_plural = 'Тег'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название Ингридиента ',
        help_text='Необходимо названия Ингридиента'
    )

    measurement_unit = models.CharField(
        max_length=200,
        verbose_name='Единицы измерения',
        help_text='Необходимо Единица измерения'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиент'

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Recipe(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название',
        help_text='Необходимо названия Рецепта'
    )

    text = models.TextField(
        verbose_name='Описание',
        help_text='Необходимо описание',
    )
    author = models.ForeignKey(
        User,
        related_name='recipes',
        on_delete=models.CASCADE,
        verbose_name='Автор',
        help_text='Необходим Автор',
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Тег',
        help_text='Необходимо выбрать тег'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name='Ингредиенты',
        help_text='Необходимо выбрать ингредиенты'

    )
    image = models.ImageField(
        upload_to='recipes/images/',
        verbose_name='Изоброжение',
        help_text='Необходимо изображение',
        )
    cooking_time = models.PositiveSmallIntegerField(
       verbose_name='Время приготовления в минутах',
       help_text='Укажите время приготоаления',

    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепт'

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE
    )

    amount = models.IntegerField(
       verbose_name='Количество',
       help_text='Укажите Количество',

    )

    def __str__(self):
        return f'В рецепте {self.recipe} есть ингредиент {self.ingredient}'


class ShoppingCart(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='shopping_cart'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='shopping_cart',
    )

    class Meta:
        verbose_name = 'Список пакупок'
        verbose_name_plural = 'Список пакупок'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_shopping_cart'
            )
        ]

    def __str__(self):
        return f'Рецепт {self.recipe} в списке покупок у {self.user}'


class Favorite(models.Model):

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='favorite_recipe'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favorite_user',
    )

    class Meta:
        verbose_name = 'Избраное'
        verbose_name_plural = 'Избраное'

    def __str__(self):
        return f'Рецепт {self.recipe} в избранном у {self.user}'
