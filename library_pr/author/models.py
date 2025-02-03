from django.db import models



class AuthorModel(models.Model):
    first_name = models.CharField(max_length=64, default='Test name')
    last_name = models.CharField(max_length=64, default='Test surname')
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return f'Автор {self.first_name} {self.last_name}'


class BiographyModel(models.Model):
    text = models.TextField()
    author = models.OneToOneField(AuthorModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'Биография автора {self.author}'

class BookModel(models.Model):
    name = models.CharField(max_length=128)
    author = models.ManyToManyField(AuthorModel)

    def __str__(self):
        return f'Книга {self.name} авторы {self.author}'
class ArticleModel(models.Model):
    name = models.CharField(max_length=256)
    author = models.ForeignKey(AuthorModel, on_delete=models.PROTECT)
    def __str__(self):
        return f'статья {self.name} автора {self.author}'



