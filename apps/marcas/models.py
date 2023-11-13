from django.db import models

# Create your models here.


class Marca(models.Model):
    nome = models.CharField(max_length=120)
    img_marca = models.ImageField(upload_to="static/midias/produtos/")
    adicionado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
