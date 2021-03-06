# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20170502_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='graduationDate',
        ),
        migrations.AddField(
            model_name='user',
            name='graduation_semester',
            field=models.CharField(blank=True, choices=[('W', 'Winter'), ('SP', 'Spring'), ('SU', 'Summer'), ('F', 'Fall')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='graduation_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
