import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import AuthorModelViewSet, BookModelViewSet
from .models import AuthorModel, BookModel


class TestAuthorViewSet(TestCase):

    def setUp(self):
        self.first_name = 'ИванИван'
        self.birthday_year = '1900'
        self.data_author = {'first_name': self.first_name, 'birthday_year': self.birthday_year}
        self.put_data = {'first_name': 'ДмитрийДмитрий', 'birthday_year': 2000}
        self.url_author = '/api/author/'
        self.url_book = '/api/book/'
        self.admin = ['admin', 'admin@admin.com', 'admin12345']
        self.get_list = {'get': 'list'}
        self.post_create = {'post': 'create'}

    def test_get_list(self):
        factory = APIRequestFactory()
        print(factory)
        request = factory.get(self.url_author)
        view = AuthorModelViewSet.as_view(self.get_list)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url_author, self.data_author, format='json')
        view = AuthorModelViewSet.as_view(self.post_create)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url_author, self.data_author, format='json')
        admin = User.objects.create_superuser(*self.admin)
        force_authenticate(request, admin)
        view = AuthorModelViewSet.as_view(self.post_create)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        author = AuthorModel.objects.create(first_name=self.first_name, birthday_year=self.birthday_year)
        client = APIClient()
        response = client.get(f'{self.url_author}{author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        author = AuthorModel.objects.create(first_name=self.first_name, birthday_year=self.birthday_year)
        client = APIClient()
        response = client.put(f'{self.url_author}{author.id}/', self.put_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        author = AuthorModel.objects.create(first_name=self.first_name, birthday_year=self.birthday_year)
        client = APIClient()

        User.objects.create_superuser(*self.admin)
        client.login(username=self.admin[0], password=self.admin[2])

        response = client.put(f'{self.url_author}{author.id}/', self.put_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        author = AuthorModel.objects.get(id=author.id)
        self.assertEqual(author.first_name, 'ДмитрийДмитрий')
        self.assertEqual(author.birthday_year, 2000)
        client.logout()




class TestBookViewSet(APITestCase):
    def setUp(self):
        self.url_book = '/api/book/'

        self.name_author = 'Пушкин'
        self.birthday_author = 1799
        self.book_name = 'Пиковая дама'
        self.new_book_name = 'Руслан и Людмила'
        self.admin_name = ['admin', 'admin@admin.ru', 'admin12345']

    def admin_login(self):
        User.objects.create_superuser(*self.admin_name)
        self.client.login(username='admin', password='admin12345')

    def test_get_list(self):
        response = self.client.get(self.url_book)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        author = AuthorModel.objects.create(first_name=self.name_author,
                                            birthday_year=self.birthday_author)
        book = BookModel.objects.create(name_book='Пиковая дама')

        book.authors.set([author])

        self.admin_login()

        response = self.client.put(f'{self.url_book}{book.id}/',
                                   {'name_book': self.new_book_name,
                                    'authors': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_book = BookModel.objects.get(id=book.id)
        self.assertEqual(new_book.name_book, 'Руслан и Людмила')
        self.client.logout()
    def test_edit_mixer(self):
        book = mixer.blend(BookModel)
        self.admin_login()

        response = self.client.put(f'{self.url_book}{book.id}/',
                                   {'name_book': self.new_book_name,
                                    'authors': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_book = BookModel.objects.get(id=book.id)
        self.assertEqual(new_book.name_book, 'Руслан и Людмила')
        self.client.logout()
    def test_get_detail(self):
        book = mixer.blend(BookModel, name_book = 'Алые паруса')
        response = self.client.get(f'{self.url_book}{book.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_book = json.loads(response.content)
        self.assertEqual(response_book['name_book'], 'Алые паруса')

    def test_get_detail_author(self):
        book = mixer.blend(BookModel, authors__first_name = 'Пушкин')
        response = self.client.get(f'{self.url_book}{book.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_book = json.loads(response.content)
        self.assertEqual(response_book['authors'][0]['first_name'], 'Пушкин')


