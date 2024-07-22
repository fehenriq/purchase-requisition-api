# Generated by Django 4.2.4 on 2024-02-13 12:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0002_service_provider"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="status",
            field=models.CharField(
                choices=[("Opened", "Opened"), ("Approved", "Approved"), ("Denied", "Denied")],
                default="Pending",
                max_length=8,
                verbose_name="Status",
            ),
        ),
    ]
