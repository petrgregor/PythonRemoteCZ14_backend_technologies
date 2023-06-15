from datetime import datetime, date

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Avg
from django.forms import Form, CharField, ModelForm, DateField, DateInput
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView

from accounts.models import Profile
from viewer.models import Movie, Person, Genre, Country, Rating, Comment


# regular expression
@login_required
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
    genres = Genre.objects.all()
    context = {'movies': movie_list, 'genres': genres}
    return render(request, template_name='movies.html', context=context)


"""
# Class-based view - verze pomocí metody
class MoviesView(View):
    def get(self, request):
        movie_list = Movie.objects.all()
        genres = Genre.objects.all()
        context = {'movies': movie_list, 'genres': genres}
        return render(request, template_name='movies.html', context=context)
"""


# Class-based view - verze pomocí TemplateView
class MoviesView(TemplateView):
    template_name = 'movies.html'
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    extra_context = {'movies': movies, 'genres': genres}


"""
# Class-based view - verze pomocí ListView
class MoviesView2(ListView):
    template_name = 'movies.html'
    model = Movie
"""


def movies_by_length(request, order):
    movies = Movie.objects.all().order_by('length')
    if order == 'desc':
        movies = Movie.objects.all().order_by('-length')
    context = {'movies': movies}
    return render(request, template_name='movies_by_length.html', context=context)


def movies_by_year(request, order):
    movies = Movie.objects.all().order_by('year')
    if order == 'desc':
        movies = Movie.objects.all().order_by('-year')
    genres = Genre.objects.all()
    context = {'movies': movies, 'genres': genres}
    return render(request, template_name='movies.html', context=context)


def actors(request):
    persons_list = Person.objects.all()
    actors_list = []
    for person in persons_list:
        if Movie.objects.filter(actors=person).count() > 0:
            actors_list.append(person)
    context = {'actors': actors_list}
    return render(request, template_name='actors.html', context=context)


# Class-based view - TemplateView
class ActorsView(TemplateView):
    template_name = 'actors.html'
    persons_list = Person.objects.all()
    actors_list = []
    for person in persons_list:
        if Movie.objects.filter(actors=person).count() > 0:
            actors_list.append(person)
    extra_context = {'actors': actors_list}


def directors(request):
    persons_list = Person.objects.all()
    directors_list = []
    for person in persons_list:
        if Movie.objects.filter(directors=person).count() > 0:
            directors_list.append(person)
    context = {'directors': directors_list}
    return render(request, template_name='directors.html', context=context)


# Class-based view - TemplateView
class DirectorsView(TemplateView):
    template_name = 'directors.html'
    persons_list = Person.objects.all()
    directors_list = []
    for person in persons_list:
        if Movie.objects.filter(directors=person).count() > 0:
            directors_list.append(person)
    extra_context = {'directors': directors_list}


def movie(request, pk):
    movie = Movie.objects.get(id=pk)
    genres = Genre.objects.filter(movies=movie)
    countries = Country.objects.filter(movies=movie)
    actors = Person.objects.filter(acting_in_movies=movie)
    directors = Person.objects.filter(directing_movies=movie)
    previous_part = Movie.previous_part
    user = request.user
    rating = None
    if user.is_authenticated and Rating.objects.filter(movie=movie, user=user).count() > 0:
        user_rating = Rating.objects.get(movie=movie, user=user)
        rating = user_rating.rating

    # průměrné hodnocení
    avg_rating = Rating.objects.filter(movie=movie).aggregate(Avg('rating'))

    if request.method == 'POST':
        new_comment = request.POST.get('comment')

        # první varianta aktualizace komentáře
        """
        if Comment.objects.filter(movie=movie, user=user).count() > 0:  # pokud již komentář existuje
            user_comment = Comment.objects.get(movie=movie, user=user)
            user_comment.comment = new_comment  # tak komentář aktualizujeme
            user_comment.save()
        else:  # pokud uživatel zadává první komentář k tomuto filmu
            Comment.objects.create(movie=movie, user=user, comment=new_comment)
        """

        # druhá (lepší) varianta aktualizace komentáře
        user_comment = Comment.objects.get_or_create(movie=movie, user=user)[0]
        user_comment.comment = new_comment
        user_comment.save()


    comments = Comment.objects.filter(movie=movie)

    context = {'movie': movie, 'genres': genres, 'countries': countries,
               'actors': actors, 'directors': directors, 'rating': rating,
               'avg_rating': avg_rating['rating__avg'], 'comments': comments}
    return render(request, template_name='movie.html', context=context)


