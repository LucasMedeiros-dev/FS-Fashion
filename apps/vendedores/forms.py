from django import forms
from django.core.validators import FileExtensionValidator
from django.forms import ModelForm
from .models import Vendedor


class VendedorForm(ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nome', 'foto', 'cpf', 'email']
        labels = {
            'nome': 'Nome',
            'foto': 'Foto',
            'cpf': 'CPF',
            'email': 'Email',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Selecione uma foto'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o CPF'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite o email'}),
        }

    foto = forms.ImageField(
        validators=[FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png'])]
    )
