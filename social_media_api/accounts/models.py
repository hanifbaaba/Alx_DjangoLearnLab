from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField( upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="following_set",
        blank=True)
    following = models.ManyToManyField(
          'self',
          symmetrical=False,
          related_name='followers_set',
          blank=True      
    )
    
    def __str__(self):
        return self.username




