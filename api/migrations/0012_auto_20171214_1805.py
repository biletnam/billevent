# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20171211_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=255)),
                ('max_use', models.IntegerField(default=0)),
                ('percentage', models.FloatField(blank=True, default=0, help_text='entre 0 et 1', verbose_name='pourcentage')),
                ('amount', models.FloatField(blank=True, default=0, help_text='en euros', verbose_name='montant')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Event')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='api.Coupon'),
        ),
    ]
