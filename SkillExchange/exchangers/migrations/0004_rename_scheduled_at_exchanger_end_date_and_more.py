# Generated by Django 5.1.3 on 2024-12-14 18:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchangers', '0003_rename_scheduled_at_request_end_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exchanger',
            old_name='scheduled_at',
            new_name='end_date',
        ),
        migrations.AddField(
            model_name='exchanger',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
