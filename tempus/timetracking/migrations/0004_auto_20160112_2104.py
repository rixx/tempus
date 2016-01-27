# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetracking', '0003_auto_20160111_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('name', 'category')]),
        ),
    ]