from django.db import models
from localflavor.br.models import BRCPFField
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
# Create your models here.


class BrazilianCellPhoneField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 13
        kwargs['validators'] = [
            RegexValidator(
                # Updated regex pattern
                regex=r'^(55\d{11})|(0?\d{2}\s?9\d{4}\s?-?\d{4})$',
                message='Insira um telefone válido',
                code='telefone_invalido'
            )
        ]
        super().__init__(*args, **kwargs)


class Cliente(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=50)
    sobrenome = models.CharField(verbose_name="Sobrenome", max_length=50)
    cpf = BRCPFField(verbose_name="CPF", unique=True)
    nascimento = models.DateField(verbose_name="Data de Nascimento")
    email = models.EmailField(verbose_name="Email", max_length=254, blank=True)
    telefone = BrazilianCellPhoneField(verbose_name="Celular", blank=True)
    telefone_zap = models.BooleanField(verbose_name="Whatsapp")
    endereco = models.TextField(verbose_name="Endereço")
    cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cpf} - {self.nome} {self.sobrenome}"
