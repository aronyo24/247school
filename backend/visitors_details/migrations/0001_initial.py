# Generated by Django 5.2.1 on 2025-06-14 06:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('private_ip', models.CharField(blank=True, max_length=50, null=True)),
                ('user_agent', models.TextField()),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('last_visit', models.DateTimeField(default=django.utils.timezone.now)),
                ('visit_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
