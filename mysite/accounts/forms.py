from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Atributos:
        model = CustomUser
        campo = ['username', 'email', 'password']

    def salvar(self, commit=True):
        user = super().salvar(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.salvar()
        return user
