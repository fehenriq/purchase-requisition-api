# Generated by Django 4.2.4 on 2024-04-12 15:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0008_alter_service_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='has_quotation',
            field=models.BooleanField(default=True, verbose_name='Has Quotation?'),
        ),
        migrations.AddField(
            model_name='service',
            name='quotation_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Quotation Date'),
        ),
        migrations.AddField(
            model_name='service',
            name='quotation_emails',
            field=models.TextField(blank=True, null=True, verbose_name='Service Quotation Emails'),
        ),
        migrations.AlterField(
            model_name='service',
            name='approver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_approver', to=settings.AUTH_USER_MODEL, verbose_name='Approver'),
        ),
        migrations.AlterField(
            model_name='service',
            name='status',
            field=models.CharField(choices=[('Opened', 'Opened'), ('Approved', 'Approved'), ('Denied', 'Denied'), ('Canceled', 'Canceled'), ('Quotation', 'Quotation')], default='Opened', max_length=9, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='service',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Value'),
        ),
    ]
