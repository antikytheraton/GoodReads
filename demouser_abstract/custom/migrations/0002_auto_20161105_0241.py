# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='location',
            new_name='cinta',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='birth_date',
            new_name='fecha_ingreso',
        ),
    ]
