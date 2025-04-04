from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig

from catalog.views import ProductListView, ProductDetailView, HomeView, ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("base/", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    #path('test-pag/', views.test_pagination),
]
