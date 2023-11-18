from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from localflavor.br.models import BRCNPJField
# Create your models here.


class BrazilianCellPhoneField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 11
        kwargs['validators'] = [
            RegexValidator(
                regex=r'^0?\d{2}\s?9\d{4}\s?-?\d{4}$',
                message='Insira um telefone válido',
                code='telefone_invalido'
            )
        ]
        super().__init__(*args, **kwargs)


class Fornecedor(models.Model):
    nome = models.CharField(max_length=120)
    empresa = models.CharField(max_length=120)
    cnpj = BRCNPJField()
    email = models.EmailField(max_length=254)
    telefone = BrazilianCellPhoneField(blank=True)
    telefone_zap = models.BooleanField(default=False)
    adicionado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.empresa
