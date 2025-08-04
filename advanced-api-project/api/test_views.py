from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        
        self.book1 = Book.objects.create(title="Django for APIs", author="William", publication_year=2020)
        self.book2 = Book.objects.create(title="Python Basics", author="Sara", publication_year=2021)
        self.list_url = reverse("book_list_create")

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": "Author A",
            "publication_year": 2023
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url + "?author=William")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], "William")

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url + "?search=Django")
        self.assertEqual(len(response.data), 1)
        self.assertIn("Django", response.data[0]['title'])

    def test_order_books_by_title(self):
        response = self.client.get(self.list_url + "?ordering=title")
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, sorted(titles))

    def test_update_book(self):
        detail_url = reverse("book_detail", args=[self.book1.id])
        data = {
            "title": "Updated Django Book",
            "author": "William",
            "publication_year": 2020
        }
        response = self.client.put(detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django Book")

    def test_delete_book(self):
        detail_url = reverse("book_detail", args=[self.book1.id])
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_authentication_required(self):
        self.client.logout()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
