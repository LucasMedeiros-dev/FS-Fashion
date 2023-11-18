from django.shortcuts import render
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
