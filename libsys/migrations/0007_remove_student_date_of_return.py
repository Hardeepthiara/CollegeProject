# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-02 10:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libsys', '0006_auto_20160302_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date_of_return',
        ),
    ]