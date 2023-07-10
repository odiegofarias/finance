from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('gerenciar/', views.gerenciar, name='gerenciar'),
    path('cadastrar_banco/', views.cadastrar_banco, name='cadastrar_banco'),
    path('deletar_banco/<int:id>', views.deletar_banco, name='deletar_banco'),
    path('cadastrar_categoria/', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('atualiza_categoria/<int:id>', views.atualiza_categoria, name='atualiza_categoria'),
    path('dashboard/', views.dashboard, name='dashboard'),

]
