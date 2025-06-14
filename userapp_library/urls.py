from django.urls import path
from .views import UserModelViewSet


app_name = 'userapp_library'
urlpatterns = [
    path('', UserModelViewSet.as_view())
]