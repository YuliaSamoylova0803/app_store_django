from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForms

def home(request):
    if request.method == 'POST':
        form = ProductForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
    else:
        form = ProductForms()

    # Получаем все товары и настраиваем пагинацию
    products_list = Product.objects.all().order_by('id')
    paginator = Paginator(products_list, 6) # 6 товаров

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "catalog/home.html", {
        'form': form,
        'page_obj': page_obj
    })


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}. Сообщение получено!")
    return render(request, "catalog/contacts.html")


def home_view(request):
    # Выборка последних 5 созданных продуктов
    latest_products = Product.objects.order_by('-created_at')[:5]

    # Вывод в консоль
    for product in latest_products:
        print(f"Product: {product.name}, Created at: {product.created_at}")

    # Передача данных в шаблон (если нужно отобразить на странице)
    context = {
        'latest_products': latest_products
    }

    return render(request, 'home.html', context)


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/product_list.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)
