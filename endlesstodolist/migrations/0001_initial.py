# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('due', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('priority', models.IntegerField(choices=[(0, b'Minimal'), (1, b'Low'), (2, b'Normal'), (3, b'High'), (4, b'Urgent')])),
                ('reminders', models.ManyToManyField(to='endlesstodolist.Reminder')),
                ('tags', models.ManyToManyField(to='endlesstodolist.Tag')),
            ],
        ),
    ]
