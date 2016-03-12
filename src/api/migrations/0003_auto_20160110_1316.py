# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_reportdata_productline'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportdata',
            name='AverageLatency',
            field=models.IntegerField(blank=True, default=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reportdata',
            name='MaxLatency',
            field=models.IntegerField(blank=True, default=3000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reportdata',
            name='MinLatency',
            field=models.IntegerField(blank=True, default=100),
            preserve_default=False,
        ),
    ]
