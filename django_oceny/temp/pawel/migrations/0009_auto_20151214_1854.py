# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawel', '0008_auto_20151214_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oceny',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ocena_choice', models.IntegerField(default=0, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])),
            ],
        ),
        migrations.RemoveField(
            model_name='przedmiot',
            name='nazwa_przedmiotu_text',
        ),
        migrations.RemoveField(
            model_name='przedmiot',
            name='ocena_choice',
        ),
        migrations.RemoveField(
            model_name='przedmiot',
            name='osoba',
        ),
        migrations.AddField(
            model_name='przedmiot',
            name='nazwa_przedm',
            field=models.CharField(default=b'NaN', max_length=20),
        ),
        migrations.AlterField(
            model_name='osoba',
            name='imie_text',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='osoba',
            name='nazwisko_text',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='oceny',
            name='nazwa_przedmiotu_text',
            field=models.ForeignKey(to='pawel.Przedmiot'),
        ),
        migrations.AddField(
            model_name='oceny',
            name='osoba',
            field=models.ForeignKey(to='pawel.Osoba'),
        ),
    ]
