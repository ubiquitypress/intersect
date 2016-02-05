# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mime_type', models.CharField(max_length=50)),
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
    ]
