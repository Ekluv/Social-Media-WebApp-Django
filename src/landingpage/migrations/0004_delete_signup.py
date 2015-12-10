# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0003_auto_20151206_2255'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
