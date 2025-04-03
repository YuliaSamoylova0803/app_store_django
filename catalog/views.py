from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForms
from django.views.generic import ListView, DeleteView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormMixin


# app_name/<model_name>_action
# catalog/home
class HomeView(FormMixin, ListView):
    template_name = 'catalog/home.html'
    form_class = ProductForms
    model = Product
    paginate_by = 6
    ordering = ['id']
    context_object_name = 'products'

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.get_form()
        return context


# Временный код для проверки (удалите после тестирования)
from django.http import HttpResponse
def test_pagination(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page = paginator.get_page(1)
    return HttpResponse(f"Всего товаров: {paginator.count}, Страниц: {paginator.num_pages}, На странице: {len(page)}")


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f'Спасибо, {name}.Сообщение получено!')


# app_name/<model_name>_action
# catalog/contacts
class HomeViewView(ListView):
    template_name = 'home.html'
    context_object_name = 'latest_products'
    queryset = Product.objects.order_by('created_at')[:5]

    def get(self, request, *args, **kwargs):
        for product in self.get_queryset():
            print(f'Product: {product.name}, Created at: {product.created_at}')
        return super().get(request, *args, **kwargs)


# app_name/<model_name>_action
# catalog/product_list
class ProductListView(ListView):
    model = Product

# app_name/<model_name>_action
# catalog/product_detail
class ProductDetailView(DetailView):
    model = Product
