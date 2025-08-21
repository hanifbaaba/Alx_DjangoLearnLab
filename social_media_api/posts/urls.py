from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostCreateView, CommentCreateView

router = DefaultRouter()
router.register(r'posts', PostCreateView, basename='post')
router.register(r'comments', CommentCreateView, basename='comment')