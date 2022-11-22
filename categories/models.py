from django.db import models
from autoslug import AutoSlugField
from django.core.validators import RegexValidator
from utils.regex import text_regex


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="Nome da categoria",
        null=False,
        blank=False,
        validators=[
            RegexValidator(
                regex=text_regex,
                message="O nome da categoria deve conter apenas letras, números, espaços, vírgulas, pontos, hífens e sublinhados. Ex: Máquinas Agrícolas",
                code="invalid_name",
            ),
        ],
    )
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categorias"


class Cultures(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="Nome da cultura",
        null=False,
        blank=False,
        validators=[
            RegexValidator(
                regex=text_regex,
                message="O nome da cultura deve conter apenas letras, números, espaços, vírgulas, pontos, hífens e sublinhados. Ex: Soja",
                code="invalid_name",
            ),
        ],
    )
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Culturas"


class SizeOfArea(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="Tamanho da área",
        null=False,
        blank=False,
        validators=[
            RegexValidator(
                regex=text_regex,
                message="O tamanho da área deve conter apenas letras, números, espaços, vírgulas, pontos, hífens e sublinhados. Ex: Até 500 hectares",
                code="invalid_name",
            )
        ],
    )
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tamanho da área"


class Family(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="Nome da família",
        null=False,
        blank=False,
        validators=[
            RegexValidator(
                regex=text_regex,
                message="O nome da família deve conter apenas letras, números, espaços, vírgulas, pontos, hífens e sublinhados. Ex: Pulverizadores Automotrizes",
                code="invalid_name",
            )
        ],
    )
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Famílias"


class SubFamily(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="Nome da subfamília",
        null=False,
        blank=False,
        validators=[
            RegexValidator(
                regex=text_regex,
                message="O nome da subfamília deve conter apenas letras, números, espaços, vírgulas, pontos, hífens e sublinhados. Ex: Bicos de Pulverização",
            )
        ],
    )
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Subfamílias"


class ModelsAndVersions(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="Qual o modelo ou versão do produto?",
        null=False,
        blank=False,
        validators=[
            RegexValidator(
                regex=text_regex,
                message="O modelo ou versão do produto deve conter apenas letras, números, espaços, vírgulas, pontos, hífens e sublinhados. Ex: 1000",
                code="invalid_name",
            )
        ],
    )
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Modelos e versões"


class Disponibility(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="Disponibilidade",
        null=False,
        blank=False,
        validators=[
            RegexValidator(
                regex=text_regex,
                message="A disponibilidade deve conter apenas letras, números, espaços, vírgulas, pontos, hífens e sublinhados. Ex: Em estoque",
                code="invalid_name",
            )
        ],
    )
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Disponibilidade"


class Launch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="Lançamento",
        null=False,
        blank=False,
        validators=[
            RegexValidator(
                regex=text_regex,
                message="O lançamento deve conter apenas letras, números, espaços, vírgulas, pontos, hífens e sublinhados. Ex: 2020",
                code="invalid_name",
            )
        ],
    )
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Lançamentos"
