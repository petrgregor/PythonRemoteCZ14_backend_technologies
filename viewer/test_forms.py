from django.test import TestCase

from viewer.models import *
from viewer.views import MovieForm, CountryForm, GenreForm


class MovieFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name="Komedie")
        country_czech = Country.objects.create(name="Czech", abbreviation="CZ")
        Person.objects.create(
            first_name="David",
            last_name="Novotný",
            birth_date="1969-06-12",
            sex=0,
            country=country_czech
        )
        Person.objects.create(
            first_name="Tomáš",
            last_name="Svoboda",
            birth_date="1972-04-28",
            sex=0,
            country=country_czech
        )

    def test_movie_form_valid(self):
        form = MovieForm(
            data={
                'title': 'Hodinový manžel',
                'title_cz': 'Hodinový manžel',
                'year': 2014,
                'genre': ['1'],
                'country': ['1'],
                'actors': ['1'],
                'directors': ['1'],
                'description': "Filmový debut divadelního režiséra a scénáristy Tomáše Svobody vypráví "
                        "příběh čtyř přátel, vášnivých hráčů vodního póla, kteří společně provozují "
                        "bazén. Ten jim jednoho dne jako nevyhovující vypustí hygiena a čtveřice "
                        "se tak rázem ocitá doslova na dně. Jeden z nich pak na dně bazénu začne "
                        "dokonce i bydlet, když se pohádá s manželkou a uražen odejde z domova. "
                        "Z nedostatku příležitostí začnou chlapi podnikat jako 'hodinoví manželé' "
                        "a zakrátko si najdou klientelu mezi místními dámami. Každý z nich má svou "
                        "pravidelnou zákaznici, ale ty mají kromě oprav často i velmi specifická "
                        "přání a potřeby. To se však pomalu přestává líbit partnerkám a manželkám "
                        "našich hrdinů... Takto rozehraný příběh pak graduje nečekanou cestou do "
                        "Tater, kde se vše pořádně zamotá, aby nakonec vše dospělo do zdárného konce, "
                        "který slibuje nejedno překvapení. (Hollywood Classic Entertainment (H.C.E.)) ",
                'language': 'Czech',
                'series': False,
                'pg_rating': 0,
                'length': 100,
                'previous_part': None
            }
        )
        self.assertTrue(form.is_valid())


    def test_movie_title_field(self):
        user_input_title = ""
        form = MovieForm(
            data={
                'title': user_input_title,
                'title_cz': 'Hodinový manžel',
                'year': 2014,
                'genre': ['1'],
                'country': ['1'],
                'actors': ['1'],
                'directors': ['1'],
                'description': "Filmový debut divadelního režiséra a scénáristy Tomáše Svobody vypráví "
                        "příběh čtyř přátel, vášnivých hráčů vodního póla, kteří společně provozují "
                        "bazén. Ten jim jednoho dne jako nevyhovující vypustí hygiena a čtveřice "
                        "se tak rázem ocitá doslova na dně. Jeden z nich pak na dně bazénu začne "
                        "dokonce i bydlet, když se pohádá s manželkou a uražen odejde z domova. "
                        "Z nedostatku příležitostí začnou chlapi podnikat jako 'hodinoví manželé' "
                        "a zakrátko si najdou klientelu mezi místními dámami. Každý z nich má svou "
                        "pravidelnou zákaznici, ale ty mají kromě oprav často i velmi specifická "
                        "přání a potřeby. To se však pomalu přestává líbit partnerkám a manželkám "
                        "našich hrdinů... Takto rozehraný příběh pak graduje nečekanou cestou do "
                        "Tater, kde se vše pořádně zamotá, aby nakonec vše dospělo do zdárného konce, "
                        "který slibuje nejedno překvapení. (Hollywood Classic Entertainment (H.C.E.)) ",
                'language': 'Czech',
                'series': False,
                'pg_rating': 0,
                'length': 100,
                'previous_part': None
            }
        )
        self.assertFalse(form.is_valid())


class CountryFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name="Komedie")
        country_czech = Country.objects.create(name="Czech", abbreviation="CZ")
        Person.objects.create(
            first_name="David",
            last_name="Novotný",
            birth_date="1969-06-12",
            sex=0,
            country=country_czech
        )
        Person.objects.create(
            first_name="Tomáš",
            last_name="Svoboda",
            birth_date="1972-04-28",
            sex=0,
            country=country_czech
        )
    def test_country_form_valid(self):
        form = CountryForm(
            data = {
                'name': 'Germany',
                'abbreviation': 'DE'
            }
        )
        self.assertTrue(form.is_valid())

    def test_empty_country_name_field(self):
        form = CountryForm(
            data = {
                'name': '',
                'abbreviation': 'PL'
            }
        )
        self.assertFalse(form.is_valid())

    def test_short_country_name_field(self):
        form = CountryForm(
            data = {
                'name': 'Pl',
                'abbreviation': 'PL'
            }
        )
        self.assertFalse(form.is_valid())

    def test_empty_country_abbreviation_field(self):
        form = CountryForm(
            data = {
                'name': 'Poland',
                'abbreviation': ''
            }
        )
        self.assertFalse(form.is_valid())

    def test_long_country_abbreviation_field(self):
        form = CountryForm(
            data = {
                'name': 'Poland',
                'abbreviation': 'Poland'
            }
        )
        self.assertFalse(form.is_valid())

class GenreFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name="Komedie")
        country_czech = Country.objects.create(name="Czech", abbreviation="CZ")
        Person.objects.create(
            first_name="David",
            last_name="Novotný",
            birth_date="1969-06-12",
            sex=0,
            country=country_czech
        )
        Person.objects.create(
            first_name="Tomáš",
            last_name="Svoboda",
            birth_date="1972-04-28",
            sex=0,
            country=country_czech
        )
    def test_empty_genre_name_field(self):
        form = GenreForm(
            data = {
                'name': '',
            }
        )
        self.assertFalse(form.is_valid())