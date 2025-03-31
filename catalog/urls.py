from django.urls import path

from catalog.apps import CatalogConfig

from catalog.views import product_list, product_detail, home, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("base/", product_list, name="product_list"),
    path("product/<int:product_id>", product_detail, name="product_detail")

]
