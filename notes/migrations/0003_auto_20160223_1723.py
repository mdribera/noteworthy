# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20160223_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='label',
            old_name='label_color',
            new_name='background_color',
        ),
        migrations.RenameField(
            model_name='label',
            old_name='label_text',
            new_name='text',
        ),
        migrations.AddField(
            model_name='label',
            name='text_color',
            field=models.CharField(default='ffffff', max_length=6),
            preserve_default=False,
        ),
    ]
