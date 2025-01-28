# from django.test import TestCase

# Create your tests here.
from rest_framework import serializers
from models import AuthorModel
class AuthorSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=256)
    birthday = serializers.IntegerField()


author = AuthorModel('Вася', 'Пупкин', 1995)
print(author)