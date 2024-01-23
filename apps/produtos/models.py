from django.db import models
from apps.marcas.models import Marca
from django.core.files import File  # Import File
import os  # Import os
from django.core.validators import MinValueValidator
from .funcoes.gerar_qrcode import criar_etiqueta_multiplo

# Create your models here.
CATEGORIAS_ROUPAS_CHOICES = [
    ('camisas_camisetas_masculinas', 'Camisas e Camisetas Masculinas'),
    ('calcas_masculinas', 'Calças Masculinas'),
    ('bermudas_shorts_masculinos', 'Bermudas e Shorts Masculinos'),
    ('blazers_ternos_masculinos', 'Blazers e Ternos Masculinos'),
    ('jaquetas_casacos_masculinos', 'Jaquetas e Casacos Masculinos'),
    ('roupas_esportivas_masculinas', 'Roupas Esportivas Masculinas'),
    ('roupas_intimas_masculinas', 'Roupas Íntimas Masculinas'),
    ('blusas_camisetas_femininas', 'Blusas e Camisetas Femininas'),
    ('vestidos_saias_femininas', 'Vestidos e Saias Femininas'),
    ('calcas_femininas', 'Calças Femininas'),
    ('shorts_bermudas_femininas', 'Shorts e Bermudas Femininas'),
    ('blazers_tailleurs_femininos', 'Blazers e Tailleurs Femininos'),
    ('jaquetas_casacos_femininos', 'Jaquetas e Casacos Femininos'),
    ('roupas_esportivas_femininas', 'Roupas Esportivas Femininas'),
    ('roupas_intimas_femininas', 'Roupas Íntimas Femininas'),
    ('roupas_bebes', 'Roupas para Bebês'),
    ('roupas_meninos', 'Roupas para Meninos'),
    ('roupas_meninas', 'Roupas para Meninas'),
    ('uniformes_escolares', 'Uniformes Escolares'),
    ('bolsas_mochilas', 'Bolsas e Mochilas'),
    ('cintos', 'Cintos'),
    ('chapeus_bones', 'Chapéus e Bonés'),
    ('luvas_cachecois', 'Luvas e Cachecóis'),
    ('joias_bijuterias', 'Joias e Bijuterias'),
]


class Produto(models.Model):
    nome = models.CharField(max_length=120)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    etiqueta = models.ImageField(upload_to="etiquetas/", blank=True)
    categoria = models.CharField(
        max_length=50,
        choices=CATEGORIAS_ROUPAS_CHOICES,
        default='camisas_camisetas_masculinas'
    )
    qntd_max = models.PositiveIntegerField()
    qntd_min = models.PositiveIntegerField()
    qtd_tam_p = models.PositiveIntegerField()
    qtd_tam_m = models.PositiveIntegerField()
    qtd_tam_g = models.PositiveIntegerField()
    qtd_tam_gg = models.PositiveIntegerField()
    preco = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    img_produto = models.ImageField(upload_to="produtos/")
    criado = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Logic to handle the etiqueta image
        # Check if this is a new instance (pk is None when the instance is not saved yet)
        if not self.pk:

            criar_etiqueta_multiplo(self.nome, self.preco, self.pk)
            # Path to your generated image
            image_path = 'etiquetas_latest.png'

            # Open the image file in read-binary mode
            with open(image_path, 'rb') as image_file:
                # Wrap the image file in a Django File object
                django_file = File(image_file)

                # Assign the image file to the etiqueta field
                self.etiqueta.save(os.path.basename(
                    image_path), django_file, save=False)

        # Call the parent's save method
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} {self.marca}"
