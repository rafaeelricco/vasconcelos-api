from django.db import models
from autoslug import AutoSlugField


class Category(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=30, unique=True,
                            verbose_name='Nome da categoria')
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categorias"


class Cultures(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=30, unique=True,
                            verbose_name='Nome da cultura')
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Culturas"


class SizeOfArea(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=30, unique=True,
                            verbose_name='Tamanho da área')
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tamanho da área"


class Family(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=30, unique=True,
                            verbose_name='Nome da família')
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Famílias"


class SubFamily(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=30, unique=True,
                            verbose_name='Nome da subfamília')
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Subfamílias"


class ModelsAndVersions(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=30, unique=True,
                            verbose_name='Qual o modelo ou versão do produto?')
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Modelos e versões"


class Disponibility(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=30, unique=True,
                            verbose_name='Disponibilidade')
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Disponibilidade"


class Launch(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=30, unique=True,
                            verbose_name='Lançamento')
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Lançamentos"
