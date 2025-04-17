from django import forms
from django.core.exceptions import ValidationError

from .models import Product

class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'purchase_price', 'category', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductForms, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'name'
        self.fields["name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите название продукта"
        })

        # Настройка атрибутов виджета для поля 'description'
        self.fields["description"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите описание продукта"
        })

        # Настройка атрибутов виджета для поля 'purchase_price'
        self.fields["purchase_price"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите цену продукта"
        })

        # Настройка атрибутов виджета для поля 'category'
        self.fields["category"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Выберите категорию продукта"
        })

        # Настройка атрибутов виджета для поля 'image'
        self.fields["image"].widget.attrs.update({
            "class": "form-control",
            "attept": "image/jpeg, image/png"
        })


    def clean_purchase_price(self):
        """
        Валидация цены (не может быть отрицательной)
        """
        purchase_price = self.cleaned_data.get("purchase_price")
        if purchase_price is not None and purchase_price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной")
        return purchase_price

    def clean_image(self):
        """
        Валидация изображения: проверка формата и размера
        """
        image = self.cleaned_data.get("image")

        if not image:
            return image

        valid_extensions = ["png", "jpeg", "jpg"]
        extension = image.name.split(".")[-1].lower()
        if extension not in valid_extensions:
            raise ValidationError("Недопустимый формат изображения. Разрешены только JPEG и PNG.")

        max_size = 5 * 1024 * 1024
        if image.size > max_size:
            raise ValidationError("Размер изображения не должен превышать 5 МБ.")

        return image

    def clean(self):
        """
        Валидация названия и описания на запрещенные слова
        """
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        forbidden_words = [
            "спам",
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар"
        ]
        errors = {}

        for word in forbidden_words:
            if word.lower() in name.lower():
                errors["name"] = f"Название содержит запрещенное слово: '{word}'"

        for word in forbidden_words:
            if word.lower() in description.lower():
                errors["description"] = f"Описание содержит запрещенное слово: '{word}'"

        if errors:
            for field, message in errors.items():
                self.add_error(field, message)

        return cleaned_data
