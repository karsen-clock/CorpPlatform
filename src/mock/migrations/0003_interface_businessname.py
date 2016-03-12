# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mock', '0002_auto_20151128_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='interface',
            name='businessName',
            field=models.CharField(default=-19, max_length=50),
            preserve_default=False,
        ),
    ]
