# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 10:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mercanet.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionMercanet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de la commande')),
                ('responseText', models.CharField(blank=True, max_length=256, verbose_name='Status de la transaction')),
                ('transactionReference', models.CharField(max_length=35, verbose_name='UUID (Référence MercaNET)')),
                ('amount', models.IntegerField(verbose_name='montant payé (centimes)')),
                ('maskedPan', models.CharField(blank=True, max_length=254, verbose_name='numéro de CB masqué')),
                ('transactionDateTime', models.DateTimeField(blank=True, null=True, verbose_name='Date de la transaction')),
                ('cardProductName', models.CharField(blank=True, max_length=100, verbose_name='nom de la CB')),
                ('panExpiryDate', models.IntegerField(blank=True, null=True, verbose_name="date d'expiration ?")),
                ('customerIpAddress', models.GenericIPAddressField(blank=True, null=True, verbose_name='On a le droit de le stocker ?')),
                ('complementaryCode', models.IntegerField(blank=True, null=True, verbose_name='C koi ?')),
                ('panEntryMode', models.CharField(blank=True, max_length=20, null=True, verbose_name="mode d'entrée du n° de la CB")),
                ('captureDay', models.IntegerField(blank=True, null=True)),
                ('responseCode', models.CharField(blank=True, max_length=2, null=True, verbose_name='(responseCode)VERIF PAIEMENT SI=0')),
                ('issuerCountryCode', models.CharField(blank=True, max_length=5, null=True, verbose_name='Pays émetteur de la CB')),
                ('customerMobilePhone', models.CharField(blank=True, max_length=30, null=True, verbose_name='numéro de téléphone')),
                ('paymentMeanBrand', models.CharField(blank=True, max_length=20, null=True, verbose_name='organisme de paiement ex: VISA')),
                ('issuerCode', models.IntegerField(blank=True, null=True, verbose_name='C koi ?')),
                ('paymentMeanType', models.CharField(blank=True, max_length=20, null=True, verbose_name='type de paiement ex: CB, PayPal...')),
                ('captureLimitDate', models.IntegerField(blank=True, null=True, verbose_name='C koi ? temps pour annuler le paiement ?')),
                ('cardProductCode', models.CharField(blank=True, max_length=5, null=True, verbose_name='important ?')),
            ],
            options={
                'verbose_name_plural': 'Transactions avec la BNP',
            },
        ),
        migrations.CreateModel(
            name='TransactionRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name="montant en centimes d'euros")),
                ('callback', models.CharField(max_length=2000, verbose_name='url de retour client')),
                ('started', models.BooleanField(verbose_name='pris en charge par mercanet')),
                ('token', models.CharField(default=mercanet.models.generate_token, max_length=127, verbose_name="clef d'accès")),
                ('mercanet', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mercanet.TransactionMercanet')),
            ],
            options={
                'verbose_name': 'Requêtes de paiement',
            },
        ),
    ]