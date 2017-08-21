# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 03:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, max_length=30, null=True)),
                ('app_label', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_type', models.IntegerField(default=0, unique=True)),
                ('access_type_name', models.CharField(default='VIEW', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(default=1, unique=True)),
                ('description', models.TextField(blank=True, verbose_name="Role's Description")),
            ],
        ),
        migrations.AddField(
            model_name='accesscontrol',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='drf_role.Permission'),
        ),
        migrations.AddField(
            model_name='accesscontrol',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drf_role.Role'),
        ),
    ]
