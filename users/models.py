from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Create your models here
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True, help_text="Изображение должно быть квадратным (рекомендуемый размер 200x200)")
    country = models.CharField(max_length=50, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",]

    def __str__(self):
        return f"{self.username} {self.email})"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
