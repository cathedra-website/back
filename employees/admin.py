from django.contrib import admin


from .models import Position, Employee, TeachDiscipline, ScientificWorkType, ScientificWork


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    fields = ("name",)
    list_display = ('name',)
    list_per_page = 10
    search_fields = ('name',)


@admin.register(ScientificWorkType)
class ScientificWorkTypeAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    list_display = ('name', )
    readonly_fields = ('slug',)
    list_per_page = 10
    search_fields = ('name', )


@admin.register(TeachDiscipline)
class TeachDisciplineAdmin(admin.ModelAdmin):

    fields = ('name', 'description', 'time_created', 'time_last_modified')
    readonly_fields = ('time_created', 'time_last_modified')
    list_display = ('name', 'short_description')
    search_fields = ('name',)
    @staticmethod
    @admin.display(description="Опис")
    def short_description(discipline: TeachDiscipline):
        return f"{discipline.description[:20]}..."


@admin.register(ScientificWork)
class ScientificWorkAdmin(admin.ModelAdmin):
    fields = ('name', 'publishing_house', 'size', 'language', 'isbn', 'type', 'workers', 'coworkers', 'description')
    list_display = ('name', 'size')
    list_editable = ('size',)
    save_on_top = True
    search_fields = ('name', 'isbn')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ('last_name', 'first_name', 'middle_name', 'email',
              'ranks', 'links', 'degree_history', 'study_interests',
              'diploma_work_topics', 'position', 'awards',
              'time_created', 'time_last_modified', 'slug')
    readonly_fields = ('slug', 'time_created', 'time_last_modified')
