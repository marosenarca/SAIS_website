# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0013_auto_20160530_0351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='Desc',
        ),
        migrations.AddField(
            model_name='address',
            name='AddressType',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='management.AddressType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='Brgy',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='City',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='HouseNumber',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='Landline',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='StudentID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='management.Student'),
            preserve_default=False,
        ),
    ]
