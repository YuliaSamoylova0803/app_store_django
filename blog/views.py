from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import mail_admins
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from blog.models import Blog
from .forms import BlogForm

# Create your views here.
class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blog:blog_list")
    success_message = "Статья успешно создана!"
    permission_required = "blog.can_add_blog"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm("blog.can_add_blog"):
            messages.error(request, "У вас нет прав для создания статей")
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"
    context_object_name = "blogs"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.has_perm("blog.can_view_unpublished"):
            queryset = queryset.filter(is_published=True)
        return queryset.order_by("-created_at")


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = "blog"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.is_published and not self.request.user.has_perm('blog.can_view_unpublished'):
            raise PermissionDenied
        obj.views_counter += 1
        obj.save()

        if obj.views_counter == 100:
            messages.success(self.request, f'Статья "{obj.title}" достигла 100 просмотров!')

        return obj

    # def send_congratulation_email(self):
    #     """Отправка email админу"""
    #     subject = f"Статья {self.object.title} набрала 10 просмотров!"
    #     message = f"Поздравляем! Статья {self.object.title} набрала 100 просмотров."
    #     mail_admins(subject, message)


class BlogUpdateViews(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_form.html'
    success_message = "Статья успешно обновлена!"
    permission_required = "blog.can_change_blog"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not request.user.has_perm("blog.can_change_blog"):
            messages.error(request, "У вас нет прав для редактирования статей")
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteViews(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Blog
    template_name = "blog/blog_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")
    success_message = "Статья успешно удалена!"
    permission_required = "blog.can_delete_blog"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('blog.can_delete_blog'):
            messages.error(request, 'У вас нет прав для удаления статей')
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)