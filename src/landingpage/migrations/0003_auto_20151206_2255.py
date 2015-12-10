# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0002_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='submitted_by',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
