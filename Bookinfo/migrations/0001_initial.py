# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('picture', models.ImageField(upload_to=b'')),
                ('auther', models.CharField(max_length=150)),
                ('publisher', models.CharField(max_length=150)),
                ('page_num', models.IntegerField()),
                ('index', models.CharField(max_length=150)),
                ('info', models.TextField()),
            ],
        ),
    ]
