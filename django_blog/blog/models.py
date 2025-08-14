from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

def __str__(self):
    return self.title

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True , null=True)
#     profile_picture = models.ImageField(upload_to="profile_pics", blank=True, null=True )

# def __str__(self):
#     return f"{self.user.name} Profile"


def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk': self.pk}) 

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
           ordering = ['-created_at'] 

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'