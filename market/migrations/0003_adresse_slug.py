# Generated by Django 4.2.17 on 2024-12-16 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("market", "0002_alter_service_options_adresse"),
    ]

    operations = [
        migrations.AddField(
            model_name="adresse",
            name="slug",
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
