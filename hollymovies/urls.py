"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import api.views
from accounts.views import SignUpView, ProfileCreateView
from viewer.views import *


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    path('hello/<s>/', hello),
    path('hello2', hello2),
    path('hello3/<str:s0>/', hello3),

    path('', home, name='home'),
    # path('movies/', movies, name='movies'),  # view pomocí funkce
    path('movies/', MoviesView.as_view(), name='movies'),  # view pomocí třídy
    path('movies_by_length/<order>/', movies_by_length, name='movies_by_length'),
    path('movies_by_year/<order>/', movies_by_year, name='movies_by_year'),
    path('movie/<pk>/', movie, name='movie'),
    #path('actors/', actors, name='actors'),  # view pomocí funkce
    path('actors/', ActorsView.as_view(), name='actors'),  # view pomocí třídy (TemplateView)
    # path('directors/', directors, name='directors'),  # view pomocí funkce
    path('directors/', DirectorsView.as_view(), name='directors'),  # view pomocí třídy (TemplateView)
    path('person/<pk>/', person, name='person'),
    path('search/', search, name='search'),
    path('filter_movie/<s>/', filter_movie, name='filter_movie'),

    # new_country pomocí dvou view
    # path('new_country/', new_country, name='new_country'),
    # path('add_country/', add_country, name='add_country'),

    # new_country pomocí jedné view
    # path('new_country/', new_country2, name='new_country'),

    # new_country pomocí CountryCreateView
    path('new_country/', CountryCreateView.as_view(), name='new_country'),
    path('country/update/<pk>/', CountryUpdateView.as_view(), name='country_update'),
    path('country/delete/<pk>/', CountryDeleteView.as_view(), name='country_delete'),
    path('countries/', countries, name='countries'),

    path('genres/', genres, name='genres'),
    path('new_genre/', GenreCreateView.as_view(), name='new_genre'),
    path('genre/update/<pk>/', GenreUpdateView.as_view(), name='genre_update'),
    path('genre/delete/<pk>/', GenreDeleteView.as_view(), name='genre_delete'),

    path('persons/', persons, name='persons'),
    path('new_person/', PersonCreateView.as_view(), name='new_person'),
    path('person/update/<pk>/', PersonUpdateView.as_view(), name='person_update'),
    path('person/delete/<pk>/', PersonDeleteView.as_view(), name='person_delete'),

    path('new_movie/', MovieCreateView.as_view(), name='new_movie'),
    path('movie/update/<pk>/', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/delete/<pk>/', MovieDeleteView.as_view(), name='movie_delete'),

    # authentication
    path('accounts/signup/', SignUpView.as_view(), name='signup'),  # signup
    path('accounts/', include('django.contrib.auth.urls')),  # login, logout, change password,...

    path('movie_rate/<movie_id>/<rating>/', rate_movie, name='rate_movie'),
    path('delete_rating/<movie_id>/', delete_rating, name='delete_rating'),

    path('delete_comment/<movie_id>/<user_id>/', delete_comment, name='delete_comment'),

    # API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/movies/', api.views.Movies.as_view({'get': 'list'})),
    path('api/movies/', api.views.Movies.as_view()),
    path('api/movie/<pk>/', api.views.Movie.as_view()),
    path('api/persons/', api.views.Persons.as_view()),
    path('api/person/<pk>/', api.views.Person.as_view()),
    path('api/actors/', api.views.Actors.as_view()),
    path('api/action_movies/', api.views.ActionMovies.as_view()),
    path('api/comments/', api.views.Comments.as_view()),

    path('users/', users, name='users'),
    path('profile/<pk>/', profile, name='profile'),
    path('new_profile/', ProfileCreateView.as_view(), name='new_profile'),
]
