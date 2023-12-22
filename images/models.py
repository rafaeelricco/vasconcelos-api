from distutils.command.upload import upload
from django.db import models
from filer.fields.image import FilerImageField
from products.models import Product


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image_file = FilerImageField(
        null=True, blank=True, related_name="image_file", on_delete=models.CASCADE)

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images', null=True, blank=True)

    def __str__(self):
        return self.image_file.name
