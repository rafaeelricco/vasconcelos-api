from django.db import models
from filer.fields.image import FilerImageField
from parts.models import Parts


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image_url = FilerImageField(
        null=True, blank=True, on_delete=models.CASCADE, related_name="image")

    part = models.ForeignKey(
        Parts, on_delete=models.CASCADE, related_name='images', null=True, blank=True)

    def __str__(self):
        return self.image_url.name
