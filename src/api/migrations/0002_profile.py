# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.ForeignKey(related_name='profile_user', primary_key=True, db_column='user_id', serialize=False, to='api.User')),
            ],
            options={
                'db_table': 'user_profiles',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
