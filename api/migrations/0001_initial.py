# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 10:39
from __future__ import unicode_literals

import api.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Billet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BilletOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
                ('billet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billet_options', to='api.Billet')),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="Nom de l'évènement")),
                ('visibility', models.CharField(choices=[('closed', 'Fermée'), ('hidden', 'Cachée'), ('invite', 'Par invitation'), ('public', 'Public')], default='closed', max_length=20, verbose_name='Visibilitée')),
                ('description', models.TextField(verbose_name='Description')),
                ('ticket_background', models.ImageField(blank=True, upload_to='', verbose_name="Fond d'image tickets")),
                ('sales_opening', models.DateTimeField(default=datetime.datetime.now, verbose_name='Ouverture des ventes')),
                ('sales_closing', models.DateTimeField(default=datetime.datetime.now, verbose_name='Clôture des ventes')),
                ('max_seats', models.IntegerField(default=1600, verbose_name='Nombre maximal de place')),
                ('seats_goal', models.IntegerField(default=1600, verbose_name='Nombre de place visé')),
                ('logo_url', models.CharField(blank=True, default='http://logos.bde-insa-lyon.fr/bal/Logo_bal.png', max_length=2500, null=True, verbose_name='Url du logo')),
                ('start_time', models.DateTimeField(default=datetime.datetime.now, verbose_name="Début de l'évènement")),
                ('end_time', models.DateTimeField(default=datetime.datetime.now, verbose_name="Fin de l'évènement")),
                ('website', models.CharField(blank=True, default='', max_length=250, verbose_name='Site Web')),
                ('place', models.CharField(blank=True, default='', max_length=250, verbose_name='Nom du lieu')),
                ('address', models.CharField(blank=True, default='', max_length=250, verbose_name='Adresse du lieu')),
            ],
            options={
                'verbose_name': 'Evènement',
            },
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField(default=1)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('link_sent', models.BooleanField()),
                ('reason', models.TextField(blank=True)),
                ('token', models.CharField(default=api.models.generate_token, max_length=32)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='api.Client')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='api.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('seats', models.IntegerField(default=1)),
                ('price_ht', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Prix HT')),
                ('price_ttc', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Prix TTC')),
                ('target', models.CharField(choices=[('Order', 'Globalement sur la commande'), ('Billet', 'Pour chaque billet'), ('Participant', 'Pour chaque participant')], default='Participant', max_length=30)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Event', verbose_name='Evènement')),
            ],
            options={
                'verbose_name': 'Tarif des option',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Pas initialisée'), (1, 'Sélection des produits'), (2, 'Sélection des options'), (3, 'Paiement'), (5, 'Confirmée')], default=0, verbose_name='status')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Client')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('address', models.CharField(blank=True, max_length=250)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Organisateur',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('billet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='api.Billet')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentProtocol', models.CharField(choices=[('CB', 'payment by Credit Card'), ('ESP', 'payment by cash'), ('VIR', 'payment by bank transfer')], max_length=50)),
                ('paymentMin', models.IntegerField(default=-1000000)),
                ('paymentMax', models.IntegerField(default=1000000)),
            ],
            options={
                'verbose_name': 'Moyens de paiement',
            },
        ),
        migrations.CreateModel(
            name='PricingRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CheckMaxProductForInvite', 'Vérifie la limite par rapport aux invitations'), ('MaxProductByOrder', 'Limite le nombre dans une commande'), ('MaxSeats', 'Limite le nombre de personnes')], max_length=50)),
                ('description', models.TextField()),
                ('value', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Règles de poduits (Jauges/Limite)',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('seats', models.IntegerField(default=1)),
                ('price_ht', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Prix HT')),
                ('price_ttc', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Prix TTC')),
                ('categorie', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='api.Categorie', verbose_name='Catégorie')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Event', verbose_name='Evènement')),
            ],
            options={
                'verbose_name': 'Tarif des produit',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('help_text', models.TextField()),
                ('question_type', models.IntegerField(verbose_name='type de question')),
                ('required', models.BooleanField(default=False)),
                ('target', models.CharField(choices=[('Order', 'Globalement sur la commande'), ('Billet', 'Pour chaque billet'), ('Participant', 'Pour chaque participant')], default='Participant', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Participant')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Question')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='questions',
            field=models.ManyToManyField(blank=True, to='api.Question'),
        ),
        migrations.AddField(
            model_name='product',
            name='rules',
            field=models.ManyToManyField(blank=True, to='api.PricingRule'),
        ),
        migrations.AddField(
            model_name='option',
            name='products',
            field=models.ManyToManyField(related_name='options', to='api.Product'),
        ),
        migrations.AddField(
            model_name='option',
            name='questions',
            field=models.ManyToManyField(blank=True, to='api.Question'),
        ),
        migrations.AddField(
            model_name='option',
            name='rules',
            field=models.ManyToManyField(blank=True, to='api.PricingRule'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='api.Organizer'),
        ),
        migrations.AddField(
            model_name='categorie',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Event', verbose_name='Evènements'),
        ),
        migrations.AddField(
            model_name='billetoption',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Option'),
        ),
        migrations.AddField(
            model_name='billetoption',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billet_options', to='api.Order'),
        ),
        migrations.AddField(
            model_name='billetoption',
            name='participant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='options_by_billet', to='api.Participant'),
        ),
        migrations.AddField(
            model_name='billet',
            name='options',
            field=models.ManyToManyField(related_name='billets', through='api.BilletOption', to='api.Option'),
        ),
        migrations.AddField(
            model_name='billet',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billets', to='api.Order'),
        ),
        migrations.AddField(
            model_name='billet',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billets', to='api.Product'),
        ),
    ]
