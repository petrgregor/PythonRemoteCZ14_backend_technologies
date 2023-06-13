from django.test import TestCase

from viewer.models import *


class MovieModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """ Create database """
        genre_komedie = Genre.objects.create(name="Komedie")
        country_czech = Country.objects.create(name="Czech republic", abbreviation="CZ")
        person_actor = Person.objects.create(
            first_name="David",
            last_name="Novotný",
            birth_date="1969-06-12",
            sex=0,
            country=country_czech
        )
        person_director = Person.objects.create(
            first_name="Tomáš",
            last_name="Svoboda",
            birth_date="1972-04-28",
            sex=0,
            country=country_czech
        )
        movie = Movie.objects.create(
            title="Hodinový manžel",
            title_cz="Hodinový manžel",
            year=2014,
            description="Filmový debut divadelního režiséra a scénáristy Tomáše Svobody vypráví "
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
            language="Czech",
            series=False,
            pg_rating=0,
            length=100,
            previous_part=None
        )
        movie.genre.add(genre_komedie)
        movie.country.add(country_czech)
        movie.actors.add(person_actor)
        movie.directors.add(person_director)
        movie.save()

    def test_title(self):
        movie = Movie.objects.get(id=1)
        self.assertEqual(movie.title, "Hodinový manžel")

    def test_title_cz(self):
        movie = Movie.objects.get(id=1)
        self.assertEqual(movie.title_cz, "Hodinový manžel")

    def test_year(self):
        movie = Movie.objects.get(id=1)
        self.assertEqual(movie.year, 2014)

    def test_movie_str(self):
        movie = Movie.objects.get(id=1)
        self.assertEqual(movie.__str__(), "Hodinový manžel (2014)")

    def test_genre(self):
        movie = Movie.objects.get(id=1)
        """
        genre_count = movie.genre.count()
        self.assertEqual(genre_count, 1)
        """
        self.assertEqual(movie.genre.count(), 1)

    # TODO test_genre_name
    def _test_genre_name(self):
        movie = Movie.objects.get(id=1)
        movie_genre = movie.genre
        print(f"movie_genre: {movie_genre}")
        genre = Genre.objects.get(id=1)
        self.assertEqual(movie_genre, "Komedie")
