from .models import Carrinho


def carrinho(request):
    if request.user.is_authenticated:
        carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
        return {'carrinho': carrinho}
    return {'carrinho': None}
