from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Emprestimo, PerfilLeitor

@receiver(post_save, sender=Emprestimo)
def atualizar_perfil_livro(sender, instance, created, **kwargs):
    usuario = instance.usuario
    livro = instance.livro
    perfil, _ = PerfilLeitor.objects.get_or_create(usuario=usuario)

    if created:
        livro.disponivel = False
        livro.save()
    elif instance.devolvido:
        livro.disponivel = True
        livro.save()

    perfil.possui_livro = usuario.emprestimos.filter(devolvido=False).exists()
    perfil.total_livros_lidos = usuario.emprestimos.filter(devolvido=True).count()
    perfil.save()