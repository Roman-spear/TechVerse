# Generated by Django 5.2.4 on 2025-07-04 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0040_canonical_detail_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='aidetail',
            name='service_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
