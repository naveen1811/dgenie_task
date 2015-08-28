# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20150828_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='food',
        ),
        migrations.AddField(
            model_name='food',
            name='restaurant',
            field=models.ForeignKey(default=None, to='food.Restaurant'),
            preserve_default=False,
        ),
    ]
