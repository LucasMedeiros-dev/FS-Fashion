# shop/models.py

from django.db import models
from django.conf import settings
from apps.produtos.models import Produto


class Carrinho(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                related_name='carrinhos', null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-criado_em',)

    def __str__(self):
        return f'Carrinho {self.id}'

    @property
    def get_total(self):
        return sum(item.get_cost() for item in self.itens.all())


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(
        Carrinho, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(
        Produto, related_name='itens_carrinho', on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.preco * self.quantidade
