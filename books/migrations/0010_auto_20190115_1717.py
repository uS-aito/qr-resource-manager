# Generated by Django 2.1.4 on 2019-01-15 08:17

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20190115_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='image',
            field=models.ImageField(blank=True, default='/Users/saitoy55/git/13Flabo/django-projects/qrbook/media/no_image.png', null=True, upload_to=books.models.Resource.get_image_path),
        ),
    ]
