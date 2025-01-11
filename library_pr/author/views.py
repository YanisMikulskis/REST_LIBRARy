from rest_framework.viewsets import ModelViewSet
from .models import AuthorModel
from .serializers import AuthorModelSerializer

class AuthorModelViewSet(ModelViewSet):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorModelSerializer


# Create your views here.
