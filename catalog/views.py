from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def home(request):
    return render(request, "catalog/home.html")


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
