# Generated by Django 5.0.4 on 2024-05-19 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_degrees', '0003_alter_educationaldegree_options'),
        ('employees', '0008_remove_teachdiscipline_discipline_name_unique_constraint'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalDegreeQualificationWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=255, verbose_name='Рік')),
                ('slug', models.SlugField(allow_unicode=True, max_length=300, verbose_name='Слаг')),
                ('degree_name', models.CharField(max_length=255, verbose_name='Назва освітнього ступеня')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Список кваліфікаційних робіт',
                'verbose_name_plural': 'Списки кваліфікаційних робіт',
            },
        ),
        migrations.CreateModel(
            name='QualificationWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ПІБ студента')),
                ('topic_of_work', models.CharField(verbose_name='Тема кваліфікаційної роботи')),
                ('scientific_supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='scientific_supervisors', related_query_name='scientific_supervisor', to='employees.employee', verbose_name='Науковий керівник')),
            ],
            options={
                'verbose_name': 'Кваліфікаційна робота',
                'verbose_name_plural': 'Кваліфікаційні роботи',
            },
        ),
        migrations.DeleteModel(
            name='EducationalDegreeQualificationWorksFiles',
        ),
        migrations.AlterField(
            model_name='educationaldegree',
            name='qualification_works',
            field=models.ManyToManyField(blank=True, related_name='qualification_works_lists', related_query_name='qualification_work_list', to='educational_degrees.educationaldegreequalificationworks', verbose_name='Кваліфікаційні роботи'),
        ),
        migrations.AddField(
            model_name='educationaldegreequalificationworks',
            name='qualification_work',
            field=models.ManyToManyField(blank=True, related_name='qualification_works', related_query_name='qualification_work', to='educational_degrees.qualificationwork', verbose_name='Кваліфікаційні роботи'),
        ),
    ]
