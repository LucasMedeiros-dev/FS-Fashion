from django.db import models
from apps.fornecedores.models import Fornecedor
# Create your models here.


class Marca(models.Model):
    nome = models.CharField(max_length=120, blank=False)
    fornecedores = models.ForeignKey(
        Fornecedor, verbose_name="Fornecedor", on_delete=models.CASCADE)
    img_marca = models.ImageField(upload_to="marcas/")
    adicionado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
