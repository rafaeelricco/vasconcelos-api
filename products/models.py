from django.db import models
from ckeditor.fields import RichTextField
from categories.models import Category
from autoslug import AutoSlugField
from categories.models import Cultures
from categories.models import SizeOfArea
from categories.models import Disponibility


class Product(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100, verbose_name='Nome do produto')

    promise = models.CharField(
        max_length=100, verbose_name='Promessa', blank=True, null=True)

    description = RichTextField(verbose_name='Descrição do produto')

    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)

    cover = models.FileField(
        blank=True, null=True, unique=True, verbose_name='Capa do produto',
        upload_to='public/covers')

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Qual a linha do produto?')

    area = models.ManyToManyField(
        SizeOfArea, blank=True, verbose_name='Qual o tamanho da área?')

    cultures = models.ManyToManyField(
        Cultures, blank=True, verbose_name='Qual a cultura?')

    disponibility = models.ForeignKey(
        Disponibility, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Disponibilidade')

    launch = models.BooleanField(default=False, verbose_name='É lançamento?')

    flyer = models.CharField(blank=True, null=True,
                             verbose_name='Link do folheto', unique=True, max_length=300)

    youtube = models.URLField(
        max_length=200, blank=True, null=True, verbose_name='Possui vídeo no youtube?', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Produtos"


class Featured(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False,
                            null=False, verbose_name='Nome do produto')
    description = models.TextField(
        blank=True, null=True, max_length=130, verbose_name='Promessa do produto')
    link = models.URLField(max_length=200, null=False,
                           blank=False, verbose_name='Link para o produto')
    image = models.ImageField(
        blank=False, null=False, upload_to='public/featured', verbose_name='Imagem do produto')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Produtos em Destaque'
