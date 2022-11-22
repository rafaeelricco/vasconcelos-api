from autoslug import AutoSlugField
from django.db import models
from utils.compress_img import compress
from django.core.validators import RegexValidator
from utils.regex import text_regex, year_regex, price_regex


class Useds(models.Model):
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
                message="Nome do produto inválido, apenas letras, números e espaços",
                code="invalid_name",
            ),
        ],
    )

    branding = models.CharField(
        max_length=100, verbose_name="Marca do produto", null=False, blank=False
    )

    description = models.TextField(
        max_length=2000,
        verbose_name="Descrição do produto",
        null=False,
        blank=False,
    )

    cover = models.FileField(
        upload_to="covers",
        blank=True,
        null=True,
        unique=True,
        verbose_name="Capa do produto",
    )

    model = models.CharField(
        max_length=100,
        verbose_name="Modelo do produto",
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                regex=text_regex,
                message="Modelo do produto é inválido. Apenas letras e números.",
                code="invalid",
            ),
        ],
    )

    year = models.CharField(
        verbose_name="Ano do produto",
        max_length=4,
        null=False,
        blank=False,
        validators=[
            RegexValidator(
                regex=year_regex,
                message="Ano do produto é inválido. Ex: 2020",
                code="invalid",
            ),
        ],
    )

    price = models.CharField(
        verbose_name="Preço do produto",
        max_length=12,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=price_regex,
                message="Preço do produto é inválido. Ex: R$600.000,00",
                code="invalid",
            ),
        ],
    )

    slug = AutoSlugField(populate_from="name", unique=True, always_update=True)

    def save(self, *args, **kwargs):
        if self.cover:
            self.cover = compress(self.cover)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Usado"
        verbose_name_plural = "Usados"
