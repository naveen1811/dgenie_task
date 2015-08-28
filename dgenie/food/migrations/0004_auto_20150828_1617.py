# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20150828_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='dish',
            field=models.CharField(max_length=1000, db_index=True),
            preserve_default=True,
        ),
    ]
