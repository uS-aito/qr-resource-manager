# Generated by Django 2.1.4 on 2018-12-27 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20181227_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='resource_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
