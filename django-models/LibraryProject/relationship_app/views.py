from django.shortcuts import render
# from django.http import HttpResponse
from .models import Book
from .models import Library

from django.views.generic import DetailView
# Create your views here.
def books_view(request):
    books_list = Book.objects.all()
    context = {'books_list': books_list}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'
    template_name ='relationship_app/library_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = ['books'] = self.objects.books.all()
        return context
