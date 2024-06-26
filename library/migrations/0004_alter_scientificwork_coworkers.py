# Generated by Django 5.0.6 on 2024-05-21 12:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0003_alter_scientificwork_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scientificwork",
            name="coworkers",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=100),
                blank=True,
                default=list,
                size=None,
                verbose_name="Автори роботи(інші)",
            ),
        ),
    ]
