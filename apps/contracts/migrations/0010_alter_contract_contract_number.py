# Generated by Django 4.2.4 on 2024-03-12 15:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contracts", "0009_alter_contract_contract_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="contract_number",
            field=models.CharField(max_length=10, verbose_name="Contract Number"),
        ),
    ]
