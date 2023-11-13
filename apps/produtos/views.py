from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from . import forms
from . import models
# Create your views here.


class CadastrarProd(generic.FormView):
    template_name = "produtos/cadastro.html"
    form_class = forms.ProdutoCadastro
    success_url = reverse_lazy('dashboard')


class EstoqueProd(generic.ListView):
    paginate_by = 10
    template_name = "produtos/estoque.html"
    form_class = forms.ProdutoCadastro
    queryset = models.Produto.objects.all()
    context_object_name = "produtos"
