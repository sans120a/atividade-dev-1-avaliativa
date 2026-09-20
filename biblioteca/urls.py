from django.urls import path
from .views import LivrosMaisEmprestadosView

urlpatterns = [
    path('livros/ranking/', LivrosMaisEmprestadosView.as_view(), name='ranking-livros'),
]