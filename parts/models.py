from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from categories.models import Family, SubFamily, ModelsAndVersions


class Parts(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100, verbose_name='Nome do produto')

    code = models.CharField(
        max_length=100, verbose_name='Código do Produto', blank=True, null=True)

    branding = models.CharField(
        max_length=100, verbose_name='Marca do produto', blank=True, null=True)

    description = RichTextField(verbose_name='Descrição do produto')

    slug = AutoSlugField(populate_from='name',
                         unique=True, always_update=True)

    family = models.ForeignKey(
        Family, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Qual a família do produto?')

    subfamily = models.ForeignKey(
        SubFamily, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Qual a subfamília do produto?')

    model_version = models.ManyToManyField(
        ModelsAndVersions, blank=True, verbose_name='Modelo/versão')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Peças"
