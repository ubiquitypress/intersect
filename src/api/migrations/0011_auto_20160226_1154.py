# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20160222_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='mime_type',
            field=models.CharField(max_length=250),
        ),
    ]
