# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthortableTest',
            fields=[
                ('author_name', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('complete_addr', models.TextField(blank=True, null=True)),
                ('pubmed_id', models.CharField(max_length=20)),
                ('department', models.TextField(blank=True, null=True)),
                ('institution', models.TextField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('tools_used', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'authortable_test',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PubmedTitles',
            fields=[
                ('pubmed_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pubmed_titles',
                'managed': False,
            },
        ),
    ]
