from django.test import TestCase
from django.contrib.auth.models import User
from movies.models import Genre, Movie, Review, Rating, MovieList, Favorite
from datetime import date


class ModelsTestCase(TestCase):

    def setUp(self):
        # Создание пользователя
        self.user = User.objects.create(username="test_user", password="password123")

        # Создание жанра
        self.genre = Genre.objects.create(name="Action", description="Action-packed movies")

        # Создание фильма
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="This is a test movie.",
            release_date=date(2023, 1, 1),
        )
        self.movie.genres.add(self.genre)

        # Создание отзыва
        self.review = Review.objects.create(
            user=self.user,
            movie=self.movie,
            content="Great movie!",
            rating=9
        )

        # Создание оценки
        self.rating = Rating.objects.create(
            user=self.user,
            movie=self.movie,
            score=10
        )

        # Создание списка фильмов
        self.movie_list = MovieList.objects.create(
            user=self.user,
            name="My Favorites"
        )
        self.movie_list.movies.add(self.movie)

        # Создание избранного списка
        self.favorite = Favorite.objects.create(user=self.user)
        self.favorite.movies.add(self.movie)

    def test_genre_creation(self):
        """Тест создания жанра"""
        self.assertEqual(self.genre.name, "Action")
        self.assertEqual(self.genre.description, "Action-packed movies")

    def test_movie_creation(self):
        """Тест создания фильма"""
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.description, "This is a test movie.")
        self.assertEqual(self.movie.release_date, date(2023, 1, 1))
        self.assertIn(self.genre, self.movie.genres.all())  # Жанр связан с фильмом

    def test_review_creation(self):
        """Тест создания отзыва"""
        self.assertEqual(self.review.content, "Great movie!")
        self.assertEqual(self.review.rating, 9)
        self.assertEqual(self.review.movie, self.movie)
        self.assertEqual(self.review.user, self.user)

    def test_rating_creation(self):
        """Тест создания оценки"""
        self.assertEqual(self.rating.score, 10)
        self.assertEqual(self.rating.movie, self.movie)
        self.assertEqual(self.rating.user, self.user)

    def test_movie_list_creation(self):
        """Тест создания пользовательского списка фильмов"""
        self.assertEqual(self.movie_list.name, "My Favorites")
        self.assertIn(self.movie, self.movie_list.movies.all())

    def test_favorite_creation(self):
        """Тест создания избранного"""
        self.assertIn(self.movie, self.favorite.movies.all())
        self.assertEqual(self.favorite.user, self.user)

    def test_average_rating(self):
        """Тест вычисления среднего рейтинга фильма"""
        # У фильма одна оценка с рейтингом 10
        self.assertEqual(self.movie.average_rating, 10)
