# Generated by Django 2.1.4 on 2018-12-27 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_resource_resource_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.Resource')),
            ],
            bases=('books.resource',),
        ),
    ]