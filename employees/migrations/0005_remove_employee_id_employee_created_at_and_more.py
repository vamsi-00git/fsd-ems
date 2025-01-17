# Generated by Django 5.1.4 on 2024-12-18 13:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_alter_employee_designation_alter_employee_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AddField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='employee',
            name='unique_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
