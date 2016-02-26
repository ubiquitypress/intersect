# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_deletedissue'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedAuthor',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('primary_contact', models.IntegerField()),
                ('seq', models.FloatField()),
                ('first_name', models.CharField(max_length=40)),
                ('middle_name', models.CharField(max_length=40, null=True, blank=True)),
                ('last_name', models.CharField(max_length=90)),
                ('country', models.CharField(max_length=90, null=True, blank=True)),
                ('email', models.CharField(max_length=90)),
                ('url', models.CharField(max_length=255, null=True, blank=True)),
                ('suffix', models.CharField(max_length=40, null=True, blank=True)),
                ('deleted_article', models.BigIntegerField()),
                ('user_group',models.BigIntegerField(blank=True, null=True)),
            ],
        ),
    ]
