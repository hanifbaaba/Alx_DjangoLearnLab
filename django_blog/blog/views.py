from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import UserRegisterForm, UserUpdateForm, PostForm, CommentForm
from .models import Post, Comment


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = UserRegisterForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {"u_form": u_form}
    return render(request, "blog/profile.html", context)


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-published_date"]
    paginate_by = 10


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
def CommentCreateView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post-detail", pk=post.pk)
    else:
        form = CommentForm()
    return render(request, "blog/add_comment.html", {"form": form, "post": post})


@login_required
def CommentUpdateView(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author != request.user:
        messages.error(request, "You are not allowed to edit this comment.")
        return redirect("post-detail", pk=comment.post.pk)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("post-detail", pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, "blog/edit_comment.html", {"form": form, "comment": comment})


@login_required
def CommentDeleteView(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author != request.user:
        messages.error(request, "You are not allowed to delete this comment.")
        return redirect("post-detail", pk=comment.post.pk)

    if request.method == "POST":
        comment.delete()
        return redirect("post-detail", pk=comment.post.pk)

    return render(request, "blog/delete_comment.html", {"comment": comment})
