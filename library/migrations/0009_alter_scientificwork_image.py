# Generated by Django 5.0.6 on 2024-05-24 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_scientificwork_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scientificwork',
            name='image',
            field=models.ImageField(blank=True, default='scientific_work_images/default_image.jpg', null=True, upload_to='scientific_work_images', verbose_name='Обкладинка наукової роботи'),
        ),
    ]