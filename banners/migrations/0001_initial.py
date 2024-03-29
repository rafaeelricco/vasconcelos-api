# Generated by Django 4.1.2 on 2022-10-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Chamada do banner')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Descrição do banner')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link do botão')),
                ('image', models.ImageField(blank=True, null=True, upload_to='public/banners', verbose_name='Imagem do banner')),
            ],
            options={
                'verbose_name_plural': 'Banners do Site',
            },
        ),
    ]
