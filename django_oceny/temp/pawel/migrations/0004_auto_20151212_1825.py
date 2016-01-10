# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawel', '0003_auto_20151212_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ocena',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ocena_choice', models.CharField(default=b'-', max_length=1, choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6')])),
            ],
        ),
        migrations.RemoveField(
            model_name='przedmiot',
            name='ocena',
        ),
        migrations.AddField(
            model_name='ocena',
            name='przedmiot',
            field=models.ForeignKey(to='pawel.Przedmiot'),
        ),
    ]
