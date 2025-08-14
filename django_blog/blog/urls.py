from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import register_view, profile_view, PostListView,PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),

    path("posts/", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    # path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    # path("post/<int:pk>/update/"), PostUpdateView.as_view(), name = 'post-update'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    
]

["post/<int:pk>/delete/", "post/new/"]
