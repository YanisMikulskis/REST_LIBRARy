"""
URL configuration for library_pr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from author.views import AuthorModelViewSet, BookModelViewSet, BiographyModelViewSet, ArticleModelViewSet
from author.views import *
from rest_framework.permissions import AllowAny
from userapp_library.views import UserListAPIView
from rest_framework.authtoken import views
# from rest_framework.authtoken.views import C


from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='rest_library',
        default_version='0.1',
        description='doc to out project',
        contact=openapi.Contact(email='admin@admin.local'),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=[AllowAny]
)





router = DefaultRouter()
router.register('author', AuthorModelViewSet)
router.register('book', BookModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('article', ArticleModelViewSet)
# router.register('user', UserListAPIView)



urlpatterns = [
    path('', RedirectView.as_view(url='api/')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),




    # path('api/<str:version>/user/', UserListAPIView.as_view(), name='user')


    # path('api/users/0.1', include('userapp_library.urls', namespace='0.1')),
    # path('api/users/0.2', include('userapp_library.urls', namespace='0.2'))
    path('api/users/', UserListAPIView.as_view(), name = 'user'),
    # path('api/token', views.)

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),




]
