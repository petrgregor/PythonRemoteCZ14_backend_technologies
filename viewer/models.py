from django.db import models
from django.db.models import Model, CharField


class Country(Model):
    name = CharField(max_length=32)
    abbreviation = CharField(max_length=3)
