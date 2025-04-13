from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import AuthorModel, BiographyModel, BookModel, ArticleModel
from rest_framework import serializers


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'

    # Если сериализатор используется вложенно — изменяем поля
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context.get('nested', False):
            allowed = {'first_name'}
            existing = set(self.fields)
            for field in existing - allowed:
                self.fields.pop(field)







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
    # authors = AuthorModelSerializer(many=True, read_only=True)
    authors = serializers.SerializerMethodField()
    def validate(self, attrs): #данные = {'name_book': 'fdsfkk', 'authors': [<AuthorModel: Автор Иван Иванов>, <AuthorModel: Автор Пётр Сергеев>, <AuthorModel: Автор Виктор Иванов>]}

        print(f'данные = {attrs}')
        return attrs
    class Meta:
        model = BookModel
        # authors = model.objects.values('authors')
        # names = []
        # for i in authors:
        #     pk = list(i.values())[0]
        #     if pk is None:
        #         names.append('-')
        #     else:
        #         names.append(AuthorModel.objects.get(id=pk))
        # # print([AuthorModel.objects.get(id=list(i.values())[0]) for i in authors])
        # print(names)
        fields = '__all__'
    def get_authors(self, obj):
        serializer = AuthorModelSerializer(obj.authors.all(), many=True, context={'nested': True})
        return serializer.data
