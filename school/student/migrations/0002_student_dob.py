# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 3, 20, 41, 42, 722931, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
