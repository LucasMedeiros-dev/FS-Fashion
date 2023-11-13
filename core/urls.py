from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name="dashboard"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('produto/', include('apps.produtos.urls'), name="prod"),
]
