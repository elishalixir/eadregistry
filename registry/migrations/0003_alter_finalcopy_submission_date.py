# Generated by Django 4.0.1 on 2022-01-21 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0002_rename_location_finalcopy_project_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalcopy',
            name='Submission_date',
            field=models.DateField(),
        ),
    ]