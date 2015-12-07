# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='interface',
            fields=[
                ('protocol', models.CharField(max_length=50)),
                ('interfaceName', models.CharField(serialize=False, primary_key=True, max_length=100)),
                ('responseData', models.CharField(max_length=2000)),
                ('operator', models.CharField(max_length=20)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('updatetime', models.DateTimeField(auto_now_add=True)),
                ('isvalid', models.BooleanField()),
            ],
        ),
    ]
