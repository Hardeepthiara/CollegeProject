# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-02 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libsys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'M'), ('Female', 'F')], max_length=1),
        ),
    ]
