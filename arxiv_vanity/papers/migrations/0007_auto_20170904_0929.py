# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 09:29
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("papers", "0006_auto_20170822_1553")]

    operations = [
        migrations.AlterField(
            model_name="paper",
            name="categories",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=100), size=None
            ),
        ),
        migrations.AlterField(
            model_name="paper",
            name="primary_category",
            field=models.CharField(max_length=100),
        ),
    ]
