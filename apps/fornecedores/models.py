from django.db import models
from localflavor.br.models import BRCNPJField
# Create your models here.


class Fornecedor(models.Model):
    nome = models.CharField(max_length=120)
    empresa = models.CharField(max_length=120)
    cnpj = BRCNPJField()
    email = models.EmailField(max_length=254)
    # telefone = models.phone_field()
    adicionado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.empresa
