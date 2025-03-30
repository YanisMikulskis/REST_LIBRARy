from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import AuthorModel, BiographyModel, BookModel, ArticleModel
from rest_framework import serializers


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'


class BiographyModelSerializer(ModelSerializer):
    class Meta:
        model = BiographyModel
        fields = ['text', 'author']

class ArticleModelSerializer(ModelSerializer):
    # author = AuthorModelSerializer()
    class Meta:
        model = ArticleModel
        # exclude = ['name']
        fields = ['name_article', 'author']

class BookModelSerializer(ModelSerializer):
    # authors = serializers.StringRelatedField(many=True) проблема была в этом
    def validate(self, attrs): #данные = {'name_book': 'fdsfkk', 'authors': [<AuthorModel: Автор Иван Иванов>, <AuthorModel: Автор Пётр Сергеев>, <AuthorModel: Автор Виктор Иванов>]}

        print(f'данные = {attrs}')
        return attrs
    class Meta:
        model = BookModel
        fields = '__all__'