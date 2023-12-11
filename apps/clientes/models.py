from django.db import models
from localflavor.br.models import BRCPFField
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
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


class Cliente(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=50)
    sobrenome = models.CharField(verbose_name="Sobrenome", max_length=50)
    cpf = BRCPFField(verbose_name="CPF")
    nascimento = models.DateField(verbose_name="Data de Nascimento")
    telefone = BrazilianCellPhoneField(verbose_name="Celular")
    telefone_zap = models.BooleanField(verbose_name="Whatsapp")
    endereço = models.TextField(verbose_name="Endereço")
