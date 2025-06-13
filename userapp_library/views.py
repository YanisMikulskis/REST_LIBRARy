from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserSerializerFull
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserSerializerFull
        return UserSerializer

# class UserListAPIView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def get_serializer_class(self):
#         if self.request.version == '0.2':
#             return UserSerializerFull
#         return UserSerializer


# class UserListAPIView(APIView):
#     # queryset = User.objects.all()
#
#     def get_serializer_class(self):
#         if self.request.version == '0.2':
#             return UserSerializerFull
#         return UserSerializer
#
#
#     def get(self, request, *args, **kwargs):
#         users = User.objects.all()
#         serializer_class = self.get_serializer_class()
#         serializer = serializer_class(users, many=True)
#         return Response(serializer.data)


# Create your views here.
