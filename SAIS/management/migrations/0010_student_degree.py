# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_auto_20160529_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Degree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='management.Degree'),
            preserve_default=False,
        ),
    ]