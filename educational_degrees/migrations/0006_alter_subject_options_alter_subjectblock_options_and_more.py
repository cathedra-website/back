# Generated by Django 5.0.4 on 2024-05-20 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_degrees', '0005_educationaldegreedisciplineprograms_subject_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Навчальна дисциплина', 'verbose_name_plural': 'Навчальні дисциплини'},
        ),
        migrations.AlterModelOptions(
            name='subjectblock',
            options={'verbose_name': 'Блок навчальних дисциплин', 'verbose_name_plural': 'Блоки навчальних дисциплин'},
        ),
        migrations.AlterField(
            model_name='educationaldegreedisciplineprograms',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='subjects_disciplines', related_query_name='disciplines_subjects', to='educational_degrees.subject', verbose_name='Навчальні дисциплини'),
        ),
    ]