def person(request, pk):
    person = Person.objects.get(pk=pk)
    acting = Movie.objects.filter(actors=person)
    directing = Movie.objects.filter(directors=person)
    context = {'person': person, 'acting': acting, 'directing': directing}
    return render(request, template_name='person.html', context=context)


def search(request):
    if request.method == 'POST':
        pattern = request.POST.get('search').strip()
        if len(pattern) > 0:
            movies_title = Movie.objects.filter(title__contains=pattern)
            movies_title_cz = Movie.objects.filter(title_cz__contains=pattern)
            movies_description = Movie.objects.filter(description__contains=pattern)
            persons_first_name = Person.objects.filter(first_name__contains=pattern)
            persons_last_name = Person.objects.filter(last_name__contains=pattern)
            context = {'pattern': pattern,
                       'movies_title': movies_title,
                       'movies_title_cz': movies_title_cz,
                       'movies_description': movies_description,
                       'persons_first_name': persons_first_name,
                       'persons_last_name': persons_last_name}
            return render(request, template_name='search.html', context=context)
    return render(request, 'home.html')


def filter_movie(request, s):
    genre = Genre.objects.get(name=s)
    movies = Movie.objects.filter(genre=genre)
    genres = Genre.objects.all()
    context = {'movies': movies, 'genres': genres}
    return render(request, 'movies.html', context)


# Přidávání Country do databáze pomocí dvou view
# Tato view zobrazí formulář pro přidání nové země
def new_country(request):
    return render(request, 'new_country.html')


