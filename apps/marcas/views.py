from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Marca
from . import forms
# Create your views here.


class CadastrarMarca(LoginRequiredMixin, generic.edit.CreateView):
    success_url = reverse_lazy('marcas:lista')
    template_name = "marcas/cadastro.html"
    model = Marca
    form_class = forms.MarcaForm


class MarcaListView(LoginRequiredMixin, generic.list.ListView):
    template_name = 'marcas/ver_marcas.html'
    model = Marca
    context_object_name = 'marcas'

    def get_queryset(self):
        nome = self.request.GET.get('nome')
        if nome:
            queryset = self.model.objects.filter(
                nome__icontains=nome)
            return queryset
        else:
            return super().get_queryset()


class MarcaDetailView(LoginRequiredMixin, generic.detail.DetailView):
    template_name = 'marcas/detalhe.html'
    model = Marca
    context_object_name = 'marca'


class MarcaUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    template_name = 'marcas/atualizar.html'
    model = Marca
    form_class = forms.MarcaForm
    success_url = reverse_lazy('marcas:lista')


class MarcaDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    template_name = 'marcas/excluir.html'
    model = Marca
    success_url = reverse_lazy('marcas:lista')  # redirect URL after deletion
