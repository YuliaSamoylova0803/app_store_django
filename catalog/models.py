import uuid

from django.db import models
from django.utils.text import slugify

from users.models import CustomUser
# Create your models here.


class Category(models.Model):
    # наименование, описание, изображение, категория, цена за покупку, дата создания, дата последнего изменения.
    name = models.CharField(max_length=150, verbose_name="Название категории")
    description = models.TextField(
        null=True, blank=True, verbose_name="Описание категории"
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="products/images", blank=True, null=True, verbose_name="Изображение"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="products",
    )
    purchase_price = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата последнего изменения"
    )

    owner = models.ForeignKey(CustomUser, verbose_name="Владелец", help_text="Укажите владельца продукта", blank=True, null=True, on_delete=models.SET_NULL)
    is_published = models.BooleanField(default=False,verbose_name="Опубликован", help_text="Отметьте, чтобы опубликовать продукт")


    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "purchase_price"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),

        ]


    def __str__(self):
        return f"{self.name}: {self.description}"


class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.TextField(verbose_name='Адрес')

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} {self.email}'