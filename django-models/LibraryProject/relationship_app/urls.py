from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, UserRegistrationView, is_admin, is_librarian, is_member
from django.contrib.auth.views import LoginView, LogoutView
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('books/', views.books_view, name='books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register.as_view(), name='register'),
    # path('register/', UserRegistrationView.as_view(template_name = 'relationship_app/register.html'), name = 'register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin/', admin_view, name = 'admin'),
    path('librarian/',librarian_view, name = 'librarian'),
    path('member/',member_view, name = 'member')

]

