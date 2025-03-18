from django.contrib import admin
from .models import Movie, Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'original_title', 'release_date', 'imdb_rating', 'average_rating')
    list_filter = ('release_date', 'genres')
    search_fields = ('title', 'original_title', 'description')
    filter_horizontal = ('genres',)
    readonly_fields = ('created_at', 'updated_at', 'average_rating')
