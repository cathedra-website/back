# Generated by Django 5.0.4 on 2024-05-20 11:57

import employees.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employees", "0008_remove_teachdiscipline_discipline_name_unique_constraint"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="awards",
            field=employees.models.CustomArrayField(
                base_field=models.TextField(max_length=1024),
                blank=True,
                default=list,
                size=None,
                verbose_name="Академічні нагороди та премії",
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="chosen_publications",
            field=employees.models.CustomArrayField(
                base_field=models.TextField(max_length=1024),
                blank=True,
                default=list,
                size=None,
                verbose_name="Вибрані публікації",
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="employee_images/", verbose_name="Фото"
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="ranks",
            field=employees.models.CustomArrayField(
                base_field=models.TextField(max_length=1024),
                blank=True,
                default=list,
                size=None,
                verbose_name="Наукові ступені",
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="study_interests",
            field=employees.models.CustomArrayField(
                base_field=models.TextField(max_length=1024),
                blank=True,
                default=list,
                size=None,
                verbose_name="Сфера наукових інтересів",
            ),
        ),
        migrations.AlterField(
            model_name="scientificwork",
            name="coworkers",
            field=employees.models.CustomArrayField(
                base_field=models.CharField(max_length=100),
                blank=True,
                default=list,
                size=None,
                verbose_name="Автори роботи(інші)",
            ),
        ),
    ]
