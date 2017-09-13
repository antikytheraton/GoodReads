# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 02:34
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=100)),
                ('date_published', models.DateField()),
                ('cover', models.URLField()),
                ('prologue', models.TextField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('literary_genre', models.CharField(choices=[('CF', 'Ciencia Ficcion'), ('FS', 'Fantasia'), ('TR', 'Terror'), ('IT', 'Tecnologia'), ('DR', 'Drama')], max_length=50)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=None)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor', to='Authors.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarista', to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libro', to='Books.Book')),
            ],
        ),
    ]
