from django.core.validators import RegexValidator
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.text import slugify

from files.models import File


# TODO: Have to be changed to the view of the JSON
def links_default():
    """Default json style for Employee.links"""
    return {}


class Position(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва наукового звання')

    class Meta:
        verbose_name = 'Наукове звання'
        verbose_name_plural = 'Наукові звання'
        constraints = [models.UniqueConstraint(fields=('name',), name='name_unique_constraint')]
        indexes = (models.Index(fields=('name',), name='name_index'),)

    def __str__(self):
        return f"Наукове звання {self.name}"


class Employee(models.Model):
    last_name = models.CharField(blank=False, max_length=100, verbose_name="Прізвище")
    first_name = models.CharField(blank=False, max_length=100, verbose_name="Ім'я")
    middle_name = models.CharField(blank=False, max_length=100, verbose_name="По батькові")
    email = models.EmailField(verbose_name="Адреса електронної пошти", blank=True, null=True)
    ranks = ArrayField(models.CharField(max_length=255), blank=True, default=list, verbose_name="Наукові ступені")
    links = models.JSONField(default=links_default, verbose_name="Посилання", blank=True)
    degree_history = models.TextField(verbose_name="Освіта та кар'єра")
    study_interests = ArrayField(models.CharField(max_length=255), blank=True, default=list, verbose_name="Сфера "
                                                                                                          "наукових "
                                                                                                          "інтересів")
    diploma_work_topics = ArrayField(models.CharField(max_length=255), blank=True, default=list, verbose_name="Теми "
                                                                                                              "курсових та дипломних робіт")
    position = models.ForeignKey(to=Position,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name="position_employees",
                                 related_query_name="position_employee",
                                 verbose_name="Наукове звання")
    awards = ArrayField(models.CharField(max_length=512), blank=True, default=list, verbose_name="Академічні нагороди "
                                                                                                 "та премії")
    image = models.ForeignKey(to=File,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,
                              related_name="image_employees",
                              related_query_name="image_employee",
                              verbose_name="Зображення")
    chosen_publications = ArrayField(models.CharField(max_length=512), blank=True, default=list,
                                     verbose_name="Вибрані публікації")
    teach_disciplines = models.ManyToManyField(to="TeachDiscipline",
                                               related_name="discipline_employees",
                                               related_query_name="discipline_employee",
                                               verbose_name="Викладацька діяльність")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Час створення сторінки співробітника")
    time_last_modified = models.DateTimeField(auto_now=True, verbose_name="Час останньої зміни сторінки співробітника")
    slug = models.SlugField(max_length=300, verbose_name="Слаг", allow_unicode=True)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.last_name + self.first_name + self.middle_name, allow_unicode=True)
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
    # def save(self, *args, **kwargs):
    #     # TODO: Is it work?
    #     if not self.created_at and self.created_at:
    #         self.updated_at = timezone.now()
    #     super(Employee, self).save(*args, **kwargs)


class TeachDiscipline(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва наукової дисципліни")
    description = models.TextField(max_length=5000, blank=True, verbose_name="Опис наукової дисципліни")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Час і дата створення")
    time_last_modified = models.DateTimeField(auto_now=True, verbose_name="Час і дата останньої зміни")

    class Meta:
        verbose_name = 'Навчальна дисципліна'
        verbose_name_plural = 'Навчальні дисципліни'
        constraints = (models.UniqueConstraint(fields=('name',), name='discipline_name_unique_constraint'),)
        indexes = (models.Index(fields=('name',), name='discipline_name_index'),
                   )
        get_latest_by = 'time_created'
        ordering = ('-time_created',)

    def __str__(self):
        return f"Навчальна дисципліна {self.name}"


class ScientificWorkType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва типу наукових робіт", default='Підручники')
    slug = models.SlugField(max_length=255, verbose_name="Слаг", allow_unicode=True)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.name, allow_unicode=True)
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
    image = models.OneToOneField(
        to=File,
        related_name="image_scientific_work",
        related_query_name="image_scientific_work",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Зображення(титульна сторінка)"
    )
    file = models.ForeignKey(
        to=File,
        related_name="files_scientific_works",
        related_query_name="file_scientific_work",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Файловий зміст"
    )
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
    coworkers = ArrayField(models.CharField(max_length=100), blank=True, default=list,
                           verbose_name="Автори роботи(інші)")
    description = models.TextField(max_length=10000, verbose_name="Опис наукової роботи", blank=True)

    class Meta:
        verbose_name = 'Наукова робота'
        verbose_name_plural = 'Наукові роботи'
        # constraints = (models.UniqueConstraint(fields=('name',), name='name_unique_constraint'))
        # indexes = (models.Index(fields=('name',), name='name_index'))

    def __str__(self):
        return f"{self.name}(ISBN:{self.isbn})"