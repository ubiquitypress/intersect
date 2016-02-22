# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_unpublishedarticle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unpublishedarticle',
            name='article',
            field=models.ForeignKey(to='api.Article'),
        ),
    ]
