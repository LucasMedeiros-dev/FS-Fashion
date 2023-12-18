from django import forms
from apps.marcas.models import Marca
from apps.produtos.models import Produto


class ProdutoCadastro(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'marca', 'preco',
                  'qntd_max', 'qntd_min', 'qtd_tam_p', 'qtd_tam_m', 'qtd_tam_g', 'qtd_tam_gg', 'img_produto']
        widgets = {
            'nome': forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Digite o nome completo do produto'}),
            'marca': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecione a marca'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o preço'}),
            'qntd_max': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quantidade máxima'}),
            'qntd_min': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quantidade mínima'}),
            'qtd_tam_p': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quantidade do tamanho P'}),
            'qtd_tam_m': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quantidade do tamanho M'}),
            'qtd_tam_g': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quantidade do tamanho G'}),
            'qtd_tam_gg': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quantidade do tamanho GG'}),
            'img_produto': forms.FileInput(attrs={'class': 'custom-file-input', 'placeholder': 'Selecione uma imagem do produto'}),
        }

        labels = {
            'nome': 'Nome',
            'marca': 'Marca',
            'preco': 'Preço',
            'qntd_max': 'Quantidade Máxima',
            'qntd_min': 'Quantidade Mínima',
            'qtd_tam_p': 'Quantidade Tamanho P',
            'qtd_tam_m': 'Quantidade Tamanho M',
            'qtd_tam_g': 'Quantidade Tamanho G',
            'qtd_tam_gg': 'Quantidade Tamanho GG',
            'img_produto': 'Imagem do Produto',
        }
