# Generated by Django 5.0.6 on 2024-05-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("educational_degrees", "0010_educationaldegreestudyprogramsfiles_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="educationaldegreedetailsfiles",
            options={
                "verbose_name": "Файл детальної інформації при науковий ступінь",
                "verbose_name_plural": "Файли детальної інформації при наукові ступені",
            },
        ),
        migrations.AlterModelOptions(
            name="educationaldegreestudyprogramsfiles",
            options={
                "verbose_name": "Файл опису освітньої програми",
                "verbose_name_plural": "Файли опису освітніх програм",
            },
        ),
        migrations.AlterModelOptions(
            name="subject",
            options={
                "verbose_name": "Навчальна дисципліна",
                "verbose_name_plural": "Навчальні дисципліни",
            },
        ),
        migrations.AlterField(
            model_name="educationaldegree",
            name="detailed_info",
            field=models.ManyToManyField(
                blank=True,
                related_name="detailed_info_files",
                related_query_name="detailed_info_file",
                to="educational_degrees.educationaldegreedetailsfiles",
                verbose_name="Детальна інформація про освітній ступінь",
            ),
        ),
    ]
