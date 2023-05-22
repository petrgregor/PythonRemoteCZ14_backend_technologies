from django.contrib import admin

from viewer.models import Country, Person, Movie, Genre, Rating, Comment

# Register your models here.
admin.site.register(Country)
admin.site.register(Person)
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Comment)
