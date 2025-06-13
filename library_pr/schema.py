import graphene
from graphene_django import DjangoObjectType
from author.models import AuthorModel, BookModel

# class Query(graphene.ObjectType):
#     hello = graphene.String(default_value='Hello!')
#
# schema = graphene.Schema(query=Query)

class BookType(DjangoObjectType):
    class Meta:
        model = BookModel
        fields = '__all__'

class AuthorType(DjangoObjectType):
    class Meta:
        model = AuthorModel
        fields = '__all__'


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_authors = graphene.List(AuthorType)
    author_by_id = graphene.Field(AuthorType, id=graphene.Int(required=True))
    books_by_author_name = graphene.List(BookType, name_author=graphene.String(required=False))
    def resolve_all_books(self, info):
        return BookModel.objects.all()

    def resolve_all_authors(self, info):
        return AuthorModel.objects.all()

    def resolve_author_by_id(self, info, id):
        try:
            return AuthorModel.objects.get(id=id)
        except AuthorModel.DoesNotExists:
            return None

    def resolve_books_by_author_name(self, info, name_author=None):
        books = BookModel.objects.all()
        if name_author:
            books = books.filter(authors__first_name = name_author)
        return books


class AuthorMutation(graphene.Mutation):
    class Arguments:
        birthday_year = graphene.Int(required=True)
        id = graphene.ID()
    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, birthday_year, id):
        update_authors = AuthorModel.objects.get(pk=id)
        update_authors.birthday_year = birthday_year
        update_authors.save()
        return AuthorMutation(author=update_authors)
class Mutation(graphene.ObjectType):
    update_author = AuthorMutation.Field()






schema = graphene.Schema(query=Query, mutation=Mutation)

