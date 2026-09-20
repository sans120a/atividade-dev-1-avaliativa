from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LivrosMaisEmprestadosView, LivroViewSet, UsuarioViewSet, EmprestimoViewSet

router = DefaultRouter()

router.register(r'Livro', LivroViewSet, basename='livro')
router.register(r'Usuario', UsuarioViewSet, basename='usuario')
router.register(r'Emprestimo', EmprestimoViewSet, basename='emprestimo')

urlpatterns = [
    path('livros/ranking/', LivrosMaisEmprestadosView.as_view(), name='ranking-livros'),
]