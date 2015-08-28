# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_auto_20150828_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='restaurant',
            field=models.ForeignKey(related_name='food', to='food.Restaurant'),
            preserve_default=True,
        ),
    ]
