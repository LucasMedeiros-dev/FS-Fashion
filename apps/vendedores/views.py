from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import forms
from django.urls import reverse_lazy
from .models import Vendedor


class VendedorListView(LoginRequiredMixin, ListView):
    model = Vendedor
    template_name = 'vendedores/lista.html'


class VendedorDetailView(LoginRequiredMixin, DetailView):
    model = Vendedor
    template_name = 'vendedores/detalhe.html'


class VendedorCreateView(LoginRequiredMixin, CreateView):
    model = Vendedor
    template_name = 'vendedores/cadastro.html'
    form_class = forms.VendedorForm


class VendedorUpdateView(LoginRequiredMixin, UpdateView):
    model = Vendedor
    template_name = 'vendedores/atualizar.html'
    form_class = forms.VendedorForm


class VendedorDeleteView(LoginRequiredMixin, DeleteView):
    model = Vendedor
    template_name = 'vendedores/excluir.html'
    success_url = reverse_lazy('vendedor_list')
