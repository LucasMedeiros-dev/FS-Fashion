from django.urls import path
from . import views
app_name = "marcas"

urlpatterns = [
    path('cadastro/', views.CadastrarMarca.as_view(), name="cadastro"),
    path('', views.MarcaListView.as_view(), name="lista"),
]
