from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from ..produtos.models import Produto
# Create your views here.


class VendasView(LoginRequiredMixin, generic.ListView):
    paginate_by = 10
    template_name = "frente_loja/frente_loja.html"
    context_object_name = "produtos"

    def get_queryset(self):
        query = self.request.GET.get('buscar')
        queryset = Produto.objects.filter(qtd_tam_p__gt=0) | Produto.objects.filter(
            qtd_tam_m__gt=0) | Produto.objects.filter(qtd_tam_g__gt=0) | Produto.objects.filter(qtd_tam_gg__gt=0)
        try:
            query = int(query)
        except:
            query = None
        if query is not None:
            queryset = queryset.filter(id=query)
        return queryset
