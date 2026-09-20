from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.response import Response
from .models import Livro

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

