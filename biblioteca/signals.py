from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Emprestimo, PerfilLeitor
from datetime import date
from decimal import Decimal

@receiver(post_save, sender=Emprestimo)
def atualizar_perfil_livro(sender, instance, created, **kwargs):
    usuario = instance.usuario
    livro = instance.livro
    perfil, _ = PerfilLeitor.objects.get_or_create(usuario=usuario)

    if created:
        livro.disponivel = False
        livro.save()
    else:
        if instance.devolvido:
            livro.disponivel = True
            livro.save()

    hoje = date.today()
    if not instance.devolvido and hoje > instance.data_devolucao:
        dias = (hoje-instance.data_devolucao).days
        perfil.total_divida += Decimal(dias*2.00)
    elif instance.devolvido:
        perfil.total_divida = Decimal(0.00)

    perfil.possui_livro = usuario.emprestimos.filter(devolvido=False).exists()
    perfil.total_livros_lidos = usuario.emprestimos.filter(devolvido=True).count()
    perfil.save()