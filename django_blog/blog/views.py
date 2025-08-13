from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import RegisterForm, PostForm
from .models import Post


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect("profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def profile_view(request):
    if request.method == 'POST':
     request.user.email = request.POST.get('email')
     request.user.save()
    return render(request, "registration/profile.html")


class PostListView(ListView):
  model = Post
  template_name = "blog/post_list.html"        
  context_object_name = "posts"
  ordering = ["-published_date"]
  paginate_by = 10  # 

class PostDetailView(DetailView):
  model = Post
  template_name = "blog/post_detail.html"     
  context_object_name = "post"

class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  form_class = PostForm
  template_name = "blog/post_form.html" 

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post
  form_class = PostForm
  template_name = "blog/post_form.html"

  def test_func(self):
    post = self.get_object()
    return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Post
  template_name = "blog/post_confirm_delete.html"
  success_url = reverse_lazy("post-list")

  def test_func(self):
    post = self.get_object()
    return post.author == self.request.user