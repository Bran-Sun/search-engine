# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysearch', '0003_auto_20170914_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keylist',
            name='list',
            field=models.CharField(default='', max_length=5000),
        ),
    ]