from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, FormView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Vendedor
from . import forms


class VendedorListView(UserPassesTestMixin, ListView):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

    model = Vendedor
    template_name = 'vendedores/lista.html'
    context_object_name = 'vendedores'


class VendedorDetailView(UserPassesTestMixin, DetailView):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

    model = Vendedor
    template_name = 'vendedores/detalhe.html'


class VendedorCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

    model = Vendedor
    template_name = 'vendedores/cadastro.html'
    form_class = forms.VendedorForm
    success_url = reverse_lazy('vendedor:lista')


class VendedorUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

    model = Vendedor
    template_name = 'vendedores/atualizar.html'
    form_class = forms.VendedorForm


class VendedorDeleteView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

    model = Vendedor
    template_name = 'vendedores/excluir.html'
    success_url = reverse_lazy('vendedor:lista')


class MudarSenhaView(UserPassesTestMixin, FormView):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

    # Especifique o caminho do seu template
    template_name = 'vendedores/mudar_senha.html'
    form_class = forms.MudarSenhaForm
    # URL para redirecionar após a mudança de senha
    success_url = reverse_lazy('password_change_done')

    def get_form_kwargs(self):
        kwargs = super(MudarSenhaView, self).get_form_kwargs()
        self.user = get_object_or_404(
            User, pk=self.kwargs['pk'])  # Obter o usuário pelo ID
        kwargs['user'] = self.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(MudarSenhaView, self).form_valid(form)
