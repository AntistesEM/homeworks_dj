# Generated by Django 4.2.2 on 2023-06-17 09:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("advertisements", "0004_favorite_test"),
    ]

    operations = [
        migrations.RenameField(
            model_name="favorite",
            old_name="favorites",
            new_name="advertisement",
        ),
    ]
