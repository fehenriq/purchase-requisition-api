# Generated by Django 4.2.4 on 2023-08-16 17:02

import uuid

import django.utils.timezone
from django.db import migrations, models

import apps.users.validators.superuser


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100, validators=[apps.users.validators.superuser.valid_name], verbose_name='Complete Name')),
                ('email', models.EmailField(max_length=100, unique=True, validators=[apps.users.validators.superuser.valid_email], verbose_name='E-mail')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active Account')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Administrator')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'permissions': (('admin_user', 'Can Admin Users'), ('disable_user', 'Can disable User')),
            },
        ),
    ]
