# Generated by Django 5.0.2 on 2025-06-05 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0026_industrycategory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecategory',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='service_category_image'),
        ),
    ]
