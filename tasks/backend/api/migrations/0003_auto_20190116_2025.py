# Generated by Django 2.1.5 on 2019-01-16 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_device_patient_statistics_therapyday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='api.Device'),
        ),
    ]
