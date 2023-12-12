from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Fornecedor
from . import forms
# Create your views here.


class CadastrarFornecedor(generic.edit.CreateView):
    template_name = "fornecedores/cadastro.html"
    model = Fornecedor
    form_class = forms.FornecedorForm


class FornecedorListView(generic.list.ListView):
    template_name = 'fornecedores/lista.html'
    model = Fornecedor
    context_object_name = 'fornecedores'


class FornecedorDetailView(generic.detail.DetailView):
    template_name = 'fornecedores/detalhe.html'
    model = Fornecedor
    context_object_name = 'fornecedor'


class FornecedorUpdateView(generic.edit.UpdateView):
    template_name = 'fornecedores/atualizar.html'
    model = Fornecedor
    form_class = forms.FornecedorForm


class FornecedorDeleteView(generic.edit.DeleteView):
    template_name = 'fornecedores/excluir.html'
    model = Fornecedor
    # redirect URL after deletion
    success_url = reverse_lazy('fornecedores:lista')
