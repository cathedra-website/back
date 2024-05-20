import os

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.text import slugify
from unidecode import unidecode

from backend.settings import DEFAULT_SCIENTIFIC_WORK_IMAGE_PATH
from employees.models import Employee


class CustomArrayField(ArrayField):
    def to_python(self, value: list[str]):
        value = value[0].split(';')
        try:
            value.remove('')
        except:
            pass
        return value


class ScientificWorkType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва типу наукових робіт", default='Підручники')
    slug = models.SlugField(max_length=255, verbose_name="Слаг", allow_unicode=True)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(unidecode(self.name), allow_unicode=True)
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = 'Тип наукових робіт'
        verbose_name_plural = 'Типи наукових робіт'
        constraints = (models.UniqueConstraint(fields=('name',), name='worktype_name_unique_constraint'),
                       models.UniqueConstraint(fields=('slug',), name='worktype_slug_unique_constraint'))
        indexes = (models.Index(fields=('name',), name='worktype_name_index'),
                   models.Index(fields=('slug',), name='worktype_slug_index'))

    def __str__(self):
        return f"Тип наукових робіт {self.name}"


class ScientificWork(models.Model):
    name = models.CharField(max_length=512, verbose_name="Назва наукової роботи")
    publishing_house = models.CharField(max_length=512, verbose_name="Видавництво")
    size = models.PositiveSmallIntegerField(verbose_name="Кількість сторінок")
    language = models.CharField(max_length=100, default='українська', verbose_name="Мова")
    isbn = models.CharField(max_length=17, validators=[RegexValidator(
        regex=r'^\d{3}-\d{3}-\d{3}-\d{3}-\d$',
        message='ISBN повинен мати формат XXX-XXX-XXX-XXX-X',
        code='invalid_format'
    )], verbose_name="ISBN")
    image = models.ImageField(verbose_name="Обкладинка наукової роботи", upload_to='scientific_work_images', null=True,
                              blank=True, default=DEFAULT_SCIENTIFIC_WORK_IMAGE_PATH)
    file = models.FileField(verbose_name='Вміст наукової роботи', upload_to='scientific_work_files', null=True, blank=True)
    type = models.ForeignKey(
        to=ScientificWorkType,
        on_delete=models.SET_NULL,
        related_name="scientific_works",
        related_query_name="scientific_work",
        null=True,
        verbose_name="Тип наукової роботи"
    )
    workers = models.ManyToManyField(to=Employee,
                                     related_name="scientific_works",
                                     related_query_name="scientific_work",
                                     verbose_name="Автори роботи(Співробітники кафедри)",
                                     blank=True)
    coworkers = CustomArrayField(models.CharField(max_length=100), blank=True, default=list,
                           verbose_name="Автори роботи(інші)")
    description = models.TextField(max_length=10000, verbose_name="Опис наукової роботи", blank=True)

    class Meta:
        verbose_name = 'Наукова робота'
        verbose_name_plural = 'Наукові роботи'
        constraints = (models.UniqueConstraint(fields=('isbn',), name='scientific_work_isbn_unique_constraint'),
                       models.UniqueConstraint(fields=('name',), name='scientific_work_name_unique_constraint'))
        indexes = (models.Index(fields=('name',), name='scientific_work_name_index'),)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.image:
            self.image.name = DEFAULT_SCIENTIFIC_WORK_IMAGE_PATH

        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f"{self.name}(ISBN:{self.isbn})"
