from django.template import Library
from Introduction_to_Django.LibraryProject.bookshelf.models import Book
from Introduction_to_Django.LibraryProject.bookshelf.models import Author
from Introduction_to_Django.LibraryProject.bookshelf.models import Librarian
from Introduction_to_Django.LibraryProject.bookshelf.models import Library



author_name = 'Hanif'
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

library_name = 'Hanif Library'
library = Library.objects.get(Library=library_name)
all_books = library.books.all()

library_name = 'Hanif Library'
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)