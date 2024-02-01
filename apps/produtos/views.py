from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from . import forms
from . import models
# Create your views here.


class CadastrarProd(LoginRequiredMixin, generic.FormView):
    template_name = "produtos/cadastro.html"
    form_class = forms.ProdutoCadastro
    success_url = reverse_lazy('produto:cadastro')

    def form_valid(self, form) -> HttpResponse:
        nome = form.cleaned_data['nome']
        marca = form.cleaned_data['marca']
        preco = form.cleaned_data['preco']
        categoria = form.cleaned_data['categoria']
        qntd_max = form.cleaned_data['qntd_max']
        qntd_min = form.cleaned_data['qntd_min']
        qtd_tam_p = form.cleaned_data['qtd_tam_p']
        qtd_tam_m = form.cleaned_data['qtd_tam_m']
        qtd_tam_g = form.cleaned_data['qtd_tam_g']
        qtd_tam_gg = form.cleaned_data['qtd_tam_gg']
        img_produto = form.cleaned_data['img_produto']
        models.Produto.objects.get_or_create(nome=nome, marca=marca, categoria=categoria, preco=preco, qntd_max=qntd_max, qntd_min=qntd_min, qtd_tam_p=qtd_tam_p,
                                             qtd_tam_m=qtd_tam_m, qtd_tam_g=qtd_tam_g, qtd_tam_gg=qtd_tam_gg, img_produto=img_produto)
        return super().form_valid(form)


class AtualizarProd(LoginRequiredMixin, generic.UpdateView):
    template_name = "produtos/atualizacao.html"
    form_class = forms.ProdutoCadastro
    success_url = reverse_lazy('produto:estoque')
    model = models.Produto

    def form_valid(self, form):
        print("TAVA VALIDO")
        return super().form_valid(form)

    def form_invalid(self, form):
        # printa os errors
        print(form.errors)
        return super().form_invalid(form)


class EstoqueProd(LoginRequiredMixin, generic.ListView):
    paginate_by = 10
    template_name = "produtos/produto.html"
    form_class = forms.ProdutoCadastro
    context_object_name = "produtos"

    def get_queryset(self):
        query = self.request.GET.get('buscar')
        queryset = models.Produto.objects.all()
        try:
            query = int(query)
        except:
            query = None
        if query is not None:
            queryset = queryset.filter(id=query)
        return queryset


class ProdutoDetail(LoginRequiredMixin, generic.detail.DetailView):
    template_name = 'produtos/detalhe.html'
    model = models.Produto


class ExlcuirConfirm(LoginRequiredMixin, generic.DeleteView):
    template_name = 'produtos/excluir.html'
    model = models.Produto
    success_url = reverse_lazy('produto:estoque')
