from django.urls import path
from . import views


urlpatterns = [
    path('novo_valor/', views.novo_valor, name='novo_valor'), # type: ignore
    path('extrato/', views.extrato, name='extrato'),
    path('limpa_filtros/', views.limpa_filtros, name='limpa_filtros'),
    path('exportar_pdf/', views.exportar_pdf, name='exportar_pdf'), # type: ignore
]
