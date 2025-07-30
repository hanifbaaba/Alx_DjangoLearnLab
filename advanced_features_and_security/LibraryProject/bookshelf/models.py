from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()


class Author(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

  def __str__(self):
    return self.title

class Library(models.Model):
  name = models.CharField(max_length=100)
  books = models.ManyToManyField(Book, related_name='books')

  def __str__(self):
    return self.name

class Librarian(models.Model):
  name = models.CharField(max_length=100)
  library = models.OneToOneField(Library, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
ROLE_CHOICES = (
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f'{self.user.username} ({self.role})'
    
    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        ]

class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile/")
   

  
class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("User must have email address")
        user = self.model(self.normalize_email(email))
        user.set_password(password)
        user.save(using = user._db)
        return user
    
    def create_superuser(self, email, password):
        user =self.crete_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)