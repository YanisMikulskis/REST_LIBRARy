import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import AuthorModelViewSet
# from .models import AuthorModel, BookModel


class TestAuthorViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        print(factory)
        request = factory.get('/api/author/')
        view = AuthorModelViewSet.as_view({'get':'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/author/', {'first_name': 'ИванИван',
                                                'birthday_year': 1900}, format='json')
        view = AuthorModelViewSet.as_view({'post':'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)