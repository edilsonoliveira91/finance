from django.urls import path
from .views import novo_valor, view_extrato, exportar_pdf

urlpatterns = [
    path('novo_valor', novo_valor, name='novo_valor'),
    path('view_extrato/', view_extrato, name="view_extrato"),
    path('exportar_pdf/', exportar_pdf, name="exportar_pdf")
]