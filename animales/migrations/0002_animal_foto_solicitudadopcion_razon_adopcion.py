# Generated by Django 5.1.3 on 2024-11-19 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='animales_fotos/'),
        ),
        migrations.AddField(
            model_name='solicitudadopcion',
            name='razon_adopcion',
            field=models.TextField(blank=True, null=True, verbose_name='¿Por qué deseas adoptar a esta mascota?'),
        ),
    ]
