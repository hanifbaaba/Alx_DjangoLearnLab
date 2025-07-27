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
    path('admin/',views.admin_view, name = 'admin_view'),
    path('librarian/',views.librarian_view, name = 'librarian_view'),
    path('member/',views.member_view, name = 'member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),

]


