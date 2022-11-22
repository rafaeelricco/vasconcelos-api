from django.db import models
from ckeditor.fields import RichTextField
from products.models import Product
from filer.fields.image import FilerImageField


class TextBlock(models.Model):
    id = models.AutoField(primary_key=True)
    text = RichTextField(
        verbose_name="Descrição do produto",
        blank=False,
        null=False,
    )
    image_file = FilerImageField(
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="text_blocks",
        null=True,
        blank=True,
    )

    def __str__(self):
        name = f"{self.product.name}"
        return name

    class Meta:
        verbose_name = "Bloco de texto"
        verbose_name_plural = "Blocos de texto"
