# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20160222_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unpublishedarticle',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
