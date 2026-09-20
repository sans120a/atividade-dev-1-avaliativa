from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LivrosMaisEmprestadosView, LivroViewSet, UsuarioViewSet, EmprestimoViewSet

router = DefaultRouter()

router.register(r'Livro', LivroViewSet, basename='livro')
router.register(r'Usuario', UsuarioViewSet, basename='usuario')
router.register(r'Emprestimo', EmprestimoViewSet, basename='emprestimo')

urlpatterns = [
    path('api/livros/ranking/', LivrosMaisEmprestadosView.as_view(), name='ranking-livros'),
    path('api/', include(router.urls))
]