# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(unique=True, max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('avatar', models.URLField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ciudad', models.CharField(max_length=15, verbose_name=b'ciudad')),
            ],
            options={
                'verbose_name_plural': 'Ciudades',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('dni', models.CharField(max_length=30, serialize=False, verbose_name=b'DNI', primary_key=True)),
                ('telefono', models.CharField(max_length=15, null=True, verbose_name=b'Telefono', blank=True)),
                ('ciudad', models.ForeignKey(to='users.Ciudad')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pais', models.CharField(max_length=5, verbose_name=b'pais')),
            ],
            options={
                'verbose_name_plural': 'Paises',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cliente',
            name='pais',
            field=models.ForeignKey(to='users.Pais'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
