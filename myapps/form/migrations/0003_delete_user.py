# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 21:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20170728_1235'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
