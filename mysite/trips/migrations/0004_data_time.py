# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='time',
            field=models.CharField(default=datetime.datetime(2015, 6, 10, 8, 23, 59, 647109, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
