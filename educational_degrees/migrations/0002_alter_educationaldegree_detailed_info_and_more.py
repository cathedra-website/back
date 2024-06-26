# Generated by Django 5.0.4 on 2024-04-24 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_degrees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationaldegree',
            name='detailed_info',
            field=models.ManyToManyField(blank=True, related_name='detailed_info_files', related_query_name='detailed_info_file', to='educational_degrees.educationaldegreedetailsfiles', verbose_name='Описи освітнього ступіня'),
        ),
        migrations.AlterField(
            model_name='educationaldegree',
            name='disciplines_programs',
            field=models.ManyToManyField(blank=True, related_name='disciplines_programs', related_query_name='discipline_program', to='educational_degrees.educationaldegreedisciplineprogramsfiles', verbose_name='Програми навчальних дисциплін'),
        ),
        migrations.AlterField(
            model_name='educationaldegree',
            name='qualification_works',
            field=models.ManyToManyField(blank=True, related_name='qualification_works', related_query_name='qualification_work', to='educational_degrees.educationaldegreequalificationworksfiles', verbose_name='Кваліфікаційні роботи'),
        ),
        migrations.AlterField(
            model_name='educationaldegree',
            name='study_plans',
            field=models.ManyToManyField(blank=True, related_name='study_plans', related_query_name='study_plan', to='educational_degrees.educationaldegreestudyplansfiles', verbose_name='Навчальні плани'),
        ),
        migrations.AlterField(
            model_name='educationaldegree',
            name='study_programs_desc',
            field=models.ManyToManyField(blank=True, related_name='study_programs', related_query_name='study_program', to='educational_degrees.educationaldegreestudyprogramsfiles', verbose_name='Описи освітньої програми'),
        ),
    ]
