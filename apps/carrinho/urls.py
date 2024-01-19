# shop/urls.py

from django.urls import path
from .views import CartAdd, CartRemove, CartDetail

app_name = 'carrinho'

urlpatterns = [
    path('adicionar/<int:produto_id>/', CartAdd.as_view(), name='adicionar'),
    path('remover/<int:item_id>/', CartRemove.as_view(), name='remover'),
    path('', CartDetail.as_view(), name='detalhe'),
]
