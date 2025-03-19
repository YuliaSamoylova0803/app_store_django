from django.db import models

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
        return f"Category {self.name}: description ({self.description})"


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

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "price"]

    def __str__(self):
        return f"Product {self.name}: description ({self.description})"
