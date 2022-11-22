from django.db import models
from utils.compress_img import compress
from django.core.validators import (
    URLValidator,
    validate_image_file_extension,
    RegexValidator,
)
from utils.regex import text_regex


class Banners(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=100,
        verbose_name="Chamada do banner",
        null=False,
        blank=False,
        validators=[
            RegexValidator(
                regex=text_regex,
                message="A chamada do banner deve conter apenas letras, números, espaços, vírgulas, pontos, hífens e sublinhados. Ex: Banner de promoção",
                code="invalid_title",
            ),
        ],
    )
    description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Descrição do banner",
        validators=[
            RegexValidator(
                regex=text_regex,
                message="A descrição do banner deve conter apenas letras, números, espaços, vírgulas, pontos, hífens e sublinhados. Ex: Aqui você tem garantia de estar adquirindo máquinas agrícolas de alta tecnologia, qualidade e resistência.",
                code="invalid_description",
            ),
        ],
    )
    link = models.URLField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Link do botão",
        validators=[
            URLValidator(
                regex=r"^(http|https)://",
                message="O link do botão deve conter http:// ou https://",
                code="invalid_link",
            ),
        ],
    )
    image = models.ImageField(
        upload_to="banners/home",
        verbose_name="Imagem do banner",
        null=False,
        blank=False,
        validators=[validate_image_file_extension],
    )

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Banners do Site"
