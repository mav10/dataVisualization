# Generated by Django 2.1.5 on 2019-01-22 05:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190122_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='reapir',
            name='milage',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
