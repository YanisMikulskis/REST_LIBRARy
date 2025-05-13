from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, action
from .models import AuthorModel, BookModel, BiographyModel, ArticleModel

# from REST_LIBRARy.author.models import AuthorModel, BookModel, BiographyModel, ArticleModel

from .serializers import AuthorModelSerializer, BiographyModelSerializer, BookModelSerializer, ArticleModelSerializer, \
AuthorModelSerializerBase, BookModelSerializerBase

from .pagination import ArticleLimitPagination, BookLimitPagination, BiographyLimitPagination, AuthorLimitPagination

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from django_filters import filterset
from .filters import AuthorFilter, BookFilter, BiographyFilter, ArticleFilter
# Create your views here.
from rest_framework.permissions import (
    AllowAny,
    BasePermission, IsAuthenticatedOrReadOnly,
    DjangoModelPermissions,
    IsAuthenticatedOrReadOnly,
    DjangoModelPermissionsOrAnonReadOnly,
    IsAuthenticated)

from rest_framework.authentication import TokenAuthentication


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


# ------------------

class AuthorModelViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = AuthorModel.objects.all()
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    serializer_class = AuthorModelSerializer
    pagination_class = AuthorLimitPagination
    filterset_class = AuthorFilter

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return AuthorModelSerializerBase
        return AuthorModelSerializer



class BookModelViewSet(ModelViewSet):
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    queryset = BookModel.objects.all()
    serializer_class = BookModelSerializer
    pagination_class = BookLimitPagination
    filterset_class = BookFilter

    def get_serializer_class(self):
        # if self.request.version == '0.2':
        #     return BookModelSerializerBase
        # return BookSerializer
        if self.request.method in ['GET']:
            return BookModelSerializer
        return BookModelSerializerBase


#

class BiographyModelViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin,
                            viewsets.GenericViewSet, ):
    permission_classes = [
        DjangoModelPermissionsOrAnonReadOnly]  # данная категория прав настраивается в админке на каждого юзера

    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = BiographyModel.objects.all()
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    serializer_class = BiographyModelSerializer
    pagination_class = BiographyLimitPagination
    filterset_class = BiographyFilter


class ArticleModelViewSet(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          viewsets.GenericViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = ArticleModel.objects.all()
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    serializer_class = ArticleModelSerializer
    pagination_class = ArticleLimitPagination
    filterset_class = ArticleFilter
