from django import forms


class ProdutoCadastro(forms.Form):
    nome = forms.CharField(
        label="Nome",
        max_length=120, required=True,
        widget=forms.TextInput(
            attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Insira o Nome do Produto'}))

    marca = forms.CharField(
        label="Marca",
        max_length=120, required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Teste'}))

    qntd_max = forms.IntegerField(
        label="Quantidade Máxima",
        required=True,
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}))

    qntd_min = forms.IntegerField(
        label="Quantidade Mínima",
        required=True,
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}))

    qtd_tam_p = forms.IntegerField(
        label="Quantidade P",
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}))

    qtd_tam_m = forms.IntegerField(
        label="Quantidade M",
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}))

    qtd_tam_g = forms.IntegerField(
        label="Quantidade G",
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}))

    qtd_tam_gg = forms.IntegerField(
        label="Quantidade GG",
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}))

    img_produto = forms.ImageField(
        required=True,
        widget=forms.FileInput(
            attrs={'class': 'custom-file-input'}
        ))
