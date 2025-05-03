from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig

from catalog.views import ProductListView, ProductDetailView, HomeView, ContactsView, ProductCreateViews, ProductUpdateView, ProductDeleteView, CategoryProductView

app_name = CatalogConfig.name

urlpatterns = [
    # Общедоступные пути
    path("base/", ProductListView.as_view(), name="product_list"),  # Общедоступный
    path("contacts/", ContactsView.as_view(), name="contacts"),

    # Защищенные пути (только для авторизованных)
    path("home/", HomeView.as_view(), name="home"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/new/", ProductCreateViews.as_view(), name="product_form"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("category/<int:category_id>/", CategoryProductView.as_view(), name="category_products"),
]
