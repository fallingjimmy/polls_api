# Generated by Django 2.2.10 on 2021-05-30 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210530_0350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='poll',
        ),
    ]
