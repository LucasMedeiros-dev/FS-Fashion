from django import forms
from .models import Marca


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ["nome", "img_marca"]

    nome = forms.CharField(
        label="Marca",
        max_length=120, required=True,
        widget=forms.TextInput(
            attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Insira o Nome do Produto', 'id': 'marca_nome'}))
    img_marca = forms.ImageField(
        label="Logotipo",
        required=True,
        widget=forms.FileInput(
            attrs={'class': 'custom-file-input', 'id': 'img_marca'}
        ))
