# Generated by Django 5.0.6 on 2024-05-20 16:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employees", "0011_remove_scientificwork_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="image",
            field=models.ImageField(
                blank=True,
                default="employee_images\\default_avatar.jpg",
                upload_to="employee_images/",
                verbose_name="Фото",
            ),
        ),
    ]
