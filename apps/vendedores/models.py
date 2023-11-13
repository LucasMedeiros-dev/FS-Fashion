from django.db import models
from localflavor.br.models import BRCPFField
# Create your models here.


class Vendedor(models.Model):
    nome = models.CharField(max_length=120)
    foto = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=None)
    cpf = BRCPFField()
    email = models.EmailField(max_length=254)
    adicionado = models.DateTimeField(auto_now_add=True)
