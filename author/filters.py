from django_filters import rest_framework as filters
from .models import AuthorModel, BookModel, BiographyModel, ArticleModel

class AuthorFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = AuthorModel
        fields = ['first_name']


class BookFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = BookModel
        fields = ['authors']


class BiographyFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = BiographyModel
        fields = ['author']


class ArticleFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = ArticleModel
        fields = ['author']

# class