from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from books.models import Author, Book
from books.serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    class_serializer = AuthorSerializer


class BookViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    class_serializer = BookSerializer