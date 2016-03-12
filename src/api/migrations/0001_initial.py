# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reportData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BuildNo', models.IntegerField()),
                ('TotalCases', models.IntegerField()),
                ('FailureCases', models.IntegerField()),
                ('SuccessRate', models.FloatField()),
                ('AverageTime', models.IntegerField()),
                ('MinTime', models.IntegerField()),
                ('MaxTime', models.IntegerField()),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
