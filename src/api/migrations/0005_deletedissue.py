# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_deletedarticle'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedIssue',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('volume', models.SmallIntegerField(null=True, blank=True)),
                ('number', models.CharField(max_length=10, null=True, blank=True)),
                ('year', models.SmallIntegerField(null=True, blank=True)),
                ('published', models.IntegerField()),
                ('current', models.IntegerField()),
                ('date_published', models.DateTimeField(null=True, blank=True)),
                ('date_notified', models.DateTimeField(null=True, blank=True)),
                ('access_status', models.IntegerField()),
                ('open_access_date', models.DateTimeField(null=True, blank=True)),
                ('show_volume', models.IntegerField()),
                ('show_number', models.IntegerField()),
                ('show_year', models.IntegerField()),
                ('show_title', models.IntegerField()),
                ('style_file_name', models.CharField(max_length=90, null=True, blank=True)),
                ('original_style_file_name', models.CharField(max_length=255, null=True, blank=True)),
                ('last_modified', models.DateTimeField(null=True, blank=True)),
                ('journal', models.ForeignKey(to='api.Journal')),
            ],
        ),
    ]
