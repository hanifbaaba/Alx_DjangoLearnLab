from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import UserRegisterForm, PostForm, UserCreationForm , ProfileUpdateForm,UserUpdateForm
from .models import Post
from django.contrib import messages
from django .forms import PostForm


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
  

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'blog/profile.html', context)


# class BlogLoginView(LoginView):
#     template_name = 'blog/login.html'

# class BlogLogoutView(LogoutView):
#     template_name = 'blog/logout.html'