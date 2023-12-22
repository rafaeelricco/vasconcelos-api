# Generated by Django 4.1.2 on 2022-10-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consortium',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100, unique=True, verbose_name='Nome completo')),
                ('email', models.CharField(max_length=100, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('state', models.CharField(max_length=100, verbose_name='Estado')),
                ('city', models.CharField(max_length=100, verbose_name='Cidade')),
                ('product_request', models.CharField(blank=True, max_length=100, null=True, verbose_name='Produto selecionado')),
                ('accept_contact', models.BooleanField(default=True, verbose_name='Aceita receber contato?')),
            ],
            options={
                'verbose_name_plural': 'Dados do Consórcio',
            },
        ),
    ]