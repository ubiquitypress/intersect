# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_deletedsection'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnPublishedArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seq', models.FloatField()),
                ('access_status', models.IntegerField()),
                ('article', models.BigIntegerField(db_column='article_id')),
                ('issue',models.BigIntegerField(db_column='issue_id')),
            ],
        ),
    ]
