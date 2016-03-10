# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecomendBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField()),
                ('book', models.ForeignKey(to='Bookinfo.Book')),
            ],
        ),
    ]
