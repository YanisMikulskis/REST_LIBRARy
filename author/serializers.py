from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import AuthorModel, BiographyModel, BookModel, ArticleModel
from rest_framework import serializers


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'

    # Если сериализатор используется вложенно — изменяем поля
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.context.get('nested', False):
    #         allowed = {'first_name'}
    #         existing = set(self.fields)
    #         for field in existing - allowed:
    #             self.fields.pop(field)

class BookSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = BookModel
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
    authors = AuthorModelSerializer(many=True)
    # def validate(self, attrs):
    #     return attrs
    class Meta:
        model = BookModel
        fields = '__all__'
