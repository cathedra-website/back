from django.contrib import admin
from django.contrib.postgres.fields import ArrayField
from django.forms import Textarea
from django.utils.safestring import mark_safe

from library.models import ScientificWork, ScientificWorkType


@admin.register(ScientificWorkType)
class ScientificWorkTypeAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    list_display = ('name', )
    readonly_fields = ('slug',)
    list_per_page = 10
    search_fields = ('name', )


@admin.register(ScientificWork)
class ScientificWorkAdmin(admin.ModelAdmin):
    fields = ('name', 'publishing_house', 'size', 'language', 'isbn', 'type', 'workers', 'coworkers', 'description', 'file', 'image', 'title')
    list_display = ('name', 'isbn', 'size', 'title')
    save_on_top = True
    search_fields = ('name', 'isbn')
    list_per_page = 10
    readonly_fields = ('title',)
    list_filter = ('type__name',)
    formfield_overrides = {
        ArrayField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})}
    }
    filter_horizontal = ('workers',)

    @admin.display(description='Обкладинка')
    def title(self, scientific_work: ScientificWork):
        return mark_safe(f"<img src='{scientific_work.image.url}' width=50>") if scientific_work.image else 'Без обкладинки'
