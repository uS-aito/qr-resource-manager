# Generated by Django 2.1.4 on 2019-01-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20190116_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='username',
        ),
        migrations.AddField(
            model_name='resource',
            name='username',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
