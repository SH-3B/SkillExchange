# Generated by Django 5.1.3 on 2024-12-15 19:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchangers', '0007_remove_exchanger_skills_exchanged_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchanger',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='exchanger',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='request',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='request',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
