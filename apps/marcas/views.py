from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Marca
from . import forms
# Create your views here.


class CadastrarMarca(generic.edit.CreateView):
    template_name = "marcas/cadastro.html"
    model = Marca
    form_class = forms.MarcaForm


class MarcaListView(generic.list.ListView):
    template_name = 'marcas/ver_marcas.html'
    model = Marca
    paginate_by = 100  # if pagination is desired
    context_object_name = 'marcas'


class MarcaDetailView(generic.detail.DetailView):
    template_name = 'marcas/detalhe.html'
    model = Marca
    context_object_name = 'marca'


class MarcaUpdateView(generic.edit.UpdateView):
    template_name = 'marcas/atualizar.html'
    model = Marca
    form_class = forms.MarcaForm


class MarcaDeleteView(generic.edit.DeleteView):
    template_name = 'marcas/excluir.html'
    model = Marca
    success_url = reverse_lazy('marcas:lista')  # redirect URL after deletion
