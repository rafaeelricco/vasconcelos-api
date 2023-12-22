from autoslug import AutoSlugField
from django.db import models


class Useds(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100, verbose_name='Nome do produto')

    branding = models.CharField(
        max_length=100, verbose_name='Marca do produto')

    description = models.TextField(verbose_name='Descrição do produto')

    cover = models.FileField(upload_to='covers', blank=True,
                             null=True, unique=True, verbose_name='Capa do produto')

    model = models.CharField(max_length=100, verbose_name='Modelo do produto')

    year = models.CharField(max_length=100, verbose_name='Ano do produto')

    price = models.CharField(max_length=100, verbose_name='Preço do produto')

    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Usados"
