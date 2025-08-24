from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile, name="profile"),

    path("posts/", views.PostListView.as_view(), name="post-list"),
    path("post/new/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),

    path("post/<int:pk>/comments/new", views.CommentCreateView, name="add-comment"),
    path("comment/<int:pk>/update/", views.CommentUpdateView, name="comment-update"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView, name="comment-delete"),
    path("search/", views.search_posts, name="search-posts"),
    path("tags/<str:tag_name>/", views.posts_by_tag, name="posts-by-tag"),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts_by_tag'),
]

