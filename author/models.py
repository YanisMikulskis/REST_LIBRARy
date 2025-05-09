from django.db import models



class AuthorModel(models.Model):
    first_name = models.CharField(max_length=64, default='Test name', verbose_name='Имя автора')
    last_name = models.CharField(max_length=64, default='Test surname', verbose_name='Фамилия автора')
    birthday_year = models.PositiveIntegerField(verbose_name='Год рождения автора')
    # class Meta:
    #     app_label = 'RESt_LIBRARy/author'
    def __str__(self):
        return f'Автор {self.first_name} {self.last_name}'




class BiographyModel(models.Model):
    text = models.TextField(verbose_name=f'Текст биографии')
    author = models.OneToOneField(AuthorModel, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return f'Биография автора {self.author}'

class BookModel(models.Model):
    name_book = models.CharField(max_length=128,verbose_name='Название книги')
    authors = models.ManyToManyField(AuthorModel, verbose_name='Авторы')

    def __str__(self):
        return f'Книга {self.name_book} авторы {self.authors}'
class ArticleModel(models.Model):
    name_article = models.CharField(max_length=256,verbose_name='Название статьи')
    author = models.ForeignKey(AuthorModel, on_delete=models.PROTECT, verbose_name='Автор статьи')
    def __str__(self):
        return f'статья {self.name} автора {self.author}'



