from django.urls import path
from .views import UserListAPIView


app_name = 'userapp_library'
urlpatterns = [
    path('', UserListAPIView.as_view())
]