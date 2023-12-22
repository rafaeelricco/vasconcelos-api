from django.db import models
from utils.compress_img import compress


class Banners(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='Chamada do banner')
    description = models.TextField(
        max_length=500, null=True, blank=True, verbose_name='Descrição do banner')
    link = models.URLField(max_length=200, null=True,
                           blank=True, verbose_name='Link do botão')
    image = models.ImageField(
        upload_to='public/banners', verbose_name='Imagem do banner', null=True, blank=True)

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Banners do Site"
