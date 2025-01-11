from rest_framework.serializers import HyperlinkedModelSerializer
from .models import AuthorModel


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'