# Generated by Django 2.2.10 on 2021-05-30 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210530_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='own_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
