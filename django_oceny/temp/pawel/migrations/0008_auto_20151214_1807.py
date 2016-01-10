# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawel', '0007_auto_20151214_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='przedmiot',
            name='ocena_choice',
            field=models.IntegerField(default=0, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
    ]
