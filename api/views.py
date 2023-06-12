from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from rest_framework import viewsets, permissions, mixins, generics

import viewer
from api.serializers import MovieSerializer, PersonSerializer, CommentSerializer
from viewer.models import Movie, Person, Genre, Comment

# Create your views here.
"""
class Movies(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]
"""


class Movies(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Movie(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class Persons(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Person(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




"""
class Actors(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    #queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_queryset(self):
        persons_list = viewer.models.Person.objects.all()
        actors_list = []
        for person in persons_list:
            if viewer.models.Movie.objects.filter(actors=person).count() > 0:
                actors_list.append(person)
        return actors_list

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
"""

"""
class Actors(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    persons_list = viewer.models.Person.objects.all()
    actors_list = []
    for person in persons_list:
        if viewer.models.Movie.objects.filter(actors=person).count() > 0:
            actors_list.append(person)
    queryset = actors_list
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
"""

class Actors(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        persons_list = viewer.models.Person.objects.all()
        actors_list = []
        for person in persons_list:
            if viewer.models.Movie.objects.filter(actors=person).count() > 0:
                actors_list.append(person)
        return actors_list

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ActionMovies(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # genre = Genre.objects.get(name="Akční")
    # queryset = viewer.models.Movie.objects.filter(genre=genre)
    serializer_class = MovieSerializer

    def get_queryset(self):
        genre = Genre.objects.get(name="Akční")
        return viewer.models.Movie.objects.filter(genre=genre)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Comments(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)