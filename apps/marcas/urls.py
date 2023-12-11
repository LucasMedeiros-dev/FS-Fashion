from django.urls import path
from . import views
app_name = "marcas"

urlpatterns = [
    path('marca/<int:pk>', views.MarcaDetailView.as_view(), name="detalhe"),
    path('excluir/<int:pk>', views.MarcaDeleteView.as_view(), name="excluir"),
    path('atualizar/<int:pk>', views.MarcaUpdateView.as_view(), name="atualizar"),
    path('cadastro/', views.CadastrarMarca.as_view(), name="cadastro"),
    path('', views.MarcaListView.as_view(), name="lista"),
]
