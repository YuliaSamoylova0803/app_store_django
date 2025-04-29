from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = 'Creates moderator group with permissions'

    def handle(self, *args, **options):
        # Создаём группу
        group, created = Group.objects.get_or_create(name="Модератор продуктов")

        if created:
            # Получаем разрешения
            content_type = ContentType.objects.get_for_model(Product)

            # Разрешение на отмену публикации
            unpublish_perm, _ = Permission.objects.get_or_create(
                codename='can_unpublish_product',
                content_type=content_type
            )

            # Разрешение на удаление
            delete_perm = Permission.objects.get(
                codename='delete_product',
                content_type=content_type
            )

            # Добавляем разрешения в группу
            group.permissions.add(unpublish_perm, delete_perm)
            self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" создана'))
        else:
            self.stdout.write(self.style.WARNING('Группа уже существует'))