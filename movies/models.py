from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    release_date = models.DateField(db_index=True)
    runtime = models.PositiveIntegerField(help_text="Duration in minutes", null=True, blank=True)
    poster = models.ImageField(upload_to='movie_posters/', blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def average_rating(self):
        ratings = self.ratings.all()
        if not ratings.exists():
            return 0.0
        return round(sum(rating.score for rating in ratings) / ratings.count(), 1)

    @classmethod
    def search(cls, query):
        return cls.objects.filter(
            Q(title__icontains=query) |
            Q(original_title__icontains=query) |
            Q(description__icontains=query) |
            Q(genres__name__icontains=query)
        ).distinct()

    class Meta:
        ordering = ['-release_date']
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        indexes = [
            models.Index(fields=['-release_date', '-imdb_rating']),
            models.Index(fields=['title']),
            models.Index(fields=['original_title']),
        ]

    def __str__(self):
        return self.title
