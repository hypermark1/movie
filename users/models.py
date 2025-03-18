from django.contrib.auth.models import AbstractUser
from django.db import models
from movies.models import Movie


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('moderator', 'Moderator'),
        ('user', 'Regular User'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    avatar = models.ImageField(upload_to='user_avatars/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    def is_moderator(self):
        return self.role in ['admin', 'moderator']
        
    def is_admin(self):
        return self.role == 'admin'


class MovieList(models.Model):
    LIST_TYPES = [
        ('favorite', 'Избранное'),
        ('watchlist', 'Хочу посмотреть'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movielists')
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, related_name='movie_lists')
    list_type = models.CharField(max_length=10, choices=LIST_TYPES, default='watchlist')

    class Meta:
        verbose_name = "Список фильмов"
        verbose_name_plural = "Списки фильмов"

    def __str__(self):
        return f"{self.name} by {self.user.username}"

