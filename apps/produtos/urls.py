from django.urls import path
from . import views

app_name = "produto"

urlpatterns = [
    path('cadastro/', views.CadastrarProd.as_view(), name="cadastro"),
    path('estoque/', views.EstoqueProd.as_view(), name="estoque"),
]
