# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 00:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_auto_20170915_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='Authors.Author'),
        ),
    ]