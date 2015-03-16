# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25, verbose_name=b'Nombre')),
                ('direccion', models.CharField(max_length=40, verbose_name=b'Direccion')),
                ('telefono', models.CharField(max_length=15, verbose_name=b'Telefono')),
                ('correo', models.EmailField(max_length=75)),
                ('foto', models.ImageField(null=True, upload_to=b'clinics/img', blank=True)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
