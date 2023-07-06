from django.urls import path
from . import views


urlpatterns = [
    path('novo_valor/', views.novo_valor, name='novo_valor'), # type: ignore
    path('extrato/', views.extrato, name='extrato'),
]
