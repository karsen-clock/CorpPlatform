# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interface',
            old_name='responseData',
            new_name='mockConfig',
        ),
    ]
