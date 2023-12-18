from django.urls import path
from . import views

app_name = "fornecedor"

urlpatterns = [
    path('<int:pk>', views.FornecedorDetailView.as_view(), name="detalhe"),
    path('excluir/<int:pk>', views.FornecedorDeleteView.as_view(), name="excluir"),
    path('atualizar/<int:pk>', views.FornecedorUpdateView.as_view(), name="atualizar"),
    path('cadastro/', views.CadastrarFornecedor.as_view(), name="cadastro"),
    path('', views.FornecedorListView.as_view(), name="lista"),
]
