from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(null=True, blank=True, verbose_name="Содержимое")
    preview = models.ImageField(upload_to="blogs/images", blank=True, null=True, verbose_name="Превью")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано", help_text="Отметьте, чтобы опубликовать запись")
    views_counter = models.PositiveIntegerField(verbose_name="Счетчик просмотров", default=0,
                                                help_text="Укажите количество просмотров")

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"
        ordering = ["title"]
        permissions = [
            ("can_add_blog", "Может добавлять статьи"),
            ("can_change_blog", "Может изменять статьи"),
            ("can_delete_blog", "Может удалять статьи"),
            ("can_view_blog", "Может просматривать статьи"),
            ("can_view_unpublished", "Может просматривать неопубликованные статьи"),
            ("can_publish_blog", "Может публиковать статьи"),
        ]

    def __str__(self):
        return self.title
