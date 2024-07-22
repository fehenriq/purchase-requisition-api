# Generated by Django 4.2.4 on 2024-03-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0007_alter_service_approval_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="status",
            field=models.CharField(
                choices=[("Opened", "Opened"), ("Approved", "Approved"), ("Denied", "Denied")],
                default="Opened",
                max_length=8,
                verbose_name="Status",
            ),
        ),
    ]
