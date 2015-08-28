# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_id', models.IntegerField(max_length=10, db_index=True)),
                ('dish', models.CharField(max_length=100, db_index=True)),
                ('price', models.IntegerField(max_length=5)),
                ('item_sid', models.IntegerField(max_length=10, db_index=True)),
                ('is_addon_must', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resturant',
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
    ]
