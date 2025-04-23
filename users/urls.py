from django.contrib.auth.decorators import login_required
from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, edit_profile

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="catalog:product_list"), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("edit_profile/", login_required(edit_profile), name="edit_profile"),
]