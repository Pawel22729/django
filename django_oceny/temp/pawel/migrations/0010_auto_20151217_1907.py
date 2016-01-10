# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawel', '0009_auto_20151214_1854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oceny',
            name='nazwa_przedmiotu_text',
        ),
        migrations.AddField(
            model_name='oceny',
            name='nazwa_przedm',
            field=models.CharField(default=b'NaN', max_length=20),
        ),
        migrations.DeleteModel(
            name='Przedmiot',
        ),
    ]
