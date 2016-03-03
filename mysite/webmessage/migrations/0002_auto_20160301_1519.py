# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-01 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('webmessage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile',
        ),
        migrations.AddField(
            model_name='mailbox',
            name='public_key',
            field=models.CharField(default='NO KEY', max_length=2048),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]