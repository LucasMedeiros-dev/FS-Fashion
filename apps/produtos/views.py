from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from barcode.writer import ImageWriter
from barcode import EAN13
from PIL import Image
from io import BytesIO
from hashlib import md5
import base64
import uuid
from . import forms
from . import models
# Create your views here.


class CadastrarProd(generic.FormView):
    template_name = "produtos/cadastro.html"
    form_class = forms.ProdutoCadastro
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form) -> HttpResponse:
        nome = form.cleaned_data['nome']
        marca = form.cleaned_data['marca']
        qntd_max = form.cleaned_data['qntd_max']
        qntd_min = form.cleaned_data['qntd_min']
        qtd_tam_p = form.cleaned_data['qtd_tam_p']
        qtd_tam_m = form.cleaned_data['qtd_tam_m']
        qtd_tam_g = form.cleaned_data['qtd_tam_g']
        qtd_tam_gg = form.cleaned_data['qtd_tam_gg']
        img_produto = form.cleaned_data['img_produto']
        models.Produto.objects.get_or_create(nome=nome, marca=marca, qntd_max=qntd_max, qntd_min=qntd_min, qtd_tam_p=qtd_tam_p,
                                             qtd_tam_m=qtd_tam_m, qtd_tam_g=qtd_tam_g, qtd_tam_gg=qtd_tam_gg, img_produto=img_produto)
        return super().form_valid(form)


class EstoqueProd(generic.ListView):
    paginate_by = 10
    template_name = "produtos/estoque.html"
    form_class = forms.ProdutoCadastro
    queryset = models.Produto.objects.all()
    context_object_name = "produtos"


class ProdutoDetail(generic.detail.DetailView):
    template_name = 'produtos/detalhe.html'
    model = models.Produto
