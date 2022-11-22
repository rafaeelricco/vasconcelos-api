from django.db import models
from autoslug import AutoSlugField
from categories.models import Category
from categories.models import Cultures
from utils.compress_img import compress
from categories.models import SizeOfArea
from categories.models import Disponibility
from django.core.validators import (
    RegexValidator,
    URLValidator,
)
from utils.regex import text_regex, link_regex


class Product(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(
        max_length=50,
        verbose_name="Nome do produto",
        unique=True,
        null=False,
        blank=False,
        validators=[
            RegexValidator(
                regex=text_regex,
                message="O nome do produto deve conter apenas letras, números e espaços. Ex: Meridia 200",
                code="invalid_name",
            ),
        ],
    )

    promise = models.CharField(
        max_length=100,
        verbose_name="Promessa",
        null=True,
        blank=True,
        unique=True,
        validators=[
            RegexValidator(
                regex=text_regex,
                message="A promessa deve conter apenas letras, números e espaços. Ex: Robustez e qualidade para o seu Plantio.",
                code="invalid_promise",
            ),
        ],
    )

    slug = AutoSlugField(
        populate_from="name",
        unique=True,
        always_update=True,
    )

    cover = models.ImageField(
        null=False,
        blank=False,
        unique=True,
        verbose_name="Capa do produto",
        upload_to="covers/products",
        default="",
    )

    # Foreign Keys and ManyToMany
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Qual a categoria do produto?",
        blank=True,
        null=True,
    )

    area = models.ManyToManyField(SizeOfArea, verbose_name="Qual o tamanho da área?")

    cultures = models.ManyToManyField(
        Cultures,
        verbose_name="Qual a cultura?",
    )

    disponibility = models.ForeignKey(
        Disponibility,
        on_delete=models.CASCADE,
        verbose_name="Disponibilidade",
        blank=True,
        null=True,
    )
    # End Foreign Keys and ManyToMany

    launch = models.BooleanField(
        default=False,
        verbose_name="É lançamento?",
    )

    featured = models.BooleanField(
        default=False, verbose_name="Quer destacar este produto?"
    )

    flyer = models.URLField(
        blank=True,
        null=True,
        unique=True,
        max_length=300,
        verbose_name="Link do folheto",
        validators=[
            URLValidator(
                regex=link_regex,
                message="O link do folheto deve começar com http:// ou https://",
                code="invalid_flyer",
            ),
        ],
    )

    youtube = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Possui vídeo no youtube?",
        unique=True,
        validators=[
            URLValidator(
                regex=link_regex,
                message="O link do vídeo deve começar com http:// ou https://",
                code="invalid_youtube",
            ),
        ],
    )

    def save(self, *args, **kwargs):
        if self.cover:
            self.cover = compress(self.cover)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Produtos"
        verbose_name = "Produto"
