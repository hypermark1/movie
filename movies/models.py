from django.contrib.auth.models import User
from django.db import models


# Жанры фильмов
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# Фильмы
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField(db_index=True)  # Индекс для быстрой фильтрации по дате
    poster = models.ImageField(upload_to='movie_posters/', blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name='movies')

    @property
    def average_rating(self):
        ratings = self.ratings.all()
        return sum(rating.score for rating in ratings) / ratings.count() if ratings.exists() else 0

    def __str__(self):
        return self.title


# Отзывы
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    rating = models.PositiveIntegerField(db_index=True)  # Индекс для сортировки и поиска
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.movie.title}"


# Оценки
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    score = models.PositiveIntegerField()  # Оценка от 1 до 10

    class Meta:
        unique_together = ('user', 'movie')  # Один пользователь может оценить фильм только один раз

    def __str__(self):
        return f"Rating {self.score} for {self.movie.title} by {self.user.username}"


# Списки фильмов (кастомные списки, например, "любимые" или "хочу посмотреть")
class MovieList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movielists')
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, related_name='movie_lists')

    def __str__(self):
        return f"{self.name} by {self.user.username}"


# Избранные фильмы
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    movies = models.ManyToManyField(Movie, related_name='favorited_by')  # ManyToMany связь для избранного фильма

    def __str__(self):
        return f"Favorites of {self.user.username}"

