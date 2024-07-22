# Generated by Django 4.2.4 on 2024-04-27 03:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("purchases", "0010_alter_purchaseproduct_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchaseproduct",
            name="quantity",
            field=models.DecimalField(decimal_places=5, max_digits=12, verbose_name="Quantity"),
        ),
    ]
