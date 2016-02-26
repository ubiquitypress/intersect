# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedArticle',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('locale', models.CharField(max_length=5, null=True, blank=True)),
                ('section_id', models.BigIntegerField(null=True, blank=True)),
                ('language', models.CharField(max_length=10, null=True, blank=True)),
                ('comments_to_ed', models.TextField(null=True, blank=True)),
                ('citations', models.TextField(null=True, blank=True)),
                ('date_submitted', models.DateTimeField(null=True, blank=True)),
                ('last_modified', models.DateTimeField(null=True, blank=True)),
                ('date_status_modified', models.DateTimeField(null=True, blank=True)),
                ('status', models.IntegerField()),
                ('submission_progress', models.IntegerField()),
                ('current_round', models.IntegerField()),
                ('submission_file_id', models.BigIntegerField(null=True, blank=True)),
                ('revised_file_id', models.BigIntegerField(null=True, blank=True)),
                ('review_file_id', models.BigIntegerField(null=True, blank=True)),
                ('editor_file_id', models.BigIntegerField(null=True, blank=True)),
                ('pages', models.CharField(max_length=255, null=True, blank=True)),
                ('fast_tracked', models.IntegerField()),
                ('hide_author', models.IntegerField()),
                ('comments_status', models.IntegerField()),
                ('journal', models.BigIntegerField()),
                ('user', models.BigIntegerField()),
            ],
        ),
    ]
