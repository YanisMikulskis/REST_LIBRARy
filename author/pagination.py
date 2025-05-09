from rest_framework.pagination import LimitOffsetPagination

class ArticleLimitPagination(LimitOffsetPagination):
    def __init__(self):
        self.default_limit = 10



class BookLimitPagination(LimitOffsetPagination):
    def __init__(self):
        self.default_limit = 10


class BiographyLimitPagination(LimitOffsetPagination):
    def __init__(self):
        self.default_limit = 10


class AuthorLimitPagination(LimitOffsetPagination):
    def __init__(self):
        self.default_limit = 10

