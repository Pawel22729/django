# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawel', '0004_auto_20151212_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ocena',
            name='przedmiot',
        ),
        migrations.AddField(
            model_name='przedmiot',
            name='ocena_choice',
            field=models.CharField(default=b'-', max_length=1, choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6')]),
        ),
        migrations.DeleteModel(
            name='Ocena',
        ),
    ]
