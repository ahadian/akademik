# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-07-19 12:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raport', '0004_auto_20160719_1222'),
        ('kelas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pengajar',
            name='kd_guru',
        ),
        migrations.RemoveField(
            model_name='pengajar',
            name='kelas',
        ),
        migrations.RemoveField(
            model_name='pengajar',
            name='mapel',
        ),
        migrations.DeleteModel(
            name='Kelas',
        ),
        migrations.DeleteModel(
            name='Mapel',
        ),
        migrations.DeleteModel(
            name='Pengajar',
        ),
    ]