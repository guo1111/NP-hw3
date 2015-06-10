# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('sex', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('hobby', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
