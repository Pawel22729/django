# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Przedmiot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazwa_przedmiotu_text', models.CharField(max_length=100)),
                ('ocena', models.IntegerField(default=0)),
                ('osoba', models.ForeignKey(to='pawel.Osoba')),
            ],
        ),
    ]
