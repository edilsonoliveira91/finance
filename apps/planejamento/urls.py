from django.urls import path
from .views import definir_planejamento

urlpatterns = [
    path('definir_planejamento/', definir_planejamento, name="definir_planejamento"),
]