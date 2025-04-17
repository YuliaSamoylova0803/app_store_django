from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig

from catalog.views import ProductListView, ProductDetailView, HomeView, ContactsView, ProductCreateViews, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("base/", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/new/", ProductCreateViews.as_view(), name="product_form"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),

]
