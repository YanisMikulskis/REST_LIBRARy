from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, action
from .models import AuthorModel, BookModel, BiographyModel, ArticleModel
from .serializers import AuthorModelSerializer, BiographyModelSerializer, BookModelSerializer, ArticleModelSerializer
from .pagination import ArticleLimitPagination, BookLimitPagination, BiographyLimitPagination, AuthorLimitPagination

# class AuthorModelViewSet(ModelViewSet):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     parser_classes = [JSONParser, FormParser]
#     queryset = AuthorModel.objects.all()
#     serializer_class = AuthorModelSerializer
#     pagination_class = AuthorLimitPagination

# class AuthorModelView(APIView):
#
#     renderer_classes = [JSONRenderer]
#     def get(self, request, format=None):
#         authors = AuthorModel.objects.all()
#         serializer = AuthorModelSerializer(authors, many=True)
#         return Response(serializer.data)


# @api_view(['GET'])
# @renderer_classes([JSONRenderer])
# def author_view(request):
#     authors = AuthorModel.objects.all()
#     serializer = AuthorModelSerializer(authors, many=True)
#     return Response(serializer.data)

from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, UpdateAPIView



# class AuthorCreateAPIView(CreateAPIView):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = AuthorModel.objects.all()
#     serializer_class = AuthorModelSerializer
# class AuthorListAPIView(ListAPIView):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = AuthorModel.objects.all()
#     serializer_class = AuthorModelSerializer
# class AuthorRetrieveAPIView(RetrieveAPIView):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = AuthorModel.objects.all()
#     serializer_class = AuthorModelSerializer
# class AuthorDestroyAPIView(DestroyAPIView):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = AuthorModel.objects.all()
#     serializer_class = AuthorModelSerializer
# class AuthorUpdateAPIView(UpdateAPIView):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = AuthorModel.objects.all()
#     serializer_class = AuthorModelSerializer





from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# class AuthorViewSet(viewsets.ViewSet):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     def list(self, request):
#         authors = AuthorModel.objects.all()
#         serializer = AuthorModelSerializer(authors, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         author = get_object_or_404(AuthorModel, pk=pk)
#         serializer = AuthorModelSerializer(author)
#         return Response(serializer.data)
#     @action(detail=True, methods = ['get'])
#     def only(self, request, pk=None):
#         author = AuthorModel.objects.get(id=pk)
#         return Response({'name': author.first_name, 'lastname': author.last_name})
    # def destroy(self, request, pk=None):
    #     author = get_object_or_404(AuthorModel, pk=pk)
    #     serializer = AuthorModelSerializer(author)
    #     return Response(serializer.data)
    # def only(self, request, pk=None):
    #     only_author = AuthorModel.objects.get(id=pk)
    #     serializer = AuthorModelSerializer(only_author)
    #     return Response(serializer.data)






# class AuthorModelViewSet(viewsets.ModelViewSet):
#     queryset = AuthorModel.objects.all()
#     renderer_classes = [JSONRenderer]
#     serializer_class = AuthorModelSerializer



from rest_framework import mixins

# class AuthorCustomViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
#     queryset = AuthorModel.objects.all()
#     serializer_class = AuthorModelSerializer
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

# class AuthorModelViewSet(ListAPIView):
#     # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     # queryset = AuthorModel.objects.all()
#     serializer_class = AuthorModelSerializer
#     # parser_classes = [JSONParser, FormParser, MultiPartParser]
#     def get_queryset(self):
#         name = self.kwargs['name']
#         return AuthorModel.objects.filter(first_name = name)


# class AuthorParam(ModelViewSet):
#     queryset = AuthorModel.objects.all()
#     serializer_class = AuthorModelSerializer
#
#     def get_queryset(self):
#         name = self.request.query_params.get('name', '')
#         authors = AuthorModel.objects.all()
#         if name:
#             authors = authors.filter(first_name=name)
#         return authors
from django_filters import filterset

from .filters import AuthorFilter, BookFilter, BiographyFilter, ArticleFilter
#------------------------
# class AuthorModelViewSet(ModelViewSet):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = AuthorModel.objects.all()
#     parser_classes = [JSONParser, FormParser, MultiPartParser]
#     serializer_class = AuthorModelSerializer
#     filterset_fields = ['id', 'first_name', 'last_name']
#     pagination_class = AuthorLimitPagination
#
# class BookModelViewSet(ModelViewSet):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = BookModel.objects.all()
#     parser_classes = [JSONParser, FormParser, MultiPartParser]
#     serializer_class = BookModelSerializer
#     filterset_fields = ['author']
#     pagination_class = BookLimitPagination
#
#
# class BiographyModelViewSet(ModelViewSet):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = BiographyModel.objects.all()
#     parser_classes = [JSONParser, FormParser, MultiPartParser]
#     serializer_class = BiographyModelSerializer
#     filterset_fields = ['author']
#     pagination_class = BiographyLimitPagination
#
# class ArticleModelViewSet(ModelViewSet):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = ArticleModel.objects.all()
#     parser_classes = [JSONParser, FormParser, MultiPartParser]
#     serializer_class = ArticleModelSerializer
#     pagination_class = ArticleLimitPagination
#     filterset_fields = ['author']
# Create your views here.

#------------------
class AuthorModelViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         viewsets.GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = AuthorModel.objects.all()
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    serializer_class = AuthorModelSerializer
    pagination_class = AuthorLimitPagination
    filterset_class = AuthorFilter


class BookModelViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = BookModel.objects.all()
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    serializer_class = BookModelSerializer
    pagination_class = BookLimitPagination
    filterset_class = BookFilter


class BiographyModelViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = BiographyModel.objects.all()
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    serializer_class = BiographyModelSerializer
    pagination_class = BiographyLimitPagination
    filterset_class = BiographyFilter


class ArticleModelViewSet(mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = ArticleModel.objects.all()
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    serializer_class = ArticleModelSerializer
    pagination_class = ArticleLimitPagination
    filterset_class = ArticleFilter



