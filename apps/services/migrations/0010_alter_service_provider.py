# Generated by Django 4.2.4 on 2024-04-12 18:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0009_service_has_quotation_service_quotation_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="provider",
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name="Provider"),
        ),
    ]
