from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import UserProfile
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect


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

class LoginView(LoginView):
    template_name = 'users/login.html'

class LogoutView(LogoutView):
    next_page = reverse_lazy('login')

class UserRegistrationView(CreateView):
    form_class = UserCreationForm()
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')



def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# @user_passes_test(is_admin)
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')

# @user_passes_test(is_librarian)
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')

# @user_passes_test(is_member)
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')

# ///
# def is_admin(user):
#     return user.userprofile.role == 'Admin'

# def is_librarian(user):
#     return user.userprofile.role == 'Librarian'

# def is_member(user):
#     return user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        publication_year = request.POST.get('publication_year')

        book = Book(title=title, author_id=author_id, publication_year=publication_year)
        book.save()
        return redirect('book_list')  
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author_id = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('book_list')  
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  

    return render(request, 'relationship_app/delete_book.html', {'book': book})