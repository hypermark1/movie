from django.contrib import admin
from .models import Review, Rating


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('content', 'movie__title', 'user__username')
    readonly_fields = ('created_at',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'score')
    list_filter = ('score',)
    search_fields = ('movie__title', 'user__username') 