# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawel', '0006_auto_20151214_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='przedmiot',
            name='nazwa_przedmiotu_text',
            field=models.CharField(default=b'Nazwa Przedmiotu', max_length=100),
        ),
        migrations.AlterField(
            model_name='przedmiot',
            name='ocena_choice',
            field=models.IntegerField(default=0, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
    ]
