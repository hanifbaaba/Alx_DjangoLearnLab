from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books_view, name='books'),
    path('library/int:pk>/', views.LibraryDetailView.as_view(), name='library_detail')
]




