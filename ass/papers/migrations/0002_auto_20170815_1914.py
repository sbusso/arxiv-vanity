# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 19:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Render',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('state', models.CharField(choices=[('unstarted', 'Unstarted'), ('running', 'Running'), ('success', 'Success'), ('failure', 'Failure')], default='unstarted', max_length=20)),
                ('container_id', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'get_latest_by': 'created_at',
            },
        ),
        migrations.AlterModelOptions(
            name='paper',
            options={'get_latest_by': 'updated', 'ordering': ['-updated']},
        ),
        migrations.AddField(
            model_name='render',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='papers.Paper'),
        ),
    ]
