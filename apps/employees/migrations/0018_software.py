# Generated by Django 4.2.4 on 2024-11-29 01:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0017_alter_employee_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=60, null=True, verbose_name='Complete Name')),
            ],
        ),
    ]
