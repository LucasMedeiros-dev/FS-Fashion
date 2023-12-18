from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Fornecedor
from . import forms
# Create your views here.


class CadastrarFornecedor(LoginRequiredMixin, generic.edit.CreateView):
    success_url = reverse_lazy('fornecedor:cadastro')
    template_name = "fornecedores/cadastro.html"
    model = Fornecedor
    form_class = forms.FornecedorForm


class FornecedorListView(LoginRequiredMixin, generic.list.ListView):
    template_name = 'fornecedores/lista.html'
    model = Fornecedor
    context_object_name = 'fornecedores'

    def get_queryset(self):
        tipo = self.request.GET.get('tipo')
        val = self.request.GET.get('val')
        if tipo in ['nome', 'empresa', 'cnpj'] and not val is None:
            if tipo == 'nome':
                # Perform logic for 'nome' tipo
                queryset = self.model.objects.filter(
                    nome__icontains=val)
            elif tipo == 'empresa':
                # Perform logic for 'empresa' tipo
                queryset = self.model.objects.filter(
                    empresa__icontains=val)

            elif tipo == 'cnpj':
                # Perform logic for 'cnpj' tipo
                queryset = self.model.objects.filter(
                    cnpj__icontains=val)

            return queryset
        else:
            return super().get_queryset()


class FornecedorDetailView(LoginRequiredMixin, generic.detail.DetailView):
    template_name = 'fornecedores/detalhe.html'
    model = Fornecedor
    context_object_name = 'fornecedor'


class FornecedorUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    success_url = reverse_lazy('fornecedor:lista')
    template_name = 'fornecedores/atualizar.html'
    model = Fornecedor
    form_class = forms.FornecedorForm


class FornecedorDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    template_name = 'fornecedores/excluir.html'
    model = Fornecedor
    # redirect URL after deletion
    success_url = reverse_lazy('fornecedor:lista')
