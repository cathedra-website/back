# Generated by Django 5.0.4 on 2024-05-19 20:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_degrees', '0004_educationaldegreequalificationworks_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalDegreeDisciplinePrograms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=255, verbose_name='Рік')),
                ('slug', models.SlugField(allow_unicode=True, max_length=300, verbose_name='Слаг')),
                ('degree_name', models.CharField(max_length=255, verbose_name='Назва освітнього ступеня')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Програма навчальної дисциплини ',
                'verbose_name_plural': 'Програми навчальних дисциплин ',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('semester', models.IntegerField(verbose_name='Номер семестру')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Скорочена назва блоку')),
                ('full_name', models.CharField(max_length=255, verbose_name='Повна назва блоку')),
            ],
        ),
        migrations.DeleteModel(
            name='EducationalDegreeDisciplineProgramsFiles',
        ),
        migrations.AlterField(
            model_name='educationaldegree',
            name='disciplines_programs',
            field=models.ManyToManyField(blank=True, related_name='disciplines_programs_lists', related_query_name='discipline_program_list', to='educational_degrees.educationaldegreedisciplineprograms', verbose_name='Програми навчальних дисциплін'),
        ),
        migrations.AddField(
            model_name='educationaldegreedisciplineprograms',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='qualification_works', related_query_name='qualification_work', to='educational_degrees.subject', verbose_name='Кваліфікаційні роботи'),
        ),
        migrations.AddField(
            model_name='subject',
            name='block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='block_subject', related_query_name='subject_block', to='educational_degrees.subjectblock', verbose_name='Блок навчальної дисциплини'),
        ),
    ]