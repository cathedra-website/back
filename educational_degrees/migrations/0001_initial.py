# Generated by Django 5.0.4 on 2024-04-23 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalDegreeDetailsFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='educational_degrees_files/', verbose_name='Файл')),
                ('name', models.CharField(max_length=255, verbose_name='Назва файла')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Файл опису наукового ступіня',
                'verbose_name_plural': 'Файли опису наукового ступіня',
            },
        ),
        migrations.CreateModel(
            name='EducationalDegreeDisciplineProgramsFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='educational_degrees_files/', verbose_name='Файл')),
                ('name', models.CharField(max_length=255, verbose_name='Назва файла')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Файл освітньої дисциплини',
                'verbose_name_plural': 'Файли освітніх дисциплин',
            },
        ),
        migrations.CreateModel(
            name='EducationalDegreeQualificationWorksFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='educational_degrees_files/', verbose_name='Файл')),
                ('name', models.CharField(max_length=255, verbose_name='Назва файла')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Файл кваліфікаційної роботи',
                'verbose_name_plural': 'Файли кваліфікаційних робіт',
            },
        ),
        migrations.CreateModel(
            name='EducationalDegreeStudyPlansFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='educational_degrees_files/', verbose_name='Файл')),
                ('name', models.CharField(max_length=255, verbose_name='Назва файла')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Файл навчального плану',
                'verbose_name_plural': 'Файли навчальних планів',
            },
        ),
        migrations.CreateModel(
            name='EducationalDegreeStudyProgramsFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='educational_degrees_files/', verbose_name='Файл')),
                ('name', models.CharField(max_length=255, verbose_name='Назва файла')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Файл освітньої програми',
                'verbose_name_plural': 'Файли освітніх програм',
            },
        ),
        migrations.CreateModel(
            name='EducationalDegree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва освітнього ступіня')),
                ('description', models.TextField(verbose_name='Опис освітнього ступіня')),
                ('slug', models.SlugField(allow_unicode=True, max_length=300, verbose_name='Слаг')),
                ('detailed_info', models.ManyToManyField(to='educational_degrees.educationaldegreedetailsfiles')),
                ('disciplines_programs', models.ManyToManyField(to='educational_degrees.educationaldegreedisciplineprogramsfiles')),
                ('qualification_works', models.ManyToManyField(to='educational_degrees.educationaldegreequalificationworksfiles')),
                ('study_plans', models.ManyToManyField(to='educational_degrees.educationaldegreestudyplansfiles')),
                ('study_programs_desc', models.ManyToManyField(to='educational_degrees.educationaldegreestudyprogramsfiles')),
            ],
            options={
                'verbose_name': 'Освітній ступінь',
                'verbose_name_plural': 'Освітні ступіні',
                'indexes': [models.Index(fields=['slug'], name='educational_degree_slug_index')],
            },
        ),
        migrations.AddConstraint(
            model_name='educationaldegree',
            constraint=models.UniqueConstraint(fields=('name',), name='educational_degree_name_unique_constraint'),
        ),
        migrations.AddConstraint(
            model_name='educationaldegree',
            constraint=models.UniqueConstraint(fields=('slug',), name='educational_degree_slug_unique_constraint'),
        ),
    ]
