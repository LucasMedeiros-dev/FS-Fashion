# shop/views.py

from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Produto, Carrinho, ItemCarrinho
from django.contrib import messages


class CartAdd(View):
    def post(self, request):
        produto_id = request.POST.get('produto_id')
        tamanho = request.POST.get('tamanho')

        carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
        produto = get_object_or_404(Produto, id=produto_id)

        item, created = ItemCarrinho.objects.get_or_create(
            tamanho=tamanho,
            carrinho=carrinho,
            produto=produto,
            preco=produto.preco
        )

        if not created:
            item.quantidade += 1
            item.save()

        return redirect('carrinho:detalhe')


class CartRemove(View):
    def get(self, request, item_id):
        item = get_object_or_404(ItemCarrinho, id=item_id)
        item.delete()
        return redirect('carrinho:detalhe')


class CartDetail(View):
    def get(self, request):
        carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
        return render(request, 'carrinho/carrinho.html', {'carrinho': carrinho})

    def post(self, request):
        carrinho = Carrinho.objects.get(usuario=request.user)
        # remova do estoque as camisas, de acordo com o tamanho
        # Tenta remover do estoque as camisas, de acordo com o tamanho
        try:
            for item in carrinho.itens.all():
                produto = item.produto
                if item.tamanho == 'P':
                    if produto.qtd_tam_p >= item.quantidade:
                        produto.qtd_tam_p -= item.quantidade
                    else:
                        raise ValueError(f"Estoque insuficiente para {
                                         item.produto.nome} tamanho P")
                elif item.tamanho == 'M':
                    if produto.qtd_tam_m >= item.quantidade:
                        produto.qtd_tam_m -= item.quantidade
                    else:
                        raise ValueError(f"Estoque insuficiente para {
                                         item.produto.nome} tamanho M")
                elif item.tamanho == 'G':
                    if produto.qtd_tam_g >= item.quantidade:
                        produto.qtd_tam_g -= item.quantidade
                    else:
                        raise ValueError(f"Estoque insuficiente para {
                                         item.produto.nome} tamanho G")
                elif item.tamanho == 'GG':
                    if produto.qtd_tam_gg >= item.quantidade:
                        produto.qtd_tam_gg -= item.quantidade
                    else:
                        raise ValueError(
                            f"Estoque insuficiente para {item.produto.nome} Tamanho GG")
                produto.save()
                carrinho.itens.all().delete()
                carrinho.save()
        except ValueError as e:
            # Adiciona uma mensagem de erro
            messages.error(request, str(e))
            # Redireciona para a página anterior ou uma página de erro
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        # Se tudo der certo, redireciona para a página inicial
        messages.success(request, "Compra realizada com sucesso!")
        return HttpResponseRedirect('/')
