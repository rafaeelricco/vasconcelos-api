from django.db import models


class Consortium(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(
        max_length=100, verbose_name='Nome completo', unique=True)
    email = models.CharField(
        max_length=100, verbose_name='E-mail')
    phone = models.CharField(
        max_length=15, verbose_name='Telefone')
    state = models.CharField(
        max_length=100, verbose_name='Estado', )
    city = models.CharField(max_length=100, verbose_name='Cidade', )
    product_request = models.CharField(
        max_length=100, verbose_name='Produto selecionado', null=True, blank=True)
    accept_contact = models.BooleanField(
        default=True, verbose_name='Aceita receber contato?')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Dados do Consórcio'
