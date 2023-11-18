from django import forms
from .models import Marca
from apps.fornecedores.models import Fornecedor


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ["nome", "fornecedores", "img_marca"]

    nome = forms.CharField(
        label="Marca",
        max_length=120, required=True,
        widget=forms.TextInput(
            attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Insira a Marca', 'id': 'marca_nome'}))
    fornecedores = forms.ModelChoiceField(
        label="Marca",
        queryset=Fornecedor.objects.all(),
        required=True, empty_label=None,
        widget=forms.Select(
            attrs={'autofocus': True, 'class': 'form-control'}))
    img_marca = forms.ImageField(
        label="Logotipo",
        required=True,
        widget=forms.FileInput(
            attrs={'class': 'custom-file-input', 'id': 'img_marca'}
        ))
