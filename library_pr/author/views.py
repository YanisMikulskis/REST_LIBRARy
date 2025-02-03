from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser, FormParser
from .models import AuthorModel, BookModel, BiographyModel, ArticleModel
from .serializers import AuthorModelSerializer, BiographyModelSerializer, BookModelSerializer, ArticleModelSerializer

class AuthorModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    parser_classes = [JSONParser, FormParser]
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorModelSerializer

class BookModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = BookModel.objects.all()
    parser_classes = [JSONParser, FormParser]
    serializer_class = BookModelSerializer
class BiographyModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = BiographyModel.objects.all()
    parser_classes = [JSONParser, FormParser]
    serializer_class = BiographyModelSerializer
class ArticleModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = ArticleModel.objects.all()
    parser_classes = [JSONParser, FormParser]
    serializer_class = ArticleModelSerializer
# Create your views here.
