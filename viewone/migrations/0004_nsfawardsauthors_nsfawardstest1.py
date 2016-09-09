# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewone', '0003_pubmedauthor'),
    ]

    operations = [
        migrations.CreateModel(
            name='NsfawardsAuthors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=25, null=True)),
                ('last_name', models.CharField(blank=True, max_length=25, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('author_role', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'nsfawards_authors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NsfawardsTest1',
            fields=[
                ('award_title', models.TextField(blank=True, null=True)),
                ('award_start_date', models.DateField(blank=True, null=True)),
                ('award_end_date', models.DateField(blank=True, null=True)),
                ('award_amount', models.IntegerField(blank=True, null=True)),
                ('award_instrument', models.CharField(blank=True, max_length=40, null=True)),
                ('organization_code', models.IntegerField(blank=True, null=True)),
                ('org_directorate', models.CharField(blank=True, max_length=31, null=True)),
                ('program_manager', models.CharField(blank=True, max_length=35, null=True)),
                ('abstract', models.TextField(blank=True, null=True)),
                ('initial_amendment_date', models.DateField(blank=True, null=True)),
                ('latest_amendment_date', models.DateField(blank=True, null=True)),
                ('award_id', models.IntegerField(primary_key=True, serialize=False)),
                ('institution_name', models.CharField(blank=True, max_length=70, null=True)),
                ('institution_city', models.CharField(blank=True, max_length=30, null=True)),
                ('institution_zipcode', models.BigIntegerField(blank=True, null=True)),
                ('institution_phone_number', models.BigIntegerField(blank=True, null=True)),
                ('institution_street_address', models.CharField(blank=True, max_length=50, null=True)),
                ('institution_country', models.CharField(blank=True, max_length=25, null=True)),
                ('institution_state', models.CharField(blank=True, max_length=20, null=True)),
                ('institution_state_code', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'db_table': 'nsfawards_test1',
                'managed': False,
            },
        ),
    ]