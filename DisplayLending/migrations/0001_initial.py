# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Bookinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LendRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('begin_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True)),
                ('is_return', models.NullBooleanField()),
                ('book', models.ForeignKey(related_name='lend_book', to='Bookinfo.Book')),
                ('user', models.ForeignKey(related_name='lend_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
