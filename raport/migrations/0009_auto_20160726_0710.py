# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-07-26 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raport', '0008_auto_20160724_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raport',
            name='harian',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='raport',
            name='uas',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='raport',
            name='uts',
            field=models.FloatField(default=0, null=True),
        ),
    ]