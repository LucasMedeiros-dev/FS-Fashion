from django.urls import path
from . import views

app_name = "vendedor"

urlpatterns = [
    path('<int:pk>', views.VendedorDetailView.as_view(), name="detalhe"),
    path('senha/<int:pk>', views.MudarSenhaView.as_view(), name="senha"),
    path('excluir/<int:pk>', views.VendedorDeleteView.as_view(), name="excluir"),
    path('atualizar/<int:pk>', views.VendedorUpdateView.as_view(), name="atualizar"),
    path('cadastro/', views.VendedorCreateView.as_view(), name="cadastro"),
    path('', views.VendedorListView.as_view(), name="lista"),
]
