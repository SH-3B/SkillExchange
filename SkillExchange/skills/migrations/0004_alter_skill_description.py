# Generated by Django 5.1.3 on 2024-12-18 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_alter_skill_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(default='', max_length=600),
            preserve_default=False,
        ),
    ]
