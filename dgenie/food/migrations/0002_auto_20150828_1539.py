# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rest_id', models.IntegerField(max_length=10, db_index=True)),
                ('name', models.CharField(max_length=300, db_index=True)),
                ('rating', models.FloatField(max_length=5, null=True, blank=True)),
                ('service', models.CharField(max_length=300, db_index=True)),
                ('food', models.ForeignKey(to='food.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='resturant',
            name='food',
        ),
        migrations.DeleteModel(
            name='Resturant',
        ),
    ]
