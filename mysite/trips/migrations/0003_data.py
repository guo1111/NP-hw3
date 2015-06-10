# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_delete_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
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
