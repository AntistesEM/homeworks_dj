# Generated by Django 4.2.1 on 2023-06-03 18:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("measurement", "0005_alter_measurement_options_alter_sensor_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="measurement",
            options={"verbose_name": "Измерение", "verbose_name_plural": "Измерения"},
        ),
        migrations.AlterModelOptions(
            name="sensor",
            options={"verbose_name": "Датчик", "verbose_name_plural": "Датчики"},
        ),
        migrations.RemoveField(
            model_name="measurement",
            name="photo",
        ),
        migrations.AlterField(
            model_name="measurement",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="sensor",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="sensor",
            name="name",
            field=models.CharField(max_length=50),
        ),
    ]
