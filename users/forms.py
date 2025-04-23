from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False,
                                   help_text="Необязательное поле: введите ваш номер телефона.")
    username = forms.CharField(max_length=50, required=True)
    avatar = forms.ImageField(required=False, help_text="Изображение должно быть квадратным (рекомендуемый размер 200x200)")
    # usable_password = None
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput, help_text="Ваш пароль должен содержать как минимум 8 символов.")
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput, help_text="Введите тот же пароль для подтверждения.")


    class Meta:
        model = CustomUser
        fields = ("avatar", "email", "username", "phone_number")

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен состоять только из цифр")
        return phone_number


class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone_number", "avatar", "country")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["avatar"].widget.attrs.update({"class": "form-control-file"})
        self.fields["email"].disabled = True
