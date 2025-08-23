from django.shortcuts import render, get_object_or_404,redirect
from .models import Comment, Post, Like
from .serializers import CommentSerializer, PostSerializer
from rest_framework.permissions import  IsAuthenticated
from rest_framework import generics, mixins, permissions, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from notifications.models import Notification


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

class UserFeedView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # serializer_class = PostSerializer
    # queryset = Post.objects.all()

    def feed(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


def like_unlike_post(request,pk):
    post = generics.get_object_or_404(Post,pk= pk)
    user = request.user

    if request.method == 'POST':
        like, created = Like.objects.get_or_create(user=user, post=post)


    if not created:
        like.delete()
    
    else:
        # Like.objects.create(user=user, post = post)
        Notification.objects.create(
            user = post.author,
            sender = user,
            post = post,
            notification_type = like
        )
    return redirect('post_detail', pk=pk)
