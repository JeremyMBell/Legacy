# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=2, choices=[(b'1', b'science'), (b'2', b'arts'), (b'3', b'history'), (b'4', b'business'), (b'5', b'computers'), (b'6', b'engineering'), (b'7', b'medicine'), (b'8', b'everyday')])),
                ('title', models.CharField(max_length=40)),
                ('background', models.TextField(blank=True)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
