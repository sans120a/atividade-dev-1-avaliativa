from rest_framework import serializers
from .models import Livro, Emprestimo, Usuario, Categoria, Autor

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class EmprestimoSerializer(serializers.ModelSerializer):
    livro = LivroSerializer(read_only=True)
    livro_id = serializers.PrimaryKeyRelatedField(
        queryset=Livro.objects.all(), source='livro', write_only=True
    )
    usuario_detalhes = UsuarioSerializer(source='usuario', read_only=True)
    class Meta:
        model = Emprestimo
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'