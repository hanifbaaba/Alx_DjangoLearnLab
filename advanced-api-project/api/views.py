from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, mixins, permissions, filters
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend


class BookListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] 

    def get(self, request, *args, **kwargs):
        """
        GET /books/ — Returns a list of all books.
        """
        return self.list(request, *args, **kwargs)

class BookDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  

    def get(self, request, *args, **kwargs):
        """
        GET /books/<id>/ — Returns details of a specific book.
        """
        return self.retrieve(request, *args, **kwargs)

class BookCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def post(self, request, *args, **kwargs):
        """
        POST /books/create/ — Create a new book.
        """
        return self.create(request, *args, **kwargs)

class BookUpdateView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def put(self, request, *args, **kwargs):
        """
        PUT /books/update/<id>/ — Update an existing book.
        """
        return self.update(request, *args, **kwargs)

class BookDeleteView(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def delete(self, request, *args, **kwargs):
        """
        DELETE /books/delete/<id>/ — Delete a book.
        """
        return self.destroy(request, *args, **kwargs)

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']