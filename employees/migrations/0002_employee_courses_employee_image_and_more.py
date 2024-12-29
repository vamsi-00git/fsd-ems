# Generated by Django 5.1.4 on 2024-12-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='courses',
            field=models.CharField(default='No Course Assigned', max_length=255),
        ),
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='employee_images/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(choices=[('Developer', 'Developer'), ('Manager', 'Manager'), ('HR', 'HR')], max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]
