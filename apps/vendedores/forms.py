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
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome', 'id': 'nome'}),
            'foto': forms.FileInput(attrs={'class': 'custom-file-input', 'id': 'foto'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o CPF', 'id': 'cpf'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite o email', 'id': 'email'}),
        }
