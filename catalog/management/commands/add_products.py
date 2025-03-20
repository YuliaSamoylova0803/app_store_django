from django.core.management.base import BaseCommand
from catalog.models import Product,Category
from django.core.management import call_command

class Command(BaseCommand):
    help = "Load test data from fixture"

    def handle(self, *args, **options):

        #Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Загрузка данных по категориям из фикстуры
        call_command('loaddata', 'categories_fixture.json')
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded data from fixture'))

        # Загрузка данных по продуктам из фикстуры
        call_command('loaddata', 'products_fixture.json')
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded data from fixture'))

        # Остальной код
        category, _ = Category.objects.get_or_create(name='Крупы', description='Пищевой продукт, состоящий из цельных или дроблёных зёрен различных культур')

        products = [
            {'name': 'Рис', 'description': 'Зёрна одноимённого растения, является основным пищевым продуктом для населения Земли', 'purchase_price': '150', 'category': category},
            {'name': 'Греча',
             'description': 'Гречку (гречневую крупу) получают из зерен гречихи посевной',
             'purchase_price': '120', 'category': category},
            {'name': 'Пшено',
             'description': 'Kрупа, получаемая из плодов культурных видов проса (Panicum), освобождённых от колосковых чешуек посредством обдирки',
             'purchase_price': '80', 'category': category},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))
