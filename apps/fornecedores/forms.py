from django import forms
from .models import Fornecedor


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ["nome", "empresa", "cnpj",
                  "email", "telefone", "telefone_zap"]

    nome = forms.CharField(
        label="Nome",
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={'autofocus': True, 'class': 'form-control',
                   'placeholder': 'Insira o Nome da Pessoa', 'id': 'fornecedor_nome'}
        )
    )
    empresa = forms.CharField(
        label="Empresa",
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Insira o Nome da Empresa', 'id': 'fornecedor_empresa'}
        )
    )
    cnpj = forms.CharField(
        label="CNPJ",
        max_length=18,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Insira o CNPJ', 'id': 'fornecedor_cnpj'}
        )
    )
    email = forms.EmailField(
        label="Email",
        max_length=254,
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Insira o Email', 'id': 'fornecedor_email'}
        )
    )
    telefone = forms.CharField(
        label="Telefone",
        max_length=15,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Insira o Telefone', 'id': 'fornecedor_telefone'}
        )
    )
    telefone_zap = forms.BooleanField(
        label="Telefone (WhatsApp)",
        required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input',
                   'id': 'fornecedor_telefone_zap'}
        )
    )
