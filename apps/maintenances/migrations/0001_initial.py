# Generated by Django 4.2.4 on 2024-06-25 15:32

import datetime
import uuid

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("departments", "0002_remove_department_code_alter_department_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Maintenance",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "company",
                    models.CharField(
                        choices=[("Gimi", "Gimi"), ("GBL", "GBL"), ("GPB", "GPB"), ("GS", "GS")],
                        default="Gimi",
                        max_length=4,
                        verbose_name="Company",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Name")),
                ("extension", models.CharField(max_length=10, verbose_name="Extension")),
                ("object", models.CharField(max_length=50, verbose_name="Object")),
                ("url", models.URLField(blank=True, null=True, verbose_name="Attachment URL")),
                ("obs", models.TextField(blank=True, null=True, verbose_name="Observation")),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Created At"
                    ),
                ),
                (
                    "request_date",
                    models.DateField(default=datetime.date.today, verbose_name="Request Date"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Opened", "Opened"),
                            ("Scheduled", "Scheduled"),
                            ("Completed", "Completed"),
                            ("Canceled", "Canceled"),
                        ],
                        default="Opened",
                        max_length=9,
                        verbose_name="Status",
                    ),
                ),
                (
                    "forecast_date",
                    models.DateField(blank=True, null=True, verbose_name="Forecast Date"),
                ),
                (
                    "approver_obs",
                    models.TextField(blank=True, null=True, verbose_name="Approver Observation"),
                ),
                (
                    "approver_status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Checking", "Checking"),
                            ("Completed", "Completed"),
                            ("Denied", "Denied"),
                        ],
                        max_length=9,
                        null=True,
                        verbose_name="Approver Status",
                    ),
                ),
                ("end_date", models.DateTimeField(blank=True, null=True, verbose_name="End Date")),
                (
                    "approver",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="maintenance_approver",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Approver",
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="departments.department",
                        verbose_name="Department",
                    ),
                ),
                (
                    "requester",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="maintenance_requester",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Requester",
                    ),
                ),
            ],
        ),
    ]
