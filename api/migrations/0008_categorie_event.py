# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 22:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20171116_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='event',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Event', verbose_name='Evènements'),
            preserve_default=False,
        ),
    ]
