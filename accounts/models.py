from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, OneToOneField, CASCADE, TextField


# class User(User):
#
#     def __str__(self):
#         return f"{self.username}"
#
#     def has_profile(self):
#         return Profile.objects.filter(user=self).exists()


# Create your models here.
class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    biography = TextField()

    def __str__(self):
        return f"{self.user.username}"
