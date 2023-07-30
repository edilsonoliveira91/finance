from django.urls import path
from .views import home, gerenciar, cadastrar_banco, deletar_banco, cadastrar_categoria, update_categoria


urlpatterns = [
    path('home/', home, name='home'),
    path('gerenciar/', gerenciar, name='gerenciar'),
    path('cadastrar_banco/', cadastrar_banco, name='cadastrar_banco'),
    path('deletar_banco/<int:id>/', deletar_banco, name='cadastrar_banco'),
    path('cadastar_categoria/', cadastrar_categoria, name='cadastrar_categoria'),
    path('update_categoria/<int:id>', update_categoria, name='update_categoria')
]