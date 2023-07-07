from django.urls import path
from . import views


urlpatterns = [
    path('definir_planejamento/', views.definir_planejamento, name='definir_planejamento'),
    path('atualiza_valor_vcategoria/<int:id>', views.atualiza_valor_vcategoria, name='atualiza_valor_vcategoria'), # type: ignore
]
