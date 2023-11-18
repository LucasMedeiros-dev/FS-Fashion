from django.db import models
from apps.marcas.models import Marca


# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=120)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    qntd_max = models.PositiveIntegerField()
    qntd_min = models.PositiveIntegerField()
    qtd_tam_p = models.PositiveIntegerField()
    qtd_tam_m = models.PositiveIntegerField()
    qtd_tam_g = models.PositiveIntegerField()
    qtd_tam_gg = models.PositiveIntegerField()
    cod_barras = models.CharField(max_length=50)
    img_produto = models.ImageField(upload_to="static/")
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} {self.marca}"
