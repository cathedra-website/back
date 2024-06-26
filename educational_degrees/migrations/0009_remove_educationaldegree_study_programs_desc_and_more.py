# Generated by Django 5.0.6 on 2024-05-24 10:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("educational_degrees", "0008_alter_qualificationwork_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="educationaldegree",
            name="study_programs_desc",
        ),
        migrations.AlterModelOptions(
            name="educationaldegreedetailsfiles",
            options={
                "verbose_name": "Файл опису освітньої програми",
                "verbose_name_plural": "Файли опису освітніх програм",
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
                verbose_name="Описи освітньої програми",
            ),
        ),
        migrations.DeleteModel(
            name="EducationalDegreeStudyProgramsFiles",
        ),
    ]
