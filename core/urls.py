from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name="dashboard"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('marcas/', include('apps.marcas.urls'), name="marcas"),
    path('produto/', include('apps.produtos.urls'), name="produto"),
    path('fornecedor/', include('apps.fornecedores.urls'), name="fornecedor"),
    path('vendedor/', include('apps.vendedores.urls'), name="vendedor"),
    path('clientes/', include('apps.clientes.urls'), name="cliente"),
    path('carrinho/', include('apps.carrinho.urls'), name="carrinho"),
    path('vendas/', include('apps.frente_loja.urls'), name="vendas"),
]
