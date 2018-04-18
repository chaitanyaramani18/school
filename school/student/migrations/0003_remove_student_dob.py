# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='dob',
        ),
    ]
