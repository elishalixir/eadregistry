# Generated by Django 4.0.1 on 2022-01-21 20:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0005_remove_finalcopy_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalcopy',
            name='admin_upload',
            field=models.FileField(default=django.utils.timezone.now, upload_to='media'),
            preserve_default=False,
        ),
    ]