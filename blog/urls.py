from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogDetailView, BlogListView, BlogUpdateViews, BlogDeleteViews

app_name = BlogConfig.name

urlpatterns = [
    path("blogs/new/", BlogCreateView.as_view(), name="blog_create"),
    path("blogs/blog_list/", BlogListView.as_view(), name="blog_list"),
    path("blogs/blog_detail/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blogs/<int:pk>/update/", BlogUpdateViews.as_view(), name="blog_update"),
    path("blogs/<int:pk>/delete/", BlogDeleteViews.as_view(), name="blog_delete")

]