import django_filters
from .models import Movie, Genre


class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    genres = django_filters.ModelMultipleChoiceFilter(
        queryset=Genre.objects.all(),
        widget=django_filters.widgets.RangeWidget(attrs={'class': 'form-control'})
    )
    release_date = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(attrs={'class': 'form-control', 'type': 'date'})
    )
    min_rating = django_filters.NumberFilter(field_name='average_rating', lookup_expr='gte')
    max_rating = django_filters.NumberFilter(field_name='average_rating', lookup_expr='lte')

    class Meta:
        model = Movie
        fields = ['title', 'genres', 'release_date', 'min_rating', 'max_rating'] 