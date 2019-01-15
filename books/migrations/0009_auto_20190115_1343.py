# Generated by Django 2.1.4 on 2019-01-15 04:43

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_monitor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=books.models.Resource.get_image_path),
        ),
    ]
