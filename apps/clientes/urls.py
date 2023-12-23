from django.urls import path
from . import views

app_name = "clientes"

urlpatterns = [
    path('<int:pk>', views.ClienteDetailView.as_view(), name="detalhe"),
    path('excluir/<int:pk>', views.ClienteDeleteView.as_view(), name="excluir"),
    path('atualizar/<int:pk>', views.ClienteUpdateView.as_view(), name="atualizar"),
    path('cadastro/', views.CadastrarCliente.as_view(), name="cadastro"),
    path('', views.ClienteListView.as_view(), name="lista"),
]
