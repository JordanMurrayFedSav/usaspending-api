# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-30 12:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0065_dropping_unused_award_columns'),
    ]

    operations = [
        migrations.RunSQL(
            ["drop index if exists idx_broker_subaward_imported_true"],
            ["""
                create index if not exists idx_broker_subaward_imported_true on 
                broker_subaward (imported) where imported is true"""],
        ),
        migrations.RemoveField(
            model_name='brokersubaward',
            name='imported',
        ),
    ]