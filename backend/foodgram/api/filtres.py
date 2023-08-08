from django_filters import rest_framework as filters

from recipes.models import Tag, Recipe


class RecipeFilter(filters.FilterSet):

    is_favorited = filters.NumberFilter(
        field_name='favorite__user', method='filter_users_lists'
    )
    is_in_shopping_cart = filters.NumberFilter(
        field_name='buyer__user', method='filter_users_lists'
    )
    tags = filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        queryset=Tag.objects.all(),
        to_field_name='slug'
    )

    class Meta:
        model = Recipe
        fields = ('tags', 'author', 'is_favorited', 'is_in_shopping_cart')
