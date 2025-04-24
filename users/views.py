from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail
from .forms import CustomUserCreationForm, CustomUserEditForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_mail(user.email)
        return super().form_valid(form)

    def send_welcome_mail(self, user_email):
        subject = "Добро пожаловать в наш сервис!"
        message = "Спасибо, что зарегистрировались в нашем сервисе!"
        from_email = "Ulia629736@yandex.ru"
        recipient_list = [user_email,]
        send_mail(subject,message, from_email, recipient_list)


@login_required
def edit_profile(request):
    form = CustomUserEditForm(instance=request.user)  # Инициализация формы вне условий

    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('catalog:product_list')  # Переход на главную страницу

    return render(request, 'users/edit_profile.html', {'form': form})