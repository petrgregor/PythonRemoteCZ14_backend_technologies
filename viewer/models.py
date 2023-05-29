from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, CharField, DateField, BooleanField, ForeignKey, SET_NULL, DateTimeField, \
    PositiveIntegerField, TextField, CASCADE, ManyToManyField


class Country(Model):
    name = CharField(max_length=32, unique=True)
    abbreviation = CharField(max_length=3, unique=True)

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['name']

    def __str__(self):
        return self.name + " (" + self.abbreviation + ")"


class Person(Model):
    first_name = CharField(max_length=32, null=True)
    last_name = CharField(max_length=32, null=True)
    birth_date = DateField(null=True)
    sex = BooleanField(null=True)  # M=0, F=1
    country = ForeignKey(Country, null=True, on_delete=SET_NULL)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return self.first_name + " " + self.last_name


class Genre(Model):
    name = CharField(max_length=32)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Movie(Model):
    title = CharField(max_length=64, null=False)
    title_cz = CharField(max_length=64, null=True)
    year = PositiveIntegerField(null=True)
    genre = ManyToManyField(Genre, related_name='movies')
    country = ManyToManyField(Country, related_name='movies')
    actors = ManyToManyField(Person, related_name='acting_in_movies')
    directors = ManyToManyField(Person, related_name='directing_movies')
    description = TextField(null=True)
    language = CharField(max_length=32)
    series = BooleanField(null=True)
    pg_rating = PositiveIntegerField(null=True)
    length = PositiveIntegerField(null=True)
    previous_part = ForeignKey("Movie", null=True, blank=True, on_delete=SET_NULL)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title', 'year']

    def __str__(self):
        return f"{self.title} ({self.year})"


class Rating(Model):
    movie = ForeignKey(Movie, null=False, on_delete=CASCADE, related_name='movie_rating')
    user = ForeignKey(User, null=True, on_delete=SET_NULL, related_name='user_rating')
    rating = PositiveIntegerField(null=False)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['movie', 'user']

    def __str__(self):
        return f"{self.movie.title} - {self.user.username} ({self.rating})"


class Comment(Model):
    movie = ForeignKey(Movie, null=False, on_delete=CASCADE, related_name='movie_comment')
    user = ForeignKey(User, null=False, on_delete=CASCADE, related_name='user_comment')
    comment = TextField(null=False)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['movie', 'user']

    def __str__(self):
        return f"{self.movie.title} - {self.user.username}: {self.comment[:50]}"
