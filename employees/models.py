import os
import json
from django.contrib.admin.widgets import AdminTextInputWidget
from django.contrib.postgres.forms import SimpleArrayField
from django.core.validators import RegexValidator
from django.db import models
from django.core.files import File
from django.contrib.postgres.fields import ArrayField
from django import forms
from django.forms.fields import CharField
from django.utils.text import slugify
from rest_framework.exceptions import ValidationError
from unidecode import unidecode

from backend.settings import DEFAULT_EMPLOYEE_AVATAR_IMAGE_PATH
from files.models import File


# TODO: Have to be changed to the view of the JSON
def links_default():
    """Default json style for Employee.links"""
    return {'Scopus': ''}


class CustomArrayField(ArrayField):
    def to_python(self, value: list[str]):
        value = value[0].split(';')
        try:
            value.remove('')
        except:
            pass
        return value

# class CustomArrayField(ArrayField):
#
#     def to_python(self, value):
#         if isinstance(value, list):
#             return value
#         if isinstance(value, str):
#             try:
#                 value = value.strip('{}').split(';')
#                 return [item for item in value if item]  # remove empty strings
#             except ValueError:
#                 raise ValidationError("Invalid input for an array field")
#         return super().to_python(value)
#
#     def get_prep_value(self, value):
#         if isinstance(value, list):
#             return '{' + ';'.join(value) + '}'
#         return super().get_prep_value(value)


class Position(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва наукового звання')

    class Meta:
        verbose_name = 'Наукове звання'
        verbose_name_plural = 'Наукові звання'
        constraints = [models.UniqueConstraint(fields=('name',), name='name_unique_constraint')]
        indexes = (models.Index(fields=('name',), name='name_index'),)

    def __str__(self):
        return f"Наукове звання {self.name}"


class TeachDiscipline(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва наукової дисципліни")
    description = models.TextField(max_length=5000, blank=True, verbose_name="Опис наукової дисципліни")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Час і дата створення")
    time_last_modified = models.DateTimeField(auto_now=True, verbose_name="Час і дата останньої зміни")

    class Meta:
        verbose_name = 'Навчальна дисципліна'
        verbose_name_plural = 'Навчальні дисципліни'
        indexes = (models.Index(fields=('name',), name='discipline_name_index'),
                   )
        get_latest_by = 'time_created'
        ordering = ('-time_created',)

    def __str__(self):
        return f"Навчальна дисципліна {self.name}"


class Employee(models.Model):
    last_name = models.CharField(blank=False, max_length=100, verbose_name="Прізвище")
    first_name = models.CharField(blank=False, max_length=100, verbose_name="Ім'я")
    middle_name = models.CharField(blank=False, max_length=100, verbose_name="По батькові")
    email = models.EmailField(verbose_name="Адреса електронної пошти", blank=True, null=True)
    ranks = ArrayField(base_field=models.TextField(max_length=1024), blank=True, default=list, verbose_name="Наукові ступені")
    links = models.JSONField(default=links_default, verbose_name="Посилання", blank=True)
    degree_history = models.TextField(verbose_name="Освіта та кар'єра")
    study_interests = ArrayField(models.TextField(max_length=1024), blank=True, default=list, verbose_name="Сфера "
                                                                                                          "наукових "
                                                                                                          "інтересів")
    diploma_work_topics = ArrayField(models.CharField(max_length=1024), blank=True, default=list, verbose_name="Теми "
                                                                                                              "курсових та дипломних робіт")
    position = models.ForeignKey(to=Position,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name="position_employees",
                                 related_query_name="position_employee",
                                 verbose_name="Наукове звання")
    awards = ArrayField(models.TextField(max_length=1024), blank=True, default=list, verbose_name="Академічні нагороди "
                                                                                                 "та премії")

    image = models.ImageField(upload_to='employee_images/', blank=True,
                              verbose_name='Фото', default=DEFAULT_EMPLOYEE_AVATAR_IMAGE_PATH)
    chosen_publications = ArrayField(models.TextField(max_length=1024), blank=True, default=list,
                                     verbose_name="Вибрані публікації")
    teach_disciplines = models.ManyToManyField(to=TeachDiscipline,
                                               related_name="discipline_employees",
                                               related_query_name="discipline_employee",
                                               verbose_name="Викладацька діяльність",
                                               blank=True)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Час створення сторінки співробітника")
    time_last_modified = models.DateTimeField(auto_now=True, verbose_name="Час останньої зміни сторінки співробітника")
    slug = models.SlugField(max_length=300, verbose_name="Слаг", allow_unicode=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        cyrillic_name = f"{self.last_name}-{self.first_name}-{self.middle_name}"
        latinic_name = unidecode(cyrillic_name)
        self.slug = slugify(latinic_name, allow_unicode=True)
        if not self.image:
            self.image.name = DEFAULT_EMPLOYEE_AVATAR_IMAGE_PATH

        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = "Співробітник кафедри"
        verbose_name_plural = "Співробітники кафедри"
        get_latest_by = 'time_created'
        constraints = (models.UniqueConstraint(fields=('first_name', 'last_name', 'middle_name'),
                                               name='employee_fullname_unique_constraint'),
                       models.UniqueConstraint(fields=('email',), name='employee_email_unique_constraint'),
                       models.UniqueConstraint(fields=('slug',), name='employee_slug_unique_constraint')
                       )
        indexes = (models.Index(fields=('slug',), name='employee_slug_index'),
                   )
        ordering = ('-time_created',)

    def __str__(self):
        return f"Співробітник {self.last_name} {self.first_name} {self.middle_name}"


