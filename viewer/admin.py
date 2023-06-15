from django.contrib import admin
from django.contrib.admin import ModelAdmin

from viewer.models import Country, Person, Movie, Genre, Rating, Comment


class MovieAdmin(ModelAdmin):
    fieldsets = [
        (
            'General information',
            {
                'fields': ['title', 'title_cz']
            }
        ),
        (
            'External Information',
            {
                'fields': ['genre', 'year', 'country', 'language', 'length', 'image_url', 'image'],
                'description': (
                    'These fields are going to be filled with data parsed '
                    'from external databases.'
                )
            }
        ),
        (
            'Persons',
            {
                'fields': ['actors', 'directors'],
            }
        ),
        (
            'User Information',
            {
                'fields': ['pg_rating', 'description'],
                'description': 'These fields are intended to be filled in by our users.'
            }
        )
    ]
    readonly_fields = ['created']

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description=None)

    ordering = ['year', 'id']
    list_display = ['year', 'id', 'title']
    list_display_links = ['title']
    list_per_page = 20
    list_filter = ['genre', 'country']
    search_fields = ['title', 'title_cz']
    actions = ['cleanup_description']


class PersonAdmin(ModelAdmin):

    @staticmethod
    def show_sex(obj):
        if obj.sex is None:
            return 'Unknown'
        if obj.sex:
            return 'Female'
        if not obj.sex:
            return 'Male'
        return 'Unknown'

    list_display = ['first_name', 'last_name', 'show_sex']

    fieldsets = [
        ('General information',
         {
             'fields': ['first_name', 'last_name', 'birth_date', 'sex', 'country']  # TODO - sex = Female/Male
         }
         )
    ]


# Register your models here.
admin.site.register(Country)
admin.site.register(Person, PersonAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Comment)



