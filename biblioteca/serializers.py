from rest_framework import serializers
from .models import Livro, Emprestimo, Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'idade', 'cpf']

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'isbn', 'titulo', 'disponivel', 'paginas', 'data_publicacao']

class EmprestimoSerializer(serializers.ModelSerializer):
    livro = LivroSerializer(read_only=True)
    livro_id = serializers.PrimaryKeyRelatedField(
        queryset=Livro.objects.all(), source='livro', write_only=True
    )
    usuario_detalhes = UsuarioSerializer(source='usuario', read_only=True)
    class Meta:
        model = Emprestimo
        fields = ['id', 'livro', 'livro_id', 'usuario', 'usuario_detalhes', 'data_realizada', 'data_devolucao', 'devolvido']