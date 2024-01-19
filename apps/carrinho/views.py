# shop/views.py

from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Produto, Carrinho, ItemCarrinho


class CartAdd(View):
    def post(self, request, produto_id):
        carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
        produto = get_object_or_404(Produto, id=produto_id)
        item, created = ItemCarrinho.objects.get_or_create(
            carrinho=carrinho, produto=produto)
        if not created:
            item.quantidade += 1
            item.save()
        return redirect('carrinho:detalhe')


class CartRemove(View):
    def post(self, request, item_id):
        item = get_object_or_404(ItemCarrinho, id=item_id)
        item.delete()
        return redirect('carrinho:detalhe')


class CartDetail(View):
    def get(self, request):
        carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
        return render(request, 'carrinho/carrinho.html', {'carrinho': carrinho})
