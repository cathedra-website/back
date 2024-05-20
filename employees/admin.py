import json

from django.contrib import admin
from django.db import models
from django.forms import Textarea
from django.utils.safestring import mark_safe

from .models import Position, Employee, TeachDiscipline, CustomArrayField


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    fields = ("name",)
    list_display = ('name',)
    list_per_page = 10
    search_fields = ('name',)


@admin.register(TeachDiscipline)
class TeachDisciplineAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'time_created', 'time_last_modified')
    readonly_fields = ('time_created', 'time_last_modified')
    list_display = ('name', 'short_description')
    search_fields = ('name',)
    list_per_page = 10

    @staticmethod
    @admin.display(description="Опис")
    def short_description(discipline: TeachDiscipline):
        return f"{discipline.description[:20]}..."


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
        CustomArrayField: {'widget': Textarea(attrs={'rows': 4})}
    }
    save_on_top = True

    def default_links_value(self, employee: Employee):
        default_links_value = self.model._meta.get_field('links').get_default()
        return mark_safe(f'<pre>{json.dumps(default_links_value, indent=4)}</pre>')

    fields = ('last_name', 'first_name', 'middle_name', 'degree_history', 'position', 'teach_disciplines', 'email',
              'ranks', 'links', 'study_interests',
              'diploma_work_topics', 'awards', 'chosen_publications', 'image', 'employee_photo',
              'time_created', 'time_last_modified', 'slug',)
    list_display = ('full_name', 'employee_photo')
    #  add 'chosen_publications' as many-to-many field between employee and scientific work;
    # format view of image field in admin panel;
    # format view of teach_disciplines in admin_panel;

    readonly_fields = ('slug', 'time_created', 'time_last_modified', 'employee_photo', 'full_name')
    ordering = ('position', 'time_last_modified')
    list_filter = ('position__name',)
    search_fields = ('last_name', 'first_name', 'middle_name', 'email', 'slug')
    filter_horizontal = ('teach_disciplines',)

    @admin.display(description='Зображення')
    def employee_photo(self, employee: Employee):
        return mark_safe(f"<img src='{employee.image.url}' width=50>") if employee.image else 'Без фото'

    @admin.display(description='ПІБ')
    def full_name(self, employee: Employee):
        return f'{employee.last_name} {employee.first_name} {employee.middle_name}'
