# Generated by Django 5.1.3 on 2024-11-19 01:09

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('disponible_para_adopcion', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudAdopcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.TextField()),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('fecha_solicitud', models.DateTimeField(default=django.utils.timezone.now)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animales.animal')),
            ],
        ),
    ]
