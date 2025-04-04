from django.core.mail import mail_admins
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
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
    template_name = "blog/blog_list.html"
    context_object_name = "object_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1

        #Проверяем достижения 100 просмотров
        if self.object.views_counter == 100:
            print(f"Статья {self.object.title} набрала 100 просмотров!")

        self.object.save()
        return self.object

    # def send_congratulation_email(self):
    #     """Отправка email админу"""
    #     subject = f"Статья {self.object.title} набрала 10 просмотров!"
    #     message = f"Поздравляем! Статья {self.object.title} набрала 100 просмотров."
    #     mail_admins(subject, message)


class BlogUpdateViews(UpdateView):
    model = Blog
    fields = ["title", "content", "preview", "is_published"]
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteViews(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")