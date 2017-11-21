# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-11-07 17:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('likes_count', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recipy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frigerator.Product'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frigerator.Recipy'),
        ),
        migrations.AddField(
            model_name='comment',
            name='recipy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frigerator.Recipy'),
        ),
    ]
