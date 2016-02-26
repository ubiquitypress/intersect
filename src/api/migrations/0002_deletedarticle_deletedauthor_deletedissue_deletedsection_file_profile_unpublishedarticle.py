# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('intersect_user', models.BigIntegerField(serialize=False, primary_key=True, db_column='intersect_user_id')),
                ('user', models.BigIntegerField(db_column='user_id')),
                ('journal', models.BigIntegerField(db_column='journal_id')),
            ],
            options={
                'db_table': 'user_profiles',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='DeletedArticle',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('locale', models.CharField(max_length=5, null=True, blank=True)),
                ('user', models.BigIntegerField(db_column='user')),
                ('journal', models.BigIntegerField(db_column='journal')),
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
            ],
        ),
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
                ('deleted_article', models.BigIntegerField(blank=True, null=True,db_column='deleted_article_id')),
                ('user_group', models.BigIntegerField(blank=True, null=True,db_column='user_group_id')),
            ],
        ),
        migrations.CreateModel(
            name='DeletedIssue',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('journal', models.BigIntegerField(db_column='journal')),
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
            ],
        ),
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
                ('journal', models.BigIntegerField(db_column='journal_id')),
                ('review_form', models.BigIntegerField(db_column='review_form_id')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mime_type', models.CharField(max_length=256)),
                ('original_filename', models.CharField(max_length=1000)),
                ('uuid_filename', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=200, null=True, blank=True)),
                ('description', models.CharField(max_length=1000, null=True, blank=True)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('stage_uploaded', models.IntegerField()),
                ('kind', models.CharField(max_length=100)),
                ('sequence', models.IntegerField(default=1)),
                ('article_file', models.IntegerField(default=-1)),
                ('issue_file', models.IntegerField(default=-1)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('sequence', '-kind'),
            },
        ),
        migrations.CreateModel(
            name='UnPublishedArticle',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('seq', models.FloatField()),
                ('access_status', models.IntegerField()),
                ('article', models.BigIntegerField(db_column='article_id')),
                ('issue', models.BigIntegerField(db_column='issue_id')),
            ],
        ),
    ]
