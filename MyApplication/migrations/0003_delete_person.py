# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApplication', '0002_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
