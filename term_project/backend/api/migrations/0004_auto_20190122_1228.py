# Generated by Django 2.1.5 on 2019-01-22 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_reapir_milage'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='repair',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Reapir'),
        ),
        migrations.AddField(
            model_name='repairwork',
            name='repair',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Reapir'),
        ),
    ]
