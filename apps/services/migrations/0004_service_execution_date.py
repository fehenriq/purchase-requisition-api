# Generated by Django 4.2.4 on 2024-02-26 18:39

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0003_alter_service_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="execution_date",
            field=models.DateField(default=datetime.date.today, verbose_name="Execution Date"),
        ),
    ]
