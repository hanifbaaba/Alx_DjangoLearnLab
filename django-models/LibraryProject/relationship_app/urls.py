from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('books/', views.books_view, name='books'),
    path('library/int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login', LoginView.as_view('login.html'), name = 'login'),
    path('logout', LogoutView.as_view('logout.html'), name = 'logout'),
    path('views.register', UserRegistrationView.as_view('register.html'), name = 'register')
]
