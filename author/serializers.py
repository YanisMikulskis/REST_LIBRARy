from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import AuthorModel, BiographyModel, BookModel, ArticleModel
from rest_framework import serializers


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'


class AuthorModelSerializerBase(ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('first_name',)


class BiographyModelSerializer(ModelSerializer):
    class Meta:
        model = BiographyModel
        fields = ['text', 'author']

class ArticleModelSerializer(ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ['name_article', 'author']




class BookModelSerializer(ModelSerializer):
    authors = AuthorModelSerializer(many=True)
    class Meta:
        model = BookModel
        fields = '__all__'

class BookModelSerializerBase(ModelSerializer):
    authors = AuthorModelSerializerBase(many=True)
    class Meta:
        model = BookModel
        fields = '__all__'
