# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 09:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20170527_1825'),
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='perfil_fk',
            field=models.ForeignKey(default=user.models.Perfil, on_delete=django.db.models.deletion.CASCADE, to='user.Perfil'),
        ),
    ]
