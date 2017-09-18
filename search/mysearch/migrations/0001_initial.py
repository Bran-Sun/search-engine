# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgurl', models.CharField(max_length=50)),
                ('identity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='KeyList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50)),
                ('associate', models.ManyToManyField(to='mysearch.Information')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='information',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysearch.Person'),
        ),
    ]
