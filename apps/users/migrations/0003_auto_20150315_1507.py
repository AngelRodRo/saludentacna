# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_ciudad_pais'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='pais',
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='pais',
            field=models.ForeignKey(default=b'', to='users.Pais'),
            preserve_default=True,
        ),
    ]
