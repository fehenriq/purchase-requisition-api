# Generated by Django 4.2.4 on 2024-02-09 13:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contracts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="project_name",
            field=models.CharField(
                blank=True, max_length=120, null=True, verbose_name="Client Name"
            ),
        ),
    ]
