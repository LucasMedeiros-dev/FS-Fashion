from django.urls import path
from . import views

app_name = "vendas"

urlpatterns = [
    path('vender/', views.VendasView.as_view(), name="vender"),
]
