# Generated by Django 4.2.2 on 2023-06-28 05:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storys', '0004_alter_story_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 28, 5, 14, 5, 690393, tzinfo=datetime.timezone.utc)),
        ),
    ]
