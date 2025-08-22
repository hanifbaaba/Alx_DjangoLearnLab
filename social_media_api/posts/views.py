from django.shortcuts import render
from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer
from rest_framework.permissions import  IsAuthenticated
from rest_framework import generics, mixins, permissions, viewsets


class IsAuthorOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.author == request.user

class PostCreateView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_class = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        POST /post/create/ — Create a new post.
        """
        return self.create(request, *args, **kwargs)
    

class PostUpdateView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_class = [permissions.IsAuthenticated]
    
    def put(self, request, *args, **kwargs):
        """
        PUT /post/update/ — update the post.
        """
        return self.update(request, *args, **kwargs)

class PostDeleteView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_class = [permissions.IsAuthenticated]
    

    def delete(self, request, *args, **kwargs):
        """
        DELETE /post/delete/<id>/ — Delete a post.
        """
        return self.destroy(request, *args, **kwargs)

class CommentCreateView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_class = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        POST /comment/create/ — Create a new comment.
        """
        return self.create(request, *args, **kwargs)


class  CommentUpdateView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_class = [permissions.IsAuthenticated]
    
    def put(self, request, *args, **kwargs):
        """
        PUT /comment/update/ — update the comment.
        """
        return self.update(request, *args, **kwargs)

class CommentDeleteView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_class = [permissions.IsAuthenticated]
    

    def delete(self, request, *args, **kwargs):
        """
        DELETE /comment/delete/<id>/ — Delete a comment.
        """
        return self.destroy(request, *args, **kwargs)
