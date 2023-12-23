from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'email', 'cpf', 'nascimento',
                  'telefone', 'telefone_zap', 'endereco']

    nome = forms.CharField(
        label="Nome",
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={'autofocus': True, 'class': 'form-control',
                   'placeholder': 'Insira o Nome da Pessoa', 'id': 'cliente_nome'}
        )
    )

    email = forms.EmailField(
        label="Email",
        max_length=120,
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Insira o Email', 'id': 'cliente_email'}
        )
    )
    sobrenome = forms.CharField(
        label="Sobrenome",
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Insira o Sobrenome', 'id': 'cliente_sobrenome'}
        )
    )
    cpf = forms.CharField(
        label="CPF",
        max_length=14,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Insira o CPF', 'id': 'cliente_cpf'}
        )
    )
    nascimento = forms.DateField(
        label="Data de Nascimento",
        required=True,
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            attrs={
                'class': 'form-control date-range-picker',
                'placeholder': 'Insira a Data de Nascimento',
                'id': 'cliente_nascimento'
            }
        )
    )
    telefone = forms.CharField(
        label="Telefone",
        max_length=15,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Insira o Telefone', 'id': 'cliente_telefone'}
        )
    )
    telefone_zap = forms.ChoiceField(
        label="Telefone (WhatsApp):",
        choices=[(True, 'Sim'), (False, 'Não')],
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control', 'id': 'cliente_telefone_zap'}
        )
    )
    endereco = forms.CharField(
        label="Endereço",
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Insira o Endereço', 'id': 'cliente_endereco'}
        )
    )
