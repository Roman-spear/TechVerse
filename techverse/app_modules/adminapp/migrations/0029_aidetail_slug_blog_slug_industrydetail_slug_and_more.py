# Generated by Django 5.2.1 on 2025-06-18 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0028_aiservices'),
    ]

    operations = [
        migrations.AddField(
            model_name='aidetail',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='industrydetail',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
