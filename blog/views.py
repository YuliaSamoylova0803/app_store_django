from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.models import Blog

# Create your views here.
class BlogCreateView(CreateView):
    model = Blog
    fields = ["title", "content", "preview", "is_published"]
    success_url = reverse_lazy("blog:blog_list")


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DeleteView):
    model = Blog


class BlogUpdateViews(UpdateView):
    model = Blog
    fields = ["title", "content", "preview", "created_at", "is_published"]
    success_url = reverse_lazy("blog:blog_list")


class BlogDeleteViews(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")