# Tato view zpracuje formulář pro přidání nové země
def add_country(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        abbreviation = request.POST.get('abbreviation')
        if Country.objects.filter(name__iexact=name).count() > 0 or \
                Country.objects.filter(abbreviation__iexact=abbreviation).count() > 0:
            context = {'message': f"This country is in database."}
        elif len(abbreviation) > 3:
            context = {'message': f"Abbreviation can be maximum 3 letters."}
        elif len(name) < 3:
            context = {'message': f"Name must can be minimum 3 letters."}
        else:
            country = Country(name=name, abbreviation=abbreviation)
            country.save()
            context = {'message': f"Country '{country}' added to database."}  # vypsat potvrzení o úspěšném zápisu do databáze.
    return render(request, 'home.html', context)


# Přidávání Country do databáze pomocí jedné view
def new_country2(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        abbreviation = request.POST.get('abbreviation')
        if Country.objects.filter(name__iexact=name).count() > 0 or \
                Country.objects.filter(abbreviation__iexact=abbreviation).count() > 0:
            context = {'message': f"This country is in database."}
        elif len(abbreviation) > 3:
            context = {'message': f"Abbreviation can be maximum 3 letters."}
        elif len(name) < 3:
            context = {'message': f"Name must can be minimum 3 letters."}
        else:
            country = Country(name=name, abbreviation=abbreviation)
            country.save()
            context = {
                'message': f"Country '{country}' added to database."}  # vypsat potvrzení o úspěšném zápisu do databáze.
    else:
        return render(request, 'new_country2.html')  # zobrazí se formulář
    return render(request, 'home.html', context)


# základní možnost vytvoření formuláře
"""
class CountryForm(Form):
    name = CharField(max_length=32)
    abbreviation = CharField(max_length=3)

    def clean_name(self):
        pass

    def clean_abbreviation(self):
        pass

    def clean(self):
        pass
        
        
class CountryCreateView(FormView):
    template_name = 'new_country3.html'
    form_class = CountryForm
"""


def countries(request):
    countries = Country.objects.all()
    context = {'countries': countries}
    return render(request, 'countries.html', context)


class CountryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Country
        fields = '__all__'
        #fields = ['abbreviation', 'name']  # pomocí fields lze i měnit pořadí položek ve formuláři
        #exclude = ['abbreviation']

    def clean_name(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name').strip()
        if name is None:
            raise ValidationError('Name can not be empty.')
        if len(name) < 3:
            raise ValidationError('Name should have minimum 3 letters.')
        name = name.title()
        return name
        
    def clean_abbreviation(self):
        cleaned_data = super().clean()
        abbreviation = cleaned_data.get('abbreviation').strip()
        if abbreviation is None:
            raise ValidationError('Abbreviation can not be empty.')
        if len(abbreviation) > 3:
            raise ValidationError('Abbreviation should have maximum 3 letters.')
        abbreviation = abbreviation.upper()
        return abbreviation

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if name is not None:
            name = name.strip()
        else:
            raise ValidationError('ERROR in name field.')
        abbreviation = cleaned_data.get('abbreviation')
        if abbreviation is not None:
            abbreviation = abbreviation.strip()
        else:
            raise ValidationError('ERROR in abbreviation field.')
        """if name[0] != abbreviation[0]:
            raise ValidationError('Name and abbreviation must begin with same letter.')"""


class CountryCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'new_country3.html'
    form_class = CountryForm
    success_url = reverse_lazy('countries')
    permission_required = 'viewer.add_country'


class CountryUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'new_country3.html'
    model = Country
    form_class = CountryForm
    success_url = reverse_lazy('countries')
    permission_required = 'viewer.change_country'


class CountryDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'country_delete_confirm.html'
    model = Country
    success_url = reverse_lazy('countries')
    permission_required = 'viewer.delete_country'


def genres(request):
    genres = Genre.objects.all()
    context = {'genres': genres}
    return render(request, 'genres.html', context)


class GenreForm(ModelForm):

    class Meta:
        model = Genre
        fields = '__all__'

    def clean_name(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name').strip()
        if name is None:
            raise ValidationError('Name can not be empty.')
        if len(name) < 3:
            raise ValidationError('Name should have minimum 3 letters.')
        name = name.title()
        return name


# TODO - add permissions
class GenreCreateView(CreateView):
    template_name = 'new_genre.html'
    form_class = GenreForm
    success_url = reverse_lazy('genres')


# TODO - add permissions
class GenreUpdateView(UpdateView):
    template_name = 'new_genre.html'
    model = Genre
    form_class = GenreForm
    success_url = reverse_lazy('genres')


# TODO - add permissions
class GenreDeleteView(DeleteView):
    template_name = 'genre_delete_confirm.html'
    model = Genre
    success_url = reverse_lazy('genres')


def persons(request):
    persons = Person.objects.all()
    context = {'persons': persons}
    return render(request, 'persons.html', context)


class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = '__all__'

    """
    def clean_first_name(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name').strip()
        return first_name

    def clean_last_name(self):
        cleaned_data = super().clean()
        last_name = cleaned_data.get('last_name').strip()
        return last_name
    """

    def clean(self):
        cleaned_data = super().clean()
        """
        first_name = cleaned_data.get('first_name').strip()
        last_name = cleaned_data.get('last_name').strip()
        if first_name == "" and last_name == "":
            raise ValidationError("Both first name and last name can not be empty.")
        """

    """
    def clean_birth_date(self):
        cleaned_data = super().clean()
        birth_date = cleaned_data.get('birth_date')
        if birth_date > date.today():
            raise ValidationError("Birth date can not be in future.")
    """

    birth_date = DateField()


# TODO - add permissions
class PersonCreateView(CreateView):
    template_name = 'new_person.html'
    form_class = PersonForm
    success_url = reverse_lazy('persons')


# TODO - add permissions
class PersonUpdateView(UpdateView):
    template_name = 'new_person.html'
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('persons')


# TODO - add permissions
class PersonDeleteView(DeleteView):
    template_name = 'person_delete_confirm.html'
    model = Person
    success_url = reverse_lazy('persons')


class MovieForm(ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'

    # TODO - clean methods


# TODO - add permissions
class MovieCreateView(CreateView):
    template_name = 'new_movie.html'
    form_class = MovieForm
    success_url = reverse_lazy('movies')


# TODO - add permissions
class MovieUpdateView(UpdateView):
    template_name = 'new_movie.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('movies')


# TODO - add permissions
class MovieDeleteView(DeleteView):
    template_name = 'movie_delete_confirm.html'
    model = Movie
    success_url = reverse_lazy('movies')


@login_required
def rate_movie(request, movie_id, rating):
    movie = Movie.objects.get(pk=movie_id)
    user = request.user
    # rating = rating
    # rating = None
    if user.is_authenticated and Rating.objects.filter(movie=movie, user=user).count() > 0:  # pokud už daný uživatel pro tento film hodnotil
        user_rating = Rating.objects.get(movie=movie, user=user)
        user_rating.rating = rating  # tak aktualizojeme hodnotu (nové hodnocení)
        user_rating.save()
        rating = user_rating.rating
    else:  # pokud ještě nehodnotil
        Rating.objects.create(movie=movie, user=user, rating=rating)  # vytvoříme nový záznam

    genres = Genre.objects.filter(movies=movie)
    countries = Country.objects.filter(movies=movie)
    actors = Person.objects.filter(acting_in_movies=movie)
    directors = Person.objects.filter(directing_movies=movie)
    previous_part = Movie.previous_part
    comments = Comment.objects.filter(movie=movie)
    # průměrné hodnocení
    avg_rating = Rating.objects.filter(movie=movie).aggregate(Avg('rating'))
    context = {'movie': movie, 'genres': genres, 'countries': countries,
               'actors': actors, 'directors': directors, 'rating': rating,
               'avg_rating': avg_rating['rating__avg'], 'comments': comments}
    return render(request, template_name='movie.html', context=context)


def delete_rating(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    user = request.user
    if Rating.objects.filter(movie=movie, user=user).count() > 0:
        user_rating = Rating.objects.get(movie=movie, user=user)
        user_rating.delete()

    genres = Genre.objects.filter(movies=movie)
    countries = Country.objects.filter(movies=movie)
    actors = Person.objects.filter(acting_in_movies=movie)
    directors = Person.objects.filter(directing_movies=movie)
    previous_part = Movie.previous_part
    rating = None

    comments = Comment.objects.filter(movie=movie)

    # průměrné hodnocení
    avg_rating = Rating.objects.filter(movie=movie).aggregate(Avg('rating'))
    context = {'movie': movie, 'genres': genres, 'countries': countries,
               'actors': actors, 'directors': directors, 'rating': rating,
               'avg_rating': avg_rating['rating__avg'], 'comments': comments}
    return render(request, template_name='movie.html', context=context)


def delete_comment(request, movie_id, user_id):
    movie = Movie.objects.get(id=movie_id)
    user = User.objects.get(id=user_id)

    if Comment.objects.filter(movie=movie, user=user).count() > 0:
        user_comment = Comment.objects.get(movie=movie, user=user)
        user_comment.delete()

    genres = Genre.objects.filter(movies=movie)
    countries = Country.objects.filter(movies=movie)
    actors = Person.objects.filter(acting_in_movies=movie)
    directors = Person.objects.filter(directing_movies=movie)
    previous_part = Movie.previous_part
    rating = None

    comments = Comment.objects.filter(movie=movie)

    # průměrné hodnocení
    avg_rating = Rating.objects.filter(movie=movie).aggregate(Avg('rating'))
    context = {'movie': movie, 'genres': genres, 'countries': countries,
               'actors': actors, 'directors': directors, 'rating': rating,
               'avg_rating': avg_rating['rating__avg'], 'comments': comments}
    return render(request, template_name='movie.html', context=context)


def users(request):
    users = User.objects.all()
    profiles = Profile.objects.all()
    context = {'users': users, 'profiles': profiles}
    return render(request, 'users.html', context)

def profile(request, pk):
    profile = Profile.objects.get(user=User.objects.get(id=pk))
    context = {'profile': profile}
    return render(request, 'profile.html', context)
