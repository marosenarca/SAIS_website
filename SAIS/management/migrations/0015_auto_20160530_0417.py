# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 20:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_auto_20160530_0351'),
    ]

    operations = [
        migrations.CreateModel(
            name='HousingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Desc', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='HousingType',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='management.HousingType'),
            preserve_default=False,
        ),
    ]
