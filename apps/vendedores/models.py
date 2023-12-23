from django.db import models
from localflavor.br.models import BRCPFField
# Create your models here.


class Vendedor(models.Model):
    nome = models.CharField(max_length=120)
    foto = models.ImageField(
        upload_to="static/vendedores/")
    cpf = BRCPFField(unique=True)
    email = models.EmailField(max_length=254, unique=True)
    adicionado = models.DateTimeField(auto_now_add=True)
