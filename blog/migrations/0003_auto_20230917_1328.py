# Generated by Django 3.2.20 on 2023-09-17 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_book_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book_Category',
            new_name='age_range',
        ),
        migrations.AddField(
            model_name='post',
            name='age_range',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='age', to='blog.age_range'),
        ),
    ]
