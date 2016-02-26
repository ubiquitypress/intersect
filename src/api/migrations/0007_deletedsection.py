# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_deletedauthor'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedSection',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('seq', models.FloatField(default=0.0)),
                ('editor_restricted', models.IntegerField(default=0)),
                ('meta_indexed', models.IntegerField(default=0)),
                ('meta_reviewed', models.IntegerField(default=0)),
                ('abstracts_not_required', models.IntegerField(default=0)),
                ('hide_title', models.IntegerField(default=0)),
                ('hide_author', models.IntegerField(default=0)),
                ('hide_about', models.IntegerField(default=0)),
                ('disable_comments', models.IntegerField(default=0)),
                ('abstract_word_count', models.BigIntegerField(null=True, blank=True)),
                ('journal', models.BigIntegerField()),
                ('review_form', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
    ]
