from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    genero = models.CharField(max_length=200)

    def __str__(self):
        return self.genero

class LivroManager(models.Manager):
    def disponiveis(self):
        return self.filter(disponivel=True)

class Livro(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="livros_categoria",
    )
    autor = models.ManyToManyField(
        Autor,
        related_name= "livros_autor",
        blank=True,
    )
    isbn = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=200)
    sinopse = models.TextField(blank= True)
    paginas = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    data_publicacao = models.DateField()
    objects = LivroManager()

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome

class PerfilLeitor(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name="perfil_leitor"
    )
    total_divida = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    possui_livro = models.BooleanField(default=False)
    total_livros_lidos = models.IntegerField(default=0)

    def __str__(self):
        return f"perfil de {self.usuario.nome}"

class Emprestimo(models.Model):
    livro = models.ForeignKey(
        Livro,
        on_delete = models.PROTECT,
        related_name="historico_emprestimos",
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete = models.PROTECT,
        related_name="emprestimos",
    )
    data_realizada = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField()
    devolvido = models.BooleanField(default=False)

    def __str__(self):
        return f"emprestimo do {self.livro.titulo} para {self.usuario.nome}"