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
    author = AuthorModelSerializer()
    class Meta:
        model = ArticleModel
        exclude = ['name']

class BookModelSerializer(ModelSerializer):
    author = serializers.StringRelatedField(many=True)
    class Meta:
        model = BookModel
        fields = '__all__'