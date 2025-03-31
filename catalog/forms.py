from django import forms
from .models import Product

class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'purchase_price', 'category', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }