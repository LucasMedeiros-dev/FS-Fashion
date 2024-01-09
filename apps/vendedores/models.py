from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User, Permission
from django.utils.crypto import get_random_string
from localflavor.br.models import BRCPFField
from django.dispatch import receiver
from django.db import models
# Create your models here.


def gerar_senha(length=8):
    # Uma senha segura deve conter letras, dígitos e caracteres especiais
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()_+'
    random_password = get_random_string(
        length=length, allowed_chars=characters)
    return random_password


class Vendedor(models.Model):
    id_usuario = models.PositiveIntegerField(null=True, blank=True)
    nome = models.CharField(max_length=120)
    foto = models.ImageField(
        upload_to="static/vendedores/")
    cpf = BRCPFField(unique=True)
    email = models.EmailField(max_length=254, unique=True)
    adicionado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.cpf}"

    class Meta:
        permissions = [
            ("vendedor_permission", "Pode acessar funções de vendedor"),
        ]


@receiver(post_save, sender=Vendedor)
def create_user_for_vendedor(sender, instance, created, **kwargs):
    if created:
        senha_random = gerar_senha()

        user = User.objects.create_user(
            username=instance.email, email=instance.email, password=senha_random)
        instance.id_usuario = user.id
        instance.save()


@receiver(post_delete, sender=Vendedor)
def delete_user_for_vendedor(sender, instance, **kwargs):
    if instance.id_usuario:
        try:
            user = User.objects.get(id=instance.id_usuario)
            user.delete()
        except User.DoesNotExist:
            pass
