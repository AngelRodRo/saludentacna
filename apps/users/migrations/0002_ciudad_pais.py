# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciudad',
            name='pais',
            field=models.ForeignKey(default='', to='users.Pais'),
            preserve_default=False,
        ),
    ]
