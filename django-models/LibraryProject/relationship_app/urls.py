from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('books/', views.books_view, name='books'),
    path('library/int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login', UserLoginView.as_view(), name = 'login'),
    path('logout', UserLogoutView.as_view(), name = 'logout'),
    path('register', UserRegistrationView.as_view(), name = 'register')
]
