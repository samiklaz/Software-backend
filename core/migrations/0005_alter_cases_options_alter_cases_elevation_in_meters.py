# Generated by Django 4.0.3 on 2022-03-28 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_cases_lat_alter_cases_long'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cases',
            options={'verbose_name_plural': 'Cases'},
        ),
        migrations.AlterField(
            model_name='cases',
            name='elevation_in_meters',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]