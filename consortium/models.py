from django.db import models
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    RegexValidator,
)
from utils.regex import text_regex, email_regex, phone_regex, city_regex, state_regex


class Consortium(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(
        verbose_name="Nome completo",
        max_length=100,
        unique=True,
        null=False,
        blank=False,
        validators=[
            MaxLengthValidator(100),
            MinLengthValidator(3),
            RegexValidator(
                regex=text_regex,
                message="O nome deve conter apenas letras e espaços. Ex: João da Silva",
                code="invalid_name",
            ),
        ],
    )
    email = models.CharField(
        max_length=100,
        verbose_name="E-mail",
        null=False,
        blank=False,
        validators=[
            MaxLengthValidator(100),
            MinLengthValidator(3),
            RegexValidator(
                regex=email_regex,
                message="O e-mail deve ser válido",
                code="invalid_email. Ex: sample@gmail.com",
            ),
        ],
    )
    phone = models.CharField(
        max_length=15,
        verbose_name="Telefone",
        null=False,
        blank=False,
        validators=[
            MaxLengthValidator(15),
            MinLengthValidator(3),
            RegexValidator(
                regex=phone_regex,
                message="O telefone deve ser válido. Ex: 11 99999-9999",
                code="invalid_phone",
            ),
        ],
    )
    state = models.CharField(
        max_length=100,
        verbose_name="Estado",
        validators=[
            MaxLengthValidator(100),
            MinLengthValidator(3),
            RegexValidator(
                regex=state_regex,
                message="O estado deve conter apenas letras e espaços. Ex: São Paulo",
                code="invalid_state",
            ),
        ],
    )
    city = models.CharField(
        max_length=100,
        verbose_name="Cidade",
        validators=[
            MaxLengthValidator(100),
            MinLengthValidator(3),
            RegexValidator(
                regex=city_regex,
                message="A cidade deve conter apenas letras e espaços. Ex: São Paulo",
                code="invalid_city",
            ),
        ],
    )
    product_request = models.CharField(
        max_length=100, verbose_name="Produto selecionado", null=True, blank=True
    )
    accept_contact = models.BooleanField(
        default=True, verbose_name="Aceita receber contato?"
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Dados do Consórcio"
