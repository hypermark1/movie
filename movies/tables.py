import django_tables2 as tables
from .models import Movie


class MovieTable(tables.Table):
    title = tables.Column(linkify=True)
    average_rating = tables.Column(verbose_name='Rating')
    release_date = tables.DateColumn(format='Y')
    
    class Meta:
        model = Movie
        template_name = "django_tables2/bootstrap5.html"
        fields = ('title', 'release_date', 'genres', 'average_rating')
        attrs = {'class': 'table table-striped table-hover'}
        
    def render_average_rating(self, value):
        return f"{value:.1f}/10" if value else "No ratings"
        
    def render_genres(self, value):
        return ", ".join(genre.name for genre in value.all()) 