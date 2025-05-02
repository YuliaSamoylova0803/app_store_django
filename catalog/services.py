from asgiref.timeout import timeout
from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED

def get_product_list_from_cache():
    """
    Получает данные по продуктам из кеша, если кеш пуст, получает данные из БД
    """
    if not CACHE_ENABLED:
        return Product.objects.all()

    key = "product_list"
    products = cache.get(key)

    if products is not None:
        return products

    products = Product.objects.all()
    cache.set(key, products)
    return products


class CategoryService:

    @staticmethod
    def get_products_by_category(category_id):
        """
        Возвращает список продуктов в указанной категории (с кешированием).
        """
        return Product.objects.filter(category_id=category_id).select_related("category")

