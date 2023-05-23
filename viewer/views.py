from django.shortcuts import render
from django.http import HttpResponse

from viewer.models import Movie, Person, Genre, Country


# regular expression
def hello(request, s):
    return HttpResponse(f'Hello, {s} world!')


# URL encoding
def hello2(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello, {s} world!')


def hello3(request, s0):
    s1 = request.GET.get('s1', '')
    s2 = "beautiful"
    s3 = "wonderful"
    context = {'adjectives': [s0, s1, s2, s3]}
    return render(request, template_name="hello.html", context=context)


def home(request):
    return render(request, template_name='home.html')


def movies(request):
    movie_list = Movie.objects.all()
    context = {'movies': movie_list}
    return render(request, template_name='movies.html', context=context)


def actors(request):
    persons_list = Person.objects.all()
    actors_list = []
    for person in persons_list:
        if Movie.objects.filter(actors=person).count() > 0:
            actors_list.append(person)
    context = {'actors': actors_list}
    return render(request, template_name='actors.html', context=context)


def directors(request):
    persons_list = Person.objects.all()
    directors_list = []
    for person in persons_list:
        if Movie.objects.filter(directors=person).count() > 0:
            directors_list.append(person)
    context = {'directors': directors_list}
    return render(request, template_name='directors.html', context=context)


def movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    genres = Genre.objects.filter(movies=movie)
    countries = Country.objects.filter(movies=movie)
    actors = Person.objects.filter(acting_in_movies=movie)
    directors = Person.objects.filter(directing_movies=movie)
    previous_part = Movie.previous_part
    context = {'movie': movie, 'genres': genres, 'countries': countries,
               'actors': actors, 'directors': directors}
    return render(request, template_name='movie.html', context=context)


def person(request, pk):
    person = Person.objects.get(pk=pk)
    context = {'person': person}
    return render(request, template_name='person.html', context=context)
