# Generated by Django 4.2 on 2024-02-15 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="star",
            name="slug",
            field=models.SlugField(max_length=155, unique_for_date="created_at"),
        ),
    ]
