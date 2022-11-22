from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from categories.models import Family, SubFamily, ModelsAndVersions
from django.core.validators import (
    RegexValidator,
    MinLengthValidator,
    MaxLengthValidator,
)
from utils.regex import parts_regex, text_regex, code_regex


class Parts(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(
        max_length=50,
        verbose_name="Nome do produto",
        unique=True,
        null=False,
        blank=False,
        validators=[
            RegexValidator(
                regex=parts_regex,
                message="O nome do produto deve conter apenas letras, números e espaços. Ex: Meridia 200",
                code="invalid_name",
            ),
            MinLengthValidator(3),
            MaxLengthValidator(50),
        ],
    )

    code = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Código do produto",
        validators=[
            RegexValidator(
                regex=code_regex,
                message="O código do produto deve conter apenas letras, números e espaços. Ex: 001MSO345",
                code="invalid_code",
            ),
            MinLengthValidator(3),
            MaxLengthValidator(50),
        ],
        default="Não informado",
    )

    branding = models.CharField(
        max_length=50,
        verbose_name="Marca do produto",
        blank=False,
        null=False,
        default="Não informado",
        validators=[
            RegexValidator(
                regex=text_regex,
                message="A marca do produto deve conter apenas letras, números e espaços. Ex: Jacto",
                code="invalid_branding",
            ),
            MinLengthValidator(3),
            MaxLengthValidator(50),
        ],
    )

    cover = models.ImageField(
        null=False,
        blank=False,
        unique=True,
        verbose_name="Capa do produto",
        upload_to="covers/parts",
        default="",
    )

    description = RichTextField(verbose_name="Descrição do produto", max_length=2000)

    slug = AutoSlugField(
        populate_from="name",
        unique=True,
        always_update=True,
        editable=False,
    )

    family = models.ForeignKey(
        Family,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Qual a família do produto?",
    )

    subfamily = models.ForeignKey(
        SubFamily,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Qual a subfamília do produto?",
    )

    model_version = models.ManyToManyField(
        ModelsAndVersions, blank=True, verbose_name="Modelo/versão"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Peça"
        verbose_name_plural = "Peças"
