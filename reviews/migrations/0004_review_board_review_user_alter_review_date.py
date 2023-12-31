# Generated by Django 4.2.2 on 2023-06-27 05:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0002_board_user'),
        ('reviews', '0003_alter_review_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='board',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='boards.board'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 27, 5, 44, 12, 324890, tzinfo=datetime.timezone.utc)),
        ),
    ]
