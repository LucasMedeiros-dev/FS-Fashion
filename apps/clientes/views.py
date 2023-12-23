from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Cliente
from . import forms
# Create your views here.


class CadastrarCliente(LoginRequiredMixin, generic.edit.CreateView):
    success_url = reverse_lazy('clientes:cadastro')
    template_name = "clientes/cadastro.html"
    model = Cliente
    form_class = forms.ClienteForm


class ClienteListView(LoginRequiredMixin, generic.list.ListView):
    template_name = 'clientes/lista.html'
    model = Cliente
    context_object_name = 'clientes'

    def get_queryset(self):
        nome = self.request.GET.get('nome')
        if nome:
            queryset = self.model.objects.filter(
                nome__icontains=nome)
            return queryset
        else:
            return super().get_queryset()


class ClienteDetailView(LoginRequiredMixin, generic.detail.DetailView):
    template_name = 'clientes/detalhe.html'
    model = Cliente
    context_object_name = 'clientes'


class ClienteUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    success_url = reverse_lazy('clientes:lista')
    template_name = 'clientes/atualizar.html'
    model = Cliente
    form_class = forms.ClienteForm


class ClienteDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    template_name = 'clientes/excluir.html'
    model = Cliente
    # redirect URL after deletion
    success_url = reverse_lazy('clientes:lista')
