# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prodotto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('da_comprare', models.BooleanField(default=True)),
            ],
        ),
    ]
