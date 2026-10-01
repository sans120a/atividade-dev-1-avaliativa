from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LivrosMaisEmprestadosView, LivroViewSet, UsuarioViewSet, EmprestimoViewSet, CategoriaViewSet, AutorViewSet

router = DefaultRouter()

router.register(r'livros', LivroViewSet, basename='livro')
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'emprestimos', EmprestimoViewSet, basename='emprestimo')
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'autores', AutorViewSet, basename='autor')

urlpatterns = [
    path('api/livros/ranking/', LivrosMaisEmprestadosView.as_view(), name='ranking-livros'),
    path('api/', include(router.urls))
]