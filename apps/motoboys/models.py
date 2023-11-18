from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from localflavor.br.models import BRCPFField
# Create your models here.


class BrazilianPlates(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 11
        kwargs['validators'] = [
            RegexValidator(
                regex=r'^([A-Z]{3}[0-9][A-Z][0-9]{3})|([A-Z]{3}[0-9]{4})$',
                message='Insira uma placa válida.',
                code='placa_invalida'
            ),
        ]
        super().__init__(*args, **kwargs)


class Motoboy(models.Model):
    nome = models.CharField(max_length=120)
    foto = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=None)
    cpf = BRCPFField()
    email = models.EmailField(max_length=254)
    adicionado = models.DateTimeField(auto_now_add=True)
    placa = BrazilianPlates()

    def __str__(self):
        return self.nome
