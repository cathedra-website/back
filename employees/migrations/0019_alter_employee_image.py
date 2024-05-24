# Generated by Django 5.0.6 on 2024-05-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employees", "0018_alter_employee_image"),
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
