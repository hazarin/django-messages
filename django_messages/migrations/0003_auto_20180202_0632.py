# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-02 06:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_messages', '0002_auto_20160607_0852'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='message',
            index_together=set([('sender', 'recipient')]),
        ),
    ]
