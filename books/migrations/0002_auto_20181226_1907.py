# Generated by Django 2.1.4 on 2018-12-26 10:07

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=200)),
                ('resource_image', models.ImageField(upload_to=books.models.Resource.get_image_path)),
                ('resource_checkout_date', models.DateField()),
                ('resource_return_date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='choise',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choise',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]