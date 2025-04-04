from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogDetailView, BlogListView, BlogUpdateViews, BlogDeleteViews

app_name = BlogConfig.name

urlpatterns = [
    path("new/", BlogCreateView.as_view(), name="blog_create"),
    path("blog_list/", BlogListView.as_view(), name="blog_list"),
    path("blog_detail/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("<int:pk>/update/", BlogUpdateViews.as_view(), name="blog_update"),
    path("<int:pk>/delete/", BlogDeleteViews.as_view(), name="blog_delete")

]