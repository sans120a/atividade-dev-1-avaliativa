from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.response import Response
from .models import Livro, Emprestimo, Usuario
from .serializers import LivroSerializer, EmprestimoSerializer, UsuarioSerializer
from rest_framework import viewsets

class LivrosMaisEmprestadosView(APIView):
    def get(self, request):
        livros = Livro.objects.annotate(
            total_emprestimos = Count('historico_emprestimos')
        ).order_by('-total_emprestimos')

        dados=[]
        for livro in livros:
            dados.append({
                "id": livro.id,
                "titulo": livro.titulo,
                "total_emprestimos": livro.total_emprestimos
            })

        return Response(dados)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.object.all()
    serializer_class = UsuarioSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer