# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-10 18:47
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
            name='Marksheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enroll_number', models.IntegerField()),
                ('uploaded_on', models.DateField(auto_now_add=True)),
                ('pdf_url', models.URLField()),
            ],
            options={
                'ordering': ['uploaded_on'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Student'), (2, 'Teacher')], null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='marksheet',
            name='standard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.Standard'),
        ),
        migrations.AddField(
            model_name='marksheet',
            name='student_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
