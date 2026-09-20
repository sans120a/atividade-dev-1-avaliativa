from rest_framework import serializers
from .models import Livro, Emprestimo, Usuario

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'isbn', 'titulo', 'disponivel', 'paginas', 'data_publicacao']

class EmprestimoSerializer(serializers.ModelSerializer):
    livro = LivroSerializer(read_only=True)
    livro_id = serializers.PrimaryKeyRelatedField(
        queryset=Livro.objects.all(), source='livro', write_only=True
    )