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
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from author.views import AuthorModelViewSet, BookModelViewSet, BiographyModelViewSet, ArticleModelViewSet
from author.views import *



router = DefaultRouter()
router.register('author', AuthorModelViewSet)

router.register('book', BookModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('article', ArticleModelViewSet)
#
# router.register('biographies', BiographyModelViewSet)
# router.register('articles', ArticleModelViewSet)
# router.register('books', BookModelViewSet)


urlpatterns = [
    path('', RedirectView.as_view(url='api/')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),




    # path('api/create/', AuthorCreateAPIView.as_view()),
    # path('api/list/', AuthorListAPIView.as_view()),
    # path('api/retrieve/<int:pk>/', AuthorRetrieveAPIView.as_view()),
    # path('api/destroy/<int:pk>/', AuthorDestroyAPIView.as_view()),
    # path('api/update/<int:pk>/', AuthorUpdateAPIView.as_view()

    # path('api/filters/', include(router.urls))
    # path('api/<str:name>/', AuthorModelViewSet.as_view()),
    # path('api/viewsets/', include(router.urls),
    # path'api/viewsets/<int:pk>/'

]
