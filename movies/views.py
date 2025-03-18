import django_filters
from .models import Movie
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin


class MovieFilter(django_filters.FilterSet):
    release_date = django_filters.DateFromToRangeFilter()
    genres = django_filters.ModelMultipleChoiceFilter(queryset=Genre.objects.all())

    class Meta:
        model = Movie
        fields = ['release_date', 'genres']

