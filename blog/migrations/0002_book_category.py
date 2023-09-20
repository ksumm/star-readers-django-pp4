# Generated by Django 3.2.20 on 2023-09-17 13:24

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_name', models.CharField(max_length=50)),
                ('age_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('slug', models.SlugField(max_length=500, unique=True)),
            ],
            options={
                'db_table': 'age_range',
            },
        ),
    ]